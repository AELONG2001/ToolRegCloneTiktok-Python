from PySide6.QtWidgets import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.utils import wait
from time import sleep


def handleInsertNewUsername(self):
    self.self_main.table_account_info.scrollToBottom()
    # waitForNavigation = WebDriverWait(self.driver, 100)
    # inputNewUserName = waitForNavigation.until(
    #     EC.presence_of_element_located(("css selector", "input[name='new-username']"))
    # )
    # for char in self.user_id:
    #     inputNewUserName.send_keys(char)
    #     sleep(0.3)

    # # inputNewUserName.send_keys(self.user_id)

    # wait(2, 3)
    # submitNewAccount = self.driver.find_element("css selector", "button[type='submit']")
    # submitNewAccount.click()
    # # inputNewUserName.send_keys(Keys.ENTER)
    
    # checkUserNameExist = self.driver.find_elements(
    #     "xpath",
    #     '//span[contains(text(), "This username isn’t available. Try a suggested username, or enter a new one.")]',
    # )

    # if checkUserNameExist:
    #   skipElement = self.driver.find_element("xpath", "//div[text()='Skip']")
    #   skipElement.click()
    #   self.is_skip_new_username = True
    # else:
    #    self.is_skip_new_username = False
    #    return

    waitForNavigation = WebDriverWait(self.driver, 100)
    skipElement = waitForNavigation.until(
        EC.presence_of_element_located(("xpath", '//div[text()="Skip"]'))
    )
    skipElement.click()
    
    
   
