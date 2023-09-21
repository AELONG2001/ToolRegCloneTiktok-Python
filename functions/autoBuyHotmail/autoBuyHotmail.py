import requests

def handleAutoBuyHotmail():
    try:
        params = {
            "apikey": "919cadef6eb94c3d83a6b312c49b66ed",
            "mailcode": "HOTMAIL",
            "quantity": 1
        }
       
        response = requests.get("https://api.hotmailbox.me/mail/buy", params=params)
        data = response.json()

        for mail in data["Data"]["Emails"]:
              email = mail.get("Email", "")
              password = mail.get("Password", "")
              email_password = f"{email}|{password}"

        return email_password
    except requests.exceptions.RequestException as e:
        print(e)