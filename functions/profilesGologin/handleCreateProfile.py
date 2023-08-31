import requests
import os


def handleCreateProfile():
    try:
        api_token_gologin = os.getenv("API_TOKEN_GOLOGIN")

        url = "https://api.gologin.com/browser/64eff7cbc759ff37b48c62a7/clone"
        headers = {
            "Authorization": f"Bearer {api_token_gologin}",
            "Content-Type": "application/json",
        }

        response = requests.post(url, headers=headers)
        profile = response.json()

        return profile["id"]

    except requests.exceptions.RequestException as e:
        print(e)
