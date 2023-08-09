import requests
from PySide6.QtWidgets import *
from utils.utils import wait

from functions.handleMultiThreads.selenium.handleCode.handleGetCode import (
    handleGetCode,
)

from functions.handleMultiThreads.selenium.handleCode.handleSubmitCode import (
    handleSubmitCode,
)


def handleGetCodeFromMail(self, thread, driver, accounts, current_row_count):
    try:
        isGetCodeMailAgain = True
        while isGetCodeMailAgain and not self.stop_flag:
            username = accounts[thread][0]
            password = accounts[thread][1]

            url = f"https://tools.dongvanfb.net/api/get_code?mail={username}&pass={password}&type=tiktok"
            self.table_account_info.setItem(
                current_row_count, 3, QTableWidgetItem("Đang lấy code...")
            )
            wait(8, 10)
            response = requests.get(url)
            data = response.json()

            print("Data: ", data)

            if data["code"]:
                self.table_account_info.setItem(
                    current_row_count,
                    3,
                    QTableWidgetItem("Đã lấy được code đợi nhập..."),
                )
                isGetCodeMailAgain = False
                handleSubmitCode(self, thread, driver, data["code"], current_row_count)
            else:
                self.table_account_info.setItem(
                    current_row_count,
                    3,
                    QTableWidgetItem("Chưa có code đang lấy lại code..."),
                )
                handleGetCode(self, thread, driver, current_row_count)
                isGetCodeMailAgain = True

    except requests.exceptions.RequestException as e:
        print(e)
