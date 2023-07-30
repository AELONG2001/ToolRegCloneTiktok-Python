import requests
import base64
from PySide6.QtWidgets import *
from utils.utils import wait
from selenium.webdriver.common.action_chains import ActionChains
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import handleGetCode


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

        wait(10, 12)
        return getResultCaptchaChooseTwoObjectsOmo(data["job_id"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaChooseTwoObjectsOmo(self, thread, driver):
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

        result = handleCreateJobGetCaptchaChooseTwoObjectsOmo(
            self, thread, base64Data, widthCaptcha, heightCaptcha
        )
        print("result: ", result)

        [x1, y1, x2, y2] = result.split("|")

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
