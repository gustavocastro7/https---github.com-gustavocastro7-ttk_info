import json

def print_json(data):
    """
    Print JSON data in a formatted way.

    Args:
    - data (dict): JSON data to be printed.
    """
    formatted_json = json.dumps(data, indent=4)
    print(formatted_json)
