from PySide6.QtWidgets import *
from utils.utils import random_number, wait


def handleSelectYear(self, thread, driver, current_row_count):
    yearSelectElement = driver.find_element(
        "xpath", '//*[@aria-label="Year. Double-tap for more options"]'
    )
    yearSelectElement.click()
    self.table_account_info.setItem(
        current_row_count, 3, QTableWidgetItem("Đang chọn năm...")
    )
    wait(2, 4)
    dropDownSelectYear = driver.find_element(
        "id", f"Year-options-item-{random_number(18, 40)}"
    )
    dropDownSelectYear.click()
