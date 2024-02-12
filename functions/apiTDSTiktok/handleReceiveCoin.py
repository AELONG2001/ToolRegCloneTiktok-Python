import requests

def handleReceiveCoin(token):
    url = "https://traodoisub.com/api/coin"
    params = {
        "type": "TIKTOK_FOLLOW",
        "id": "TIKTOK_FOLLOW_API",
        "access_token": token.strip()
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if 'data' in data:
            return data["data"]
        else:
            print("Lỗi: Response không chứa key 'data'.")
            return None

    except Exception as e:
        print(f"Lỗi: {e}")
        return None
