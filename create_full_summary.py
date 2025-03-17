#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:47:50 2025

@author: saibotMagd
"""
import os
import pandas as pd
import argparse

def generate_readme(input_folder, output_file):
    with open(output_file, "w") as readme_file:
        # Table of Contents
        readme_file.write("# Table of Contents\n\n")
        toc_entries = []

        # Iterate through each subfolder in the input folder
        for folder_name in sorted(os.listdir(input_folder)):
            folder_path = os.path.join(input_folder, folder_name)

            # Check if it's a directory and matches the naming schema
            if os.path.isdir(folder_path) and folder_name.startswith("fair_summary_"):
                institute_name = folder_name.split("_", 1)[1]
                toc_entries.append(f"- [{institute_name}](#{institute_name.replace(' ', '-').lower()})\n")

        # Write Table of Contents entries
        print(toc_entries)
        readme_file.writelines(toc_entries)
        readme_file.write("\n")

        # Iterate again to write the content for each institute
        for folder_name in sorted(os.listdir(input_folder)):
            folder_path = os.path.join(input_folder, folder_name)

            # Check if it's a directory and matches the naming schema
            if os.path.isdir(folder_path) and folder_name.startswith("fair_summary_"):
                institute_name = folder_name.split("_", 1)[1]
                readme_file.write(f"# Research Institute Summaries\n\n")
                readme_file.write(f"## {institute_name}\n\n")

                # Display images
                for image_name in ["mean_values_over_time_high_res.png", "median_values_over_time_high_res.png"]:
                    image_path = os.path.join(folder_path, image_name)
                    if os.path.exists(image_path):
                        readme_file.write(f"![{image_name}]({'../.' + image_path})\n\n")
                        readme_file.write("[Back to top](#table-of-contents)\n\n")

                # Display CSV files as tables
                for csv_name in ["failure_explanations.csv", "publisher_failures.csv", "test_results.csv"]:
                    csv_path = os.path.join(folder_path, csv_name)
                    if os.path.exists(csv_path):
                        readme_file.write(f"### {csv_name}\n\n")
                        df = pd.read_csv(csv_path)
                        readme_file.write(df.to_markdown(index=False))
                        readme_file.write("\n\n")
                        readme_file.write("[Back to top](#table-of-contents)\n\n")

def main():
    parser = argparse.ArgumentParser(description="Generate a README.md file from a folder of institute data.")
    parser.add_argument("input_folder", type=str, help="Path to the input folder containing the subfolders.")
    parser.add_argument("output_file", type=str, help="Path to the output Markdown file.")

    args = parser.parse_args()
    generate_readme(args.input_folder, args.output_file)

if __name__ == "__main__":
    main()

