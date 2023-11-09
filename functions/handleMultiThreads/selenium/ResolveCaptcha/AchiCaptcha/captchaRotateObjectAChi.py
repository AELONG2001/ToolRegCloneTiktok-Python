from PySide6.QtWidgets import *
import requests
import base64
from selenium.webdriver.common.action_chains import ActionChains
from utils.utils import wait
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import handleGetCode
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)

def getResultCaptchaRotateObjectAChi(self, task_id):
    try:
        body = {
            "clientKey": self.captcha_key,
            "taskId": task_id,
        }

        response = requests.post("http://api.achicaptcha.com/getTaskResult", json=body)
        data = response.json()
        return data["solution"]
    except requests.exceptions.RequestException as e:
        print(e)


def handleCreateJobGetCaptchaRotateObjectAChi(
    self, base64DataImgInside, base64DataImgOutside
):
    try:
        self.self_main.table_account_info.setItem(
            self.current_row_count,
            3,
            QTableWidgetItem("Đang đợi kết quả captcha..."),
        )
        body = {
            "clientKey": self.captcha_key,
            "task": {
                "type": "TiktokCaptchaTask",
                "subType": "0",
                "image": f"{base64DataImgOutside}|{base64DataImgInside}",
            },
        }

        response = requests.post("http://api.achicaptcha.com/createTask", json=body)
        data = response.json()

        wait(6, 8)
        return getResultCaptchaRotateObjectAChi(self, data["taskId"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaRotateObjectAChi(self):
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain:
        wait(4, 6)
        captchaElements = self.driver.find_elements(
            "css selector", ".captcha_verify_slide--button"
        )
        isNotCaptchaRotate = self.driver.find_elements(
            "css selector", "#captcha-verify-image"
        )
        if not isCheckResolveCaptchaAgain and captchaElements:
            self.self_main.table_account_info.setItem(
                self.current_row_count,
                3,
                QTableWidgetItem("Có catpcha đợi giải..."),
            )

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
                #     file.write(f"{self.username_mail}|{self.password_mail}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại... 9"),
                )
                self.self_main.restart_thread(self.num_threads, self.username_mail, self.password_mail)
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

        wait(2, 4)
        if encoded_img_list and len(encoded_img_list) > 0:
            base64DataImgOutside = encoded_img_list[0]
            base64DataImgInside = encoded_img_list[1]
        else:
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                # wait(1, 2)
                # with open(self.input_file_path, "a") as file:
                #     file.write(f"{self.username_mail}|{self.password_mail}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại... 10"),
                )
                self.self_main.restart_thread(self.num_threads, self.username_mail, self.password_mail)
                return
            else:
                return

        result = handleCreateJobGetCaptchaRotateObjectAChi(
            self, base64DataImgInside, base64DataImgOutside
        )
        print("result: ", result)            

        # Lấy kích thước và tọa độ của phần tử
        element_rect = dragIcon.rect
        x = element_rect["x"]

        if result:
            # Tính toán tọa độ mới x1
            x1 = int(result) + 82
        else:
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                # wait(1, 2)
                # with open(self.input_file_path, "a") as file:
                #     file.write(f"{self.username_mail}|{self.password_mail}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại... 11"),
                )
                self.self_main.restart_thread(self.num_threads, self.username_mail, self.password_mail)
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
                #     file.write(f"{self.username_mail}|{self.password_mail}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại... 12"),
                )
                self.self_main.restart_thread(self.num_threads, self.username_mail, self.password_mail)
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
                '//div[contains(text(), "No internet connection. Please try again.")]',
            )
        
        if noInternetCaptcha:
            print("No internet captcha")
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                # wait(1, 2)
                # with open(self.input_file_path, "a") as file:
                #     file.write(f"{self.username_mail}|{self.password_mail}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại... 13"),
                )
                self.self_main.restart_thread(self.num_threads, self.username_mail, self.password_mail)
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
            '//span[contains(text(), "Maximum number of attempts reached. Try again later.")]',
        )
        emailElement = self.driver.find_elements("css selector", "input[name='email']")

        if emailElement:
            if emailElement[0].value_of_css_property("color") == "rgba(255, 76, 58, 1)":
                wait(1, 2)
                with open("data/account_created.txt", "a") as file:
                    file.write(f"{self.username_mail}|{self.password_mail}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    self.current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại... 30"),
                )
                self.self_main.restart_thread(self.num_threads, "", "")
                return

        if checkDectect:
            getCodeElement = self.driver.find_element(
                "xpath",
                '//*[@data-e2e="send-code-button"]',
            )
            if getCodeElement:
                handleGetCode(self)
