import os
import json
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from utils.utils import wait, generate_random_name

from functions.handleMultiThreads.selenium.ResolveCaptcha.AchiCaptcha.captchaRotateObjectAChi import (
    handleResolveCaptchaRotateObjectAChi,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.AchiCaptcha.captchaChooseTwoObjectsAChi import (
    handleResolveCaptchaChooseTwoObjectsAChi,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.AchiCaptcha.captchaSliderObjectAChi import (
    handleResolveCaptchaSliderObjectAChi,
)

from functions.handleMultiThreads.selenium.ResolveCaptcha.OmoCaptcha.captchaRotateObjectOmo import (
    handleResolveCaptchaRotateObjectOmo,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.OmoCaptcha.captchaChooseTwoObjectsOmo import (
    handleResolveCaptchaChooseTwoObjectsOmo,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.OmoCaptcha.captchaSliderObjectOmo import (
    handleResolveCaptchaSliderObjectOmo,
)

from utils.utils import random_number

def handleInsertCookieAndWriteAccount(self):
    cookies = self.driver.get_cookies()
    cookies_string = ";".join(
        [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
    )
    account = f"{self.username_mail}|{self.password_account}|{self.password_mail}|{cookies_string}|{self.current_date}"
    with open(self.output_file_path, "a") as f:
        f.write(account + "\n")

def showSuccessAccount(self):
    item = QTableWidgetItem("Tạo tài khoản thành công...")
    green_color = QColor(64, 170, 15)
    item.setForeground(green_color)

    self.self_main.table_account_info.setItem(self.current_row_count, 3, item)
    QCoreApplication.processEvents()

def handleUploadAvatar(self):

    isGetUserIdAgain = True
    while isGetUserIdAgain:
        try:
            waitForNavigation = WebDriverWait(self.driver, 10)
            waitForNavigation.until(
            EC.presence_of_element_located(("xpath", '//*[@data-e2e="profile-icon"]'))
            )
            isGetUserIdAgain = False
        except TimeoutException:
            try:
                self.driver.get("https://www.tiktok.com")
                isGetUserIdAgain = True
            except WebDriverException:
                handleInsertCookieAndWriteAccount(self)
                showSuccessAccount(self)
                isGetUserIdAgain = False
                self.is_restart = False
                return

    is_list_avtart_default = True

    with open("configs_account.json", "r") as json_file:
        data = json.load(json_file)
    if "url_avatar" in data and data["url_avatar"]:
        is_list_avtart_default = False
        list_avatar_folder = data["url_avatar"]
    else:
        is_list_avtart_default = True
        list_avatar_folder = "data/wibus"
    list_avatar = os.listdir(list_avatar_folder)

    pageContent = self.driver.page_source
    if '"nickName":"' in pageContent:
        try:
            userId = pageContent.split('"nickName":"')[1].split('"')[0]
        except IndexError:
            handleInsertCookieAndWriteAccount(self)
            showSuccessAccount(self)
            return
    else:
        handleInsertCookieAndWriteAccount(self)
        showSuccessAccount(self)
        return

    try:
        if userId:
            self.driver.get(f"https://www.tiktok.com/@{userId}")
        else:
            handleInsertCookieAndWriteAccount(self)
            showSuccessAccount(self)
            return
    except WebDriverException:
        handleInsertCookieAndWriteAccount(self)
        showSuccessAccount(self)
        return

    self.is_restart = False
    
    try:
        wait(2, 3)
        if self.captcha_type == 0:
            handleResolveCaptchaRotateObjectAChi(self)
            handleResolveCaptchaChooseTwoObjectsAChi(self)
            handleResolveCaptchaSliderObjectAChi(self)
        else: 
            handleResolveCaptchaRotateObjectOmo(self)
            handleResolveCaptchaChooseTwoObjectsOmo(self)
            handleResolveCaptchaSliderObjectOmo(self)

        waitForNavigation = WebDriverWait(self.driver, 60)
        editProfile = waitForNavigation.until(
            EC.presence_of_element_located(("xpath", '//span[text()="Edit profile"]'))
        )
       
        editProfile.click()
    except TimeoutException:
        handleInsertCookieAndWriteAccount(self)
        showSuccessAccount(self)
        return
    except ElementClickInterceptedException:
        handleInsertCookieAndWriteAccount(self)
        showSuccessAccount(self)
        return

    self.self_main.table_account_info.setItem(
        self.current_row_count, 3, QTableWidgetItem("Đang upload avatar...")
    )
    QCoreApplication.processEvents()

    wait(4, 6)
    inputUploadAvatar = self.driver.find_elements("css selector", "input[type='file']")
    if inputUploadAvatar:
            if is_list_avtart_default:
                relative_path = "data/wibus"
                absolute_path = os.path.abspath(relative_path)

                path_avatar_default_origin = absolute_path
                inputUploadAvatar[0].send_keys(
                    f"{path_avatar_default_origin}/{list_avatar[random_number(0, len(list_avatar) - 2)]}"
                )
            else:
                inputUploadAvatar[0].send_keys(
                    f"{list_avatar_folder}/{list_avatar[random_number(0, len(list_avatar) - 2)]}"
                )
        
    else:
        handleInsertCookieAndWriteAccount(self)
        showSuccessAccount(self)
        return

    wait(4, 6)
    applyAvatarBtn = self.driver.find_elements("xpath", '//button[text()="Apply"]')
    try:
        if not applyAvatarBtn[0].is_displayed():
            # Sử dụng JavaScript để cuộn trang đến vị trí của phần tử
            self.driver.execute_script("arguments[0].scrollIntoView();", applyAvatarBtn[0])
        applyAvatarBtn[0].click()
    except NoSuchElementException:
        handleInsertCookieAndWriteAccount(self)
        showSuccessAccount(self)
        return
    
    is_random_name = self.self_main.is_change_username_check.isChecked()
    with open("configs_account.json", "r") as json_file:
        data = json.load(json_file)

    if "url_username" in data and data["url_username"]:
        with open(data["url_username"], "r") as f:
            list_username = f.read()

    if is_random_name:
        if "url_username" in data and data["url_username"]:
            wait(4, 6)
            usernames= list_username.split("|")
            userNameRandomByFile = f"{usernames[random_number(0, len(usernames) - 1)]}_{generate_random_name(8)}"
            editUserName = self.driver.find_elements("xpath", '//*[@placeholder="Username"]')
            editUserName[0].clear()
            editUserName[0].clear()
            wait(4, 6)
            editUserName[0].send_keys(userNameRandomByFile)

            wait(4, 6)
            editName = self.driver.find_elements("xpath", '//*[@placeholder="Name"]')
            editName[0].clear()
            editName[0].clear()
            wait(4, 6)
            editName[0].send_keys(userNameRandomByFile)
        else:
            wait(4, 6)
            userNameRandom = f"{generate_random_name(8)}_{generate_random_name(8)}"
            editUserName[0] = self.driver.find_elements("xpath", '//*[@placeholder="Username"]')
            editUserName[0].clear()
            editUserName[0].clear()
            wait(4, 6)
            editUserName[0].send_keys(userNameRandom)

            wait(4, 6)
            editName = self.driver.find_elements("xpath", '//*[@placeholder="Name"]')
            editName[0].clear()
            editName[0].clear()
            wait(4, 6)
            editName[0].send_keys(userNameRandom)

    wait(4, 6)
    saveElement = self.driver.find_elements("xpath", '//*[@data-e2e="edit-profile-save"]')
    
    try:
        saveElement[0].click()
        wait(4, 6)

        if is_random_name:
            confirmChangeUser = self.driver.find_element("xpath", '//*[@data-e2e="set-username-popup-confirm"]')
            confirmChangeUser.click()

        wait(4, 6)
        cookies = self.driver.get_cookies()
        cookies_string = ";".join(
            [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
        )
        
        if is_random_name:
            if "url_username" in data and data["url_username"]:
               account = f"{userNameRandomByFile}|{self.password_account}|{self.username_mail}|{self.password_mail}|{cookies_string}|{self.current_date}"
            else:
               account = f"{userNameRandom}|{self.password_account}|{self.username_mail}|{self.password_mail}|{cookies_string}|{self.current_date}"
        else:
           account = f"{self.username_mail}|{self.password_account}|{self.password_mail}|{cookies_string}|{self.current_date}"
        
        # insert account
        with open(self.output_file_path, "a") as f:
            f.write(account + "\n")
    except ElementClickInterceptedException:
        print("không tìm thấy saveElement")
        handleInsertCookieAndWriteAccount(self)
        showSuccessAccount(self)
        return
    
    self.self_main.table_account_info.setItem(
        self.current_row_count, 3, QTableWidgetItem("upload avatar thành công...")
    )
    QCoreApplication.processEvents()
    showSuccessAccount(self)
