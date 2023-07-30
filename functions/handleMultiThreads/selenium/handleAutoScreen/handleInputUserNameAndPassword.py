from PySide6.QtWidgets import *
from utils.utils import wait


def handleInputUserNameAndPassword(self, thread, driver):
    username = self.table_account_info.item(thread, 0)
    if username is not None:
        wait(2, 4)
        emailElement = driver.find_element("css selector", "input[name='email']")
        self.table_account_info.setItem(
            thread, 3, QTableWidgetItem("Đang nhập email...")
        )
        emailElement.send_keys(username.text())

        wait(2, 4)
        passwordElement = driver.find_element("css selector", "input[type='password']")
        self.table_account_info.setItem(
            thread, 3, QTableWidgetItem("Đang nhập password...")
        )
        passwordElement.send_keys("Long123@")
