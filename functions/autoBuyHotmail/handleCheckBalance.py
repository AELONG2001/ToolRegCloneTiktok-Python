import requests

def handleCheckBalance(apikey):
    url = "https://api.hotmailbox.me/user/balance"
    params = {
        "apikey": f"{apikey}",
    }

    response = requests.get(url, params=params).json()

    return response
