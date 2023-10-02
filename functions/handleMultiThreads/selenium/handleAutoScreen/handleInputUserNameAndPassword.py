from PySide6.QtWidgets import *
from utils.utils import wait


def handleInputUserNameAndPassword(self):
    if self.username is not None:
        wait(2, 4)
        emailElement = self.driver.find_element("css selector", "input[name='email']")
        self.self_main.table_account_info.setItem(
            self.current_row_count, 3, QTableWidgetItem("Đang nhập email...")
        )
        emailElement.send_keys(self.username)

        wait(2, 4)
        passwordElement = self.driver.find_element("css selector", "input[type='password']")
        self.self_main.table_account_info.setItem(
            self.current_row_count, 3, QTableWidgetItem("Đang nhập password...")
        )
        passwordElement.send_keys(self.password_account)
