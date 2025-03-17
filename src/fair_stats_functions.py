#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:47:50 2025

@author: saibotMagd
"""

import os
import json
import re
import csv
from collections import defaultdict, Counter
import requests
import pandas as pd
import matplotlib.pyplot as plt
import logging
from tqdm.auto import tqdm
from datetime import datetime

def read_json_files(folder_path):
    """
    Reads all JSON files from the specified folder.

    Args:
        folder_path (str): The path to the folder containing JSON files.

    Returns:
        list: A list of JSON file names.
    """
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    return json_files

def parse_json_file(file_path):
    """
    Parses a JSON file and returns its content.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The parsed JSON content.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def summarize_test_results(json_files, folder_path):
    """
    Summarizes test results from JSON files.

    Args:
        json_files (list): A list of JSON file names.
        folder_path (str): The path to the folder containing JSON files.

    Returns:
        tuple: A tuple containing test results, failure explanations, and publisher failures.
    """
    test_results = defaultdict(lambda: {'pass': 0, 'fail': 0})
    failure_explanations = []
    publisher_failures = defaultdict(lambda: defaultdict(int))

    for json_file in json_files:
        file_path = os.path.join(folder_path, json_file)
        data = parse_json_file(file_path)

        for result in data.get('results', []):
            test_id = result['metric_identifier']
            test_status = result['test_status']
            test_results[test_id][test_status] += 1

            if test_status == 'fail':
                for explanation in result.get('test_debug', []):
                    failure_explanations.append((test_id, explanation))

                # Extract publisher information
                for metadata in data.get('harvested_metadata', []):
                    publishers = metadata.get('metadata', {}).get('publisher')
                    if publishers:
                        if isinstance(publishers, dict):
                            for publisher in publishers.values():
                                publisher_failures[publisher][test_id] += 1
                        elif isinstance(publishers, list):
                            for publisher in publishers:
                                publisher_failures[publisher][test_id] += 1
                        else:
                            publisher_failures[publishers][test_id] += 1

    return test_results, failure_explanations, publisher_failures

def clean_explanation(explanation):
    """
    Cleans an explanation by removing specific DOIs or URLs.

    Args:
        explanation (str): The explanation to clean.

    Returns:
        str: The cleaned explanation.
    """
    explanation = re.sub(r'https?://[^\s]+', '', explanation)
    explanation = re.sub(r'10\.\d{4,9}/[^\s]+', '', explanation)
    explanation = re.sub(r'\[\'[^\]]+\'\]', '', explanation)
    explanation = re.sub(r'\([^\)]+\)', '', explanation)
    explanation = re.sub(r'/api/v2/search\?query=/[^\s]+', '', explanation)
    explanation = explanation.strip()
    return explanation

def aggregate_failure_explanations(failure_explanations):
    """
    Aggregates failure explanations.

    Args:
        failure_explanations (list): A list of failure explanations.

    Returns:
        Counter: A counter of cleaned failure explanations.
    """
    cleaned_explanations = [(metric, clean_explanation(explanation)) for metric, explanation in failure_explanations]
    explanation_counter = Counter(cleaned_explanations)
    return explanation_counter

def save_test_results_to_csv(test_results, output_folder):
    """
    Saves test results to a CSV file.

    Args:
        test_results (dict): The test results to save.
        output_folder (str): The path to the output folder.
    """
    os.makedirs(output_folder, exist_ok=True)
    with open(os.path.join(output_folder, 'test_results.csv'), 'w', newline='') as csvfile:
        fieldnames = ['test_id', 'pass', 'fail']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for test_id, results in test_results.items():
            writer.writerow({'test_id': test_id, 'pass': results['pass'], 'fail': results['fail']})

