from PySide6.QtWidgets import *
from utils.utils import random_number, wait


def handleSelectMonth(self, thread, driver):
    self.table_account_info.setItem(thread, 3, QTableWidgetItem("Bắt đầu reg..."))
    wait(1, 2)
    monthSelectElement = driver.find_element(
        "xpath", '//*[@aria-label="Month. Double-tap for more options"]'
    )
    monthSelectElement.click()
    self.table_account_info.setItem(thread, 3, QTableWidgetItem("Đang chọn tháng..."))
    wait(5, 10)
    dropDownSelectMonth = driver.find_element(
        "id", f"Month-options-item-{random_number(0, 11)}"
    )
    dropDownSelectMonth.click()
