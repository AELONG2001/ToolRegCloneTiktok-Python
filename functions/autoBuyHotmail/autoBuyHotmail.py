import requests

def handleAutoBuyHotmail(api_key):
    try:
        isBuyMailAgain = True
        email_password = ""
        while isBuyMailAgain:
            params = {
                "apikey": f"{api_key}",
                "mailcode": "HOTMAIL",
                "quantity": 1
            }
        
            response = requests.get("https://api.hotmailbox.me/mail/buy", params=params).json()

            if "Message" in response:
                if response["Message"] == "Bạn đã mua hàng thành công":
                    email = response["Data"]["Emails"][0]["Email"]
                    password = response["Data"]["Emails"][0]["Password"]
                    email_password = f"{email}|{password}"
                    isBuyMailAgain = False
                elif response["Message"] == "Tồn trên hệ thống không đủ":
                    isBuyMailAgain = True
                else:
                   isBuyMailAgain = False
                   email_password = ""    
            else:
                isBuyMailAgain = True

        return email_password
    except requests.exceptions.RequestException as e:
        print(e)