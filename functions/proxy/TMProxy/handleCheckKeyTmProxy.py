import requests

def handleCheckKeyTmProxy(list_api_key):
    url = "https://tmproxy.com/api/proxy/stats"
    str_err = ""
    for api_key in list_api_key:
        response = requests.post(url, json={"api_key": f"{api_key}"}).json()
        if "message" in response and response["message"] == "API không tồn tại":
            str_err += f"Api Key {api_key} của TMProxy không chính xác\n"
    
    return str_err
