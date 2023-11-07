from PySide6.QtWidgets import *
from utils.utils import wait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)

def handleSubmitCode(self, code):
    wait(1, 2)
    inputCodeElement = self.driver.find_element(
        "xpath", '//input[@placeholder="Enter 6-digit code"]'
    )
    self.self_main.table_account_info.setItem(
        self.current_row_count, 3, QTableWidgetItem("Đang nhập code...")
    )
    inputCodeElement.send_keys(code)

    wait(1, 2)
    agreePolicyElement = self.driver.find_element(
        "css selector", "label[for='email-consent']"
    )
    try:
      agreePolicyElement.click()
    except ElementClickInterceptedException:
        self.driver.quit()
        handleDeleteProfile(self.profile_id)
        self.self_main.table_account_info.setItem(
            self.current_row_count,
            3,
            QTableWidgetItem("Bị chặn, đợi restart lại... 32"),
        )
        self.self_main.restart_thread(self.num_threads, self.username_mail, self.password_mail)
    except StaleElementReferenceException:
        self.driver.quit()
        handleDeleteProfile(self.profile_id)
        self.self_main.table_account_info.setItem(
            self.current_row_count,
            3,
            QTableWidgetItem("Bị chặn, đợi restart lại... 33"),
        )
        self.self_main.restart_thread(self.num_threads, self.username_mail, self.password_mail)
