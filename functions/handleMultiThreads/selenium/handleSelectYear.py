from PySide6.QtWidgets import *
from utils.utils import random_number, wait


def handleSelectYear(self, thread, driver):
    yearSelectElement = driver.find_element(
        "xpath", '//*[@aria-label="Year. Double-tap for more options"]'
    )
    yearSelectElement.click()
    self.table_account_info.setItem(thread, 3, QTableWidgetItem("Đang chọn năm..."))
    wait(5, 10)
    dropDownSelectYear = driver.find_element(
        "id", f"Year-options-item-{random_number(18, 40)}"
    )
    dropDownSelectYear.click()
