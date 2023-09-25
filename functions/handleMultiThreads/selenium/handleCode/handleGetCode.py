from PySide6.QtWidgets import *
from utils.utils import wait
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)


def handleGetCode(self, thread, input_file_path, driver, accounts, current_row_count, profile_id):
    try:
        input_file_path = input_file_path
        username = accounts[thread][0]
        password = accounts[thread][1]
        max_attempts = 5  # Số lần tối đa xuất hiện checkDectect trước khi khởi động lại thread
        attempts = 0

        while  attempts < max_attempts and not self.stop_flag:
            wait(4, 6)
            getCodeElement = driver.find_element(
                "xpath", '//*[@data-e2e="send-code-button"]'
            )
            self.table_account_info.setItem(
                current_row_count, 3, QTableWidgetItem("Ấn nút send code...")
            )
            getCodeElement.click()
            getCodeElement.click()

            wait(4, 6)
            checkDectect = driver.find_element(
                "xpath",
                '//span[contains(text(), "Maximum number of attempts reached. Try again later.")]',
            )

            if checkDectect:
                attempts += 1
            else:
                attempts = 0

        # Nếu đã thực hiện đủ số lần tối đa, khởi động lại thread
        if attempts >= max_attempts:
            wait(1, 2)
            with open(input_file_path, "a") as file:
                file.write(f"{username}|{password}\n")
            driver.quit()
            handleDeleteProfile(profile_id)
            self.table_account_info.setItem(
                current_row_count,
                3,
                QTableWidgetItem("Bị chặn, đợi restart lại..."),
            )
            self.restart_thread(thread)

    except:
        return
