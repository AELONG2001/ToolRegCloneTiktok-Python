import requests

def handleCheckApiKeyAChi(api_key):
    url = "http://api.achicaptcha.com/createTask"
    body = {
        "clientKey": f"{api_key}",
        "task": {
            "type": "TiktokCaptchaTask",
            "subType": "2",
            "image":""
        }
    }

    response = requests.post(url, json=body).json()

    return response
