import requests

def handleCheckTokenGologin(token):
    url = "https://api.gologin.com/user"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers).json()

    return response
