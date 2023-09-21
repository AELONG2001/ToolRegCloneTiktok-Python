from PySide6.QtWidgets import *
from utils.utils import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)

def handleInsertNewUsername(self, thread, driver, accounts, current_row_count, profile_id):
    waitForNavigation = WebDriverWait(driver, 100)
    skipElement = waitForNavigation.until(
        EC.presence_of_element_located(("xpath", '//div[text()="Skip"]'))
    )
    skipElement.click()
   
