import requests
from PySide6.QtWidgets import *

def handleAutoBuyHotmail(api_key):
    try:
        email_password = ""
        params = {
            "apikey": f"{api_key.strip()}",
            "mailcode": "HOTMAIL",
            "quantity": 1
        }
    
        response = requests.get("https://api.hotmailbox.me/mail/buy", params=params).json()

        if "Message" in response and response["Message"] == "Bạn đã mua hàng thành công":
            email = response["Data"]["Emails"][0]["Email"]
            password = response["Data"]["Emails"][0]["Password"]
            email_password = f"{email}|{password}"
        else:
            email_password = ""
            
        return email_password
    except requests.exceptions.RequestException as e:
        print(e)