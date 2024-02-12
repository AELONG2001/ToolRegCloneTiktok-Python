import requests

def handleGetCurrentProxyNo1Proxy(api_key):
    url = f"https://app.proxyno1.com/api/key-status/{api_key}"
    response = requests.get(url)
    data = response.json()
    https = f'{data["data"]["proxy"]["ip"]}:{data["data"]["proxy"]["HTTP_IPv4"]}'
    
    return https
