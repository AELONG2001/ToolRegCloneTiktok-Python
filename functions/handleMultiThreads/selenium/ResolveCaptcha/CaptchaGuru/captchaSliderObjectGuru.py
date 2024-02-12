from PySide6.QtWidgets import *
from PySide6.QtCore import *
import requests
import base64
from selenium.webdriver.common.action_chains import ActionChains
from utils.utils import wait
from functions.handleMultiThreads.handleRestartThread.handleRestartThread import handleRestartThread

def getResultCaptchaSliderObjectGuru(self, job_id):
    try:
        body = {
            "key": self.captcha_key,
            "action": "get",
            "id": job_id,
            "json": 1

        }

        response = requests.post("http://api.cap.guru/res.php", json=body).json()
        data = response["request"].split("=")[1].split(',')[0]
        return data
    except requests.exceptions.RequestException as e:
        print(e)


def handleCreateJobGetCaptchaSliderObjectGuru(
    self, base64
):
    try:
        self.self_main.table_account_info.setItem(
            self.current_row_count,
            3,
            QTableWidgetItem("Đang đợi kết quả captcha..."),
        )
        QCoreApplication.processEvents()
        body = {
            "key": self.captcha_key,
            "method": "base64",
            "textinstructions": "slider",
            "click": "geetest",
            "body": base64,
            "json": 1
        }

        response = requests.post("http://api.cap.guru/in.php", json=body).json()

        wait(6, 8)
        return getResultCaptchaSliderObjectGuru(self, response["request"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaSliderObjectGuru(self):
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain:
        wait(8, 10)
        captchaElements = self.driver.find_elements(
            "css selector", "#captcha-verify-image"
        )
        if not isCheckResolveCaptchaAgain and captchaElements:
            self.self_main.table_account_info.setItem(
                self.current_row_count,
                3,
                QTableWidgetItem("Có catpcha đợi giải..."),
            )
            QCoreApplication.processEvents()

        if not captchaElements:
           return
        

        dragIcon = self.driver.find_element("css selector", ".secsdk-captcha-drag-icon")

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

        img_src = captchaElement.get_attribute("src")

        response = requests.get(img_src)
        response.raise_for_status()
        base64Data = base64.b64encode(response.content).decode("utf-8")

        result = handleCreateJobGetCaptchaSliderObjectGuru(
            self, base64Data
        )
        print("result: ", result)

        # Lấy kích thước và tọa độ của phần tử
        element_rect = dragIcon.rect
        x = element_rect["x"]

        if result:
            # Tính toán tọa độ mới x1
            x1 = int(result) * 340 / 552
        else:
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                isResolveCaptchaAgain = False
                self.driver.quit()
                handleRestartThread(self)
                return
            else:
                return

        num_steps = 5

        # Thực hiện kéo thả phần tử
        action_chains = ActionChains(self.driver)
        self.self_main.table_account_info.setItem(
            self.current_row_count,
            3,
            QTableWidgetItem("Đang thực hiện giải captcha đợi xíu..."),
        )
        QCoreApplication.processEvents()
        action_chains.move_to_element(dragIcon).perform()
        action_chains.click_and_hold().perform()

        step_distance = x1 / num_steps

        # Di chuyển từng bước nhỏ và chờ một khoảng thời gian
        for _ in range(num_steps):
            action_chains.move_by_offset(step_distance, 0).perform()

        action_chains.release().perform()

        # wait(4, 6)
        # self.driver.refresh()

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

        wait(2, 4)
        if captchaElements:
            isResolveCaptchaAgain = True
            isCheckResolveCaptchaAgain = True
        else:
            isResolveCaptchaAgain = False
            isCheckResolveCaptchaAgain = False

