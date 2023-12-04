import requests
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from utils.utils import wait

def handleCreateJobGetHcaptcha(
    self, base64, current_row_count
):
    try:
        self.self_main.table_account_info.setItem(
            current_row_count,
            3,
            QTableWidgetItem("Đang đợi kết quả captcha..."),
        )
        QCoreApplication.processEvents()

        headers: {
            "Content-Type": "application/json",
            "apikey": "zkpro2001-39398ae8-0b66-e856-396d-8e4cd1f6eeec"
        }
        
        body = {
            "clientKey": "08f8b0f0b3aff156866a811508e2bb2e",
            "task": {
                "type": "TiktokCaptchaTask",
                "subType": "2",
                "image": base64,
            },
        }

        response = requests.post("free.nocaptchaai.com/solve", headers=headers, json=body)
        data = response.json()

        wait(6, 8)
        return data
    except requests.exceptions.RequestException as e:
        print(e)

def handleResolveHcaptcha(self, thread, driver):
    pass