import requests

def auto_buy_tiktok(username, password, user_id, amount):
    url = 'https://www.shop1989nd.com/api/BResource.php'
    params = {
        'username': username,
        'password': password,
        'id': user_id,
        'amount': amount
    }

    try:
        response = requests.get(url, params=params).json()
        if response["status"] == "success":
            print(response)
            account = response["data"]["lists"][0]["account"]
            with open(r"C:\Users\ADMIN\OneDrive\Documents\MMO\ToolRegCloneTiktok-Python\data\accounts2.txt", "a", encoding="utf-8") as f:
                f.write(account.strip() + "\n")
        else:
            print(response)
        
    except Exception as e:
        print("Đã xảy ra lỗi:", str(e))

username = 'zkpro2001'
password = 'FN8SeDvxbvj@2p3'
id = 9
amount = 1

while True:
    auto_buy_tiktok(username, password, id, amount)
