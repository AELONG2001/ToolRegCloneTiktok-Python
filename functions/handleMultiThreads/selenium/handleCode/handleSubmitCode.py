from PySide6.QtWidgets import *
from utils.utils import wait


def handleSubmitCode(self, thread, driver, code, current_row_count):
    wait(1, 2)
    inputCodeElement = driver.find_element(
        "xpath", '//input[@placeholder="Enter 6-digit code"]'
    )
    self.table_account_info.setItem(
        current_row_count, 3, QTableWidgetItem("Đang nhập code...")
    )
    inputCodeElement.send_keys(code)

    wait(1, 2)
    agreePolicyElement = driver.find_element(
        "css selector", "label[for='email-consent']"
    )
    agreePolicyElement.click()
