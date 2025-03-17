# Research Institute Summaries

## summary_gerbi

![mean_values_over_time_high_res.png](./data/fair_summary_gerbi/mean_values_over_time_high_res.png)

[Back to top](#table-of-contents)

![median_values_over_time_high_res.png](./data/fair_summary_gerbi/median_values_over_time_high_res.png)

[Back to top](#table-of-contents)

### failure_explanations.csv

| metric       | explanation                                                                                                                                 |   count |
|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------------|--------:|
| FsF-F3-01M   | WARNING: Valid data  identifier missing.                                                                                                    |      23 |
| FsF-A1-03D   | WARNING: Skipping protocol test for data since NO content  identifier is given in metadata                                                  |      23 |
| FsF-I1-01M   | INFO: Check of structured data  embedded in the data page                                                                                   |       6 |
| FsF-I1-01M   | INFO: RDFa like  serialization found in the data page - RDFa                                                                                |       6 |
| FsF-I1-01M   | SUCCESS: Found structured data  in the data page                                                                                            |       6 |
| FsF-I1-01M   | INFO: Check if RDF-based typed link included                                                                                                |       6 |
| FsF-I1-01M   | INFO: NO RDF-based typed link found                                                                                                         |       6 |
| FsF-I1-01M   | INFO: Check if RDF metadata available through content negotiation                                                                           |       6 |
| FsF-I1-01M   | INFO: NO RDF metadata available through content negotiation                                                                                 |       6 |
| FsF-I1-01M   | INFO: NO SPARQL endpoint found through re3data based on the object URI provided                                                             |       6 |
| FsF-R1.3-02D | WARNING: Could not perform file format checks as data content identifier unavailable/inaccesible                                            |      23 |
| FsF-R1.1-01M | WARNING: License information unavailable in metadata                                                                                        |      15 |
| FsF-R1.1-01M | INFO: Will consider all SPDX licenses as community specific licenses for FsF-R1.1-01M                                                       |      15 |
| FsF-R1.1-01M | WARNING: Skipping SPDX and community license verification since license information unavailable in metadata                                 |      15 |
| FsF-A1-01M   | INFO: Found CreativeCommons license -:                                                                                                      |       3 |
| FsF-A1-01M   | WARNING: Access condition looks like license, therefore the following is ignored -:                                                         |       3 |
| FsF-A1-01M   | WARNING: NO access information is available in metadata                                                                                     |      10 |
| FsF-A1-01M   | INFO: Skipping standard terms test since NO access information is available in metadata                                                     |      20 |
| FsF-A1-01M   | INFO: Skipping machine readablility test since NO access information is available in metadata                                               |      10 |
| FsF-A1-01M   | WARNING: Unable to determine the access level                                                                                               |      10 |
| FsF-R1.1-01M | INFO: License expressed as access condition , therefore moved from FsF-A1-01M -:                                                            |       3 |
| FsF-F4-01M   | INFO: Will exclusively consider community specific metadata standards for FsF-F4-01M-1 which are specified in metrics -:                    |       4 |
| FsF-F4-01M   | INFO: Will exclusively consider community specific metadata offering methods for FsF-F4-01M-1 which are specified in metrics -:             |       4 |
| FsF-F4-01M   | WARNING: Metadata is NOT found through -:                                                                                                   |       4 |
| FsF-F4-01M   | INFO: Querying DataCite API for -:                                                                                                          |       4 |
| FsF-F4-01M   | INFO: Identifier not listed in DataCite catalogue -:                                                                                        |       4 |
| FsF-F4-01M   | WARNING: Google Search Cache DB does not exist, see F-UJI installation instructions                                                         |       4 |
| FsF-F4-01M   | INFO: Identifier not listed in Google Dataset Search cache -:[' '                                                                           |       1 |
| FsF-F4-01M   | INFO: Querying Mendeley Data API for -:                                                                                                     |       5 |
| FsF-F4-01M   | INFO: Identifier not listed in Mendeley Data catalogue -:                                                                                   |       4 |
| FsF-F4-01M   | WARNING: Metadata is NOT found through registries considered by the assessment service  -:                                                  |       4 |
| FsF-I3-01M   | WARNING: Could not identify qualified related resources in metadata                                                                         |       5 |
| FsF-R1.2-01M | INFO: Check if provenance information is available in descriptive metadata                                                                  |       2 |
| FsF-R1.2-01M | INFO: Check if provenance information is available in metadata about related resources                                                      |       2 |
| FsF-R1.2-01M | WARNING: No provenance information found in metadata about related resources                                                                |       2 |
| FsF-R1.2-01M | INFO: Check if provenance specific namespaces are listed in metadata                                                                        |       2 |
| FsF-R1.2-01M | WARNING: Formal provenance metadata is unavailable                                                                                          |       2 |
| FsF-I3-01M   | INFO: No related resource found in Dublin Core metadata                                                                                     |       3 |
| FsF-R1-01MD  | INFO: Invalid resource type  specified -:                                                                                                   |       3 |
| FsF-R1-01MD  | ERROR: The evaluated resource does not identify itself as a “dataset” but as , so F-UJI may not be the right tool for this type of resource |       3 |
| FsF-R1-01MD  | WARNING: NO data object content available/accessible to perform file descriptors  tests                                                     |       5 |
| FsF-F4-01M   | INFO: Identifier not listed in Google Dataset Search cache -:['                                                                             |       3 |
| FsF-R1-01MD  | WARNING: No resource type given                                                                                                             |       2 |
| FsF-R1-01MD  | ERROR: The evaluated resource does not identify itself as a “dataset” so F-UJI may not be the right tool for this type of resource          |       2 |
| FsF-I3-01M   | INFO: No related resource found in Datacite metadata                                                                                        |       1 |

[Back to top](#table-of-contents)

### publisher_failures.csv

| publisher                                                     | metric       |   count |
|:--------------------------------------------------------------|:-------------|--------:|
| Zenodo                                                        | FsF-F3-01M   |      10 |
| Zenodo                                                        | FsF-A1-03D   |      10 |
| Zenodo                                                        | FsF-I1-01M   |      10 |
| Zenodo                                                        | FsF-R1.3-02D |      10 |
| Cold Spring Harbor Laboratory                                 | FsF-F3-01M   |      16 |
| Cold Spring Harbor Laboratory                                 | FsF-A1-03D   |      16 |
| Cold Spring Harbor Laboratory                                 | FsF-R1.1-01M |      16 |
| Cold Spring Harbor Laboratory                                 | FsF-R1.3-02D |      16 |
| bioRxiv                                                       | FsF-F3-01M   |       4 |
| bioRxiv                                                       | FsF-A1-03D   |       4 |
| bioRxiv                                                       | FsF-R1.1-01M |       4 |
| bioRxiv                                                       | FsF-R1.3-02D |       4 |
| F1000 Research Limited                                        | FsF-F3-01M   |       2 |
| F1000 Research Limited                                        | FsF-A1-01M   |       2 |
| F1000 Research Limited                                        | FsF-A1-03D   |       2 |
| F1000 Research Limited                                        | FsF-R1.1-01M |       2 |
| F1000 Research Limited                                        | FsF-R1.3-02D |       2 |
| Wiley                                                         | FsF-F3-01M   |       2 |
| Wiley                                                         | FsF-F4-01M   |       2 |
| Wiley                                                         | FsF-A1-01M   |       2 |
| Wiley                                                         | FsF-A1-03D   |       2 |
| Wiley                                                         | FsF-R1-01MD  |       2 |
| Wiley                                                         | FsF-R1.1-01M |       2 |
| Wiley                                                         | FsF-R1.3-02D |       2 |
| The Company of Biologists                                     | FsF-F3-01M   |       2 |
| The Company of Biologists                                     | FsF-A1-01M   |       2 |
| The Company of Biologists                                     | FsF-A1-03D   |       2 |
| The Company of Biologists                                     | FsF-R1.1-01M |       2 |
| The Company of Biologists                                     | FsF-R1.3-02D |       2 |
| arXiv.org                                                     | FsF-F3-01M   |       1 |
| arXiv.org                                                     | FsF-A1-01M   |       1 |
| arXiv.org                                                     | FsF-A1-03D   |       1 |
| arXiv.org                                                     | FsF-I1-01M   |       1 |
| arXiv.org                                                     | FsF-I3-01M   |       1 |
| arXiv.org                                                     | FsF-R1.3-02D |       1 |
| arXiv                                                         | FsF-F3-01M   |       1 |
| arXiv                                                         | FsF-A1-01M   |       1 |
| arXiv                                                         | FsF-A1-03D   |       1 |
| arXiv                                                         | FsF-I1-01M   |       1 |
| arXiv                                                         | FsF-I3-01M   |       1 |
| arXiv                                                         | FsF-R1.3-02D |       1 |
| Nature Publishing Group US                                    | FsF-F3-01M   |       2 |
| Nature Publishing Group US                                    | FsF-A1-03D   |       2 |
| Nature Publishing Group US                                    | FsF-R1.1-01M |       1 |
| Nature Publishing Group US                                    | FsF-R1.3-02D |       2 |
| Nature Publishing Group                                       | FsF-F3-01M   |       4 |
| Nature Publishing Group                                       | FsF-A1-03D   |       4 |
| Nature Publishing Group                                       | FsF-R1.1-01M |       2 |
| Nature Publishing Group                                       | FsF-R1.3-02D |       4 |
| Springer Nature                                               | FsF-F3-01M   |       2 |
| Springer Nature                                               | FsF-A1-03D   |       2 |
| Springer Nature                                               | FsF-R1.1-01M |       1 |
| Springer Nature                                               | FsF-R1.3-02D |       2 |
| Nature                                                        | FsF-F3-01M   |       2 |
| Nature                                                        | FsF-A1-03D   |       2 |
| Nature                                                        | FsF-R1.1-01M |       1 |
| Nature                                                        | FsF-R1.3-02D |       2 |
| TIB Open Publishing                                           | FsF-F3-01M   |       2 |
| TIB Open Publishing                                           | FsF-A1-03D   |       2 |
| TIB Open Publishing                                           | FsF-R1.1-01M |       2 |
| TIB Open Publishing                                           | FsF-R1.3-02D |       2 |
| TIB Open Publishing (Technische Informationsbibliothek (TIB)) | FsF-F3-01M   |       1 |
| TIB Open Publishing (Technische Informationsbibliothek (TIB)) | FsF-A1-03D   |       1 |
| TIB Open Publishing (Technische Informationsbibliothek (TIB)) | FsF-R1.1-01M |       1 |
| TIB Open Publishing (Technische Informationsbibliothek (TIB)) | FsF-R1.3-02D |       1 |
| Springer Berlin Heidelberg                                    | FsF-F3-01M   |       2 |
| Springer Berlin Heidelberg                                    | FsF-A1-03D   |       2 |
| Springer Berlin Heidelberg                                    | FsF-R1.3-02D |       2 |
| Springer                                                      | FsF-F3-01M   |       1 |
| Springer                                                      | FsF-A1-03D   |       1 |
| Springer                                                      | FsF-R1.3-02D |       1 |
| SpringerLink                                                  | FsF-F3-01M   |       1 |
| SpringerLink                                                  | FsF-A1-03D   |       1 |
| SpringerLink                                                  | FsF-R1.3-02D |       1 |
| Springer Science and Business Media LLC                       | FsF-F3-01M   |       2 |
| Springer Science and Business Media LLC                       | FsF-A1-03D   |       2 |
| Springer Science and Business Media LLC                       | FsF-R1.3-02D |       2 |
| F1000 Research Ltd                                            | FsF-F3-01M   |       2 |
| F1000 Research Ltd                                            | FsF-A1-01M   |       2 |
| F1000 Research Ltd                                            | FsF-A1-03D   |       2 |
| F1000 Research Ltd                                            | FsF-R1.1-01M |       2 |
| F1000 Research Ltd                                            | FsF-R1.3-02D |       2 |

[Back to top](#table-of-contents)

### test_results.csv

| test_id      |   pass |   fail |
|:-------------|-------:|-------:|
| FsF-F1-01D   |     23 |      0 |
| FsF-F1-02D   |     23 |      0 |
| FsF-F2-01M   |     23 |      0 |
| FsF-F3-01M   |      0 |     23 |
| FsF-F4-01M   |     19 |      4 |
| FsF-A1-01M   |     13 |     10 |
| FsF-A1-02M   |     23 |      0 |
| FsF-A1-03D   |      0 |     23 |
| FsF-I1-01M   |     17 |      6 |
| FsF-I2-01M   |     23 |      0 |
| FsF-I3-01M   |     18 |      5 |
| FsF-R1-01MD  |     18 |      5 |
| FsF-R1.1-01M |      8 |     15 |
| FsF-R1.2-01M |     21 |      2 |
| FsF-R1.3-01M |     23 |      0 |
| FsF-R1.3-02D |      0 |     23 |

[Back to top](#table-of-contents)

