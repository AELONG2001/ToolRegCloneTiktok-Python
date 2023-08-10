from PySide6.QtWidgets import *
from utils.utils import wait


def handleInputUserNameAndPassword(self, thread, driver, accounts, current_row_count):
    username = accounts[thread][0]
    if username is not None:
        wait(2, 4)
        emailElement = driver.find_element("css selector", "input[name='email']")
        self.table_account_info.setItem(
            current_row_count, 3, QTableWidgetItem("Đang nhập email...")
        )
        emailElement.send_keys(username)

        wait(2, 4)
        passwordElement = driver.find_element("css selector", "input[type='password']")
        self.table_account_info.setItem(
            current_row_count, 3, QTableWidgetItem("Đang nhập password...")
        )
        passwordElement.send_keys("Long123@")
