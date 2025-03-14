import argparse
import requests

def get_dois_from_openalex(institute_id):
    """
    Fetch DOIs from OpenAlex API for a given institute ID.

    Parameters:
    - institute_id (str): The ID of the institute to filter the works by.

    Returns:
    - list: A list of DOIs associated with the institute.
    """
    base_url = "https://api.openalex.org/works"
    dois = []

    # Fetch the first page to determine the total number of pages
    data = requests.get(f"{base_url}?page=1&filter=authorships.institutions.lineage:{institute_id}&sort=cited_by_count:desc&per_page=10").json()
    nr_pages = data['meta']['count'] // 200 + 1

    for page in range(1, nr_pages + 1):
        response = requests.get(base_url, params={
            'page': page,
            'filter': f'authorships.institutions.lineage:{institute_id}',
            'sort': 'cited_by_count:desc',
            'per_page': 200
        })
        data = response.json()

        # Extract DOIs from the response
        for work in data.get('results', []):
            doi = work.get('doi')
            if doi:
                dois.append(doi)

    return dois

def main():
    parser = argparse.ArgumentParser(description="Fetch DOIs from OpenAlex API for a given institute ID and save them to a text file.")
    parser.add_argument("institute_id", type=str, help="The ID of the institute to filter the works by.")
    parser.add_argument("outputfile", type=str, help="The path to the output text file where the DOIs will be saved.")

    args = parser.parse_args()

    dois = get_dois_from_openalex(args.institute_id)

    # Write DOIs to the output file
    with open(args.outputfile, 'w') as file:
        for doi in dois:
            file.write(f"{doi}\n")

    print(f"DOIs have been saved to {args.outputfile}")

if __name__ == "__main__":
    main()

