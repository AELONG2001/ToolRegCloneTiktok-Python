from PySide6.QtWidgets import *
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def handleInsertNewUsername(thread, driver, accounts):
    waitForNavigation = WebDriverWait(driver, 100)
    skipElement = waitForNavigation.until(
        EC.presence_of_element_located(("xpath", '//div[text()="Skip"]'))
    )
    skipElement.click()
