from PySide6.QtWidgets import *
from utils.utils import random_number, wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)


def handleSelectMonth(self, thread, driver, accounts, current_row_count, profile_id):
    input_file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\hotmail.txt"

    username = accounts[thread][0]
    password = accounts[thread][1]
    hotmail = f"{username}|{password}"

    with open(input_file_path, "r") as f:
        mail_content = f.readlines()

    for i in range(len(mail_content)):
        mail_content[i] = mail_content[i].replace("\n", "")

    update_mail = []
    for line in mail_content:
        if line.strip() != hotmail.strip():
            update_mail.append(line)

    with open(input_file_path, "w") as f:
        for hotmail in update_mail:
            f.writelines(hotmail + "\n")

    try:
        waitForNavigation = WebDriverWait(driver, 100)
        monthSelectElement = waitForNavigation.until(
            EC.presence_of_element_located(
                ("xpath", '//*[@aria-label="Month. Double-tap for more options"]')
            )
        )
        self.table_account_info.setItem(
            current_row_count, 3, QTableWidgetItem("Bắt đầu reg...")
        )
        monthSelectElement.click()
        self.table_account_info.setItem(
            current_row_count, 3, QTableWidgetItem("Đang chọn tháng...")
        )
        wait(4, 6)
        dropDownSelectMonth = driver.find_element(
            "id", f"Month-options-item-{random_number(0, 11)}"
        )
        dropDownSelectMonth.click()
    except TimeoutException:
        print("Không tìm thấy monthSelectElement sau khoảng thời gian chờ")
        file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\hotmail.txt"
        username = accounts[thread][0]
        password = accounts[thread][1]
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

