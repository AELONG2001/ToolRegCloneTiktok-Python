import requests
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from utils.utils import wait
from functions.handleMultiThreads.selenium.handleCode.handleSubmitCode import (
    handleSubmitCode,
)
from functions.handleMultiThreads.handleRestartThread.handleRestartThread import handleRestartThread
from functions.handleMultiThreads.handleRestartThread.handleRestartThreadNewMail import handleRestartThreadNewMail

def handleGetCodeFromMail(self):
    self.self_main.table_account_info.scrollToBottom()
    try:
        max_attempts = 5
        attempts = 0
        isCode = True
        while attempts < max_attempts and isCode:
            params = {
                "mail": self.username_mail,
                "pass": self.password_mail,
                "type": "tiktok"
            }

            url = f"https://tools.dongvanfb.net/api/get_code"
            self.self_main.table_account_info.setItem(
                self.current_row_count, 3, QTableWidgetItem("Đang lấy code...")
            )
            QCoreApplication.processEvents()
            wait(10, 12)
            response = requests.get(url, params=params)
            data = response.json()

            print("Data: ", data)

            if data["content"] == "Invalid email or password or IMAP disabled":
               self.self_main.table_account_info.setItem(
                self.current_row_count, 3, QTableWidgetItem("hotmail đã bị block...")
               )
               QCoreApplication.processEvents()
               print("Restart invalid mail")
               attempts = 0
               isCode = False
               self.driver.close()
               handleRestartThreadNewMail(self)
               return

            if data["code"]:
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Đã lấy được code đợi nhập..."),
                )
                QCoreApplication.processEvents()
                isCode = False
                attempts = 0
                handleSubmitCode(self, data["code"])
            else:
                isCode = True
                attempts += 1

        if attempts >= max_attempts:
            self.driver.close()
            handleRestartThread(self)
            return

    except requests.exceptions.RequestException as e:
        print(e)
