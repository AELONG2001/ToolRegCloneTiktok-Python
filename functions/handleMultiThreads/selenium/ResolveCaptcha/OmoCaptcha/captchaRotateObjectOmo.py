from PySide6.QtWidgets import *
import requests
import base64
from selenium.webdriver.common.action_chains import ActionChains
from utils.utils import wait
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import handleGetCode
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)


def getResultCaptchaRotateObjectOmo(self, job_id):
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


def handleCreateJobGetCaptchaRotateObjectOmo(
    self, base64DataImgInside, base64DataImgOutside
):
    try:
        self.self_main.table_account_info.setItem(
            self.thread, 3, QTableWidgetItem("Đang đợi kết quả captcha...")
        )
        body = {
            "api_token": self.captcha_key,
            "data": {
                "type_job_id": "23",
                "image_base64": f"{base64DataImgInside}|{base64DataImgOutside}",
            },
        }

        response = requests.post("https://omocaptcha.com/api/createJob", json=body)
        data = response.json()

        wait(6, 8)
        return getResultCaptchaRotateObjectOmo(self, data["job_id"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaRotateObjectOmo(self):
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain and not self.stop_flag:
        wait(4, 6)
        captchaElements = self.driver.find_elements(
            "css selector", ".captcha_verify_slide--button"
        )
        isNotCaptchaRotate = self.driver.find_elements(
            "css selector", "#captcha-verify-image"
        )
        if not isCheckResolveCaptchaAgain and captchaElements:
            self.self_main.table_account_info.setItem(
                self.thread, 3, QTableWidgetItem("Có catpcha đợi giải...")
            )

        # Nếu không có captcha thì return và lấy code
        if not captchaElements or isNotCaptchaRotate:
            return
        
        captchaElement = captchaElements[0]

        wait(3, 4)
        noInternetCaptcha = self.driver.find_elements(
                "xpath",
                '//div[contains(text(), "No internet connection. Please try again.")]',
            )
        
        if noInternetCaptcha:
            print("No internet captcha")
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                # wait(1, 2)
                # with open(self.input_file_path, "a") as file:
                #     file.write(f"{self.username}|{self.password}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại..."),
                )
                self.self_main.restart_thread(self.num_threads, self.username, self.password)
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

        # Mã hóa các đường dẫn src thành chuỗi Base64
        encoded_img_list = []
        for img_src in img_src_list:
            try:
                response = requests.get(img_src)
                response.raise_for_status()  # Check if the request was successful

                encoded_image = base64.b64encode(response.content).decode("utf-8")
                encoded_img_list.append(encoded_image)
            except requests.exceptions.RequestException as e:
                print(e)

        if encoded_img_list and len(encoded_img_list) > 0:
            base64DataImgOutside = encoded_img_list[0]
            base64DataImgInside = encoded_img_list[1]
        else:
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                # wait(1, 2)
                # with open(self.input_file_path, "a") as file:
                #     file.write(f"{self.username}|{self.password}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại..."),
                )
                self.self_main.restart_thread(self.num_threads, self.username, self.password)
            else:
                return

        result = handleCreateJobGetCaptchaRotateObjectOmo(
            self.captcha_key, self, self.thread, base64DataImgInside, base64DataImgOutside
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
                # wait(1, 2)
                # with open(self.input_file_path, "a") as file:
                #     file.write(f"{self.username}|{self.password}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại..."),
                )
                self.self_main.restart_thread(self.num_threads, self.username, self.password)
            else:
                return

        num_steps = 5

        # Thực hiện kéo thả phần tử
        action_chains = ActionChains(self.driver)
        self.self_main.table_account_info.setItem(
            self.thread, 3, QTableWidgetItem("Đang thực hiện giải captcha đợi xíu...")
        )

        wait(3, 4)
        cannotLoadImageCaptcha = self.driver.find_elements(
                "xpath",
                '//div[contains(text(), "Couldn’t load image. Refresh to try again.")]',
            )
        
        if cannotLoadImageCaptcha:
            print("No load image captcha")
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                # wait(1, 2)
                # with open(self.input_file_path, "a") as file:
                #     file.write(f"{self.username}|{self.password}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại..."),
                )
                self.self_main.restart_thread(self.num_threads, self.username, self.password)
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
                '//div[contains(text(), "No internet connection. Please try again.")]',
            )
        
        if noInternetCaptcha:
            print("No internet captcha")
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                # wait(1, 2)
                # with open(self.input_file_path, "a") as file:
                #     file.write(f"{self.username}|{self.password}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại..."),
                )
                self.self_main.restart_thread(self.num_threads, self.username, self.password)
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
            '//span[contains(text(), "Maximum number of attempts reached. Try again later.")]',
        )
        if checkDectect:
            getCodeElement = self.driver.find_element(
                "xpath",
                '//*[@data-e2e="send-code-button"]',
            )
            if getCodeElement:
                handleGetCode(self)