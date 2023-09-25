import requests
import base64
from PySide6.QtWidgets import *
from utils.utils import wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import handleGetCode
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)

def getResultCaptchaChooseTwoObjectsAChi(captcha_key, task_id):
    try:
        body = {
            "clientKey": captcha_key,
            "taskId": task_id,
        }

        response = requests.post("http://api.achicaptcha.com/getTaskResult", json=body)
        data = response.json()
        return data["solution"]
    except requests.exceptions.RequestException as e:
        print(e)


def handleCreateJobGetCaptchaChooseTwoObjectsAChi(
    captcha_key, self, base64, current_row_count
):
    try:
        self.table_account_info.setItem(
            current_row_count,
            3,
            QTableWidgetItem("Đang đợi kết quả captcha..."),
        )
        body = {
            "clientKey": captcha_key,
            "task": {
                "type": "TiktokCaptchaTask",
                "subType": "2",
                "image": base64,
            },
        }

        response = requests.post("http://api.achicaptcha.com/createTask", json=body)
        data = response.json()

        wait(6, 8)
        return getResultCaptchaChooseTwoObjectsAChi(captcha_key, data["taskId"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaChooseTwoObjectsAChi(captcha_key, self, thread, input_file_path, driver, accounts, current_row_count, profile_id):
    input_file_path = input_file_path
    username = accounts[thread][0]
    password = accounts[thread][1]
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain:
        wait(4, 6)
        captchaElements = driver.find_elements("css selector", "#captcha-verify-image")
        isNotCaptchaChooseTwoObjects = driver.find_elements("css selector", ".secsdk-captcha-drag-icon")
        
        if not isCheckResolveCaptchaAgain and captchaElements:
            self.table_account_info.setItem(
                current_row_count,
                3,
                QTableWidgetItem("Có catpcha đợi giải..."),
            )

        if not captchaElements or isNotCaptchaChooseTwoObjects:
           return
        
        captchaElement = captchaElements[0]

        wait(3, 4)
        noInternetCaptcha = driver.find_elements(
                "xpath",
                '//div[contains(text(), "No internet connection. Please try again.")]',
            )
        
        if noInternetCaptcha:
            print("No internet captcha")
            if driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                wait(1, 2)
                with open(input_file_path, "a") as file:
                    file.write(f"{username}|{password}\n")
                driver.quit()
                handleDeleteProfile(profile_id)
                self.table_account_info.setItem(
                    current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại..."),
                )
                self.restart_thread(thread)
            else:
                return


        widthCaptcha = captchaElement.size["width"]
        heightCaptcha = captchaElement.size["height"]
        img_src = captchaElement.get_attribute("src")

        response = requests.get(img_src)
        response.raise_for_status()
        base64Data = base64.b64encode(response.content).decode("utf-8")

        result = handleCreateJobGetCaptchaChooseTwoObjectsAChi(
            captcha_key, self, base64Data, current_row_count
        )
        print("result: ", result)

        if result:
          [x1, y1, x2, y2] = result.split(",")
        else:
            if driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                wait(1, 2)
                with open(input_file_path, "a") as file:
                        file.write(f"{username}|{password}\n")
                driver.quit()
                handleDeleteProfile(profile_id)
                self.table_account_info.setItem(
                        current_row_count,
                        3,
                        QTableWidgetItem("Bị chặn, đợi restart lại..."),
                    )
                self.restart_thread(thread)
            else:
               return

        x1_relative = int(x1) * 340 / 552 - (widthCaptcha / 2)
        y1_relative = int(y1) * 212 / 344 - (heightCaptcha / 2)
        x2_relative = int(x2) * 340 / 552 - (widthCaptcha / 2)
        y2_relative = int(y2) * 212 / 344 - (heightCaptcha / 2)

        # hand logic click captcha
        try:
            action_chains = ActionChains(driver)

            action_chains.move_to_element_with_offset(
                captchaElement, x1_relative, y1_relative
            ).click().perform()

            wait(1, 2)

            action_chains.move_to_element_with_offset(
                captchaElement, x2_relative, y2_relative
            ).click().perform()
        except WebDriverException:
            print("Lỗi trong quá trình thực hiện chuỗi hành động")
            wait(1, 2)
            with open(input_file_path, "a") as file:
                file.write(f"{username}|{password}\n")
            driver.quit()
            handleDeleteProfile(profile_id)
            self.table_account_info.setItem(
                current_row_count,
                3,
                QTableWidgetItem("Bị chặn, đợi restart lại..."),
            )
            self.restart_thread(thread)

        wait(2, 3)
        submitCaptcha = driver.find_element(
            "css selector", ".verify-captcha-submit-button"
        )
        submitCaptcha.click()

        wait(2, 4)
        if captchaElements:
            isResolveCaptchaAgain = True
            isCheckResolveCaptchaAgain = True
        else:
            isResolveCaptchaAgain = False
            isCheckResolveCaptchaAgain = False

        wait(4, 6)
        checkDectect = driver.find_elements(
            "xpath",
            '//span[contains(text(), "Maximum number of attempts reached. Try again later.")]',
        )
        if checkDectect:
            getCodeElement = driver.find_element(
                "xpath",
                '//*[@data-e2e="send-code-button"]',
            )
            if getCodeElement:
                handleGetCode(self, thread, input_file_path, driver, accounts, current_row_count, profile_id)
