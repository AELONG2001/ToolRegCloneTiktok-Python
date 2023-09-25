import requests
from utils.utils import generate_random_name
import json

def handleCreateProfile(proxy):
    random_name = generate_random_name()
    ip, port = proxy.split(":")
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
                        "username": "",
                        "password": ""
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
        response = requests.post(url, headers=headers, json=body)
        profile = response.json()

        return profile["id"]

    except requests.exceptions.RequestException as e:
        print(e)
