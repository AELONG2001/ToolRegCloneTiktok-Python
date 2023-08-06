from PySide6.QtWidgets import *
from PySide6.QtCore import *
from selenium import webdriver
import math
from time import sleep
from utils.utils import wait

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

handlers = []


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

    def stop(self):
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
        input_file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\hotmail.txt"

        with open(input_file_path, "r") as f:
            mail_content = f.read()

        accounts = getMailContent(mail_content)

        print("accounts: ", accounts)

        list_profiles = [
            "C:/Users/HD/AppData/Local/Temp/GoLogin/profiles/64cda9c7d88e4175e37af066/Default",
            "C:/Users/HD/AppData/Local/Temp/GoLogin/profiles/64cda9c6ee79fe21b648e034/Default",
            "C:/Users/HD/AppData/Local/Temp/GoLogin/profiles/64cda9c58d271b1e4119bb1a/Default",
        ]
        chrome_percent_zoom = self.chrome_percent_zoom
        is_show_chrome = self.is_show_chrome

        proxy_text = self.self_main.proxy_value.toPlainText()
        proxy_list = proxy_text.splitlines()

        options = webdriver.ChromeOptions()
        if not is_show_chrome:
            options.add_argument("--headless")
        options.add_argument(f"--force-device-scale-factor={chrome_percent_zoom}")
        options.add_argument("--mute-audio")
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument(f"--user-data-dir={list_profiles[self.num_threads]}")
        # options.add_argument(f"--proxy-server={proxy_list[self.num_threads]}")

        self.driver = webdriver.Chrome(options=options)

        num_worker = self.num_threads
        num_chrome_a_row = int(self.chrome_count)
        # Số cột muốn sắp xếp trên màn hình
        cols = num_chrome_a_row
        x = (num_worker % cols) * 510
        y = math.floor(num_worker / cols) * 810
        self.driver.set_window_rect(x, y, 200, 800)
        while not self.stop_flag:
            AutomationThread.drivers_list.append(self.driver)
            self.driver.get("https://www.tiktok.com/signup/phone-or-email/email")
            handleSelectMonth(self.self_main, self.num_threads, self.driver)
            handleSelectDay(self.self_main, self.num_threads, self.driver)
            handleSelectYear(self.self_main, self.num_threads, self.driver)
            handleInputUserNameAndPassword(
                self.self_main, self.num_threads, self.driver
            )
            handleGetCode(self.self_main, self.num_threads, self.driver)

            # Resolve captcha by Omo
            handleResolveCaptchaRotateObjectOmo(
                self.self_main, self.num_threads, self.driver
            )

            handleResolveCaptchaChooseTwoObjectsOmo(
                self.self_main, self.num_threads, self.driver
            )

            # Resolve captcha by Achi
            # handleResolveCaptchaRotateObjectAChi(
            #     self.self_main, self.num_threads, self.driver
            # )
            # handleResolveCaptchaChooseTwoObjectsAChi(
            #     self.self_main, self.num_threads, self.driver
            # )

            handleGetCodeFromMail(self.self_main, self.num_threads, self.driver)
            handleSubmitAccount(self.self_main, self.num_threads, self.driver)
            handleInsertNewUsername(self.self_main, self.num_threads, self.driver)
            handleUploadAvatar(self.self_main, self.num_threads, self.driver)
            self.driver.get("https://www.tiktok.com/logout")
            wait(5, 10)

        # self.driver.quit()
