import requests
from utils.utils import generate_random_name
import json
from PySide6.QtWidgets import *

def handleCreateProfile(self):
    random_name = generate_random_name()
    username_proxy = ""
    password_proxy = ""
    if len(self.proxy.split(":")) > 2:
        get_proxy = self.proxy.split(":")
        ip = get_proxy[0]
        port = get_proxy[1]
        username_proxy = get_proxy[2]
        password_proxy = get_proxy[3]
    else:
       if ':' in self.proxy:
            ip, port = self.proxy.split(":")
       else:
           self.self_main.table_account_info.setItem(
              self.current_row_count, 3, QTableWidgetItem("Lỗi proxy...")
           )
           ip = ""
           port = ""
       
    try:
        with open("configs_account.json", "r") as json_file:
           data = json.load(json_file)

        api_token_gologin = data["api_token_gologin"]

        url = "https://api.gologin.com/browser"
        headers = {
            "Authorization": f"Bearer {api_token_gologin}",
            "Content-Type": "application/json",
        }
        body = {
                    "name": f"{random_name}",
                    "notes": "string",
                    "browserType": "chrome",
                    "os": "lin",
                    "startUrl": "string",
                    "googleServicesEnabled": False,
                    "lockEnabled": False,
                    "debugMode": False,
                    "navigator": {
                        "userAgent": "string",
                        "resolution": "string",
                        "language": "string",
                        "platform": "string",
                        "doNotTrack": False,
                        "hardwareConcurrency": 0,
                        "deviceMemory": 1,
                        "maxTouchPoints": 0
                    },
                    "geoProxyInfo": {},
                    "storage": {
                        "local": True,
                        "extensions": True,
                        "bookmarks": True,
                        "history": True,
                        "passwords": True,
                        "session": True
                    },
                    "proxyEnabled": False,
                    "proxy": {
                        "mode": "http",
                        "host": f"{ip}",
                        "port": f"{port}",
                        "username": f"{username_proxy}",
                        "password": f"{password_proxy}"
                    },
                    "dns": "string",
                    "plugins": {
                        "enableVulnerable": True,
                        "enableFlash": True
                    },
                    "timezone": {
                        "enabled": True,
                        "fillBasedOnIp": True,
                        "timezone": "string"
                    },
                    "audioContext": {
                        "mode": "off",
                        "noise": 0
                    },
                    "canvas": {
                        "mode": "off",
                        "noise": 0
                    },
                    "fonts": {
                        "families": [
                            "string"
                        ],
                        "enableMasking": True,
                        "enableDomRect": True
                    },
                    "mediaDevices": {
                        "videoInputs": 0,
                        "audioInputs": 0,
                        "audioOutputs": 0,
                        "enableMasking": False
                    },
                    "webRTC": {
                        "mode": "alerted",
                        "enabled": True,
                        "customize": True,
                        "localIpMasking": False,
                        "fillBasedOnIp": True,
                        "publicIp": "string",
                        "localIps": [
                            "string"
                        ]
                    },
                    "webGL": {
                        "mode": "noise",
                        "getClientRectsNoise": 0,
                        "noise": 0
                    },
                    "clientRects": {
                        "mode": "noise",
                        "noise": 0
                    },
                    "webGLMetadata": {
                        "mode": "mask",
                        "vendor": "string",
                        "renderer": "string"
                    },
                    "webglParams": [],
                    "profile": "string",
                    "googleClientId": "string",
                    "updateExtensions": True,
                    "chromeExtensions": [
                        "string"
                    ]
                }
        profile = requests.post(url, headers=headers, json=body).json()        
        return profile["id"]

    except requests.exceptions.RequestException as e:
        print(e)