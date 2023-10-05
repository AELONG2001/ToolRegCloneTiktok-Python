import requests

def handleAutoBuyHotmail():
    try:
        isBuyMailAgain = True
        email_password = ""
        while isBuyMailAgain:
            params = {
                "apikey": "919cadef6eb94c3d83a6b312c49b66ed",
                "mailcode": "HOTMAIL",
                "quantity": 1
            }
        
            response = requests.get("https://api.hotmailbox.me/mail/buy", params=params)
            data = response.json()

            if "Message" in data:
                if data["Message"] == "Số dư tài khoản không đủ":
                    isBuyMailAgain = False
                    email_password = ""
                    return
                if data["Message"] == "Bạn đã mua hàng thành công":
                    email = data["Data"]["Emails"][0]["Email"]
                    password = data["Data"]["Emails"][0]["Password"]
                    email_password = f"{email}|{password}"
                    isBuyMailAgain = False
            else:
                isBuyMailAgain = True

        return email_password
    except requests.exceptions.RequestException as e:
        print(e)