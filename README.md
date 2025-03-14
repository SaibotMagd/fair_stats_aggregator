![Lin_X_NFDI4BIOIMAGE](/imgs/lin_x_nfdi4bioimage.png)
# FAIR Statistics Aggregator for DOIs

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Output](#output)
7. [Limitations](#limitations)
8. [License](#license)

## Introduction
This repository hosts a prototype tool designed to analyze and aggregate FAIR (Findable, Accessible, Interoperable, and Reusable) statistics for a list of Digital Object Identifiers (DOIs). The tool currently utilizes the F-UJI FAIR checker to evaluate the FAIRness of the metadata associated with each DOI. Future versions aim to incorporate additional FAIR checkers to provide a more comprehensive analysis.

The tool processes a list of DOIs, which can be sourced from a website or fetched using a metasearch API like Crossref or DataCite. It calculates FAIR statistics for each DOI, aggregates these statistics by publication year, and identifies common metadata errors that impact FAIRness. The results are presented in an aggregated FAIR-statistic per publication year diagram and a summary of the most frequent metadata issues.

This tool also serves as a justification for metadata providers (e.g., Springer, Nature) to ensure their metadata is hosted in a machine-readable format, as this is crucial for optimal FAIRness evaluation.

**Warning**: The F-UJI FAIR checker must be initialized beforehand using a Docker container. Instructions for setting up the F-UJI checker can be found [here](https://github.com/FAIR-IMPACT/fuji). Please note that F-UJI and other FAIR checkers are in a very early beta status.

## Features
- **DOI List Processing**: Accepts a list of DOIs from a file or fetched via APIs like Crossref or DataCite.
- **FAIR Evaluation**: Uses the F-UJI FAIR checker to evaluate the FAIRness of each DOI's metadata.
- **Aggregation**: Aggregates FAIR statistics by publication year.
- **Error Summary**: Identifies and summarizes the most common metadata errors affecting FAIRness.
- **Visualization**: Generates an aggregated FAIR-statistic per publication year diagram.

## Requirements
- Python 3.x
- Docker (for running the F-UJI FAIR checker)
- Required Python packages (listed in `requirements.txt`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/saibotmagd/fair_stats_aggregator.git
   cd fair_stats_aggregator
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the F-UJI FAIR checker (https://github.com/FAIR-IMPACT/fuji) using Docker:
   ```bash
   docker pull fairimpact/fuji
   docker run -d -p 1071:1071 fairimpact/fuji
   ```

## Usage
1. Prepare a list of DOIs in a text file (one DOI per line) or use an API to fetch DOIs.

- you can use the openAlex API to get a DOI-list file for your institute by running: 
    ```bash
    python get_dois_from_openalex_id.py {openalex-institutions-id} {outputfile.txt}
    ```
2. Run the tool:
   ```bash
   python fair_stats_agg.py --doi-file path/to/doi_list.txt
   ```
   We provide sample doi_list-files for the NFDI4bioimage partner institutes the '/data/folder' (Uploaded 3/2025)
   
3. The tool will output the aggregated FAIR statistics and a summary of metadata errors, as 
    - '.png' files (diagramms of aggregated FAIR statistic), 
    - '.csv' files (aggregated sources of errors in FAIR statistics, issues of the publishing websites)
    
4. You can create a full summary as a markdown-file for every doi_list processed in one file with:
   ```bash
   python create_full_summary.py ./data/ example_summary.md
   ```

## Output
- **Aggregated FAIR-statistic per Publication Year Diagram**: A visual representation of FAIR statistics aggregated by publication year.
- **Metadata Error Summary**: A list of the most common metadata errors affecting FAIRness.
- **Justification for Metadata Providers**: A summary highlighting the importance of machine-readable metadata for optimal FAIRness evaluation.

## Limitations
- **Beta Status**: The F-UJI FAIR checker and other FAIR checkers are in a very early beta status. Results may vary and should be interpreted with caution.
- **Dependency on Docker**: The F-UJI FAIR checker requires Docker to be initialized beforehand.

## License

# CC BY-NC License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License** (CC BY-NC 4.0).

## You are free to:

- **Share** — Copy and redistribute the material in any medium or format.
- **Adapt** — Remix, transform, and build upon the material.

The licensor cannot revoke these freedoms as long as you follow the license terms.

## Under the following terms:

- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **NonCommercial** — You may not use the material for commercial purposes.

## Notices:

- You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.
- No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.

For more details, please refer to the full license text: [CC BY-NC 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/).

---

**Note**: If you intend to use this work for commercial purposes, please contact the author for alternative licensing options.
---

[Back to Top](#fair-statistics-aggregator-for-dois)
