import requests


def handleGetCurrentTMProxy(api_key):
    url = "https://tmproxy.com/api/proxy/get-current-proxy"
    response = requests.post(url, json={"api_key": f"{api_key}"})
    data = response.json()
    https = data["data"]["https"]

    return https
