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
        max_attempts = 3
        # max_getCodeAgain = 0
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

            if data["content"] == "Invalid email or password or IMAP disabled":
                with open("data/invalid_mail.txt", "a") as file:
                    file.write(f"{self.username}|{self.password}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại...28"),
                )
                self.self_main.restart_thread(self.num_threads, "", "")

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

        if attempts >= max_attempts:
            # max_getCodeAgain += 1
            # wait(1, 2)
            # with open(self.input_file_path, "a") as file:
            #     file.write(f"{self.username}|{self.password}\n")
           
            self.driver.quit()
            handleDeleteProfile(self.profile_id)
            self.self_main.table_account_info.setItem(
                self.current_row_count,
                3,
                QTableWidgetItem("Bị chặn, đợi restart lại... 5"),
            )
            self.self_main.restart_thread(self.num_threads, self.username, self.password)

        # if max_attempts >= 3:
        #     with open("data/mail_getcode_again.txt", "a") as file:
        #             file.write(f"{self.username}|{self.password}\n")
        #     self.driver.quit()
        #     handleDeleteProfile(self.profile_id)
        #     self.self_main.table_account_info.setItem(
        #         self.current_row_count,
        #         3,
        #         QTableWidgetItem("Bị chặn, đợi restart lại... 29"),
        #     )
        #     self.self_main.restart_thread(self.num_threads, "", "") 

    except requests.exceptions.RequestException as e:
        print(e)
