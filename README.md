# Python API Automation Task

This repository contains Python scripts to automate the testing of an API using Pytest and Python. The API provides several endpoints, and we aim to test the following operations:

- Create user endpoint "POST"
- List users endpoint "GET"
- Update the same created user "PUT"
- Delete user "DELETE"

## API Endpoint
The API endpoint we are testing is: https://reqres.in/

## Prerequisites
Before running the test cases, ensure you have the following installed:

- Python ([Download Python](https://www.python.org/downloads/))
- Requests library (to make API calls) - installed via `pip install requests`
- Pytest library (to run test cases) - installed via `pip install pytest`

## How to Run the Test Cases
1. Clone this repository to your local machine or download the files.
2. Navigate to the folder containing the `CLI_Tool.py` script using the command line.
3. Run the tests using the following command:

```bash
python CLI_Tool.py
```


This will execute all the test cases using Pytest and provide a summary of the test results.

## Test Cases
The test cases cover the following scenarios:

User creation, update, and delete are done successfully.
Verify that the response contains the expected response code and message.

## File Descriptions
CLI_Tool.py: This script contains the Python code to call the API endpoints and define the test cases using Pytest.