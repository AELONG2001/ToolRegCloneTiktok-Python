from PySide6.QtWidgets import *
from utils.utils import wait


def handleGetCode(self, thread, driver):
    isGetCode = True
    while isGetCode:
        wait(4, 6)
        getCodeElement = driver.find_element(
            "xpath", '//*[@data-e2e="send-code-button"]'
        )
        self.table_account_info.setItem(
            thread, 3, QTableWidgetItem("Ấn nút send code...")
        )
        print("getCodeElement: ", getCodeElement)
        getCodeElement.click()
        getCodeElement.click()

        wait(2, 4)
        checkDectect = driver.find_element(
            "xpath",
            '//span[contains(text(), "Maximum number of attempts reached. Try again later.")]',
        )

        if checkDectect:
            self.table_account_info.setItem(
                thread, 3, QTableWidgetItem("Bị chặn, đợi send code lại...")
            )
            isGetCode = True
        else:
            isGetCode = False
