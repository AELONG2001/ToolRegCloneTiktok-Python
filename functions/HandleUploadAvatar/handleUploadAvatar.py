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
from utils.utils import wait, generate_random_name, random_number
import unicodedata

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

from functions.handleMultiThreads.selenium.ResolveCaptcha.CaptchaGuru.captchaRotateObjectGuru import (
    handleResolveCaptchaRotateObjectGuru,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.CaptchaGuru.captchaChooseTwoObjectsGuru import (
    handleResolveCaptchaChooseTwoObjectsGuru,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.CaptchaGuru.captchaSliderObjectGuru import (
    handleResolveCaptchaSliderObjectGuru,
)

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def handleInsertCookieAndWriteAccount(self):
    pageContent = self.driver.page_source
    if '"nickName":"' in pageContent:
        try:
            userId = pageContent.split('"nickName":"')[1].split('"')[0]
        except IndexError:
            userId = ""
    else:
        userId = ""
    cookies = self.driver.get_cookies()
    cookies_string = ";".join(
        [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
    )
    if userId:
        account = f"{userId}|{self.password_account}|{self.username_mail}|{self.password_mail}|{cookies_string}|{self.current_date}"
    else:
        account2 = f"{self.username_mail}|{self.password_account}|{self.password_mail}|{cookies_string}|{self.current_date}"
        with open("data/output_not_user_id.txt", "a") as f:
            f.write(account2 + "\n")

        self.self_main.total_success += 1
        self.self_main.total_success_account.setText(f"Số acc đã tạo thành công: {self.self_main.total_success}")
        QCoreApplication.processEvents()
    with open(self.output_file_path, "a") as f:
        f.write(account + "\n")

    self.self_main.total_success += 1
    self.self_main.total_success_account.setText(f"Số acc đã tạo thành công: {self.self_main.total_success}")
    QCoreApplication.processEvents()

def showSuccessAccount(self):
    item = QTableWidgetItem("Tạo tài khoản thành công...")
    green_color = QColor(64, 170, 15)
    item.setForeground(green_color)

    self.self_main.table_account_info.setItem(self.current_row_count, 3, item)
    QCoreApplication.processEvents()

def handleUploadAvatar(self):
    isGetUserIdAgain = True
    attemp = 0
    max_attemp = 3
    while isGetUserIdAgain:
        if attemp >= max_attemp:
            isGetUserIdAgain = False
            cookies = self.driver.get_cookies()
            cookies_string = ";".join(
                [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
            )
            account2 = f"{self.username_mail}|{self.password_account}|{self.password_mail}|{cookies_string}|{self.current_date}"
            with open("data/output_not_user_id.txt", "a") as f:
                f.write(account2 + "\n")
            return
        try:
            waitForNavigation = WebDriverWait(self.driver, 10)
            waitForNavigation.until(
            EC.presence_of_element_located(("xpath", '//*[@data-e2e="profile-icon"]'))
            )
            isGetUserIdAgain = False
        except TimeoutException:
            try:
                self.driver.get("https://www.tiktok.com")
                attemp += 1
                isGetUserIdAgain = True
            except WebDriverException:
                cookies = self.driver.get_cookies()
                cookies_string = ";".join(
                    [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
                )
                account2 = f"{self.username_mail}|{self.password_account}|{self.password_mail}|{cookies_string}|{self.current_date}"
                with open("data/output_not_user_id.txt", "a") as f:
                    f.write(account2 + "\n")
                isGetUserIdAgain = False
                return


    with open("configs_account.json", "r") as json_file:
        data = json.load(json_file)
        
    list_avatar_folder = data["url_avatar"]
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
            try:
                self.driver.get(f"https://www.tiktok.com/@{userId}")
            except WebDriverException:
                return
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
        waitForNavigation = WebDriverWait(self.driver, 60)
        editProfile = waitForNavigation.until(
            EC.presence_of_element_located(("xpath", '//span[text()="Sửa hồ sơ"]'))
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
    if len(inputUploadAvatar) > 0:
        inputUploadAvatar[0].send_keys(
            f"{list_avatar_folder}/{list_avatar[random_number(0, len(list_avatar) - 1)]}"
        )
        
    else:
        handleInsertCookieAndWriteAccount(self)
        showSuccessAccount(self)
        return

    wait(6, 8)
    try:
        waitForNavigation = WebDriverWait(self.driver, 20)
        applyAvatarBtn = waitForNavigation.until(
            EC.presence_of_element_located(("xpath", '//button[text()="Đăng ký"]'))
        )
        if not applyAvatarBtn.is_displayed():
            self.driver.execute_script("arguments[0].scrollIntoView();", applyAvatarBtn)
            applyAvatarBtn.click()
        else:
            handleInsertCookieAndWriteAccount(self)
            showSuccessAccount(self)
            return
    except NoSuchElementException:
        handleInsertCookieAndWriteAccount(self)
        showSuccessAccount(self)
        return
    except TimeoutException:
        handleInsertCookieAndWriteAccount(self)
        showSuccessAccount(self)
    
    is_random_name = self.self_main.is_change_username_check.isChecked()
    with open("configs_account.json", "r") as json_file:
        data = json.load(json_file)

    if "url_username" in data and data["url_username"]:
        with open(data["url_username"], "r", encoding="utf-8") as f:
            usernames = f.readlines()

    if is_random_name:
        if "url_username" in data and data["url_username"]:
            if self.type_reg_country == 0:
                wait(4, 6)
            else:
                wait(10, 12)
            user_random = usernames[random_number(0, len(usernames) - 1)]
            username = remove_accents(user_random).replace(" ", "").lower()
            username_random_by_file = f"{username}_{generate_random_name(8)}"
            editUserName = self.driver.find_elements("xpath", '//*[@placeholder="TikTok ID"]')
            editUserName[0].clear()
            editUserName[0].clear()
            if self.type_reg_country == 0:
                wait(4, 6)
            else:
                wait(10, 12)
            editUserName[0].send_keys(username_random_by_file)

            if self.type_reg_country == 0:
                wait(4, 6)
            else:
                wait(10, 12)
            editName = self.driver.find_elements("xpath", '//*[@placeholder="Tên"]')
            editName[0].clear()
            editName[0].clear()
            if self.type_reg_country == 0:
                wait(4, 6)
            else:
                wait(10, 12)
            editName[0].send_keys(user_random)
        else:
            if self.type_reg_country == 0:
                wait(4, 6)
            else:
                wait(10, 12)
            userNameRandom = f"{generate_random_name(8)}_{generate_random_name(8)}"
            editUserName = self.driver.find_elements("xpath", '//*[@placeholder="TikTok ID"]')
            editUserName[0].clear()
            editUserName[0].clear()
            if self.type_reg_country == 0:
                wait(4, 6)
            else:
                wait(10, 12)
            editUserName[0].send_keys(userNameRandom)

            if self.type_reg_country == 0:
                wait(4, 6)
            else:
                wait(10, 12)
            editName = self.driver.find_elements("xpath", '//*[@placeholder="Tên"]')
            editName[0].clear()
            editName[0].clear()
            if self.type_reg_country == 0:
                wait(4, 6)
            else:
                wait(10, 12)
            editName[0].send_keys(userNameRandom)

    wait(8, 10)
    saveElement = self.driver.find_elements("xpath", '//*[@data-e2e="edit-profile-save"]')
    
    try:
        saveElement[0].click()
        wait(4, 6)
        if is_random_name:
            confirmChangeUser = self.driver.find_element("xpath", '//*[@data-e2e="set-username-popup-confirm"]')
            confirmChangeUser.click()
        
        wait(6, 8)
        cookies = self.driver.get_cookies()
        cookies_string = ";".join(
            [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
        )
        wait(6, 8)
        try:
            get_user_id = self.driver.current_url.split("@")[1]
        except IndexError:
            get_user_id = ""
        
        if get_user_id:
            account = f"{get_user_id}|{self.password_account}|{self.username_mail}|{self.password_mail}|{cookies_string}|{self.current_date}"
        else:
            account2 = f"{self.username_mail}|{self.password_account}|{self.password_mail}|{cookies_string}|{self.current_date}"
            with open("data/output_not_user_id.txt", "a") as f:
                f.write(account2 + "\n")

            self.self_main.total_success += 1
            self.self_main.total_success_account.setText(f"Số acc đã tạo thành công: {self.self_main.total_success}")
            QCoreApplication.processEvents()
        
        # insert account
        with open(self.output_file_path, "a") as f:
            f.write(account + "\n")

        self.self_main.total_success += 1
        self.self_main.total_success_account.setText(f"Số acc đã tạo thành công: {self.self_main.total_success}")
        QCoreApplication.processEvents()
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
