import requests

def handleGetNewTMProxyToCheckExpired(list_api_key):
    url = "https://tmproxy.com/api/proxy/get-new-proxy"
    str_err = ""
    for api_key in list_api_key:
        response = requests.post(url, json={"api_key": f"{api_key}"}).json()
        if "message" in response and response["message"] == "Gói Hết hạn":
            str_err += f"Api Key {api_key} của TMProxy đã hết hạn\n"
    
    return str_err
