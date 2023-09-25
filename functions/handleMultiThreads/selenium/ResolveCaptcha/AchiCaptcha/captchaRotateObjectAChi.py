from PySide6.QtWidgets import *
import requests
import base64
from selenium.webdriver.common.action_chains import ActionChains
from utils.utils import wait
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import handleGetCode
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)

def getResultCaptchaRotateObjectAChi(captcha_key, task_id):
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


def handleCreateJobGetCaptchaRotateObjectAChi(
    captcha_key, self, base64DataImgInside, base64DataImgOutside, current_row_count
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
                "subType": "0",
                "image": f"{base64DataImgOutside}|{base64DataImgInside}",
            },
        }

        response = requests.post("http://api.achicaptcha.com/createTask", json=body)
        data = response.json()

        wait(6, 8)
        return getResultCaptchaRotateObjectAChi(captcha_key, data["taskId"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaRotateObjectAChi(captcha_key, self, thread, input_file_path, driver, accounts, current_row_count, profile_id):
    input_file_path = input_file_path
    username = accounts[thread][0]
    password = accounts[thread][1]
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain:
        wait(4, 6)
        captchaElements = driver.find_elements(
            "css selector", ".captcha_verify_slide--button"
        )
        isNotCaptchaRotate = driver.find_elements(
            "css selector", "#captcha-verify-image"
        )
        if not isCheckResolveCaptchaAgain and captchaElements:
            self.table_account_info.setItem(
                current_row_count,
                3,
                QTableWidgetItem("Có catpcha đợi giải..."),
            )

        if not captchaElements or isNotCaptchaRotate:
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


        dragIcon = driver.find_element("css selector", ".secsdk-captcha-drag-icon")

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

        result = handleCreateJobGetCaptchaRotateObjectAChi(
            captcha_key, self, base64DataImgInside, base64DataImgOutside, current_row_count
        )
        print("result: ", result)            

        # Lấy kích thước và tọa độ của phần tử
        element_rect = dragIcon.rect
        x = element_rect["x"]

        if result:
            # Tính toán tọa độ mới x1
            x1 = int(result) + 82
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

        num_steps = 5

        # Thực hiện kéo thả phần tử
        action_chains = ActionChains(driver)
        self.table_account_info.setItem(
            current_row_count,
            3,
            QTableWidgetItem("Đang thực hiện giải captcha đợi xíu..."),
        )

        wait(3, 4)
        cannotLoadImageCaptcha = driver.find_elements(
                "xpath",
                '//div[contains(text(), "Couldn’t load image. Refresh to try again.")]',
            )
        
        if cannotLoadImageCaptcha:
            print("No load image captcha")
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
        
        action_chains.move_to_element(dragIcon).perform()
        action_chains.click_and_hold().perform()

        step_distance = (x1 - x) / num_steps

        # Di chuyển từng bước nhỏ và chờ một khoảng thời gian
        for _ in range(num_steps):
            action_chains.move_by_offset(step_distance, 0).perform()

        action_chains.release().perform()

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
