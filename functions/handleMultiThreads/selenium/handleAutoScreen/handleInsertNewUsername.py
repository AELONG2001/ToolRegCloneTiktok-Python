from PySide6.QtWidgets import *
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def handleInsertNewUsername(driver):
    try:
        waitForNavigation = WebDriverWait(driver, 5)
        skipElement = waitForNavigation.until(
            EC.presence_of_element_located(("xpath", '//div[text()="Skip"]'))
        )
        skipElement.click()
    except TimeoutException:
        print("Không tìm thấy skipElement sau khoảng thời gian chờ")
        driver.get("https://www.tiktok.com/")
