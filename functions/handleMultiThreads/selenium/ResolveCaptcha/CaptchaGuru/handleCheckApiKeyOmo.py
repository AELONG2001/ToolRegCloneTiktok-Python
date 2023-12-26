import requests

def handleCheckApiKeyOmo(api_key):
    url = "https://omocaptcha.com/api/getBalance"
    body = {
        "api_token": f"{api_key}",
    }

    response = requests.post(url, json=body)
    if "balance" in response.text:
        return response.json()
    else:
        return "api key not correct"
        