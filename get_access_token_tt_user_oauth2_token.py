import requests
from util.json_tools import print_json

def get_access_token(client_id, client_secret, auth_code, redirect_uri):
    """
    Get a TikTok account access token.

    Args:
    - client_id (str): ID of your developer application.
    - client_secret (str): Secret of your developer application.
    - auth_code (str): The authorization code received after user authorization.
    - redirect_uri (str): The redirect URL which the client will be directed to.

    Returns:
    - dict: Response data containing access token and related information.
    """
    endpoint = "https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/token/"
    headers = {"Content-Type": "application/json"}
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "authorization_code",
        "auth_code": auth_code,
        "redirect_uri": redirect_uri
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    return response.json()

# Example usage:
client_id = "7368653044747075601"
client_secret = "1d71aaad557d3c130e38241941246b6da1e54837"
auth_code = "9d9e91e732b41639bfe2b949b286ccc789451499"
redirect_uri = "https://diotmedia.framer.website/ttkinfo"
response_data = get_access_token(client_id, client_secret, auth_code, redirect_uri)
print_json(response_data)
