import requests

def handleConfirmTask(task_id, token):
    url = "https://traodoisub.com/api/coin"
    params = {
        "type": "TIKTOK_FOLLOW_CACHE",
        "id": task_id,
        "access_token": token.strip()
    }
    response = requests.get(url, params=params)
    data = response.json()
    print("data: ", data)
    
    return data["cache"]
