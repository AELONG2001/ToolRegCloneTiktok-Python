from PySide6.QtWidgets import *
from utils.utils import wait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from functions.handleMultiThreads.handleRestartThread import handleRestartThread
from functions.handleMultiThreads.handleRestartThread import handleRestartThreadNewMail

def handleSubmitAccount(self):
    self.self_main.table_account_info.scrollToBottom()
    isSubmitAccount = True
    max_attempts = 10
    attempts = 0
    while attempts < max_attempts and isSubmitAccount and not self.stop_flag:
        self.self_main.table_account_info.setItem(
            self.current_row_count, 3, QTableWidgetItem("Đang submit...")
        )
        wait(2, 3)
        if self.driver.current_url == "https://www.tiktok.com/login/download-app":
            handleRestartThread(self)

        submitAccount = self.driver.find_element("css selector", "button[type='submit']")
        try:
            submitAccount.click()
        except ElementClickInterceptedException:
            pass
        except StaleElementReferenceException:
            pass

        wait(6, 8)
        if self.driver.current_url == "https://www.tiktok.com/signup/create-username":
            isSubmitAccount = False
            attempts = 0
            print("Trang đã chuyển hướng, không cần thực hiện thêm click.")
        else:
            attempts += 1
            isSubmitAccount = True

    # Nếu đã thực hiện đủ số lần tối đa, khởi động lại self.thread
    if attempts >= max_attempts:
            print("Đã submit quá nhiều lần, đợi restart lại")
            self.driver.refresh()
            wait(2, 3)
            self.driver.refresh()
            wait(2, 3)
            if self.driver.current_url != "https://www.tiktok.com/signup/phone-or-email/email":
                print("Tài khoản đã được tạo rồi")
                account = f"{self.username_mail}|{self.password_account}|{self.password_mail}|{self.current_date}"
                wait(1, 2)
                with open(self.output_file_path, "a") as f:
                    f.write(account + "\n")
                handleRestartThreadNewMail(self)
            else:
               handleRestartThread(self)
