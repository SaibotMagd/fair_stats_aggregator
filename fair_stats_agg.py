#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:47:50 2025

@author: saibotMagd
"""

import argparse
import os
import sys
sys.path.insert(0, './src/')
from fair_stats_functions import (
    read_json_files, summarize_test_results, aggregate_failure_explanations,
    save_test_results_to_csv, save_failure_explanations_to_csv, save_publisher_failures_to_csv,
    create_fair_statistics, create_summary_plot, create_fair_summary_markdown, get_doi_to_fair_dict,
    get_fair_statistics_cpl
)

def main():
    """
    Main function to parse command-line arguments and run the appropriate command.
    """
    parser = argparse.ArgumentParser(description="CLI for aggregating FAIR statistics")

    parser.add_argument('--doi-filelist', type=str, required=True, help='A list of DOIs provided by grep or similar, or a txt file including a list of DOI strings.')
    parser.add_argument('--renew', type=int, default=0, help='Flag to indicate whether to recalculate the FAIR statistics for every DOI (default: 0).')

    args = parser.parse_args()

    doi_list = []
    if os.path.isfile(args.doi_filelist):
        with open(args.doi_filelist, 'r') as file:
            doi_list = [line.strip() for line in file.readlines()]
    else:
        doi_list = args.doi_filelist.split()

    doi_list = list(set(doi_list))

    # Extract the filename from the doi_filelist argument
    doi_filename = os.path.splitext(os.path.basename(args.doi_filelist))[0]

    # Define the target folder names
    fair_stats_folder = f'./data/fair_stats_{doi_filename}'
    fair_summary_folder = f'./data/fair_summary_{doi_filename}'

    # Create necessary folders if they do not exist
    os.makedirs(fair_stats_folder, exist_ok=True)
    os.makedirs(fair_summary_folder, exist_ok=True)

    # Create FAIR statistics
    create_fair_statistics(doi_list, fair_stats_folder, renew=args.renew)

    # Read JSON files
    json_files = read_json_files(fair_stats_folder)

    # Summarize test results
    test_results, failure_explanations, publisher_failures = summarize_test_results(json_files, fair_stats_folder)
    explanation_counter = aggregate_failure_explanations(failure_explanations)

    # Save results to CSV
    save_test_results_to_csv(test_results, fair_summary_folder)
    save_failure_explanations_to_csv(explanation_counter, fair_summary_folder)
    save_publisher_failures_to_csv(publisher_failures, fair_summary_folder)

    
    doi_to_fair = get_doi_to_fair_dict(fair_stats_folder)
    paper_cpl = get_fair_statistics_cpl(doi_to_fair)

    # Create summary plot
    create_summary_plot(og_df=paper_cpl, summary_folder=fair_summary_folder, aggregator='Median', show=0, savefig=1)
    create_summary_plot(og_df=paper_cpl, summary_folder=fair_summary_folder, aggregator='Mean', show=0, savefig=1)

if __name__ == "__main__":
    main()

