import requests

def handleCheckKey(key, serial_number):
    body = {
        "key": key,
        "machine_code": serial_number
    }

    data = requests.post("http://localhost/api_check_key/api.php", body).json()
    print("data: ", data)

    return data