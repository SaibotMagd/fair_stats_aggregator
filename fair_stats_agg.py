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
    create_fair_statistics, create_summary_plot, create_fair_summary_markdown
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

    # Create necessary folders if they do not exist
    os.makedirs('./data/fair-stats', exist_ok=True)
    os.makedirs('./data/fair-summary', exist_ok=True)

    # Create FAIR statistics
    create_fair_statistics(doi_list, renew=args.renew)

    # Read JSON files
    json_files = read_json_files('./data/fair-stats')

    # Summarize test results
    test_results, failure_explanations, publisher_failures = summarize_test_results(json_files, './data/fair-stats')
    explanation_counter = aggregate_failure_explanations(failure_explanations)

    # Save results to CSV
    save_test_results_to_csv(test_results, './data/fair-summary')
    save_failure_explanations_to_csv(explanation_counter, './data/fair-summary')
    save_publisher_failures_to_csv(publisher_failures, './data/fair-summary')

    # Create summary plot
    create_summary_plot(og_df=None, aggregator='Median', show=0, savefig=1, summary_folder='./data/fair-summary')
    create_summary_plot(og_df=None, aggregator='Mean', show=0, savefig=1, summary_folder='./data/fair-summary')

    # Create FAIR summary markdown
    create_fair_summary_markdown(paper_authors=None, mean_df=None, md_df=None)

if __name__ == "__main__":
    main()
