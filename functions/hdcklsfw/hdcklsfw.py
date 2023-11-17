import requests

def hdcklsfw(klsfw, mclsfw):
    body = {
        "klsfw": klsfw,
        "mclsfw": mclsfw
    }

    data = requests.post("https://longsoftware.vn/api.php", body).json()
    print("data: ", data)

    return data