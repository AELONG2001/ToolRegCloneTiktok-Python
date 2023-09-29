from PySide6.QtWidgets import *
from PySide6.QtGui import *
from utils.utils import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import os
import json
import re

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


def handleUploadAvatar(self, thread, input_file_path, output_file_path, driver, accounts, captcha_type, captcha_key, password_account, current_row_count, profile_id):
    wait(2, 4)
    output_file_path = output_file_path
    is_list_avtart_default = True

    with open("configs_account.json", "r") as json_file:
        data = json.load(json_file)
    if "url_avatar" in data:
        is_list_avtart_default = False
        list_avatar_folder = data["url_avatar"]     
    else:
        is_list_avtart_default = True
        list_avatar_folder = "data/wibus"
    username = accounts[thread][0]
    password = accounts[thread][1]

    list_avatar = os.listdir(list_avatar_folder)

    wait(2, 4)
    pageContent = driver.page_source
    if '"nickName":"' in pageContent:
        try:
            userId = pageContent.split('"nickName":"')[1].split('"')[0]
        except IndexError:
            return
    else:
        return
   
    try:
        if userId:
          driver.get(f"https://www.tiktok.com/@{userId}")
        else:
            cookies = driver.get_cookies()
            cookies_string = ";".join(
                [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
            )
            account = f"{username}|{password_account}|{password}|{cookies_string}"
            with open(output_file_path, "a") as f:
                f.write(account + "\n")
            return
    except WebDriverException:
        cookies = driver.get_cookies()
        cookies_string = ";".join(
            [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
        )
        account = f"{username}|{password_account}|{password}|{cookies_string}"
        with open(output_file_path, "a") as f:
            f.write(account + "\n")
        print("Không thể truy cập với user_id này")
        return

    
    # wait(4, 6)
    # checkCaptcha = driver.find_elements("css selector", "#verify-bar-close")

    # if checkCaptcha:
    #     return

    wait(4, 6)
    cookies = driver.get_cookies()
    cookies_string = ";".join(
        [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
    )
    account = f"{username}|{password_account}|{password}|{cookies_string}"

    # insert account
    with open(output_file_path, "a") as f:
        f.write(account + "\n")
    
    try:
        wait(2, 3)
        if captcha_type == "Achicaptcha":
            handleResolveCaptchaRotateObjectAChi(captcha_key, self, thread, input_file_path, driver, accounts, current_row_count, profile_id)
            handleResolveCaptchaChooseTwoObjectsAChi(captcha_key, self, thread, input_file_path, driver, accounts, current_row_count, profile_id)
            handleResolveCaptchaSliderObjectAChi(captcha_key, self, thread, input_file_path, driver, accounts, current_row_count, profile_id)
        else: 
            handleResolveCaptchaRotateObjectOmo(captcha_key, self, thread, input_file_path, driver, accounts, current_row_count, profile_id)
            handleResolveCaptchaChooseTwoObjectsOmo(captcha_key, self, thread, input_file_path, driver, accounts, current_row_count, profile_id)
            handleResolveCaptchaSliderObjectOmo(captcha_key, self, thread, input_file_path, driver, accounts, current_row_count, profile_id)

        waitForNavigation = WebDriverWait(driver, 200)
        editProfile = waitForNavigation.until(
            EC.presence_of_element_located(("xpath", '//span[text()="Edit profile"]'))
        )
       
        editProfile.click()
    except TimeoutException:
        print("Không tìm thấy Edit profile sau khoảng thời gian chờ")
        return
    except ElementClickInterceptedException:
        print("Không tìm thấy Edit profile sau khoảng thời gian chờ")
        return

    self.table_account_info.setItem(
        current_row_count, 3, QTableWidgetItem("Đang upload avatar...")
    )

    wait(2, 4)
    inputUploadAvatar = driver.find_elements("css selector", "input[type='file']")
    if inputUploadAvatar:
            if is_list_avtart_default:
                # current_file_path = os.path.abspath(__file__)
                # pattern = r"ToolRegCloneTiktok"
                # parts = re.split(pattern, current_file_path)

                relative_path = "data/wibus"
                absolute_path = os.path.abspath(relative_path)

                # if len(parts) > 1:
                # path_avatar_default_origin = parts[0]
                # path_avatar_default_origin = path_avatar_default_origin.replace("\\", "/")

                path_avatar_default_origin = absolute_path
                
                inputUploadAvatar[0].send_keys(
                    # f"{path_avatar_default_origin}ToolRegCloneTiktok/{list_avatar_folder}/{list_avatar[random_number(0, len(list_avatar) - 1)]}"
                    f"{path_avatar_default_origin}/{list_avatar[random_number(0, len(list_avatar) - 1)]}"
                )
            else:
                inputUploadAvatar[0].send_keys(
                    f"{list_avatar_folder}/{list_avatar[random_number(0, len(list_avatar) - 1)]}"
                )
        
    else:
        return

    wait(4, 6)
    applyAvatarBtn = driver.find_element("xpath", '//button[text()="Apply"]')
    try:
        if not applyAvatarBtn.is_displayed():
            # Sử dụng JavaScript để cuộn trang đến vị trí của phần tử
            driver.execute_script("arguments[0].scrollIntoView();", applyAvatarBtn)
        applyAvatarBtn.click()
    except NoSuchElementException:
        return
        

    wait(4, 6)
    saveElement = driver.find_element("xpath", '//*[@data-e2e="edit-profile-save"]')
    try:
        saveElement.click()
    except ElementClickInterceptedException:
        print("không tìm thấy saveElement")
        return
    
    self.table_account_info.setItem(
        current_row_count, 3, QTableWidgetItem("upload avatar thành công...")
    )

    item = QTableWidgetItem("Tạo tài khoản thành công...")
    green_color = QColor(64, 170, 15)
    item.setForeground(green_color)

    self.table_account_info.setItem(current_row_count, 3, item)

    wait(2, 4)
