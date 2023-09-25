from PySide6.QtWidgets import *
from utils.utils import wait
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException

def handleSubmitAccount(self, thread, input_file_path, output_file_path, driver, accounts, current_row_count, profile_id):
    isSubmitAccount = True
    input_file_path = input_file_path
    output_file_path = output_file_path
    username = accounts[thread][0]
    password = accounts[thread][1]

    max_attempts = 10
    attempts = 0
    while attempts < max_attempts and isSubmitAccount and not self.stop_flag:
        self.table_account_info.setItem(
            current_row_count, 3, QTableWidgetItem("Đang submit...")
        )
        submitAccount = driver.find_element("css selector", "button[type='submit']")
        try:
            submitAccount.click()
        except ElementClickInterceptedException:
            print("Không tìm thấy submitAccount element")
            cookies = driver.get_cookies()
            cookies_string = ";".join(
                [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
            )
            account = f"{username}|Long123@|{password}|{cookies_string}"
            wait(1, 2)
            with open(output_file_path, "a") as f:
                f.write(account + "\n")
            driver.quit()
            handleDeleteProfile(profile_id)
            self.table_account_info.setItem(
                current_row_count,
                3,
                QTableWidgetItem("Bị chặn, đợi restart lại..."),
            )
            self.restart_thread(thread)
        except StaleElementReferenceException:
            print("Không tìm thấy submitAccount element")
            cookies = driver.get_cookies()
            cookies_string = ";".join(
                [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
            )
            account = f"{username}|Long123@|{password}|{cookies_string}"
            wait(1, 2)
            with open(output_file_path, "a") as f:
                f.write(account + "\n")
            driver.quit()
            handleDeleteProfile(profile_id)
            self.table_account_info.setItem(
                current_row_count,
                3,
                QTableWidgetItem("Bị chặn, đợi restart lại..."),
            )
            self.restart_thread(thread)
        


        wait(6, 8)
        if driver.current_url == "https://www.tiktok.com/signup/create-username":
            isSubmitAccount = False
            attempts = 0
            print("Trang đã chuyển hướng, không cần thực hiện thêm click.")
        else:
            attempts += 1
            isSubmitAccount = True

    # Nếu đã thực hiện đủ số lần tối đa, khởi động lại thread
    if attempts >= max_attempts:
            print("Đã submit quá nhiều lần, đợi restart lại")
            driver.refresh()
            driver.refresh()
            wait(10, 12)
            if driver.current_url != "https://www.tiktok.com/signup/phone-or-email/email":
                print("Tài khoản đã được tạo rồi")
                cookies = driver.get_cookies()
                cookies_string = ";".join(
                    [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
                )
                account = f"{username}|Long123@|{password}|{cookies_string}"
                wait(1, 2)
                with open(output_file_path, "a") as f:
                    f.write(account + "\n")
                driver.quit()
                handleDeleteProfile(profile_id)
                self.table_account_info.setItem(
                    current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại..."),
                )
                self.restart_thread(thread)
            else:
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
