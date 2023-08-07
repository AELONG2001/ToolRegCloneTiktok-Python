import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from utils.utils import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions.handleMultiThreads.selenium.ResolveCaptcha.AchiCaptcha.captchaRotateObjectAChi import (
    handleResolveCaptchaRotateObjectAChi,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.AchiCaptcha.captchaChooseTwoObjectsAChi import (
    handleResolveCaptchaChooseTwoObjectsAChi,
)
from utils.utils import random_number


def handleUploadAvatar(self, thread, driver, current_row_count):
    wait(4, 6)
    list_avatar_folder = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\wibus"

    list_avatar = os.listdir(list_avatar_folder)

    wait(2, 4)
    pageContent = driver.page_source
    userId = pageContent.split('"nickName":"')[1].split('"')[0]

    if userId is None:
        return

    driver.get(f"https://www.tiktok.com/@{userId}")

    waitForNavigation = WebDriverWait(driver, 100)
    editProfile = waitForNavigation.until(
        EC.presence_of_element_located(("xpath", '//span[text()="Edit profile"]'))
    )
    editProfile.click()

    self.table_account_info.setItem(
        current_row_count, 3, QTableWidgetItem("Đang upload avatar...")
    )

    wait(4, 6)
    inputUploadAvatar = driver.find_element("css selector", "input[type='file']")
    inputUploadAvatar.send_keys(
        f"C:/Users/HD/OneDrive/Documents/WorkSpace/Tools/Python/ToolRegCloneTiktok/data/wibus/{list_avatar[random_number(0, 37)]}"
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
    3
    self.table_account_info.setItem(
        current_row_count, 3, QTableWidgetItem("upload avatar thành công...")
    )

    item = QTableWidgetItem("Tạo tài khoản thành công...")
    green_color = QColor(64, 170, 15)
    item.setForeground(green_color)

    self.table_account_info.setItem(current_row_count, 3, item)

    # delete all cookies
    driver.delete_all_cookies()

    wait(4, 6)
    handleResolveCaptchaRotateObjectAChi(self, thread, driver, current_row_count)
    handleResolveCaptchaChooseTwoObjectsAChi(self, thread, driver, current_row_count)

    wait(2, 4)
