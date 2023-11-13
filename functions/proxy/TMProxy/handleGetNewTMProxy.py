import requests


def handleGetNewTMProxy(api_key):
    url = "https://tmproxy.com/api/proxy/get-new-proxy"
    response = requests.post(url, json={"api_key": f"{api_key.strip()}"})
    data = response.json()
    https = data["data"]["https"]

    return https
