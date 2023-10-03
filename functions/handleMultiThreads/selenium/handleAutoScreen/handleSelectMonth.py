from PySide6.QtWidgets import *
from utils.utils import random_number, wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)


def handleSelectMonth(self):

    # hotmail = f"{self.username}|{self.password}"

    # # lấy mail và update lại file
    # with open(self.input_file_path, "r") as f:
    #     mail_content = f.readlines()

    # for i in range(len(mail_content)):
    #     mail_content[i] = mail_content[i].replace("\n", "")

    # update_mail = []
    # for line in mail_content:
    #     if line.strip() != hotmail.strip():
    #         update_mail.append(line)

    # with open(self.input_file_path, "w") as f:
    #     for hotmail in update_mail:
    #         f.writelines(hotmail + "\n")

    self.self_main.table_account_info.setItem(
            self.current_row_count, 3, QTableWidgetItem("Bắt đầu reg...")
        )

    try:
        waitForNavigation = WebDriverWait(self.driver, 30)
        emailSelectElement = waitForNavigation.until(
                EC.presence_of_element_located(
                    ("xpath", '//*[@data-list-item-value="email"]')
                )
        )
        emailSelectElement.click()
        wait(2, 3)
        monthSelectElement = self.driver.find_element(
        "xpath", '//*[@aria-label="Month. Double-tap for more options"]'
        )
        monthSelectElement.click()
        self.self_main.table_account_info.setItem(
                self.current_row_count, 3, QTableWidgetItem("Đang chọn tháng...")
        )
        wait(4, 6)
        dropDownSelectMonth = self.driver.find_element(
            "id", f"Month-options-item-{random_number(0, 11)}"
        )
        dropDownSelectMonth.click()
    except:
        try:
            waitForNavigation = WebDriverWait(self.driver, 30)
            monthSelectElement = waitForNavigation.until(
                EC.presence_of_element_located(
                    ("xpath", '//*[@aria-label="Month. Double-tap for more options"]')
                )
            )
            monthSelectElement.click()
            self.self_main.table_account_info.setItem(
                self.current_row_count, 3, QTableWidgetItem("Đang chọn tháng...")
            )
            wait(4, 6)
            dropDownSelectMonth = self.driver.find_element(
                "id", f"Month-options-item-{random_number(0, 11)}"
            )
            dropDownSelectMonth.click()
        except TimeoutException:
            print("Không tìm thấy monthSelectElement sau khoảng thời gian chờ")
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

    

