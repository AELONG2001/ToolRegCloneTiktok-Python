import requests

def handleGetNewTinProxy(api_key):
    url = "https://api.tinproxy.com/proxy/get-new-proxy"
    params = {
        "api_key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    https = data["data"]["http_ipv4"]
    return https
