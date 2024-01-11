from PySide6.QtWidgets import *
from PySide6.QtCore import *
from utils.utils import random_number, wait


def handleSelectYear(self):
    self.self_main.table_account_info.scrollToBottom()
    yearSelectElement = self.driver.find_element(
        "xpath", '//*[@aria-label="Năm. Nhấn đúp để xem tùy chọn khác"]'
    )
    yearSelectElement.click()
    self.self_main.table_account_info.setItem(
        self.current_row_count, 3, QTableWidgetItem("Đang chọn năm...")
    )
    QCoreApplication.processEvents()
    wait(4, 6)
    dropDownSelectYear = self.driver.find_element(
        "id", f"Year-options-item-{random_number(18, 40)}"
    )
    dropDownSelectYear.click()
