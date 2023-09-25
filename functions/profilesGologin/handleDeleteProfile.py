import requests
import json

def handleDeleteProfile(profile_id):
    try:
        with open("configs_account.json", "r") as json_file:
           data = json.load(json_file)

        api_token_gologin = data["api_token_gologin"]

        url = f"https://api.gologin.com/browser/{profile_id}"
        headers = {
            "Authorization": f"Bearer {api_token_gologin}",
            "Content-Type": "application/json",
        }

        requests.delete(url, headers=headers)

    except requests.exceptions.RequestException as e:
        print(e)
