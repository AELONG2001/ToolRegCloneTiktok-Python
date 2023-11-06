import requests

def handleCheckKey(key, serial_number):
    body = {
        "key": key,
        "machine_code": serial_number
    }

    data = requests.post("https://longsoftware.click/api.php", body).json()
    print("data: ", data)

    return data