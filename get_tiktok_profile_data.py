import json
import requests

def get_tiktok_profile_data(access_token, business_id, start_date=None, end_date=None, fields=None):
    """
    Fetch profile data of a TikTok account.

    Args:
    - access_token (str): Access token authorized by TikTok creators.
    - business_id (str): Application specific unique identifier for the TikTok account.
    - start_date (str, optional): Query start date in the format 'YYYY-MM-DD'. Default is 7 days ago.
    - end_date (str, optional): Query end date in the format 'YYYY-MM-DD'. Default is yesterday.
    - fields (list of str, optional): Requested fields to retrieve. Default is ['display_name', 'profile_image'].

    Returns:
    - dict: Profile data of the TikTok account.
    """
    endpoint = "https://business-api.tiktok.com/open_api/v1.3/business/get/"
    headers = {"Access-Token": access_token}
    params = {
        "business_id": business_id,
        "start_date": start_date,
        "end_date": end_date,
        "fields": fields
    }
    response = requests.get(endpoint, headers=headers, params=params)
    return response.json()

def main():
    # Read access token from JSON file
    with open("config/access_token.json") as f:
        access_token = json.load(f)["data"]["access_token"]

    # Read business ID from JSON file
    with open("config/business_id.json") as f:
        business_id = json.load(f)["business_id"]

    # Fetch profile data
    profile_data = get_tiktok_profile_data(access_token, business_id)

    # Print profile data
    print("Profile Data:")
    print(profile_data)

if __name__ == "__main__":
    main()
