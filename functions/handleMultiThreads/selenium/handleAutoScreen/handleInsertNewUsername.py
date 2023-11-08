from PySide6.QtWidgets import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def handleInsertNewUsername(self):
    self.self_main.table_account_info.scrollToBottom()
    waitForNavigation = WebDriverWait(self.driver, 100)
    skipElement = waitForNavigation.until(
        EC.presence_of_element_located(("xpath", '//div[text()="Skip"]'))
    )
    skipElement.click()
   
