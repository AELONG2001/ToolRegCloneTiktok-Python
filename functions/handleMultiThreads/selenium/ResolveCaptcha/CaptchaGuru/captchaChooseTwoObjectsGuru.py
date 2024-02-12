import re
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

def getResultCaptchaChooseTwoObjectsGuru(self, job_id):
    try:
        body = {
            "key": self.captcha_key,
            "action": "get",
            "id": job_id,
            "json": 1

        }

        response = requests.post("http://api.cap.guru/res.php", json=body).json()
        transformData = re.findall(r'x=(\d+),y=(\d+)', response["request"])
        data = '|'.join([f'{x}|{y}' for x, y in transformData])
        return data
    except requests.exceptions.RequestException as e:
        print(e)


def handleCreateJobGetCaptchaChooseTwoObjectsGuru(self, base64):
    try:
        self.self_main.table_account_info.setItem(
            self.current_row_count, 3, QTableWidgetItem("Đang đợi kết quả captcha...")
        )
        QCoreApplication.processEvents()
        body = {
            "key": self.captcha_key,
            "method": "base64",
            "textinstructions": "abc",
            "click": "geetest",
            "body": base64,
            "json": 1
        }

        response = requests.post("http://api.cap.guru/in.php", json=body).json()

        wait(6, 8)
        return getResultCaptchaChooseTwoObjectsGuru(self, response["request"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaChooseTwoObjectsGuru(self):
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain:
        wait(4, 6)
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

        # wait(3, 4)
        # noInternetCaptcha = self.driver.find_elements(
        #         "xpath",
        #         '//div[contains(text(), "Không thể tải hình ảnh. Hãy làm mới để thử lại.")]',
        #     )
        
        # if noInternetCaptcha:
        #     print("No internet captcha")
        #     if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
        #         isResolveCaptchaAgain = False
        #         self.driver.quit()
        #         handleRestartThread(self)
        #         return
        #     else:
        #         return
        
        widthCaptcha = captchaElement.size["width"]
        heightCaptcha = captchaElement.size["height"]
        img_src = captchaElement.get_attribute("src")

        response = requests.get(img_src)
        response.raise_for_status()
        base64Data = base64.b64encode(response.content).decode("utf-8")

        result = handleCreateJobGetCaptchaChooseTwoObjectsGuru(
            self, base64Data
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

        x1_relative = int(x1) * 340 / 552 - (widthCaptcha / 2)
        y1_relative = int(y1) * 212 / 344 - (heightCaptcha / 2)
        x2_relative = int(x2) * 340 / 552 - (widthCaptcha / 2)
        y2_relative = int(y2) * 212 / 344 - (heightCaptcha / 2)

        # hand logic click captcha
        action_chains = ActionChains(self.driver)

        # try:
        action_chains.move_to_element_with_offset(
            captchaElement, x1_relative, y1_relative
        ).click().perform()

        wait(1, 2)

        action_chains.move_to_element_with_offset(
            captchaElement, x2_relative, y2_relative
        ).click().perform()
        # except WebDriverException:
        #     print("Lỗi trong quá trình thực hiện chuỗi hành động")
        #     isResolveCaptchaAgain = False
        #     self.driver.quit()
        #     handleRestartThread(self)
        #     return
        
        wait(2, 3)
        submitCaptcha = self.driver.find_element(
            "css selector", ".verify-captcha-submit-button"
        )
        submitCaptcha.click()
        # wait(3, 4)
        # noInternetCaptchaVi = self.driver.find_elements(
        #     "xpath",
        #     '//div[contains(text(), "Không có kết nối Internet. Vui lòng thử lại.")]',
        # )
        # noInternetCaptchaEn = self.driver.find_elements(
        #     "xpath",
        #     '//div[contains(text(), "No internet connection. Please try again.")]',
        # )
        
        # if noInternetCaptchaVi or noInternetCaptchaEn:
        #     print("No internet captcha")
        #     if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
        #         isResolveCaptchaAgain = False
        #         self.driver.quit()
        #         handleRestartThread(self)
        #         return
        #     else:
        #         return
        # wait(3, 5)
        # if captchaElements:
        #     isResolveCaptchaAgain = True
        #     isCheckResolveCaptchaAgain = True
        # else:
        #     isResolveCaptchaAgain = False
        #     isCheckResolveCaptchaAgain = False

        # wait(4, 6)
        # checkDectect = self.driver.find_elements(
        #     "xpath",
        #     '//span[contains(text(), "Bạn truy cập dịch vụ của chúng tôi quá thường xuyên..")]',
        # )
        # emailElement = self.driver.find_elements("css selector", "input[name='email']")

        # if emailElement:
        #     if emailElement[0].value_of_css_property("color") == "rgba(255, 76, 58, 1)":
        #         isResolveCaptchaAgain = False
        #         self.driver.quit()
        #         handleRestartThreadNewMail(self)
        #         return
        
        # if checkDectect:
        #     getCodeElement = self.driver.find_element(
        #         "xpath",
        #         '//*[@data-e2e="send-code-button"]',
        #     )
        #     if getCodeElement:
        #         handleGetCode(self)