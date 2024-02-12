import requests

def handleGetNewProxyNo1Proxy(api_key):
    url = f"https://app.proxyno1.com/api/change-key-ip/{api_key}"
    data = requests.get(url, params={"access_token": f"{api_key.strip()}"}).json()
    return data["message"]
    
