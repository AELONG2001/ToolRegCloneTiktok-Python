import threading
from selenium import webdriver
import math
from time import sleep
from functions.handleMultiThreads.selenium.handleSelectMonth import handleSelectMonth
from functions.handleMultiThreads.selenium.handleSelectDay import handleSelectDay
from functions.handleMultiThreads.selenium.handleSelectYear import handleSelectYear
from functions.handleMultiThreads.selenium.handleInputUserNameAndPassword import (
    handleInputUserNameAndPassword,
)
from functions.handleMultiThreads.selenium.handleGetCode import (
    handleGetCode,
)


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
        chrome_percent_zoom = self.chrome_percent_zoom
        is_show_chrome = self.is_show_chrome

        options = webdriver.ChromeOptions()
        if not is_show_chrome:
            options.add_argument("--headless")
        options.add_argument(f"--force-device-scale-factor={chrome_percent_zoom}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument(
        #     "--user-data-dir=C:/Users/HD/AppData/Local/Temp/GoLogin/profiles/64be3436303d394f7791b045/Default"
        # )
        driver = webdriver.Chrome(options=options)

        num_worker = self.num_threads
        num_chrome_a_row = int(self.chrome_count)
        # Số cột muốn sắp xếp trên màn hình
        cols = num_chrome_a_row
        x = (num_worker % cols) * 510
        y = math.floor(num_worker / cols) * 810

        driver.set_window_rect(x, y, 200, 800)
        driver.get("https://www.tiktok.com/signup/phone-or-email/email")
        sleep(3)
        while not self.stop_event.is_set():
            handleSelectMonth(self.self_main, self.num_threads, driver)
            handleSelectDay(self.self_main, self.num_threads, driver)
            handleSelectYear(self.self_main, self.num_threads, driver)
            handleInputUserNameAndPassword(self.self_main, self.num_threads, driver)
            handleGetCode(self.self_main, self.num_threads, driver)
            sleep(10)

        driver.quit()
