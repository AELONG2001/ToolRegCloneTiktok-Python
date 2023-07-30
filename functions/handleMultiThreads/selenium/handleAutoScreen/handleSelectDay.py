from PySide6.QtWidgets import *
from utils.utils import random_number, wait


def handleSelectDay(self, thread, driver):
    daySelectElement = driver.find_element(
        "xpath", '//*[@aria-label="Day. Double-tap for more options"]'
    )
    daySelectElement.click()
    self.table_account_info.setItem(thread, 3, QTableWidgetItem("Đang chọn ngày..."))
    wait(2, 4)
    dropDownSelectDay = driver.find_element(
        "id", f"Day-options-item-{random_number(0, 28)}"
    )
    dropDownSelectDay.click()