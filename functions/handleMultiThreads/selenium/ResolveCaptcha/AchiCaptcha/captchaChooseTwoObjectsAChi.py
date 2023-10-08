import requests
import base64
from PySide6.QtWidgets import *
from utils.utils import wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import handleGetCode
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)

def getResultCaptchaChooseTwoObjectsAChi(self, task_id):
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


def handleCreateJobGetCaptchaChooseTwoObjectsAChi(
    self, base64
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
                "subType": "2",
                "image": base64,
            },
        }

        response = requests.post("http://api.achicaptcha.com/createTask", json=body)
        data = response.json()

        wait(6, 8)
        return getResultCaptchaChooseTwoObjectsAChi(self, data["taskId"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaChooseTwoObjectsAChi(self):
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain:
        wait(4, 6)
        captchaElements = self.driver.find_elements("css selector", "#captcha-verify-image")
        isNotCaptchaChooseTwoObjects = self.driver.find_elements("css selector", ".secsdk-captcha-drag-icon")
        
        if not isCheckResolveCaptchaAgain and captchaElements:
            self.self_main.table_account_info.setItem(
                self.current_row_count,
                3,
                QTableWidgetItem("Có catpcha đợi giải..."),
            )

        if not captchaElements or isNotCaptchaChooseTwoObjects:
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
                    QTableWidgetItem("Bị chặn, đợi restart lại... 6"),
                )
                self.self_main.restart_thread(self.num_threads, self.username, self.password)
            else:
                return


        widthCaptcha = captchaElement.size["width"]
        heightCaptcha = captchaElement.size["height"]
        img_src = captchaElement.get_attribute("src")

        response = requests.get(img_src)
        response.raise_for_status()
        base64Data = base64.b64encode(response.content).decode("utf-8")

        result = handleCreateJobGetCaptchaChooseTwoObjectsAChi(
            self, base64Data
        )
        print("result: ", result)

        if result:
          [x1, y1, x2, y2] = result.split(",")
        else:
            if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
                # wait(1, 2)
                # with open(self.input_file_path, "a") as file:
                #         file.write(f"{self.username}|{self.password}\n")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                        self.current_row_count,
                        3,
                        QTableWidgetItem("Bị chặn, đợi restart lại... 7"),
                    )
                self.self_main.restart_thread(self.num_threads, self.username, self.password)
            else:
               return

        x1_relative = int(x1) * 340 / 552 - (widthCaptcha / 2)
        y1_relative = int(y1) * 212 / 344 - (heightCaptcha / 2)
        x2_relative = int(x2) * 340 / 552 - (widthCaptcha / 2)
        y2_relative = int(y2) * 212 / 344 - (heightCaptcha / 2)

        # hand logic click captcha
        try:
            action_chains = ActionChains(self.driver)

            action_chains.move_to_element_with_offset(
                captchaElement, x1_relative, y1_relative
            ).click().perform()

            wait(1, 2)

            action_chains.move_to_element_with_offset(
                captchaElement, x2_relative, y2_relative
            ).click().perform()
        except WebDriverException:
            print("Lỗi trong quá trình thực hiện chuỗi hành động")
            # wait(1, 2)
            # with open(self.input_file_path, "a") as file:
            #     file.write(f"{self.username}|{self.password}\n")
            self.driver.quit()
            handleDeleteProfile(self.profile_id)
            self.self_main.table_account_info.setItem(
                self.current_row_count,
                3,
                QTableWidgetItem("Bị chặn, đợi restart lại... 8"),
            )
            self.self_main.restart_thread(self.num_threads, self.username, self.password)

        wait(2, 3)
        submitCaptcha = self.driver.find_element(
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
        checkDectect = self.driver.find_elements(
            "xpath",
            '//span[contains(text(), "Maximum number of attempts reached. Try again later.")]',
        )
        # checkAccountCreated = self.driver.find_elements(
        #         "xpath",
        #         '//*[contains(@fill, "rgba(254, 44, 85, 1.0)")]',
        #     )
        
        # if checkAccountCreated:
        #         wait(1, 2)
        #         with open("data/account_created.txt", "a") as file:
        #             file.write(f"{self.username}|{self.password}\n")
        #         self.driver.quit()
        #         handleDeleteProfile(self.profile_id)
        #         self.self_main.table_account_info.setItem(
        #             self.current_row_count,
        #             3,
        #             QTableWidgetItem("Bị chặn, đợi restart lại... 30"),
        #         )
        #         self.self_main.restart_thread(self.num_threads, "", "")

        
        if checkDectect:
            getCodeElement = self.driver.find_element(
                "xpath",
                '//*[@data-e2e="send-code-button"]',
            )
            if getCodeElement:
                handleGetCode(self)
