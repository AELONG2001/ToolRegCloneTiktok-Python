from PySide6.QtWidgets import *
from PySide6.QtCore import *
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import math
from time import sleep
from fake_useragent import UserAgent
from utils.utils import wait, generate_password



from functions.profilesGologin.handleCreateProfile import (
    handleCreateProfile,
)
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)

from functions.proxy.TMProxy.handleGetNewTMProxy import handleGetNewTMProxy
from functions.proxy.TMProxy.handleGetCurrentTMProxy import handleGetCurrentTMProxy

from functions.proxy.TinProxy.handleGetNewTinProxy import handleGetNewTinProxy
from functions.proxy.TinProxy.handleGetCurrentTinProxy import handleGetCurrentTinProxy

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
        num_threads,
        input_file_path,
        output_file_path,
        chrome_count ,
        captcha_type,
        captcha_key,
        proxy_type,
        random_password_account,
        chrome_percent_zoom,
        path_profile_gologin,
        is_restart = False
    ):
        super().__init__()
        self.self_main = self_main
        self.num_threads = num_threads
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.chrome_count = chrome_count
        self.captcha_type = captcha_type
        self.captcha_key = captcha_key
        self.proxy_type = proxy_type
        self.random_password_account = random_password_account
        self.chrome_percent_zoom = chrome_percent_zoom
        self.path_profile_gologin = path_profile_gologin
        self.is_restart = is_restart

        self.is_running = True
        self.stop_flag = False
        self.accounts = []
        self.password_account = ""

        self.options = webdriver.ChromeOptions()

    @Slot()
    def show_warning(self):
        QMessageBox.warning(
            None,
            "Warning",
            "Vui lòng nhập thêm mail",
        )

    def stop(self):
        username = self.accounts[self.num_threads][0]
        password = self.accounts[self.num_threads][1]
        password_account = self.password_account
        

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
                account = f"{username}|{password_account}|{password}|{cookies_string}"
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
        
        user_agent = UserAgent()

        random_user_agent = user_agent.random

        num_chrome_a_row = int(self.chrome_count)

        # check type proxys
        if self.proxy_type == 0:
            api_key_tmproxy = self.self_main.proxy_value.toPlainText()
            api_key_list = api_key_tmproxy.splitlines()

            new_proxy = handleGetNewTMProxy(api_key_list[num_worker])
            current_proxy = handleGetCurrentTMProxy(api_key_list[num_worker])

            if not new_proxy:
                self.proxy = current_proxy
            else:
                self.proxy = new_proxy
        elif self.proxy_type == 1:
            api_key_tinproxy = self.self_main.proxy_value.toPlainText()
            api_key_list = api_key_tinproxy.splitlines()

            new_proxy = handleGetNewTinProxy(api_key_list[num_worker])
            current_proxy = handleGetCurrentTinProxy(api_key_list[num_worker])

            print("new_proxy: ", new_proxy)

            if not new_proxy:
                self.proxy = current_proxy
            else:
                self.proxy = new_proxy
        else:
            get_list_proxy = self.self_main.proxy_value.toPlainText()
            proxys = get_list_proxy.splitlines()
            self.proxy = proxys[num_worker]

        # print("Proxy: ",  self.proxy)

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
            f"--user-data-dir={self.path_profile_gologin}/{self.profile_id}/Default"
        )

        # if len(self.proxy.split(":")) > 2:
        #     ip, port, username_proxy, password_proxy = self.proxy.split(":")
        #     proxy_type = "http"
        #     self.options.add_argument(f"--proxy-server={proxy_type}://{username_proxy}:{password_proxy}@{ip}:{port}")
        # else:
        
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

            if self.random_password_account:
                self.password_account = generate_password()
            else:
                if self.self_main.password_reg_account_value.text():
                    self.password_account = self.self_main.password_reg_account_value.text()
                else:
                    self.password_account = "Abc1234@"  

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
                self.input_file_path,
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
                self.password_account,
                current_row_count,
            )
            handleGetCode(
                self.self_main, self.num_threads,  self.input_file_path, self.driver, self.accounts, current_row_count, self.profile_id
            )

            if self.captcha_type == 0:
                # Resolve captcha by Achi
                handleResolveCaptchaRotateObjectAChi(
                    self.captcha_key, self.self_main, self.num_threads, self.input_file_path, self.driver, self.accounts, current_row_count, self.profile_id
                )
                handleResolveCaptchaChooseTwoObjectsAChi(
                    self.captcha_key, self.self_main, self.num_threads, self.input_file_path, self.driver, self.accounts, current_row_count, self.profile_id
                )
               
            else:
                # Resolve captcha by Omo
                handleResolveCaptchaRotateObjectOmo(
                    self.captcha_key, self.self_main, self.num_threads, self.input_file_path, self.driver, self.accounts, current_row_count, self.profile_id
                )

                handleResolveCaptchaChooseTwoObjectsOmo(
                    self.captcha_key, self.self_main, self.num_threads, self.input_file_path, self.driver, self.accounts, current_row_count, self.profile_id
                )

            handleGetCodeFromMail(
                    self.self_main,
                    self.num_threads,
                    self.input_file_path,
                    self.driver,
                    self.accounts,
                    current_row_count,
                    self.profile_id
                )
            
            handleSubmitAccount(self.self_main, self.num_threads,  self.input_file_path,
                self.output_file_path, self.driver, self.accounts, self.password_account, current_row_count, self.profile_id)
            handleInsertNewUsername(
                self.self_main, self.num_threads, self.driver, self.accounts, current_row_count, self.profile_id
            )
            handleUploadAvatar(
                self.self_main,
                self.num_threads,
                self.input_file_path,
                self.output_file_path,
                self.driver,
                self.accounts,
                self.captcha_type,
                self.captcha_key,
                self.password_account,
                current_row_count,
                self.profile_id
            )

            wait(4, 6)
            self.driver.get("https://www.tiktok.com/logout")
            wait(2, 4)
        self.driver.quit()
