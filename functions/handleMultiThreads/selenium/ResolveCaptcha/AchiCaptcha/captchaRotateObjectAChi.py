from PySide6.QtWidgets import *
import requests
import base64
from selenium.webdriver.common.action_chains import ActionChains
from utils.utils import wait
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import handleGetCode


def getResultCaptchaRotateObjectAChi(task_id):
    try:
        body = {
            "clientKey": "08f8b0f0b3aff156866a811508e2bb2e",
            "taskId": task_id,
        }

        response = requests.post("http://api.achicaptcha.com/getTaskResult", json=body)
        data = response.json()
        return data["solution"]
    except requests.exceptions.RequestException as e:
        print(e)


def handleCreateJobGetCaptchaRotateObjectAChi(
    self, thread, base64DataImgInside, base64DataImgOutside, current_row_count
):
    try:
        self.table_account_info.setItem(
            current_row_count,
            3,
            QTableWidgetItem("Đang đợi kết quả captcha..."),
        )
        body = {
            "clientKey": "08f8b0f0b3aff156866a811508e2bb2e",
            "task": {
                "type": "TiktokCaptchaTask",
                "subType": "0",
                "image": f"{base64DataImgOutside}|{base64DataImgInside}",
            },
        }

        response = requests.post("http://api.achicaptcha.com/createTask", json=body)
        data = response.json()

        wait(6, 8)
        return getResultCaptchaRotateObjectAChi(data["taskId"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaRotateObjectAChi(self, thread, driver, current_row_count):
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain:
        wait(4, 6)
        captchaElements = driver.find_elements(
            "css selector", ".captcha_verify_slide--button"
        )
        if not isCheckResolveCaptchaAgain and captchaElements:
            self.table_account_info.setItem(
                current_row_count,
                3,
                QTableWidgetItem("Có catpcha đợi giải..."),
            )

        # Nếu không có captcha thì return và lấy code
        if not captchaElements:
            return

        captchaElement = captchaElements[0]

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

        base64DataImgOutside = encoded_img_list[0]
        base64DataImgInside = encoded_img_list[1]

        result = handleCreateJobGetCaptchaRotateObjectAChi(
            self, thread, base64DataImgInside, base64DataImgOutside, current_row_count
        )
        print("result: ", result)

        # Lấy kích thước và tọa độ của phần tử
        element_rect = dragIcon.rect
        x = element_rect["x"]

        # Tính toán tọa độ mới x1
        x1 = int(result) + 82

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
                handleGetCode(self, thread, driver, current_row_count)
