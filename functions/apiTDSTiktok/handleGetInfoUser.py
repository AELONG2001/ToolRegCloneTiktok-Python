import requests

def handleGetInfoUser(token):
    url = "https://traodoisub.com/api"
    params = {
        "fields": "profile",
        "access_token": token.strip()
    }
    response = requests.get(url, params=params)
    data = response.json()

    return data["data"]
