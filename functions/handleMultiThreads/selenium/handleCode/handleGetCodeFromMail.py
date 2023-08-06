import requests
from PySide6.QtWidgets import *
from utils.utils import wait
from functions.handleMultiThreads.selenium.handleCode.handleSubmitCode import (
    handleSubmitCode,
)


def handleGetCodeFromMail(self, thread, driver):
    try:
        isGetCodeMailAgain = True
        while isGetCodeMailAgain and not self.stop_flag:
            if self.table_account_info.item(thread, 0) is not None:
                username = self.table_account_info.item(thread, 0).text()
            if self.table_account_info.item(thread, 1) is not None:
                password = self.table_account_info.item(thread, 1).text()

            url = f"https://tools.dongvanfb.net/api/get_code?mail={username}&pass={password}&type=tiktok"
            self.table_account_info.setItem(
                thread, 3, QTableWidgetItem("Đang lấy code...")
            )
            wait(4, 6)
            response = requests.get(url)
            data = response.json()

            print("Data: ", data)

            if data["code"]:
                self.table_account_info.setItem(
                    thread, 3, QTableWidgetItem("Đã lấy được code đợi nhập...")
                )
                isGetCodeMailAgain = False
                handleSubmitCode(self, thread, driver, data["code"])
            else:
                self.table_account_info.setItem(
                    thread, 3, QTableWidgetItem("Chưa có code đang lấy lại code...")
                )
                isGetCodeMailAgain = True

    except requests.exceptions.RequestException as e:
        print(e)
