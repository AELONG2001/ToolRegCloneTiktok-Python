from PySide6.QtWidgets import *
from PySide6.QtCore import *
from selenium import webdriver
import math
from time import sleep
from utils.utils import wait

from functions.handleGetProfiles.handleGetProfiles import (
    handleGetProfileIdsFromGoLogin,
)

from functions.proxy.handleGetNewTMProxy import (
    handleGetNewTMProxy,
)

from functions.handleInputFileMail.getMailContent import getMailContent


from functions.handleMultiThreads.selenium.handleAutoScreen.handleSelectMonth import (
    handleSelectMonth,
)
from functions.handleMultiThreads.selenium.handleAutoScreen.handleSelectDay import (
    handleSelectDay,
)
from functions.handleMultiThreads.selenium.handleAutoScreen.handleSelectYear import (
    handleSelectYear,
)
from functions.handleMultiThreads.selenium.handleAutoScreen.handleInputUserNameAndPassword import (
    handleInputUserNameAndPassword,
)
from functions.handleMultiThreads.selenium.handleAutoScreen.handleSubmitAccount import (
    handleSubmitAccount,
)
from functions.handleMultiThreads.selenium.handleAutoScreen.handleInsertNewUsername import (
    handleInsertNewUsername,
)
from functions.handleMultiThreads.selenium.handleCode.handleGetCode import (
    handleGetCode,
)
from functions.handleMultiThreads.selenium.handleCode.handleGetCodeFromMail import (
    handleGetCodeFromMail,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.OmoCaptcha.captchaRotateObjectOmo import (
    handleResolveCaptchaRotateObjectOmo,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.OmoCaptcha.captchaChooseTwoObjectsOmo import (
    handleResolveCaptchaChooseTwoObjectsOmo,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.AchiCaptcha.captchaRotateObjectAChi import (
    handleResolveCaptchaRotateObjectAChi,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.AchiCaptcha.captchaChooseTwoObjectsAChi import (
    handleResolveCaptchaChooseTwoObjectsAChi,
)

from functions.HandleUploadAvatar.handleUploadAvatar import handleUploadAvatar


class AutomationThread(QThread):
    def __init__(
        self,
        self_main,
        stop_event,
        num_threads,
        chrome_count,
        chrome_percent_zoom,
        is_show_chrome,
    ):
        super().__init__()
        self.self_main = self_main
        self.stop_event = stop_event
        self.num_threads = num_threads
        self.chrome_count = chrome_count
        self.chrome_percent_zoom = chrome_percent_zoom
        self.is_show_chrome = is_show_chrome
        self.is_running = True
        self.stop_flag = False

        self.options = webdriver.ChromeOptions()

    @Slot()
    def show_warning(self):
        QMessageBox.warning(
            None,
            "Warning",
            "Vui lòng nhập thêm mail",
        )

    def stop(self):
        print("Stoped")
        self.stop_flag = True
        for thread in self.self_main.chrome_threads:
            thread.terminate()

        self.self_main.stop_progress_dialog.show()
        QCoreApplication.processEvents()

        if hasattr(self, "driver"):
            self.driver.quit()
            AutomationThread.num_quit += 1

        total_threads = len(self.self_main.chrome_threads)
        completed_threads = AutomationThread.num_quit
        percent_complete = (completed_threads / total_threads) * 100

        self.self_main.stop_progress_dialog.set_progress(percent_complete)
        self.self_main.stop_progress_dialog.set_progress_text(
            f"Đã dừng {completed_threads} luồng"
        )

        QCoreApplication.processEvents()
        sleep(1)

        self.self_main.stop_progress_dialog.close()

    def run(self):
        list_profile = handleGetProfileIdsFromGoLogin()
        list_proxy = handleGetNewTMProxy(self.self_main)

        num_worker = self.num_threads
        chrome_percent_zoom = self.chrome_percent_zoom
        is_show_chrome = self.is_show_chrome

        if not is_show_chrome:
            self.options.add_argument("--headless")
        self.options.add_argument(f"--force-device-scale-factor={chrome_percent_zoom}")
        self.options.add_argument("--mute-audio")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument(f"--user-data-dir={list_profile[num_worker]}")
        # self.options.add_argument(f"--proxy-server={list_proxy[num_worker]}")

        self.driver = webdriver.Chrome(options=self.options)

        num_chrome_a_row = int(self.chrome_count)
        # Số cột muốn sắp xếp trên màn hình
        cols = num_chrome_a_row
        x = (num_worker % cols) * 510
        y = math.floor(num_worker / cols) * 810
        self.driver.set_window_rect(x, y, 200, 800)
        while not self.stop_flag:
            input_file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\hotmail.txt"

            with open(input_file_path, "r") as f:
                mail_content = f.read()

            accounts = getMailContent(mail_content)

            if len(accounts) > 0:
                username, password = accounts[num_worker]
                current_row_count = self.self_main.table_account_info.rowCount()
                self.self_main.table_account_info.setRowCount(current_row_count + 1)
                self.self_main.table_account_info.setItem(
                    current_row_count, 0, QTableWidgetItem(username)
                )
                self.self_main.table_account_info.setItem(
                    current_row_count, 1, QTableWidgetItem(password)
                )
            else:
                if hasattr(self, "driver"):
                    self.driver.quit()
                QMetaObject.invokeMethod(self, "show_warning")
                self.self_main.stop_button.setEnabled(False)
                self.self_main.stop_button.setStyleSheet(
                    "background-color: rgba(0, 0, 0, 0.2);"
                )
                self.self_main.start_button.setEnabled(True)
                self.self_main.start_button.setStyleSheet(
                    "color:rgb(255, 252, 252);\n" "background-color:rgb(64, 170, 15)"
                )
                return

            AutomationThread.drivers_list.append(self.driver)
            self.driver.get("https://www.tiktok.com/signup/phone-or-email/email")
            handleSelectMonth(
                self.self_main,
                self.num_threads,
                self.driver,
                accounts,
                current_row_count,
            )
            handleSelectDay(
                self.self_main, self.num_threads, self.driver, current_row_count
            )
            handleSelectYear(
                self.self_main, self.num_threads, self.driver, current_row_count
            )
            handleInputUserNameAndPassword(
                self.self_main,
                self.num_threads,
                self.driver,
                accounts,
                current_row_count,
            )
            handleGetCode(
                self.self_main, self.num_threads, self.driver, current_row_count
            )

            # Resolve captcha by Omo
            # handleResolveCaptchaRotateObjectOmo(
            #     self.self_main, self.num_threads, self.driver
            # )

            # handleResolveCaptchaChooseTwoObjectsOmo(
            #     self.self_main, self.num_threads, self.driver
            # )

            # Resolve captcha by Achi
            handleResolveCaptchaRotateObjectAChi(
                self.self_main, self.num_threads, self.driver, current_row_count
            )
            handleResolveCaptchaChooseTwoObjectsAChi(
                self.self_main, self.num_threads, self.driver, current_row_count
            )

            handleGetCodeFromMail(
                self.self_main,
                self.num_threads,
                self.driver,
                accounts,
                current_row_count,
            )
            handleSubmitAccount(
                self.self_main, self.num_threads, self.driver, current_row_count
            )
            handleInsertNewUsername(
                self.num_threads,
                self.driver,
                accounts,
            )
            handleUploadAvatar(
                self.self_main, self.num_threads, self.driver, current_row_count
            )
            self.driver.get("https://www.tiktok.com/logout")
            wait(5, 10)

        # self.driver.quit()
