from PySide6.QtWidgets import *
from PySide6.QtCore import *
from utils.utils import wait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from functions.handleMultiThreads.handleRestartThread.handleRestartThread import handleRestartThread
from functions.handleMultiThreads.handleRestartThread.handleRestartThreadNewMail import handleRestartThreadNewMail

def handleSubmitAccount(self):
    self.self_main.table_account_info.scrollToBottom()
    isSubmitAccount = True
    max_attempts = 10
    attempts = 0
    while attempts < max_attempts and isSubmitAccount:
        self.self_main.table_account_info.setItem(
            self.current_row_count, 3, QTableWidgetItem("Đang submit...")
        )
        QCoreApplication.processEvents()
        wait(2, 3)
        if self.driver.current_url == "https://www.tiktok.com/login/download-app":
            isSubmitAccount = False
            self.driver.quit()
            handleRestartThread(self)
            return

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
                wait(1, 2)
                cookies = self.driver.get_cookies()
                cookies_string = ";".join(
                    [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
                )
                account = f"{self.username_mail}|{self.password_account}|{self.password_mail}|{cookies_string}|{self.current_date}"
                with open("data/output_not_user_id.txt", "a") as f:
                    f.write(account + "\n")
                
                self.driver.quit()
                handleRestartThreadNewMail(self)
                return
            else:
               self.driver.quit()
               handleRestartThread(self)
               return
