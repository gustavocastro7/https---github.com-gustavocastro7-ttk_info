# coding=utf\-8
import json
import requests
from util.json_tools import print_json

from six import string_types
from six.moves.urllib.parse import urlencode, urlunparse # noqa

ACCESS_TOKEN = "xxx"
PATH = "/open_api/v1.3/user/info/"

def build_url(path, query=""):
    """
    Build request URL
    :param path: Request path
    :param query: Querystring
    :return: Request URL
    """
    scheme, netloc = "https", "business-api.tiktok.com"
    return urlunparse((scheme, netloc, path, "", query, ""))
    
def get(json_str):
    # type: (str) -> dict
    """
    Send GET request
    :param json_str: Args in JSON format
    :return: Response in JSON format
    """
    args = json.loads(json_str)
    query_string = urlencode({k: v if isinstance(v, string_types) else json.dumps(v) for k, v in args.items()})
    url = build_url(PATH, query_string)
    headers = {
        "Access-Token": "250398bba11e2624bd102f38e2f414c856491a06",
    }
    rsp = requests.get(url, headers=headers)
    return rsp.json()
    
if __name__ == '__main__':

    # Args in JSON format
    my_args = "{}"
    print_json(get(my_args))
    
