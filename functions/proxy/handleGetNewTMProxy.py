import requests


def handleGetNewTMProxy(self):
    api_key_tmproxy = self.proxy_value.toPlainText()
    api_key_list = api_key_tmproxy.splitlines()
    list_proxy = []

    url = "https://tmproxy.com/api/proxy/get-new-proxy"

    for key in api_key_list:
        response = requests.post(url, json={"api_key": f"{key}"})
        data = response.json()
        https = data["data"]["https"]
        list_proxy.append(https)

    return list_proxy
