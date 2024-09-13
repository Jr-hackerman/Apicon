import json
import argparse

# ASCII Art Banner for Apicon
banner = r"""
    ___        _           
   /   |  ____(_)___  ____ _
  / /| | / ___/ / __ \/ __ `/
 / ___ |/ /  / / /_/ / /_/ / 
/_/  |_/_/  /_/ .___/\__,_/  
            /_/       by @jrhackerman
"""

print(banner)

# Set up argument parser
parser = argparse.ArgumentParser(description="Analyze API endpoints in a JSON file")
parser.add_argument('-f', '--file', type=str, required=True, help="Path to the API documentation JSON file")
parser.add_argument('-e', '--endpoints', action='store_true', help="List the API endpoints for all methods")

# Parse the arguments
args = parser.parse_args()

# Load the JSON data from the file
with open(args.file, 'r') as file:
    api_data = json.load(file)

# Initialize counters and lists for all methods
method_counts = {}
method_endpoints = {}

# Iterate over the paths in the API documentation
for path, methods in api_data['paths'].items():
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

# Print the counts for each method
print("\nCounts of each HTTP method:")
for method, count in method_counts.items():
    print(f"{method.upper()}: {count}")

# Print the total number of endpoints across all methods
total_endpoints = sum(method_counts.values())
print(f"\nTotal endpoints (all methods): {total_endpoints}")

# If the user wants to list the endpoints, display them
if args.endpoints:
    print("\nEndpoints by method:")
    for method, endpoints in method_endpoints.items():
        print(f"\n{method.upper()} Endpoints:")
        for endpoint in endpoints:
            print(endpoint)
