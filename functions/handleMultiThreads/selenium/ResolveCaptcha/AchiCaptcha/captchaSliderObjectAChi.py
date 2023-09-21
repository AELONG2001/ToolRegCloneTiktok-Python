from PySide6.QtWidgets import *
import requests
import base64
from selenium.webdriver.common.action_chains import ActionChains
from utils.utils import wait
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import handleGetCode
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)

def getResultCaptchaSliderObjectAChi(captcha_key, task_id):
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


def handleCreateJobGetCaptchaSliderObjectAChi(
    captcha_key, self, base64, current_row_count
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
                "subType": "1",
                "image": f"{base64}",
            },
        }

        response = requests.post("http://api.achicaptcha.com/createTask", json=body)
        data = response.json()

        wait(6, 8)
        return getResultCaptchaSliderObjectAChi(captcha_key, data["taskId"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaSliderObjectAChi(captcha_key, self, thread, driver, accounts, current_row_count, profile_id):
    file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\hotmail.txt"
    username = accounts[thread][0]
    password = accounts[thread][1]
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain:
        wait(4, 6)
        captchaElements = driver.find_elements(
            "css selector", "#captcha-verify-image"
        )
        if not isCheckResolveCaptchaAgain and captchaElements:
            self.table_account_info.setItem(
                current_row_count,
                3,
                QTableWidgetItem("Có catpcha đợi giải..."),
            )

        if not captchaElements:
           return
        

        dragIcon = driver.find_element("css selector", ".secsdk-captcha-drag-icon")

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
                    QTableWidgetItem("Bị chặn, đợi restart lại..."),
                )
                self.restart_thread(thread)
            else:
                return


        img_src = captchaElement.get_attribute("src")

        print("img_src: ", img_src)

        response = requests.get(img_src)
        response.raise_for_status()
        base64Data = base64.b64encode(response.content).decode("utf-8")

        result = handleCreateJobGetCaptchaSliderObjectAChi(
            captcha_key, self, base64Data, current_row_count
        )
        print("result: ", result)

        # Lấy kích thước và tọa độ của phần tử
        element_rect = dragIcon.rect
        x = element_rect["x"]

        if result:
            # Tính toán tọa độ mới x1
            x1 = int(result) * 340 / 552 + 82
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
        action_chains.move_to_element(dragIcon).perform()
        action_chains.click_and_hold().perform()

        step_distance = (x1 - x) / num_steps

        # Di chuyển từng bước nhỏ và chờ một khoảng thời gian
        for _ in range(num_steps):
            action_chains.move_by_offset(step_distance, 0).perform()

        action_chains.release().perform()

        wait(4, 6)
        driver.refresh()

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
                handleGetCode(self, thread, driver, accounts, current_row_count, profile_id)
