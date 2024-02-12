import requests

def handleGetTask(token):
    url = "https://traodoisub.com/api"
    params = {
        "fields": "tiktok_follow",
        "access_token": token.strip()
    }
    response = requests.get(url, params=params)
    data = response.json()

    return data["data"]