def save_failure_explanations_to_csv(explanation_counter, output_folder):
    """
    Saves failure explanations to a CSV file.

    Args:
        explanation_counter (Counter): The failure explanations to save.
        output_folder (str): The path to the output folder.
    """
    os.makedirs(output_folder, exist_ok=True)
    with open(os.path.join(output_folder, 'failure_explanations.csv'), 'w', newline='') as csvfile:
        fieldnames = ['metric', 'explanation', 'count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for (metric, explanation), count in explanation_counter.items():
            writer.writerow({'metric': metric, 'explanation': explanation, 'count': count})

def save_publisher_failures_to_csv(publisher_failures, output_folder):
    """
    Saves publisher failures to a CSV file.

    Args:
        publisher_failures (dict): The publisher failures to save.
        output_folder (str): The path to the output folder.
    """
    os.makedirs(output_folder, exist_ok=True)
    with open(os.path.join(output_folder, 'publisher_failures.csv'), 'w', newline='') as csvfile:
        fieldnames = ['publisher', 'metric', 'count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for publisher, failures in publisher_failures.items():
            for metric, count in failures.items():
                writer.writerow({'publisher': publisher, 'metric': metric, 'count': count})

def make_post_request(url, headers, payload):
    """
    Makes a POST request to the specified URL with the given headers and payload.

    Args:
        url (str): The URL to send the POST request to.
        headers (dict): The headers to include in the request.
        payload (dict): The payload to send with the request.

    Returns:
        requests.Response: The response object from the POST request.
    """
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def save_response_to_json(response, filename):
    """
    Saves the response body as a JSON file.

    Args:
        response (requests.Response): The response object from the POST request.
        filename (str): The name of the file to save the JSON response to.
    """
    try:
        with open(filename, 'w') as json_file:
            json.dump(response.json(), json_file, indent=4)
        print(f"Response saved to {filename}")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON response: {e}")
    except IOError as e:
        print(f"Failed to write to file: {e}")

def create_fair_statistics(object_identifiers, fair_stats_folder, renew=0):
    """
    Executes a POST request for each object identifier and saves the response to a JSON file.

    Parameters:
        object_identifiers (list): A list of object identifiers to process.
        renew (int): A flag to indicate whether to renew the process. Default is 0.

    Returns:
        None
    """
    url = 'http://localhost:1071/fuji/api/v1/evaluate'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Basic bWFydmVsOndvbmRlcndvbWFu',
        'Content-Type': 'application/json'
    }
    # Configure logging to use tqdm
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger()

    for obj_id in tqdm(object_identifiers):
        payload = {
            "object_identifier": obj_id,
            "test_debug": True,
            "metadata_service_endpoint": "",
            "metadata_service_type": "oai_pmh",
            "use_datacite": True,
            "use_github": False,
            "metric_version": "metrics_v0.5"
        }
        if renew == 0 and os.path.isfile(os.path.join(fair_stats_folder, f'{obj_id.replace("/", "_").replace(":", "_")}_FAIRstats_.json')):
            logger.info(f"FAIR stats for {obj_id} already exists, and renew = 0 -> will not write")
            continue
        response = make_post_request(url, headers, payload)
        if response and response.status_code == 200:
            save_response_to_json(response, os.path.join(fair_stats_folder, f'{obj_id.replace("/", "_").replace(":", "_")}_FAIRstats_.json'))
        else:
            logger.info(f"Failed to retrieve data for {obj_id}: {response.status_code if response else 'No response'}")
            if response:
                tqdm.write(f"Response: {response.text}")

def create_summary_plot(og_df, summary_folder='./data/fair_summary', aggregator='Median', show=0, savefig=1):
    """
    Creates a summary plot of FAIR scores over time.

    This function generates a plot showing the FAIR scores (Findable, Accessible, Interoperable, Reusable, and overall FAIR)
    over time, aggregated by the specified aggregator ('Median' or 'Mean'). The plot can be displayed and/or saved to a file.

    Parameters:
        og_df (pd.DataFrame): The original DataFrame containing the FAIR scores and publication dates.
        aggregator (str): The aggregator to use ('Median' or 'Mean'). Default is 'Median'.
        show (int): Whether to display the plot (1 for yes, 0 for no). Default is 0.
        savefig (int): Whether to save the plot to a file (1 for yes, 0 for no). Default is 1.
        summary_folder (str): The folder path to save the plot. Default is './data/fair_summary'.

    Returns:
        None
    """
    # Create DataFrame
    df = pd.DataFrame(og_df)

    # Convert date columns to datetime
    df['publication_date'] = pd.to_datetime(df['publication_date'], errors='coerce')

    # Drop rows where both 'date' and 'publication_date' are NaN
    df = df.dropna(subset=['publication_date'])

    # Extract the year from the final_date
    df['year'] = df['publication_date'].dt.year

    if aggregator == 'Median':
        # Group by 'year' and calculate the median for each column
        grouped = df.groupby('year')[['F', 'A', 'I', 'R', 'FAIR']].median()
    elif aggregator == 'Mean':
        # Group by 'year' and calculate the mean for each column
        grouped = df.groupby('year')[['F', 'A', 'I', 'R', 'FAIR']].mean()
    else:
        print("Aggregator error: choose Median (default) or Mean.")
        return 1

    # Count the number of rows processed for each year
    row_counts = df['year'].value_counts().sort_index()

    # Plotting
    plt.figure(figsize=(14, 8))

    # Plot each line
    plt.plot(grouped.index, grouped['F'], label='Findable', color='blue', marker='o')
    plt.plot(grouped.index, grouped['A'], label='Accessible', color='green', marker='o')
    plt.plot(grouped.index, grouped['I'], label='Interoperable', color='yellow', marker='o')
    plt.plot(grouped.index, grouped['R'], label='Reusable', color='purple', marker='o')
    plt.plot(grouped.index, grouped['FAIR'], label='FAIR (incl. numbers of publications processed)', color='red', marker='o')

    # Annotate each dot with the number of processed rows
    for year, count in row_counts.items():
        plt.annotate(f'{count}', (year, grouped.loc[year, 'FAIR']), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

    # Adding titles and labels
    plt.title(f'{aggregator} Values of fair_stats Over Time')
    plt.xlabel('Year')
    plt.ylabel(f'{aggregator} Value')
    legend = plt.legend(loc="upper left", edgecolor='black')
    legend.get_frame().set_alpha(None)
    legend.get_frame().set_facecolor((1, 1, 1, 0.1))
    # Set x-ticks to include every year
    plt.xticks(grouped.index, rotation=45, ha='right')
    if savefig:
        # Show the plot
        plt.savefig(f'{summary_folder}/{aggregator.lower()}_values_over_time_high_res.png', dpi=4000/12, format='png', transparent=True)
    if show:
        plt.show()
    if not show:
        plt.close()

def create_fair_summary_markdown(paper_authors, mean_df, md_df):
    """
    Creates a markdown summary of FAIR statistics.

    This function generates a markdown summary of FAIR statistics, including mean statistics,
    median statistics, and a complete list of publications. The summary is saved to markdown files.

    Parameters:
        paper_authors (pd.DataFrame): The DataFrame containing FAIR statistics for each publication.
        mean_df (pd.DataFrame): The DataFrame containing mean FAIR statistics.
        md_df (pd.DataFrame): The DataFrame containing median FAIR statistics.

    Returns:
        None
    """
    # Save DataFrames to CSV
    paper_authors.index = range(len(paper_authors))
    paper_authors.to_csv("./data/fair_summary/LIN_fair_persons_cpl.csv")
    mean_df.to_csv("./data/fair_summary/LIN_fair_persons_mean.csv")
    md_df.to_csv("./data/fair_summary/LIN_fair_persons_md.csv")

    curr_date = datetime.today().strftime('%m-%d-%Y')

    # Convert DataFrame to markdown table
    markdown_table_md = md_df.to_markdown(index=False)
    markdown_table_mean = mean_df.to_markdown(index=False)
    markdown_table_cpl = paper_authors.to_markdown(index=False)

    # Create the markdown content
    markdown_content = (
        f"# LIN-FAIR-ness_summary\n\n"
        f"## Here are the FAIR-statistics calculated by [FAIR-checker (FUJI)](https://github.com/IFB-ElixirFr/fair-checker) (last updated: {curr_date})\n\n"
        f"## Median Statistics (last update: {curr_date})\n\n"
        f"![Median Values Over Time](./imgs/median_values_over_time_high_res.png)\n\n"
        f"## Current LIN Employee summarized Stats by median (last update: {curr_date})\n\n"
        f"{markdown_table_md}\n\n"
        f"## Current LIN Employee summarized Stats by mean (last update: {curr_date})\n\n"
        f"{markdown_table_mean}\n\n"
        f"## Current LIN Employee Stats of all publications (last update: {curr_date})\n\n"
        f"[complete list (~1 min loading time)](LIN-fair_summary_cpl.md)\n"
    )

    # Write the markdown content to the summary file
    with open("./data/fair_summary/LIN-fair_summary.md", "w") as file:
        file.write(markdown_content)

    # Write the complete list of publications to a separate file
    with open("./data/fair_summary/LIN-fair_summary_cpl.md", "w") as file:
        file.write(f"# Complete List of Publications\n\n{markdown_table_cpl}\n")

def get_doi_to_fair_dict(json_folder):
    """
    Creates a dictionary mapping DOIs to FAIR scores and publication dates.

    This function reads JSON files from the specified folder, extracts FAIR scores
    and publication dates, and returns a dictionary mapping DOIs to their corresponding
    FAIR scores and publication dates.

    Parameters:
        json_folder (str): The path to the folder containing JSON files. Default is "./data/LIN-fair".

    Returns:
        dict: A dictionary mapping DOIs to their FAIR scores and publication dates.
    """
    # Dictionary to store DOI to FAIR scores and publication date mapping
    doi_to_fair = {}

    # Load JSON files and extract FAIR scores and publication date
    for filename in os.listdir(json_folder):
        if filename.endswith('.json'):
            with open(os.path.join(json_folder, filename), 'r') as file:
                data = json.load(file)
                doi = data['request']['object_identifier']
                fair_scores = data['summary']['score_percent']
                publication_date = find_oldest_publication_date(data)
                try:
                    #print(f"good: {publication_date}")
                    doi_to_fair[doi] = {
                        'F': fair_scores.get('F', 0),
                        'A': fair_scores.get('A', 0),
                        'I': fair_scores.get('I', 0),
                        'R': fair_scores.get('R', 0),
                        'FAIR': fair_scores.get('FAIR', 0),
                        'publication_date': publication_date if publication_date else None
                    }
                except:
                    print(publication_date)
    return doi_to_fair

def get_fair_statistics_cpl(doi_to_fair):
    """
    Creates a DataFrame with FAIR statistics for each DOI.

    This function takes a dictionary mapping DOIs to FAIR scores and publication dates
    and returns a DataFrame with the FAIR statistics for each DOI.

    Parameters:
        doi_to_fair (dict): The dictionary mapping DOIs to FAIR scores and publication dates.

    Returns:
        pd.DataFrame: A DataFrame with the FAIR statistics for each DOI.
    """
    # Create a list of dictionaries, each containing the DOI and its corresponding values
    data_list = [
        {**{'doi': doi}, **values}
        for doi, values in doi_to_fair.items()
    ]

    # Create the DataFrame
    paper_cpl = pd.DataFrame(data_list)

    return paper_cpl

def find_oldest_publication_date(data):
    """
    Recursively finds the oldest publication date in the given data.

    This function traverses the input data (which can be a dictionary or a list)
    to find the oldest publication date. It uses the `normalize_date` function
    to parse and compare dates.

    Parameters:
        data (dict or list): The data to search for the oldest publication date.

    Returns:
        datetime or None: The oldest publication date as a datetime object, or None if not found.
    """
    oldest_date = None
    date_formats = ['%Y-%m-%d', '%Y/%m/%d', '%Y-%m', '%Y/%m']  # Add more formats if needed

    def traverse(data):
        nonlocal oldest_date

        if isinstance(data, dict):
            for key, value in data.items():
                if key == "publication_date":
                    if isinstance(value, list):
                        for date_str in value:
                            parse_date(date_str)
                    else:
                        parse_date(value)
                traverse(value)
        elif isinstance(data, list):
            for item in data:
                traverse(item)

    def parse_date(date_value):
        nonlocal oldest_date
        if isinstance(date_value, int):
            # Handle the case where the value is an integer (year)
            date_value = datetime(date_value, 1, 1)
            if oldest_date is None or date_value < oldest_date:
                oldest_date = date_value
        else:
            for date_format in date_formats:
                try:
                    date_value = datetime.strptime(date_value, date_format)
                    if oldest_date is None or date_value < oldest_date:
                        oldest_date = date_value
                    break  # Stop trying other formats if this one works
                except ValueError:
                    continue  # Try the next format

    traverse(data)

    if oldest_date:
        return oldest_date.strftime('%Y-%m-%d')
    else:
        return None