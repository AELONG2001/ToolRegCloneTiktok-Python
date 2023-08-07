from PySide6.QtWidgets import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def handleInsertNewUsername(thread, driver, accounts):
    output_file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\output.txt"

    username = accounts[thread][0]
    password = accounts[thread][1]
    account = f"{username}|Long123@|{password}"

    waitForNavigation = WebDriverWait(driver, 100)
    skipElement = waitForNavigation.until(
        EC.presence_of_element_located(("xpath", '//div[text()="Skip"]'))
    )
    skipElement.click()

    # with open(input_file_path, "r") as f:
    #     mail_content = f.readlines()

    # for i in range(len(mail_content)):
    #     mail_content[i] = mail_content[i].replace("\n", "")

    # update_mail = []
    # for line in mail_content:
    #     if line.strip() != hotmail.strip():
    #         update_mail.append(line)

    # update file hotmail when register successfully
    # with open(input_file_path, "w") as f:
    #     for email in update_mail:
    #         f.writelines(email + "\n")

    # insert account
    with open(output_file_path, "a") as f:
        f.write(account + "\n")
