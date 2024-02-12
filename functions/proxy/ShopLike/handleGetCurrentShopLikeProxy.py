import requests

def handleGetCurrentShopLikeProxy(api_key):
    url = "http://proxy.shoplike.vn/Api/getCurrentProxy"
    response = requests.get(url, params={"access_token": f"{api_key.strip()}"})
    data = response.json()
    https = data["data"]["proxy"]
    
    return https
