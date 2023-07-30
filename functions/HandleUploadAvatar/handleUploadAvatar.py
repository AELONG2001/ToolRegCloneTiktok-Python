import os
from PySide6.QtWidgets import *
from utils.utils import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions.handleMultiThreads.selenium.ResolveCaptcha.OmoCaptcha.captchaRotateObjectOmo import (
    handleResolveCaptchaRotateObjectOmo,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.OmoCaptcha.captchaChooseTwoObjectsOmo import (
    handleResolveCaptchaChooseTwoObjectsOmo,
)
from utils.utils import random_number


def handleUploadAvatar(self, thread, driver):
    output_file_path = r"C:\Users\HD\OneDrive\Documents\Tools\Python\ToolRegCloneTiktok\data\output.txt"

    wait(4, 6)
    list_avatar_folder = (
        r"C:\Users\HD\OneDrive\Documents\Tools\Python\ToolRegCloneTiktok\data\wibus"
    )

    list_avatar = os.listdir(list_avatar_folder)

    pageContent = driver.page_source
    userId = pageContent.split('"nickName":"')[1].split('"')[0]

    driver.get(f"https://www.tiktok.com/@{userId}")

    waitForNavigation = WebDriverWait(driver, 100)
    editProfile = waitForNavigation.until(
        EC.presence_of_element_located(("xpath", '//span[text()="Edit profile"]'))
    )
    editProfile.click()

    wait(2, 4)
    inputUploadAvatar = driver.find_element("css selector", "input[type='file']")
    inputUploadAvatar.send_keys(
        f"C:/Users/HD/OneDrive/Documents/Tools/Python/ToolRegCloneTiktok/data/wibus/{list_avatar[random_number(0, 38)]}"
    )

    wait(4, 6)
    applyAvatarBtn = driver.find_element("xpath", '//button[text()="Apply"]')
    if not applyAvatarBtn.is_displayed():
        # Sử dụng JavaScript để cuộn trang đến vị trí của phần tử
        driver.execute_script("arguments[0].scrollIntoView();", applyAvatarBtn)
    applyAvatarBtn.click()

    wait(4, 6)
    saveElement = driver.find_element("xpath", '//*[@data-e2e="edit-profile-save"]')
    saveElement.click()

    hotmails = []
    with open(output_file_path, "r") as file:
        for line in file:
            hotmail = line.strip().split("|")[0]
            hotmails.append(hotmail)

    self.table_account_info.removeRow(0)

    # delete all cookies
    driver.delete_all_cookies()

    wait(4, 6)
    handleResolveCaptchaRotateObjectOmo(self, thread, driver)
    handleResolveCaptchaChooseTwoObjectsOmo(self, thread, driver)

    wait(5, 10)
