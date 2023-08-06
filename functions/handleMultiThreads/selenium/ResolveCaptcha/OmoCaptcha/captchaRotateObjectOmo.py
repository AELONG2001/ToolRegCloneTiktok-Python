from PySide6.QtWidgets import *
import requests
import base64
from selenium.webdriver.common.action_chains import ActionChains
from utils.utils import wait
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import handleGetCode


def getResultCaptchaRotateObjectOmo(job_id):
    try:
        body = {
            "api_token": "VO3raK5ZAM2zqw03ffZTYQVCaTNw0rwJ4dX9heNPncuwJXF7u2E2hPqkm54kc5lZtrBF8ENsAuPVG1So",
            "job_id": job_id,
        }

        response = requests.post("https://omocaptcha.com/api/getJobResult", json=body)
        data = response.json()
        return data["result"]
    except requests.exceptions.RequestException as e:
        print(e)


def handleCreateJobGetCaptchaRotateObjectOmo(
    self, thread, base64DataImgInside, base64DataImgOutside
):
    try:
        self.table_account_info.setItem(
            thread, 3, QTableWidgetItem("Đang đợi kết quả captcha...")
        )
        body = {
            "api_token": "VO3raK5ZAM2zqw03ffZTYQVCaTNw0rwJ4dX9heNPncuwJXF7u2E2hPqkm54kc5lZtrBF8ENsAuPVG1So",
            "data": {
                "type_job_id": "23",
                "image_base64": f"{base64DataImgInside}|{base64DataImgOutside}",
            },
        }

        response = requests.post("https://omocaptcha.com/api/createJob", json=body)
        data = response.json()

        wait(10, 12)
        return getResultCaptchaRotateObjectOmo(data["job_id"])
    except requests.exceptions.RequestException as e:
        print(e)


def handleResolveCaptchaRotateObjectOmo(self, thread, driver):
    isResolveCaptchaAgain = True
    isCheckResolveCaptchaAgain = False
    while isResolveCaptchaAgain and not self.stop_flag:
        wait(4, 6)
        captchaElements = driver.find_elements(
            "css selector", ".captcha_verify_slide--button"
        )
        if not isCheckResolveCaptchaAgain and captchaElements:
            self.table_account_info.setItem(
                thread, 3, QTableWidgetItem("Có catpcha đợi giải...")
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

        result = handleCreateJobGetCaptchaRotateObjectOmo(
            self, thread, base64DataImgInside, base64DataImgOutside
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
            thread, 3, QTableWidgetItem("Đang thực hiện giải captcha đợi xíu...")
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
                handleGetCode(self, thread, driver)
