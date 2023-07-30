from PySide6.QtWidgets import *
from PySide6.QtGui import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def handleInsertNewUsername(self, thread, driver):
    username = self.table_account_info.item(thread, 0).text()
    password = self.table_account_info.item(thread, 1).text()
    hotmail = f"{username}|{password}"
    account = f"{username}|Long123@|{password}"
    input_file_path = r"C:\Users\HD\OneDrive\Documents\Tools\Python\ToolRegCloneTiktok\data\hotmail.txt"
    output_file_path = r"C:\Users\HD\OneDrive\Documents\Tools\Python\ToolRegCloneTiktok\data\output.txt"

    waitForNavigation = WebDriverWait(driver, 100)
    skipElement = waitForNavigation.until(
        EC.presence_of_element_located(("xpath", '//div[text()="Skip"]'))
    )
    skipElement.click()

    item = QTableWidgetItem("Tạo tài khoản thành công...")
    green_color = QColor(64, 170, 15)
    item.setForeground(green_color)

    self.table_account_info.setItem(thread, 3, item)

    with open(input_file_path, "r") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")

    update_mail = [line for line in lines if line.strip() != hotmail]

    # update file hotmail when register successfully
    with open(input_file_path, "w") as f:
        for email in update_mail:
            f.writelines(email + "\n")

    # insert account
    with open(output_file_path, "a") as f:
        f.writelines(account + "\n")
