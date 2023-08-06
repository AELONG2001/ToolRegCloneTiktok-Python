from PySide6.QtWidgets import *
from utils.utils import random_number, wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def handleSelectMonth(self, thread, driver):
    waitForNavigation = WebDriverWait(driver, 100)
    monthSelectElement = waitForNavigation.until(
        EC.presence_of_element_located(
            ("xpath", '//*[@aria-label="Month. Double-tap for more options"]')
        )
    )
    self.table_account_info.setItem(thread, 3, QTableWidgetItem("Bắt đầu reg..."))
    monthSelectElement.click()
    self.table_account_info.setItem(thread, 3, QTableWidgetItem("Đang chọn tháng..."))
    wait(4, 6)
    dropDownSelectMonth = driver.find_element(
        "id", f"Month-options-item-{random_number(0, 11)}"
    )
    dropDownSelectMonth.click()
