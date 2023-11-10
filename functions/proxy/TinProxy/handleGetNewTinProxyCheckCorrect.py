import requests

def handleGetNewTinProxyCheckCorrect(api_list_key):
    url = "https://api.tinproxy.com/proxy/get-new-proxy"
    str_err = ""
    for api_key in api_list_key:
        response = requests.get(url, params={"api_key": api_key}).json()
        if "error" in response and response["error"] == "API Key không hợp lệ":
            str_err += f"Api Key {api_key} của TinProxy không chính xác\n"

    return str_err
