from PySide6.QtWidgets import *
from PySide6.QtCore import *
from utils.utils import random_number, wait


def handleSelectDay(self):
    self.self_main.table_account_info.scrollToBottom()
    wait(4, 6)
    daySelectElement = self.driver.find_element(
        "xpath", '//*[@aria-label="Day. Double-tap for more options"]'
    )
    daySelectElement.click()
    self.self_main.table_account_info.setItem(
        self.current_row_count, 3, QTableWidgetItem("Đang chọn ngày...")
    )
    QCoreApplication.processEvents()
    wait(4, 6)
    dropDownSelectDay = self.driver.find_element(
        "id", f"Day-options-item-{random_number(0, 6)}"
    )
    dropDownSelectDay.click()
