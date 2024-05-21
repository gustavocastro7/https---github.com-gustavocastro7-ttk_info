import json
import os
import requests
import datetime
from util.json_tools import print_json

PATH = "/open_api/v1.3/oauth2/access_token/"

# Function to load authentication details from JSON file
def load_auth_from_json(json_file_path):
    with open(json_file_path, 'r') as f:
        auth_data = json.load(f)
    return auth_data.get('secret'), auth_data.get('app_id'), auth_data.get('auth_code')

def build_url(path, query=""):
    # type: (str, str) -> str
    """
    Build request URL
    :param path: Request path
    :param query: Querystring
    :return: Request URL
    """
    scheme, netloc = "https", "business-api.tiktok.com"
    return "{0}://{1}{2}?{3}".format(scheme, netloc, path, query)

def post(json_str):
    # type: (str) -> requests.Response
    """
    Send POST request
    :param json_str: Args in JSON format
    :return: Response object
    """
    url = build_url(PATH)
    args = json.loads(json_str)
    headers = {
        "Content-Type": "application/json",
    }
    rsp = requests.post(url, headers=headers, json=args)
    return rsp

def request_access_token():
    # Load authentication details from JSON file
    secret, app_id, auth_code = load_auth_from_json("config/auth.json")

    # Args in JSON format
    my_args = {
        "secret": secret,
        "app_id": app_id,
        "auth_code": auth_code
    }

    # Send POST request
    response = post(json.dumps(my_args))

    # Check if request was successful
    if response.status_code == 200 and response.json().get('code') == 0:
        # Store the access token in a JSON file
        with open("config/access_token.json", 'w') as f:
            json.dump(response.json(), f)
    else:
        # Log the error message to a log file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_msg = f"Error: {response.status_code} - {response.text}"
        with open("log/log.txt", 'a', encoding='utf-8') as log_file:
            log_file.write(f"[{timestamp}] {error_msg}\n")

    print_json(response.json())

if __name__ == '__main__':
    request_access_token()
