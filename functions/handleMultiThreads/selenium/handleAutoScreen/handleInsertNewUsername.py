from PySide6.QtWidgets import *
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)

def handleInsertNewUsername(self, thread, driver, accounts, current_row_count, profile_id):
    # file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\hotmail.txt"
    # username = accounts[thread][0]
    # password = accounts[thread][1]
    try:
        waitForNavigation = WebDriverWait(driver, 100)
        skipElement = waitForNavigation.until(
            EC.presence_of_element_located(("xpath", '//div[text()="Skip"]'))
        )
        skipElement.click()
    except TimeoutException:
        print("Không tìm thấy skipElement sau khoảng thời gian chờ")
        # with open(file_path, "a") as file:
        #         file.write(f"{username}|{password}\n")
        driver.quit()
        handleDeleteProfile(profile_id)
        self.table_account_info.setItem(
            current_row_count,
            3,
            QTableWidgetItem("Bị chặn, đợi restart lại..."),
        )
        self.restart_thread(thread)
