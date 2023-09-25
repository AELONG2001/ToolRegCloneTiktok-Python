from PySide6.QtWidgets import *
from PySide6.QtCore import *
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import math
from time import sleep
from fake_useragent import UserAgent
from utils.utils import wait


from functions.profilesGologin.handleCreateProfile import (
    handleCreateProfile,
)
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)

from functions.proxy.handleGetNewTMProxy import handleGetNewTMProxy
from functions.proxy.handleGetCurrentTMProxy import handleGetCurrentTMProxy

from functions.autoBuyHotmail.autoBuyHotmail import handleAutoBuyHotmail


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
        chrome_count ,
        captcha_type,
        captcha_key,
        chrome_percent_zoom,
        is_restart = False
    ):
        super().__init__()
        self.self_main = self_main
        self.stop_event = stop_event
        self.num_threads = num_threads
        self.chrome_count = chrome_count
        self.captcha_type = captcha_type
        self.captcha_key = captcha_key
        self.chrome_percent_zoom = chrome_percent_zoom
        self.is_restart = is_restart

        self.is_running = True
        self.stop_flag = False
        self.is_update_proxy = False
        self.accounts = []

        self.options = webdriver.ChromeOptions()
        # self.options.add_extension("TM_chrome.crx")

        self.input_file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\hotmail.txt"
        self.output_file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\output.txt"

    @Slot()
    def show_warning(self):
        QMessageBox.warning(
            None,
            "Warning",
            "Vui lòng nhập thêm mail",
        )

    def update_proxy(self, api_key):
        self.is_update_proxy = True
        print("Update Proxy")

        self.driver.get(
            "chrome-extension://pmdlifofgdjcolhfjjfkojibiimoahlc/popup.html"
        )

        sleep(2)
        disconnectButton = self.driver.find_element("css selector", ".disconnect-btn")
        disconnectButton.click()

        sleep(2)
        inputApiKey = self.driver.find_element("css selector", ".js-api-key")
        current_value = inputApiKey.get_attribute("value")
        if not current_value:
            inputApiKey.send_keys(f"{api_key}")

        sleep(3)
        autoChangeIp = self.driver.find_element("css selector", ".slider")
        autoChangeIp.click()

        sleep(2)
        minute = self.driver.find_element("css selector", ".js-time-reset-input")
        minute_value = minute.get_attribute("value")
        if not minute_value:
            minute.send_keys("10")

        sleep(2)
        connectButton = self.driver.find_element(
            "css selector", ".js-connect-current-ip"
        )
        connectButton.click()

    def stop(self):
        username = self.accounts[self.num_threads][0]
        password = self.accounts[self.num_threads][1]
        

        self.stop_flag = True
        for thread in self.self_main.chrome_threads:
            thread.terminate()

        if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
            wait(1, 2)
            # open file input
            with open(self.input_file_path, "r") as file:
                existing_data = file.readlines()

            # check data file
            exists = False
            for line in existing_data:
                parts = line.strip().split('|')
                if len(parts) >= 1 and username == parts[0]:
                    exists = True
                    break

            # check if data not exist
            if not exists:
                with open(self.input_file_path, "a") as file:
                    file.write(f"{username}|{password}\n")
        else:
            # open file output
            with open(self.output_file_path, "r") as file:
                existing_data = file.readlines()

            # check data file
            exists = False
            for line in existing_data:
                parts = line.strip().split('|')
                if len(parts) >= 1 and username == parts[0]:
                    exists = True
                    break

            # check if data not exist
            if not exists:
                cookies = self.driver.get_cookies()
                cookies_string = ";".join(
                    [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
                )
                account = f"{username}|Long123@|{password}|{cookies_string}"
                wait(1, 2)
                with open(self.output_file_path, "a") as f:
                    f.write(account + "\n")

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
        print("run")
        num_worker = self.num_threads
        chrome_percent_zoom = self.chrome_percent_zoom

        api_key_tmproxy = self.self_main.proxy_value.toPlainText()
        api_key_list = api_key_tmproxy.splitlines()
        
        user_agent = UserAgent()

        random_user_agent = user_agent.random

        num_chrome_a_row = int(self.chrome_count)

        new_proxy = handleGetNewTMProxy(api_key_list[num_worker])
        current_proxy = handleGetCurrentTMProxy(api_key_list[num_worker])

        if not new_proxy:
            self.proxy = current_proxy
        else:
            self.proxy = new_proxy

        print("Proxy: ",  self.proxy)
    
        self.profile_id = handleCreateProfile(self.proxy)
        print("profile_id: ", self.profile_id)
            
        self.options.add_argument(
            f"--force-device-scale-factor={chrome_percent_zoom}"
        )
        self.options.add_argument("--mute-audio")
        self.options.add_argument('--no-first-run')
        self.options.add_argument('--no-service-autorun')
        self.options.add_argument('--password-store-basic')
        self.options.add_argument('--lang=en-US')
        self.options.add_argument('--disabled-gpu')
        self.options.add_argument('--disabled-cpu')
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "download_restrictions": 3
        }
        self.options.add_experimental_option('prefs', prefs)
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument('--enable-main-frame-before-activation')
        self.options.add_argument('--display-capture-permissions-policy-allowed')
        self.options.add_argument('--device-scale-factor=1')
        self.options.add_argument('--disable-web-secutiry')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument('--disable-popup-blocking')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--disable-plugins-discovery')
        self.options.add_argument('--disable-gpu-shader-disk-cache')

        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument(f"user-agent={random_user_agent}")
        self.options.add_argument(
            f"--user-data-dir=C:/Users/HD/AppData/Local/Temp/GoLogin/profiles/{self.profile_id}/Default"
        )
        self.options.add_argument(f"--proxy-server={self.proxy}")

        self.driver = webdriver.Chrome(options=self.options)
        AutomationThread.drivers_list.append(self.driver)
        
        # Số cột muốn sắp xếp trên màn hình
        cols = num_chrome_a_row
        x = (num_worker % cols) * 504
        y = math.floor(num_worker / cols) * 810

        self.driver.set_window_rect(x, y, 200, 800)

        
        while not self.stop_flag:
            # if not self.is_restart:
            #    mail = handleAutoBuyHotmail()
            #    print("mail: ", mail)

            # with open(self.input_file_path, "a") as file:
            #         file.write(f"{mail}\n")

            # wait(2, 4)

            with open(self.input_file_path, "r") as f:
                mail_content = f.read()

            self.accounts = getMailContent(mail_content)

            if len(self.accounts) > 0:
                username, password = self.accounts[num_worker]
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

            # if not self.is_update_proxy:
            #     self.update_proxy(api_key_list[num_worker])
            #     sleep(5)


            try:
                self.driver.get("https://www.tiktok.com/signup/phone-or-email/email")
            except WebDriverException:            
                print("Lỗi mạng hoặc trang không thể truy cập:")
                self.driver.quit()
                handleDeleteProfile(self.profile_id)
                self.self_main.table_account_info.setItem(
                    current_row_count,
                    3,
                    QTableWidgetItem("Bị chặn, đợi restart lại..."),
                )
                self.self_main.restart_thread(self.num_threads)


            handleSelectMonth(
                self.self_main,
                self.num_threads,
                self.driver,
                self.accounts,
                current_row_count,
                self.profile_id
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
                self.accounts,
                current_row_count,
            )
            handleGetCode(
                self.self_main, self.num_threads, self.driver, self.accounts, current_row_count, self.profile_id
            )

            if self.captcha_type == "Achicaptcha":
                # Resolve captcha by Achi
                handleResolveCaptchaRotateObjectAChi(
                    self.captcha_key, self.self_main, self.num_threads, self.driver, self.accounts, current_row_count, self.profile_id
                )
                handleResolveCaptchaChooseTwoObjectsAChi(
                    self.captcha_key, self.self_main, self.num_threads, self.driver, self.accounts, current_row_count, self.profile_id
                )

               
            else:
                # Resolve captcha by Omo
                handleResolveCaptchaRotateObjectOmo(
                    self.captcha_key, self.self_main, self.num_threads, self.driver, self.accounts, current_row_count, self.profile_id
                )

                handleResolveCaptchaChooseTwoObjectsOmo(
                    self.captcha_key, self.self_main, self.num_threads, self.driver, self.accounts, current_row_count, self.profile_id
                )

            handleGetCodeFromMail(
                    self.self_main,
                    self.num_threads,
                    self.driver,
                    self.accounts,
                    current_row_count,
                    self.profile_id
                )

            
            handleSubmitAccount(self.self_main, self.num_threads, self.driver, self.accounts, current_row_count, self.profile_id)
            handleInsertNewUsername(
                self.self_main, self.num_threads, self.driver, self.accounts, current_row_count, self.profile_id
            )
            handleUploadAvatar(
                self.self_main,
                self.num_threads,
                self.driver,
                self.accounts,
                self.captcha_type,
                self.captcha_key,
                current_row_count,
                self.profile_id
            )

            wait(4, 6)
            self.driver.get("https://www.tiktok.com/logout")
            wait(2, 4)
        self.driver.quit()
