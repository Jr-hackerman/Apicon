# Apicon - API Analyzer by @jrhackerman

**Apicon** is a command-line tool designed to analyze API documentation from both OpenAPI JSON files and Swagger URLs. The tool helps you count and list API endpoints, categorize them by HTTP methods (POST, GET, PUT, DELETE, etc.), and provide a summary of the total API structure. 

It is designed for quick and easy inspection of API documentation in both local and remote formats.

## Features
- **Count API Endpoints**: Count the number of API endpoints based on HTTP methods (GET, POST, etc.)
- **List Endpoints**: List all endpoints per method
- **Total Endpoint Count**: Display the total number of API endpoints across methods
- **URL Support**: Analyze Swagger documentation directly from URLs
- **Supports OpenAPI 3.0.1 and later**

## Installation
1. Clone the repository from GitHub:
```bash
git clone https://github.com/Jr-hackerman/apicon.git
cd apicon
```

2. Install required dependencies:
```bash
pip install requests
```

## Usage
```bash
python apicon.py (-f <path_to_json_file> | -u <swagger_url>) [-e]
```

Options:
- `-f, --file`: Path to the API documentation JSON file
- `-u, --url`: URL to the Swagger documentation
- `-e, --endpoints`: List all the API endpoints with their respective HTTP methods (optional)

Note: You must use either `-f` or `-u`, but not both.

Example commands:
```bash
# Analyze local file
python apicon.py -f api_doc.json

# Analyze remote Swagger documentation
python apicon.py -u https://api.example.com/swagger.json

# Show all endpoints from local file
python apicon.py -f api_doc.json -e

# Show all endpoints from URL
python apicon.py -u https://api.example.com/swagger.json -e
```
