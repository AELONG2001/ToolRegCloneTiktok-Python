from PySide6.QtWidgets import *
from utils.utils import wait
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException

def handleSubmitAccount(self):
    isSubmitAccount = True
    max_attempts = 10
    attempts = 0
    while attempts < max_attempts and isSubmitAccount and not self.stop_flag:
        self.self_main.table_account_info.setItem(
            self.current_row_count, 3, QTableWidgetItem("Đang submit...")
        )
        submitAccount = self.driver.find_element("css selector", "button[type='submit']")
        try:
            submitAccount.click()
        except ElementClickInterceptedException:
            # print("Không tìm thấy submitAccount element")
            # account = f"{self.username}|{self.password_account}|{self.password}|1"
            # wait(1, 2)
            # with open(self.output_file_path, "a") as f:
            #     f.write(account + "\n")
            # self.driver.quit()
            # handleDeleteProfile(self.profile_id)
            # self.self_main.table_account_info.setItem(
            #     self.current_row_count,
            #     3,
            #     QTableWidgetItem("Bị chặn, đợi restart lại..."),
            # )
            # self.self_main.restart_thread(self.num_threads, "", "")
            pass
        except StaleElementReferenceException:
            # print("Không tìm thấy submitAccount element")
            # account = f"{self.username}|{self.password_account}|{self.password}|2"
            # wait(1, 2)
            # with open(self.output_file_path, "a") as f:
            #     f.write(account + "\n")
            # self.driver.quit()
            # handleDeleteProfile(self.profile_id)
            # self.self_main.table_account_info.setItem(
            #     self.current_row_count,
            #     3,
            #     QTableWidgetItem("Bị chặn, đợi restart lại..."),
            # )
            # self.self_main.restart_thread(self.num_threads, "", "")
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
            self.driver.refresh()
            wait(10, 12)
            if self.driver.current_url != "https://www.tiktok.com/signup/phone-or-email/email":
                print("Tài khoản đã được tạo rồi")
                account = f"{self.username}|{self.password_account}|{self.password}|3"
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
            else:
                # wait(1, 2)
                # with open(self.input_file_path, "a") as file:
                #     file.write(f"{self.username}|{self.password}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại... 3"),
                )
                self.self_main.restart_thread(self.num_threads, self.username, self.password)
