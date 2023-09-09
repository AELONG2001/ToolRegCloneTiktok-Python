from PySide6.QtWidgets import *
from utils.utils import wait
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)
from selenium.common.exceptions import NoSuchElementException

def handleSubmitAccount(self, thread, driver, accounts, current_row_count, profile_id):
    isSubmitAccount = True
    file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\hotmail.txt"
    username = accounts[thread][0]
    password = accounts[thread][1]

    max_attempts = 12  # Số lần tối đa xuất hiện checkDectect trước khi khởi động lại thread
    attempts = 0
    while attempts < max_attempts and isSubmitAccount and not self.stop_flag:
        self.table_account_info.setItem(
            current_row_count, 3, QTableWidgetItem("Đang submit...")
        )
        try:
          submitAccount = driver.find_element("css selector", "button[type='submit']")
          if submitAccount.is_displayed() and submitAccount.is_enabled():
            submitAccount.click()
          else:
            print("Phần tử không hiển thị hoặc không có thể click.")
        except NoSuchElementException:
           return
        
        wait(4, 5)
        checkDectect = driver.find_elements(
            "xpath",
            '//span[contains(text(), "Maximum number of attempts reached. Try again later.")]',
        )
        checkCodeExpired = driver.find_elements(
            "xpath",
            '//span[contains(text(), "Verification code is expired or incorrect. Try again.")]',
        )
        if checkDectect or checkCodeExpired:
            self.table_account_info.setItem(
                current_row_count, 3, QTableWidgetItem("Bị chặn đang submit lại...")
            )
            attempts += 1
            isSubmitAccount = True
        else:
            isSubmitAccount = False
            attempts = 0
            

    # Nếu đã thực hiện đủ số lần tối đa, khởi động lại thread
    if attempts >= max_attempts:
            emailElement = driver.find_element("css selector", "input[name='email']")
            checkAccountCreated = emailElement.find_element_by_xpath("./following-sibling::div/svg")
            if not checkAccountCreated.is_displayed():
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
