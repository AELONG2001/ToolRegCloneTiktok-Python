from PySide6.QtWidgets import *
from utils.utils import wait
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)


def handleGetCode(self):
    try:
        
        max_attempts = 5  # Số lần tối đa xuất hiện checkDectect trước khi khởi động lại self.thread
        attempts = 0

        while  attempts < max_attempts and not self.stop_flag:
            wait(4, 6)
            getCodeElement = self.driver.find_element(
                "xpath", '//*[@data-e2e="send-code-button"]'
            )
            self.self_main.table_account_info.setItem(
                self.current_row_count, 3, QTableWidgetItem("Ấn nút send code...")
            )
            getCodeElement.click()
            getCodeElement.click()

            wait(4, 6)
            checkDectect = self.driver.find_element(
                "xpath",
                '//span[contains(text(), "Maximum number of attempts reached. Try again later.")]',
            )

            if checkDectect:
                attempts += 1
            else:
                attempts = 0

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
                QTableWidgetItem("Bị chặn, đợi restart lại... 4"),
            )
            self.self_main.restart_thread(self.num_threads, self.username, self.password)

    except:
        return
