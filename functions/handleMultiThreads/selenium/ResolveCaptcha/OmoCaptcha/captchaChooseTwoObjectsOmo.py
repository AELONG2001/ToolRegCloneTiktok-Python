import requests
import base64
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from utils.utils import wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import handleGetCode
from functions.handleMultiThreads.handleRestartThread.handleRestartThread import handleRestartThread
from functions.handleMultiThreads.handleRestartThread.handleRestartThreadNewMail import handleRestartThreadNewMail

def getResultCaptchaChooseTwoObjectsOmo(self, job_id):
    try:
        body = {
            "api_token": self.captcha_key,
            "job_id": job_id,
        }

        response = requests.post("https://omocaptcha.com/api/getJobResult", json=body)
        data = response.json()
        return data["result"]
    except requests.exceptions.RequestException as e:
        print(e)


def handleCreateJobGetCaptchaChooseTwoObjectsOmo(self, base64, width, height):
    try:
        self.self_main.table_account_info.setItem(
            self.current_row_count, 3, QTableWidgetItem("Đang đợi kết quả captcha...")
        )
        QCoreApplication.processEvents()
        body = {
            "api_token": self.captcha_key,
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
        return getResultCaptchaChooseTwoObjectsOmo(self, data["job_id"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaChooseTwoObjectsOmo(self):
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain:
        if self.type_reg_country == 0:
            wait(4, 6)
        else:
            wait(14, 16)
        captchaElements = self.driver.find_elements("css selector", "#captcha-verify-image")
        isNotCaptchaChooseTwoObjects = self.driver.find_elements("css selector", ".secsdk-captcha-drag-icon")
        if not isCheckResolveCaptchaAgain and captchaElements:
            self.self_main.table_account_info.setItem(
                self.current_row_count, 3, QTableWidgetItem("Có catpcha đợi giải...")
            )
            QCoreApplication.processEvents()

        # Nếu không có captcha thì return và lấy code
        if not captchaElements or isNotCaptchaChooseTwoObjects:
            return

        captchaElement = captchaElements[0]

        wait(3, 4)
        noInternetCaptcha = self.driver.find_elements(
                "xpath",
                '//div[contains(text(), "Không thể tải hình ảnh. Hãy làm mới để thử lại.")]',
            )
        
        if noInternetCaptcha:
            print("No internet captcha")
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                isResolveCaptchaAgain = False
                self.driver.quit()
                handleRestartThread(self)
                return
            else:
                return

        widthCaptcha = captchaElement.size["width"]
        heightCaptcha = captchaElement.size["height"]
        img_src = captchaElement.get_attribute("src")

        response = requests.get(img_src)
        response.raise_for_status()
        base64Data = base64.b64encode(response.content).decode("utf-8")

        result = handleCreateJobGetCaptchaChooseTwoObjectsOmo(
            self, base64Data, widthCaptcha, heightCaptcha
        )
        print("result: ", result)
        
        if result:
            [x1, y1, x2, y2] = result.split("|")
        else:
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                isResolveCaptchaAgain = False
                self.driver.quit()
                handleRestartThread(self)
                return
            else:
               return

        x1_relative = int(x1) - (widthCaptcha / 2)
        y1_relative = int(y1) - (heightCaptcha / 2)
        x2_relative = int(x2) - (widthCaptcha / 2)
        y2_relative = int(y2) - (heightCaptcha / 2)

        # hand logic click captcha
        action_chains = ActionChains(self.driver)

        try:
            action_chains.move_to_element_with_offset(
                captchaElement, x1_relative, y1_relative
            ).click().perform()

            wait(1, 2)

            action_chains.move_to_element_with_offset(
                captchaElement, x2_relative, y2_relative
            ).click().perform()
        except WebDriverException:
            print("Lỗi trong quá trình thực hiện chuỗi hành động")
            isResolveCaptchaAgain = False
            self.driver.quit()
            handleRestartThread(self)
            return

        wait(2, 3)
        submitCaptcha = self.driver.find_element(
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
        checkDectect = self.driver.find_elements(
            "xpath",
            '//span[contains(text(), "Bạn truy cập dịch vụ của chúng tôi quá thường xuyên..")]',
        )
        emailElement = self.driver.find_elements("css selector", "input[name='email']")

        if emailElement:
            if emailElement[0].value_of_css_property("color") == "rgba(255, 76, 58, 1)":
                isResolveCaptchaAgain = False
                self.driver.quit()
                handleRestartThreadNewMail(self)
                return
        
        if checkDectect:
            getCodeElement = self.driver.find_element(
                "xpath",
                '//*[@data-e2e="send-code-button"]',
            )
            if getCodeElement:
                handleGetCode(self)