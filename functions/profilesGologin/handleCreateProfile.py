import requests
from utils.utils import generate_random_name
import json
from PySide6.QtWidgets import *
from gologin import GoLogin

def handleCreateProfile(self):
    random_name = generate_random_name()
    ip = self.proxy.split(":")[0]
    port = self.proxy.split(":")[1]
    # if len(self.proxy.split(":")) > 2:
    #     get_proxy = self.proxy.split(":")
    #     ip = get_proxy[0]
    #     port = get_proxy[1]
    #     username_proxy = get_proxy[2]
    #     password_proxy = get_proxy[3]
    # else:
    #    if ':' in self.proxy:
    #         ip, port = self.proxy.split(":")
    #    else:
    #        self.self_main.table_account_info.setItem(
    #           self.current_row_count, 3, QTableWidgetItem("Lỗi proxy...")
    #        )
    #        ip = ""
    #        port = ""
       
    try:
        with open("configs_account.json", "r") as json_file:
           data = json.load(json_file)

        gl = GoLogin({
            "token": data["api_token_gologin"],
        })

        # api_token_gologin = data["api_token_gologin"]

        # url = "https://api.gologin.com/browser"
        # headers = {
        #     "Authorization": f"Bearer {api_token_gologin}",
        #     "Content-Type": "application/json",
        # }
        profile_id = gl.create({
        "name": random_name,
        "os": 'win',
        "browserType": "chrome",
        "navigator": {
            "language": 'vi',
            "userAgent": 'random',
            "resolution": 'random',
            "platform": 'win',
        },
        'proxyEnabled': False,
        'proxy': {
            'mode': 'http',
            'host': f"{ip}",
            'port': f"{port}",
            'username': "",
            'password': ""
        },
        "webRTC": {
            "mode": "alerted",
            "enabled": True,
        },
        });
        # profile = requests.post(url, headers=headers, json=body).json()        
        # return profile["id"]
        return profile_id

    except requests.exceptions.RequestException as e:
        print(e)