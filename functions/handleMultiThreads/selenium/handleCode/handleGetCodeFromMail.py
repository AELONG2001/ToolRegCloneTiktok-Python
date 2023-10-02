import requests
from PySide6.QtWidgets import *
from utils.utils import wait

from functions.handleMultiThreads.selenium.handleCode.handleSubmitCode import (
    handleSubmitCode,
)

from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)



def handleGetCodeFromMail(self):
    try:
        max_attempts = 3  # Số lần tối đa xuất hiện checkDectect trước khi khởi động lại self.thread
        attempts = 0
        isCode = True
        while  attempts < max_attempts and isCode and not self.stop_flag:
            params = {
                "mail": self.username,
                "pass": self.password,
                "type": "tiktok"
            }

            url = f"https://tools.dongvanfb.net/api/get_code"
            self.self_main.table_account_info.setItem(
                self.current_row_count, 3, QTableWidgetItem("Đang lấy code...")
            )
            wait(10, 12)
            response = requests.get(url, params=params)
            data = response.json()

            print("Data: ", data)

            if data["code"]:
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Đã lấy được code đợi nhập..."),
                )
                isCode = False
                attempts = 0
                handleSubmitCode(self, data["code"])
            else:
                isCode = True
                attempts += 1
                # handleGetCode(self, self.thread, self.driver, self.current_row_count)
                # isGetCodeMailAgain = True

        # Nếu đã thực hiện đủ số lần tối đa, khởi động lại self.thread
        if attempts >= max_attempts:
            # wait(1, 2)
            # with open(self.input_file_path, "a") as file:
            #     file.write(f"{self.username}|{self.password}\n")
            self.driver.quit()
            handleDeleteProfile(self.profile_id)
            self.self_main.table_account_info.setItem(
                self.current_row_count,
                3,
                QTableWidgetItem("Bị chặn, đợi restart lại..."),
            )
            self.self_main.restart_thread(self.num_threads, self.username, self.password)

    except requests.exceptions.RequestException as e:
        print(e)
