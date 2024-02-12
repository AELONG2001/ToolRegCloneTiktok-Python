from PySide6.QtWidgets import *
from PySide6.QtCore import *
from utils.utils import random_number, wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from functions.handleMultiThreads.handleRestartThread.handleRestartThread import handleRestartThread

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
                ("xpath", '//*[@aria-label="Tháng. Nhấn đúp để xem tùy chọn khác"]')
            )
        )
        
        # monthSelectElement = self.driver.find_element(
        # "xpath", '//*[@aria-label="Tháng. Nhấn đúp để xem tùy chọn khác"]'
        # )
        # self.driver.execute_script("arguments[0].click();", monthSelectElement)
        
        # wait(10, 12)
        # action_chains = ActionChains(self.driver)
        # window_size = self.driver.execute_script("return [window.innerWidth, window.innerHeight];")

        # x = window_size[0] - 30
        # y = window_size[1] - 30

        # action_chains.move_by_offset(
        #     x, y
        # ).click().perform()
        
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
        

    

