import random
import requests
import os


def handleDeleteProfile(profile_id):
    try:
        api_token_gologin = os.getenv("API_TOKEN_GOLOGIN")

        url = f"https://api.gologin.com/browser/{profile_id}"
        headers = {
            "Authorization": f"Bearer {api_token_gologin}",
            "Content-Type": "application/json",
        }

        requests.delete(url, headers=headers)

    except requests.exceptions.RequestException as e:
        print(e)
