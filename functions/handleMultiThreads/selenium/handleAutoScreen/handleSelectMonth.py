from PySide6.QtWidgets import *
from PySide6.QtCore import *
from utils.utils import random_number, wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from functions.handleMultiThreads.handleRestartThread.handleRestartThread import handleRestartThread
from time import sleep

def handleSelectMonth(self):
    self.self_main.table_account_info.scrollToBottom()
    self.self_main.table_account_info.setItem(
        self.current_row_count, 3, QTableWidgetItem("Bắt đầu reg...")
    )
    QCoreApplication.processEvents()

    try:
        waitForNavigation = WebDriverWait(self.driver, 30)
        monthSelectElement = waitForNavigation.until(
            EC.presence_of_element_located(
                ("xpath", '//*[@aria-label="Month. Double-tap for more options"]')
            )
        )
        monthSelectElement.click()
        self.self_main.table_account_info.setItem(
            self.current_row_count, 3, QTableWidgetItem("Đang chọn tháng...")
        )
        QCoreApplication.processEvents()
        wait(4, 6)
        dropDownSelectMonth = self.driver.find_element(
            "id", f"Month-options-item-{random_number(0, 11)}"
        )
        dropDownSelectMonth.click()
    except TimeoutException:
        print("Không tìm thấy monthSelectElement sau khoảng thời gian chờ")
        self.driver.quit()
        handleRestartThread(self)
        

    

