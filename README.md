# Apicon - API Analyzer by @jrhackerman

**Apicon** is a command-line tool designed to analyze API documentation from OpenAPI JSON files. The tool helps you count and list API endpoints, categorize them by HTTP methods (POST, GET, PUT, DELETE, etc.), and provide a summary of the total API structure. 

It is designed for quick and easy inspection of API documentation in JSON format.

## Features

- **Count API Endpoints**: Count the number of API endpoints based on HTTP methods (GET, POST, etc.).
- **List Endpoints**: List all endpoints per method.
- **Total Endpoint Count**: Display the total number of API endpoints across methods.
- **Supports OpenAPI 3.0.1 and later**.

## Installation

1. Clone the repository from GitHub:

```bash
git clone https://github.com/Jr-hackerman/apicon.git

cd apicon

## Usage

python apicon.py -f <path_to_json_file> [-e]

Options:
-f, --file: Path to the API documentation JSON file (required).
-e, --endpoints: List all the API endpoints with their respective HTTP methods (optional).
