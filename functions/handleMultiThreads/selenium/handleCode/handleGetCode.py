from PySide6.QtWidgets import *
from utils.utils import wait
from functions.handleMultiThreads.handleRestartThread.handleRestartThread import handleRestartThread
from functions.handleMultiThreads.handleRestartThread.handleRestartThreadNewMail import handleRestartThreadNewMail

def handleGetCode(self):
    self.self_main.table_account_info.scrollToBottom()
    try:
        
        max_attempts = 5  # Số lần tối đa xuất hiện checkDectect trước khi khởi động lại self.thread
        attempts = 0
        is_get_code_again = True

        while attempts < max_attempts and is_get_code_again:
            wait(4, 6)
            getCodeElement = self.driver.find_element(
                "xpath", '//*[@data-e2e="send-code-button"]'
            )
            self.self_main.table_account_info.setItem(
                self.current_row_count, 3, QTableWidgetItem("Ấn nút send code...")
            )
            getCodeElement.click()
            getCodeElement.click()

            wait(4, 6)
            checkDectect = self.driver.find_element(
                "xpath",
                '//span[contains(text(), "Maximum number of attempts reached. Try again later.")]',
            )
            
            emailElement = self.driver.find_elements("css selector", "input[name='email']")

            if emailElement:
                if emailElement[0].value_of_css_property("color") == "rgba(255, 76, 58, 1)":
                    wait(1, 2)
                    with open("data/account_created.txt", "a") as file:
                        file.write(f"{self.username_mail}|{self.password_mail}\n")
                    
                    attempts = 0
                    is_get_code_again = False

                    self.driver.quit()
                    handleRestartThreadNewMail(self)
                    return

            if checkDectect:
                is_get_code_again = True
                attempts += 1
            else:
                is_get_code_again = False
                attempts = 0

        # Nếu đã thực hiện đủ số lần tối đa, khởi động lại self.thread
        if attempts >= max_attempts:
            self.driver.quit()
            handleRestartThread(self)
            return

    except:
        return
