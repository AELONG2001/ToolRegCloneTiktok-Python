import requests


def handleGetNewShopLikeProxy(api_key):
    https = ""
    url = "http://proxy.shoplike.vn/Api/getNewProxy"
    response = requests.get(url, params={"access_token": f"{api_key.strip()}"})
    data = response.json()
    if "data" in response:
        https = data["data"]["proxy"]
    else:
        https = ""
    
    return https

    
