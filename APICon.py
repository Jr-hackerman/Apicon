import json
import argparse
import requests
from urllib.parse import urlparse

# ASCII Art Banner for Apicon
banner = r"""
    ___        _           
   /   |  ____(_)___  ____ _
  / /| | / ___/ / ** \/ ** `/
 / ___ |/ /  / / /_/ / /_/ / 
/_/  |_/_/  /_/ .___/\__,_/  
            /_/       by @jrhackerman
"""

def validate_url(url):
    """Validate if the given string is a proper URL"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def fetch_swagger_doc(url):
    """Fetch Swagger documentation from URL"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Swagger documentation: {e}")
        return None

def analyze_api(api_data):
    """Analyze API documentation and return statistics"""
    method_counts = {}
    method_endpoints = {}

    # Iterate over the paths in the API documentation
    for path, methods in api_data.get('paths', {}).items():
        for method in methods:
            # Count occurrences of each HTTP method
            method = method.lower()
            if method in method_counts:
                method_counts[method] += 1
            else:
                method_counts[method] = 1
            
            # Store endpoints by method
            if method in method_endpoints:
                method_endpoints[method].append(path)
            else:
                method_endpoints[method] = [path]
    
    return method_counts, method_endpoints

def print_analysis(method_counts, method_endpoints, show_endpoints=False):
    """Print analysis results"""
    print("\nCounts of each HTTP method:")
    for method, count in method_counts.items():
        print(f"{method.upper()}: {count}")

    # Print the total number of endpoints across all methods
    total_endpoints = sum(method_counts.values())
    print(f"\nTotal endpoints (all methods): {total_endpoints}")

    # If the user wants to list the endpoints, display them
    if show_endpoints:
        print("\nEndpoints by method:")
        for method, endpoints in method_endpoints.items():
            print(f"\n{method.upper()} Endpoints:")
            for endpoint in sorted(endpoints):
                print(endpoint)

def main():
    print(banner)
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Analyze API endpoints from JSON file or Swagger URL")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', type=str, help="Path to the API documentation JSON file")
    group.add_argument('-u', '--url', type=str, help="URL to the Swagger documentation")
    parser.add_argument('-e', '--endpoints', action='store_true', help="List the API endpoints for all methods")
    
    # Parse the arguments
    args = parser.parse_args()

    # Load the API documentation
    api_data = None
    if args.file:
        try:
            with open(args.file, 'r') as file:
                api_data = json.load(file)
        except Exception as e:
            print(f"Error reading file: {e}")
            return
    
    elif args.url:
        if not validate_url(args.url):
            print("Error: Invalid URL format")
            return
        api_data = fetch_swagger_doc(args.url)
        if not api_data:
            return

    # Analyze and print results
    if api_data:
        method_counts, method_endpoints = analyze_api(api_data)
        print_analysis(method_counts, method_endpoints, args.endpoints)

if __name__ == "__main__":
    main()
