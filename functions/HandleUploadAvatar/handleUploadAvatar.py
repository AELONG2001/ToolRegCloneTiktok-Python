import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from utils.utils import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.AchiCaptcha.captchaRotateObjectAChi import (
    handleResolveCaptchaRotateObjectAChi,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.AchiCaptcha.captchaChooseTwoObjectsAChi import (
    handleResolveCaptchaChooseTwoObjectsAChi,
)
from utils.utils import random_number


def handleUploadAvatar(self, thread, driver, accounts, current_row_count, profile_id):
    wait(2, 4)
    output_file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\output.txt"
    list_avatar_folder = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\wibus"
    username = accounts[thread][0]
    password = accounts[thread][1]

    list_avatar = os.listdir(list_avatar_folder)

    wait(2, 4)
    pageContent = driver.page_source
    try:
        userId = pageContent.split('"nickName":"')[1].split('"')[0]
    except:
        userId = None
        return

    print("userId: ", userId)

    if userId:
        driver.get(f"https://www.tiktok.com/@{userId}")
    else:
        return
    
    wait(4, 6)
    cookies = driver.get_cookies()
    cookies_string = ";".join(
        [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
    )
    account = f"{username}|Long123@|{password}|{cookies_string}"

    # insert account
    with open(output_file_path, "a") as f:
        f.write(account + "\n")

    
    wait(4, 6)
    checkCaptcha = driver.find_elements("css selector", "#verify-bar-close")

    if checkCaptcha:
        return
    
    waitForNavigation = WebDriverWait(driver, 100)
    editProfile = waitForNavigation.until(
        EC.presence_of_element_located(("xpath", '//span[text()="Edit profile"]'))
    )
    wait(4, 6)
    handleResolveCaptchaRotateObjectAChi(self, thread, driver, accounts, current_row_count, profile_id)
    handleResolveCaptchaChooseTwoObjectsAChi(self, thread, driver, accounts, current_row_count, profile_id)
    editProfile.click()

    self.table_account_info.setItem(
        current_row_count, 3, QTableWidgetItem("Đang upload avatar...")
    )

    
    wait(2, 4)
    inputUploadAvatar = driver.find_elements("css selector", "input[type='file']")
    if inputUploadAvatar:
        inputUploadAvatar[0].send_keys(
            f"C:/Users/HD/OneDrive/Documents/WorkSpace/Tools/Python/ToolRegCloneTiktok/data/wibus/{list_avatar[random_number(0, 50)]}"
        )
    else:
        return

    wait(4, 6)
    applyAvatarBtn = driver.find_element("xpath", '//button[text()="Apply"]')
    if not applyAvatarBtn.is_displayed():
        # Sử dụng JavaScript để cuộn trang đến vị trí của phần tử
        driver.execute_script("arguments[0].scrollIntoView();", applyAvatarBtn)
    applyAvatarBtn.click()

    wait(4, 6)
    saveElement = driver.find_elements("xpath", '//*[@data-e2e="edit-profile-save"]')
    if saveElement:
        saveElement[0].click()
    else:
        return
    
    self.table_account_info.setItem(
        current_row_count, 3, QTableWidgetItem("upload avatar thành công...")
    )

    item = QTableWidgetItem("Tạo tài khoản thành công...")
    green_color = QColor(64, 170, 15)
    item.setForeground(green_color)

    self.table_account_info.setItem(current_row_count, 3, item)

    # handleDeleteProfile(profile_id)

    wait(2, 4)
