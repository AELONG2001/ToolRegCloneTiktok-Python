import requests

def handleGetListProfile(token):
    url = "https://api.gologin.com/browser/v2"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers).json()
    return response["profiles"]
