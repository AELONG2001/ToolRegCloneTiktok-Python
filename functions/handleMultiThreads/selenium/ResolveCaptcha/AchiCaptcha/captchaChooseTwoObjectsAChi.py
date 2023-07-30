import requests
import base64
from PySide6.QtWidgets import *
from utils.utils import wait
from selenium.webdriver.common.action_chains import ActionChains
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import handleGetCode


def getResultCaptchaChooseTwoObjectsAChi(task_id):
    try:
        body = {
            "clientKey": "08f8b0f0b3aff156866a811508e2bb2e",
            "taskId": task_id,
        }

        response = requests.post("http://api.achicaptcha.com/getTaskResult", json=body)
        data = response.json()
        return data["solution"]
    except requests.exceptions.RequestException as e:
        print(e)


def handleCreateJobGetCaptchaChooseTwoObjectsAChi(self, thread, base64):
    try:
        self.table_account_info.setItem(
            thread, 3, QTableWidgetItem("Đang đợi kết quả captcha...")
        )
        body = {
            "clientKey": "08f8b0f0b3aff156866a811508e2bb2e",
            "task": {
                "type": "TiktokCaptchaTask",
                "subType": "2",
                "image": base64,
            },
        }

        response = requests.post("http://api.achicaptcha.com/createTask", json=body)
        data = response.json()

        wait(10, 12)
        return getResultCaptchaChooseTwoObjectsAChi(data["taskId"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaChooseTwoObjectsAChi(self, thread, driver):
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain:
        wait(2, 4)
        captchaElements = driver.find_elements("css selector", "#captcha-verify-image")
        if not isCheckResolveCaptchaAgain and captchaElements:
            self.table_account_info.setItem(
                thread, 3, QTableWidgetItem("Có catpcha đợi giải...")
            )

        # Nếu không có captcha thì return và lấy code
        if not captchaElements:
            return

        captchaElement = captchaElements[0]

        widthCaptcha = captchaElement.size["width"]
        heightCaptcha = captchaElement.size["height"]
        img_src = captchaElement.get_attribute("src")

        response = requests.get(img_src)
        response.raise_for_status()
        base64Data = base64.b64encode(response.content).decode("utf-8")

        result = handleCreateJobGetCaptchaChooseTwoObjectsAChi(self, thread, base64Data)
        print("result: ", result)

        [x1, y1, x2, y2] = result.split(",")

        x1_relative = int(x1) * 340 / 552 - (widthCaptcha / 2)
        y1_relative = int(y1) * 212 / 344 - (heightCaptcha / 2)
        x2_relative = int(x2) * 340 / 552 - (widthCaptcha / 2)
        y2_relative = int(y2) * 212 / 344 - (heightCaptcha / 2)

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
                handleGetCode(self, thread, driver)
