from PySide6.QtWidgets import *
from utils.utils import wait


def handleSubmitAccount(self, thread, driver, current_row_count):
    isSubmitAccount = True
    while isSubmitAccount and not self.stop_flag:
        submitAccount = driver.find_element("css selector", "button[type='submit']")
        self.table_account_info.setItem(
            current_row_count, 3, QTableWidgetItem("Đang submit...")
        )
        submitAccount.click()

        wait(4, 6)
        checkDectect = driver.find_elements(
            "xpath",
            '//span[contains(text(), "Maximum number of attempts reached. Try again later.")]',
        )
        if checkDectect:
            self.table_account_info.setItem(
                current_row_count, 3, QTableWidgetItem("Bị chặn đang submit lại...")
            )
            isSubmitAccount = True
        else:
            isSubmitAccount = False
