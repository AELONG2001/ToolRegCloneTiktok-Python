from PySide6.QtWidgets import *
from utils.utils import wait


def handleGetCode(self, thread, driver):
    try:
        isGetCodeAgain = True
        while isGetCodeAgain and not self.stop_flag:
            wait(2, 4)
            getCodeElement = driver.find_element(
                "xpath", '//*[@data-e2e="send-code-button"]'
            )
            self.table_account_info.setItem(
                thread, 3, QTableWidgetItem("Ấn nút send code...")
            )
            getCodeElement.click()
            getCodeElement.click()

            wait(4, 6)
            checkDectect = driver.find_element(
                "xpath",
                '//span[contains(text(), "Maximum number of attempts reached. Try again later.")]',
            )

            if checkDectect:
                self.table_account_info.setItem(
                    thread, 3, QTableWidgetItem("Bị chặn, đợi send code lại...")
                )
                isGetCodeAgain = True
            else:
                isGetCodeAgain = False
    except:
        return
