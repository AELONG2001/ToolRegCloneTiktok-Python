from PySide6.QtWidgets import *
from utils.utils import wait
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException

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
            self.driver.quit()
            handleDeleteProfile(self.profile_id)
            self.self_main.table_account_info.setItem(
                self.current_row_count,
                3,
                QTableWidgetItem("Bị chặn, đợi restart lại... 31"),
            )
            self.self_main.restart_thread(self.num_threads, self.username_mail, self.password_mail)
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
                account = f"{self.username_mail}|{self.password_account}|{self.password_mail}|{self.current_date}"
                wait(1, 2)
                with open(self.output_file_path, "a") as f:
                    f.write(account + "\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại... 2"),
                )
                self.self_main.restart_thread(self.num_threads, "", "")
                return
            else:
                # wait(1, 2)
                # with open(self.input_file_path, "a") as file:
                #     file.write(f"{self.username_mail}|{self.password_mail}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại... 3"),
                )
                self.self_main.restart_thread(self.num_threads, self.username_mail, self.password_mail)
                return
