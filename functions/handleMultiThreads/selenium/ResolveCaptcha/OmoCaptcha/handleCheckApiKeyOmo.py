import requests

def handleCheckApiKeyOmo(api_key):
    try:
        url = "https://omocaptcha.com/api/getBalance"
        body = {
            "api_token": f"{api_key}",
        }

        response = requests.post(url, json=body).json()
        return response
    except requests.exceptions.RequestException:
        return "api key not correct"