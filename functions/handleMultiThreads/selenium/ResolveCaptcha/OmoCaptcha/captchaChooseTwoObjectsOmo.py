import requests
import base64
from PySide6.QtWidgets import *
from utils.utils import wait
from selenium.webdriver.common.action_chains import ActionChains
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import handleGetCode
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)


def getResultCaptchaChooseTwoObjectsOmo(job_id):
    try:
        body = {
            "api_token": "VO3raK5ZAM2zqw03ffZTYQVCaTNw0rwJ4dX9heNPncuwJXF7u2E2hPqkm54kc5lZtrBF8ENsAuPVG1So",
            "job_id": job_id,
        }

        response = requests.post("https://omocaptcha.com/api/getJobResult", json=body)
        data = response.json()
        return data["result"]
    except requests.exceptions.RequestException as e:
        print(e)


def handleCreateJobGetCaptchaChooseTwoObjectsOmo(self, thread, base64, width, height):
    try:
        self.table_account_info.setItem(
            thread, 3, QTableWidgetItem("Đang đợi kết quả captcha...")
        )
        body = {
            "api_token": "VO3raK5ZAM2zqw03ffZTYQVCaTNw0rwJ4dX9heNPncuwJXF7u2E2hPqkm54kc5lZtrBF8ENsAuPVG1So",
            "data": {
                "type_job_id": "22",
                "image_base64": base64,
                "width_view": width,
                "height_view": height,
            },
        }

        response = requests.post("https://omocaptcha.com/api/createJob", json=body)
        data = response.json()

        wait(6, 8)
        return getResultCaptchaChooseTwoObjectsOmo(data["job_id"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaChooseTwoObjectsOmo(self, thread, driver, accounts, current_row_count, profile_id):
    file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\hotmail.txt"
    username = accounts[thread][0]
    password = accounts[thread][1]
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain and not self.stop_flag:
        wait(2, 4)
        captchaElements = driver.find_elements("css selector", "#captcha-verify-image")
        isNotCaptchaChooseTwoObjects = driver.find_elements("css selector", ".secsdk-captcha-drag-icon")
        if not isCheckResolveCaptchaAgain and captchaElements:
            self.table_account_info.setItem(
                thread, 3, QTableWidgetItem("Có catpcha đợi giải...")
            )

        # Nếu không có captcha thì return và lấy code
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
                with open(file_path, "a") as file:
                    file.write(f"{username}|{password}\n")
                driver.quit()
                handleDeleteProfile(profile_id)
                self.table_account_info.setItem(
                    current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại...17"),
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

        result = handleCreateJobGetCaptchaChooseTwoObjectsOmo(
            self, thread, base64Data, widthCaptcha, heightCaptcha
        )
        print("result: ", result)
        
        if result:
            [x1, y1, x2, y2] = result.split("|")
        else:
            if driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                wait(1, 2)
                with open(file_path, "a") as file:
                        file.write(f"{username}|{password}\n")
                driver.quit()
                handleDeleteProfile(profile_id)
                self.table_account_info.setItem(
                        current_row_count,
                        3,
                        QTableWidgetItem("Bị chặn, đợi restart lại...18"),
                    )
                self.restart_thread(thread)
            else:
               return

        x1_relative = int(x1) - (widthCaptcha / 2)
        y1_relative = int(y1) - (heightCaptcha / 2)
        x2_relative = int(x2) - (widthCaptcha / 2)
        y2_relative = int(y2) - (heightCaptcha / 2)

        # hand logic click captcha
        action_chains = ActionChains(driver)

        action_chains.move_to_element_with_offset(
            captchaElement, x1_relative, y1_relative
        ).click().perform()

        wait(1, 2)

        action_chains.move_to_element_with_offset(
            captchaElement, x2_relative, y2_relative
        ).click().perform()

        wait(2, 3)
        submitCaptcha = driver.find_element(
            "css selector", ".verify-captcha-submit-button"
        )
        submitCaptcha.click()

        wait(3, 5)
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
                handleGetCode(self, thread, driver, accounts, current_row_count, profile_id)