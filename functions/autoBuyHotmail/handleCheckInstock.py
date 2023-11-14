import requests

def handleCheckInstock(apikey):
    url = "https://api.hotmailbox.me/mail/currentstock"
    params = {
        "apikey": f"{apikey}",
    }

    response = requests.get(url, params=params).json()

    if "Data" not in response:
        return 0
        
    return response["Data"][0]["Instock"]
    
    
