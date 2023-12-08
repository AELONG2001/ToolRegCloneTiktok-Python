from PySide6.QtWidgets import *
from PySide6.QtCore import *
from utils.utils import wait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from functions.handleMultiThreads.handleRestartThread.handleRestartThread import handleRestartThread

def handleSubmitCode(self, code):
    wait(1, 2)
    inputCodeElement = self.driver.find_element(
        "xpath", '//input[@placeholder="Enter 6-digit code"]'
    )
    self.self_main.table_account_info.setItem(
        self.current_row_count, 3, QTableWidgetItem("Đang nhập code...")
    )
    QCoreApplication.processEvents()
    inputCodeElement.send_keys(code)

    if self.type_reg_country == 0:
        wait(1, 2)
        agreePolicyElement = self.driver.find_element(
            "css selector", "label[for='email-consent']"
        )
        try:
            agreePolicyElement.click()
        except ElementClickInterceptedException:
            self.driver.quit()
            handleRestartThread(self)
            return
        except StaleElementReferenceException:
            self.driver.quit()
            handleRestartThread(self)
            return
    else:
        return
