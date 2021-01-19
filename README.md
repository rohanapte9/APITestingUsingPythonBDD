# APITestingUsingPythonBDD
This is a Python BDD Framework created to test the APIs provided by https://www.metaweather.com/api/.

The framework is created in such a way that there is a separate feature folder for every feature:

- _Location Search_ (Currently implemented with 3 automated scenarios)
- _Location_ (Will be implemented very soon)
- _Location Day_ (Will be implemented very soon) Manual Scenarios are present in Task 2 All Scenarios.xlsx

Each Feature folders have

- _Feature File_
- _Glue Code_ (Implementation of the Steps)
- _Test Data_
- _Dependencies_
- _Python 3_
- _All the modules mentioned in the requirements.txt_

## How to Run

In order to run all the tests that are present currently out of the box, just run python RunWithReports.py

## Configurations: 

Tests can have customized tags in the feature file in order to create group of tests for specific purpose. 

Modification Can be done in RunWithReports.py 

`tagOptions = ' --tags=<tag_name> '` to run all tests with a specific tag

## Reports

Reports are present in HTML and JSON format under reporting_folder_json_html
