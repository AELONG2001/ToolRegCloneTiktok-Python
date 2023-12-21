import requests
from PySide6.QtWidgets import *

def handleAutoBuyHotmail(self):
    try:
        email_password = ""
        params = {
            "apikey": f"{self.api_key_hotmailbox.strip()}",
            "mailcode": "HMAIL",
            "quantity": 1
        }
        
        response = requests.get("https://hotmailbase.com/api/user/buy", params=params).json()

        if "Message" in response and response["Message"] == "Success":
            email = response["Emails"][0]["email"]
            password = response["Emails"][0]["password"]
            email_password = f"{email}|{password}"
        else:
            email_password = ""
            
        return email_password
    except requests.exceptions.RequestException as e:
        print(e)