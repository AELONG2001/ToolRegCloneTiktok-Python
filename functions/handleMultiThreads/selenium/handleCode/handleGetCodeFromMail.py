import requests
from PySide6.QtWidgets import *
from utils.utils import wait

from functions.handleMultiThreads.selenium.handleCode.handleGetCode import (
    handleGetCode,
)

from functions.handleMultiThreads.selenium.handleCode.handleSubmitCode import (
    handleSubmitCode,
)

from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)



def handleGetCodeFromMail(self, thread, driver, accounts, current_row_count, profile_id):
    try:
        file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\hotmail.txt"
        max_attempts = 3  # Số lần tối đa xuất hiện checkDectect trước khi khởi động lại thread
        attempts = 0
        isCode = True
        while  attempts < max_attempts and isCode and not self.stop_flag:
            username = accounts[thread][0]
            password = accounts[thread][1]

            params = {
                "mail": username,
                "pass": password,
                "type": "tiktok"
            }

            url = f"https://tools.dongvanfb.net/api/get_code"
            self.table_account_info.setItem(
                current_row_count, 3, QTableWidgetItem("Đang lấy code...")
            )
            wait(8, 10)
            response = requests.get(url, params=params)
            data = response.json()

            print("Data: ", data)

            if data["code"]:
                self.table_account_info.setItem(
                    current_row_count,
                    3,
                    QTableWidgetItem("Đã lấy được code đợi nhập..."),
                )
                isCode = False
                attempts = 0
                handleSubmitCode(self, thread, driver, data["code"], current_row_count)
            else:
                isCode = True
                attempts += 1
                # handleGetCode(self, thread, driver, current_row_count)
                # isGetCodeMailAgain = True

        # Nếu đã thực hiện đủ số lần tối đa, khởi động lại thread
        if attempts >= max_attempts:
            wait(1, 2)
            with open(file_path, "a") as file:
                file.write(f"{username}|{password}\n")
            driver.quit()
            handleDeleteProfile(profile_id)
            self.table_account_info.setItem(
                current_row_count,
                3,
                QTableWidgetItem("Bị chặn, đợi restart lại..."),
            )
            self.restart_thread(thread)

    except requests.exceptions.RequestException as e:
        print(e)
