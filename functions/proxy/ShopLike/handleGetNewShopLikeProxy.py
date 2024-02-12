import requests


def handleGetNewShopLikeProxy(api_key):
    isGetProxyAgain = True
    https = ""
    while isGetProxyAgain:
        url = "http://proxy.shoplike.vn/Api/getNewProxy"
        response = requests.get(url, params={"access_token": f"{api_key.strip()}"})
        data = response.json()
        if "data" in data:
            https = data["data"]["proxy"]
            isGetProxyAgain = False
        else:
            if "mess" in data:
                if data["mess"] == "Het proxy, thu lai sau":
                    isGetProxyAgain = True
                else:
                    https = ""
                    isGetProxyAgain = False
    return https

    
