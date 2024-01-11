import re
import requests
import base64
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from selenium.webdriver.common.action_chains import ActionChains
from utils.utils import wait
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import handleGetCode
from functions.handleMultiThreads.handleRestartThread.handleRestartThread import handleRestartThread
from functions.handleMultiThreads.handleRestartThread.handleRestartThreadNewMail import handleRestartThreadNewMail

def getResultCaptchaRotateObjectGuru(self, job_id):
    try:
        params = {
            "key": self.captcha_key,
            "id": job_id,

        }
        response = requests.get("http://api.cap.guru/res.php", params=params).text
        getValueResponse = response.split("|")[1]
        data = getValueResponse.split("y=")[1]
        return data
    except requests.exceptions.RequestException as e:
        print(e)


def handleCreateJobGetCaptchaRotateObjectGuru(
    self, base64DataImgOutside, base64DataImgInside
):
    try:
        self.self_main.table_account_info.setItem(
            self.current_row_count, 3, QTableWidgetItem("Đang đợi kết quả captcha...")
        )
        QCoreApplication.processEvents()
        body = {
            "key": self.captcha_key,
            "method": "base64",
            "textinstructions": "koleso",
            "click": "geetest",
            "body0": base64DataImgOutside,
            "body1": base64DataImgInside,
        }
        response = requests.post("http://api.cap.guru/in.php", data=body)
        data = response.text.split("|")[1]

        wait(6, 8)
        return getResultCaptchaRotateObjectGuru(self, data)
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaRotateObjectGuru(self):
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain:
        if self.type_reg_country == 0:
            wait(4, 6)
        else:
            wait(14, 16)
        captchaElements = self.driver.find_elements(
            "css selector", ".captcha_verify_slide--button"
        )
        isNotCaptchaRotate = self.driver.find_elements(
            "css selector", "#captcha-verify-image"
        )
        if not isCheckResolveCaptchaAgain and captchaElements:
            self.self_main.table_account_info.setItem(
                self.current_row_count, 3, QTableWidgetItem("Có catpcha đợi giải...")
            )
            QCoreApplication.processEvents()

        # Nếu không có captcha thì return và lấy code
        if not captchaElements or isNotCaptchaRotate:
            return
        
        captchaElement = captchaElements[0]

        wait(3, 4)
        noInternetCaptcha = self.driver.find_elements(
                "xpath",
                '//div[contains(text(), "Không thể tải hình ảnh. Hãy làm mới để thử lại.")]',
        )
        
        cannotLoadImageCaptcha = self.driver.find_elements(
                "xpath",
                '//div[contains(text(), "Couldn’t load image. Refresh to try again.")]',
        )
        
        if noInternetCaptcha:
            print("No internet captcha")
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                isResolveCaptchaAgain = False
                self.driver.close()
                handleRestartThread(self)
                return
            else:
                return
        
       
        
        if cannotLoadImageCaptcha:
            print("No load image captcha")
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                isResolveCaptchaAgain = False
                self.driver.close()
                handleRestartThread(self)
                return
            else:
                return
        dragIcon = self.driver.find_element("css selector", ".secsdk-captcha-drag-icon")

        divContainTwoImgCaptcha = captchaElement.find_element(
            "xpath", "preceding-sibling::div[1]"
        )

        imgsCaptcha = divContainTwoImgCaptcha.find_elements("tag name", "img")

        img_src_list = []
        # Lặp qua từng thẻ img và lấy thuộc tính src
        for img_element in imgsCaptcha:
            img_src = img_element.get_attribute("src")
            img_src_list.append(img_src)

        # encoded_img_list = []
        # for img_src in img_src_list:
        #     try:
        #         response = requests.get(img_src)
        #         response.raise_for_status()  # Check if the request was successful

        #         encoded_image = base64.b64encode(response.content).decode("utf-8")
        #         encoded_img_list.append(encoded_image)
        #     except requests.exceptions.RequestException as e:
        #         print(e)

        if img_src_list and len(img_src_list) > 0:
            base64DataImgOutside = base64.b64encode((img_src_list[0]).encode('utf-8'))
            base64DataImgInside = base64.b64encode((img_src_list[1]).encode('utf-8'))
        else:
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                isResolveCaptchaAgain = False
                self.driver.close()
                handleRestartThread(self)
                return
            else:
                return
            
        result = handleCreateJobGetCaptchaRotateObjectGuru(
            self, base64DataImgOutside, base64DataImgInside
        )
        print("result: ", result)
        
        # Lấy kích thước và tọa độ của phần tử
        element_rect = dragIcon.rect
        x = element_rect["x"]

        # Tính toán tọa độ mới x1
        if result:
          x1 = int(result) + 82
        else:
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                isResolveCaptchaAgain = False
                self.driver.close()
                handleRestartThread(self)
                return
            else:
                return

        num_steps = 5

        # Thực hiện kéo thả phần tử
        action_chains = ActionChains(self.driver)
        self.self_main.table_account_info.setItem(
            self.current_row_count, 3, QTableWidgetItem("Đang thực hiện giải captcha đợi xíu...")
        )
        QCoreApplication.processEvents()

        wait(3, 4)
        cannotLoadImageCaptcha = self.driver.find_elements(
                "xpath",
                '//div[contains(text(), "Couldn’t load image. Refresh to try again.")]',
            )
        
        if cannotLoadImageCaptcha:
            print("No load image captcha")
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                isResolveCaptchaAgain = False
                self.driver.close()
                handleRestartThread(self)
                return
            else:
                return
            
        action_chains.move_to_element(dragIcon).perform()
        action_chains.click_and_hold().perform()

        step_distance = (x1 - x) / num_steps

        # Di chuyển từng bước nhỏ và chờ một khoảng thời gian
        for _ in range(num_steps):
            action_chains.move_by_offset(step_distance, 0).perform()

        action_chains.release().perform()

        wait(3, 4)
        noInternetCaptcha = self.driver.find_elements(
                "xpath",
                '//div[contains(text(), "Không có kết nối Internet. Vui lòng thử lại.")]',
            )
        
        if noInternetCaptcha:
            print("No internet captcha")
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
               isResolveCaptchaAgain = False
               self.driver.close()
               handleRestartThread(self)
               return
            else:
                return

        wait(2, 4)
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
                self.driver.close()
                handleRestartThreadNewMail(self)
                return

                
        if checkDectect:
            getCodeElement = self.driver.find_element(
                "xpath",
                '//*[@data-e2e="send-code-button"]',
            )
            if getCodeElement:
                handleGetCode(self)