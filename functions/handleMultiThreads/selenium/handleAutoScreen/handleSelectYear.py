from PySide6.QtWidgets import *
from utils.utils import random_number, wait


def handleSelectYear(self):
    yearSelectElement = self.driver.find_element(
        "xpath", '//*[@aria-label="Year. Double-tap for more options"]'
    )
    yearSelectElement.click()
    self.self_main.table_account_info.setItem(
        self.current_row_count, 3, QTableWidgetItem("Đang chọn năm...")
    )
    wait(4, 6)
    dropDownSelectYear = self.driver.find_element(
        "id", f"Year-options-item-{random_number(18, 40)}"
    )
    dropDownSelectYear.click()
