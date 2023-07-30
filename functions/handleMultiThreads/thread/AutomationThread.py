import threading
from selenium import webdriver
import math
from utils.utils import wait

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


class AutomationThread(threading.Thread):
    def __init__(
        self,
        self_main,
        stop_event,
        num_threads,
        chrome_count,
        chrome_percent_zoom,
        is_show_chrome,
    ):
        super(AutomationThread, self).__init__()
        self.self_main = self_main
        self.stop_event = stop_event
        self.num_threads = num_threads
        self.chrome_count = chrome_count
        self.chrome_percent_zoom = chrome_percent_zoom
        self.is_show_chrome = is_show_chrome
        self.is_running = True

    def run(self):
        list_profiles = [
            "C:/Users/HD/AppData/Local/Temp/GoLogin/profiles/64c650a4bc63ac67b4c066de/Default",
            "C:/Users/HD/AppData/Local/Temp/GoLogin/profiles/64c650a3e16c464ea66600b5/Default",
            "C:/Users/HD/AppData/Local/Temp/GoLogin/profiles/64c650a2c44fb360f5ee1dfa/Default",
            "C:/Users/HD/AppData/Local/Temp/GoLogin/profiles/64c650a17965a209109d8e7e/Default",
            "C:/Users/HD/AppData/Local/Temp/GoLogin/profiles/64c650a017eb06e28ad68020/Default",
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
        options.add_argument(f"--proxy-server={proxy_list[self.num_threads]}")
        options.add_argument(f"--user-data-dir={list_profiles[self.num_threads]}")

        driver = webdriver.Chrome(options=options)

        num_worker = self.num_threads
        num_chrome_a_row = int(self.chrome_count)
        # Số cột muốn sắp xếp trên màn hình
        cols = num_chrome_a_row
        x = (num_worker % cols) * 510
        y = math.floor(num_worker / cols) * 810
        driver.set_window_rect(x, y, 200, 800)
        while not self.stop_event.is_set():
            driver.get("https://www.tiktok.com/signup/phone-or-email/email")
            handleSelectMonth(self.self_main, self.num_threads, driver)
            handleSelectDay(self.self_main, self.num_threads, driver)
            handleSelectYear(self.self_main, self.num_threads, driver)
            handleInputUserNameAndPassword(self.self_main, self.num_threads, driver)
            handleGetCode(self.self_main, self.num_threads, driver)
            wait(4, 6)

            # resolve by Omocaptcha
            handleResolveCaptchaRotateObjectOmo(
                self.self_main, self.num_threads, driver
            )
            handleResolveCaptchaChooseTwoObjectsOmo(
                self.self_main, self.num_threads, driver
            )

            # resolve by Achicaptcha
            # handleResolveCaptchaRotateObjectAChi(
            #     self.self_main, self.num_threads, driver
            # )
            # handleResolveCaptchaChooseTwoObjectsAChi(
            #     self.self_main, self.num_threads, driver
            # )

            handleGetCodeFromMail(self.self_main, self.num_threads, driver)
            handleSubmitAccount(self.self_main, self.num_threads, driver)
            handleInsertNewUsername(self.self_main, self.num_threads, driver)
            handleUploadAvatar(self.self_main, self.num_threads, driver)
            wait(15, 20)
            driver.get("https://www.tiktok.com/logout")
            wait(5, 10)

        driver.quit()
