import requests

token = "7011841321:AAF3SCDIxgb6Jpv7MpDZIj9-UdpVcatc4oA"
chat_id = "6336555400"

with open("data/accounts2.txt", "r", encoding="utf-8") as f:
    accounts = f.readlines()

for account in accounts:
    message = account.split("|")[0]
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()
