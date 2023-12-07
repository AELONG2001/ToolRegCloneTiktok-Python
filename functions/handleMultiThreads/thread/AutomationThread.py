import re
import math
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium_authenticated_proxy import SeleniumAuthenticatedProxy
from selenium.common.exceptions import WebDriverException
from utils.utils import wait, generate_random_name, generate_password

from functions.profilesGologin.handleCreateProfile import (
    handleCreateProfile,
)

from functions.proxy.TMProxy.handleGetNewTMProxy import handleGetNewTMProxy
from functions.proxy.TMProxy.handleGetCurrentTMProxy import handleGetCurrentTMProxy

from functions.proxy.TinProxy.handleGetNewTinProxy import handleGetNewTinProxy
from functions.proxy.TinProxy.handleGetCurrentTinProxy import handleGetCurrentTinProxy

from functions.handleInputFileMail.getMailContent import getMailContent
from functions.autoBuyHotmail.autoBuyHotmail import handleAutoBuyHotmail
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
        current_date,
        chrome_count ,
        captcha_type,
        captcha_key,
        proxy_type,
        random_password_account,
        chrome_percent_zoom,
        path_profile_gologin,
        api_key_hotmailbox,
        type_reg_country,
        is_upload_avatar,
        username_restart = "",
        password_restart = "",
        is_restart = False
    ):
        super().__init__()
        self.self_main = self_main
        self.num_threads = num_threads
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.current_date = current_date
        self.chrome_count = chrome_count
        self.captcha_type = captcha_type
        self.captcha_key = captcha_key
        self.proxy_type = proxy_type
        self.random_password_account = random_password_account
        self.chrome_percent_zoom = chrome_percent_zoom
        self.path_profile_gologin = path_profile_gologin
        self.api_key_hotmailbox = api_key_hotmailbox
        self.type_reg_country = type_reg_country
        self.is_upload_avatar = is_upload_avatar
        self.username_restart = username_restart
        self.password_restart = password_restart
        self.is_restart = is_restart

        self.username_mail = ""
        self.password_mail = ""

        self.is_running = True
        self.is_skip_new_username = False
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

    def handleGetMailAndUpdateMail(self):
        with open(self.input_file_path, "r") as f:
            mail_content = f.read()

        self.accounts = getMailContent(mail_content)
         # Lấy nội dung mail
        # self.username_mail, self.password_mail = self.data_queue.get()
        self.username_mail, self.password_mail = self.accounts[self.num_threads]

        # update lại file mail
        with open(self.input_file_path, 'r') as file:
            lines = file.readlines()

        new_lines = [line for line in lines if not line.startswith(f"{self.username_mail}|{self.password_mail}")]

        with open(self.input_file_path, 'w') as file:
            file.writelines(new_lines)

    def handleGetOldMailAndRestart(self):
        self.username_mail = self.username_restart
        self.password_mail = self.password_restart

    def handleAutoBuyMail(self):
        self.mail = handleAutoBuyHotmail(self.api_key_hotmailbox)
        print("Mail: ", self.mail)
        if self.mail:
            self.username_mail, self.password_mail =  self.mail.split("|")
        else:
            self.stop_flag = True
            QMessageBox.warning(None, "Warning", "Hệ thống Hotmailbox đang không đủ mail hãy đợi một lúc rồi chạy lại.")
            return
        
    def handleCheckProxy(self):
        if self.proxy_type == 0:
            isGetTMProxyAgain = True
            while isGetTMProxyAgain:
                api_key_tmproxy = self.self_main.proxy_value.toPlainText()
                api_key_list = api_key_tmproxy.splitlines()

                new_proxy = handleGetNewTMProxy(api_key_list[self.num_threads])
                current_proxy = handleGetCurrentTMProxy(api_key_list[self.num_threads])

                if not new_proxy:
                    self.proxy = current_proxy
                else:
                    self.proxy = new_proxy
                    
                if ':' in self.proxy:
                    isGetTMProxyAgain = False
                else:
                    isGetTMProxyAgain = True
        elif self.proxy_type == 1:
            api_key_tinproxy = self.self_main.proxy_value.toPlainText()
            api_key_list = api_key_tinproxy.splitlines()

            new_proxy = handleGetNewTinProxy(api_key_list[self.num_threads])
            current_proxy = handleGetCurrentTinProxy(api_key_list[self.num_threads])

            if not new_proxy:
                self.proxy = current_proxy
            else:
                self.proxy = new_proxy
        elif self.proxy_type == 2 or self.proxy_type == 3:
            type_ip_port = self.self_main.proxy_value_ip_port.isChecked()

            get_list_proxy = self.self_main.proxy_value.toPlainText()
            proxys = get_list_proxy.splitlines()

            if type_ip_port:
                self.proxy = proxys[self.num_threads]
            else:
                ip,port,user_proxy,password_proxy = proxys[self.num_threads].split(":")
                self.proxy = f"{user_proxy}:{password_proxy}:{ip}:{port}"

        print("Proxy: ",  self.proxy)

    def stop(self):
        self.stop_flag = True
        for thread in self.self_main.chrome_threads:
            thread.terminate()

        if self.driver.current_url == "https://www.tiktok.com/signup/phone-or-email/email":
            wait(1, 2)
            # open file input
            with open(self.input_file_path, "r") as file:
                existing_data_input = file.readlines()

            if existing_data_input:
                # check data file
                exists_input = False
                for line in existing_data_input:
                    parts = line.strip().split('|')
                    if len(parts) >= 1 and self.username_mail == parts[0]:
                        exists_input = True
                        break

                # check if data not exist
                if not exists_input:
                    if existing_data_input[-1].endswith("\n"):
                        with open(self.input_file_path, "a") as file:
                            file.write(f"{self.username_mail}|{self.password_mail}\n")
                    else: 
                     with open(self.input_file_path, "a") as file:
                        file.write(f"\n{self.username_mail}|{self.password_mail}")
        else:
            # open file output
            with open(self.output_file_path, "r") as file:
                existing_data_output = file.readlines()

            if existing_data_output:
                # check data file
                exists_output = False
                for line in existing_data_output:
                    parts = line.strip().split('|')
                    if len(parts) >= 1 and self.username_mail == parts[2]:
                        exists_output = True
                        break

                # check if data not exist
                if not exists_output:
                    # if not self.is_skip_new_username:
                    #     account = f"{self.user_id}|{self.password_account}|{self.username_mail}|{self.password_mail}|{cookies_string}|{self.current_date}"
                    #     with open(self.output_file_path, "a") as f:
                    #         f.write(account + "\n")
                    # else:
                    wait(2, 4)
                    pageContent = self.driver.page_source
                    if '"nickName":"' in pageContent:
                        try:
                            userId = pageContent.split('"nickName":"')[1].split('"')[0]
                        except IndexError:
                            userId = ""
                    else:
                        userId = ""
                    cookies = self.driver.get_cookies()
                    cookies_string = ";".join(
                        [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
                    )
                    if userId:
                        account = f"{userId}|{self.password_account}|{self.username_mail}|{self.password_mail}|{cookies_string}|{self.current_date}"
                    else:
                        account = f"{self.username_mail}|{self.password_account}|{self.password_mail}|{cookies_string}|{self.current_date}"
                    wait(1, 2)
                    if existing_data_output[-1].endswith("\n"):
                        with open(self.output_file_path, "a") as f:
                            f.write(f"{account}\n")
                    else:
                        with open(self.output_file_path, "a") as f:
                            f.write(f"\n{account}")   

        if hasattr(self, "driver"):
            AutomationThread.num_quit += 1
            self.driver.quit()
        
        total_threads = len(self.self_main.chrome_threads)
        completed_threads = AutomationThread.num_quit
        percent_complete = int((completed_threads / total_threads) * 100)
        
        self.self_main.stop_progress_dialog.set_progress(percent_complete)
        self.self_main.stop_progress_dialog.set_progress_text(
            f"Đã dừng {completed_threads} luồng"
        )

        QCoreApplication.processEvents()
    def run(self):
        print("run")
        num_worker = self.num_threads
        chrome_percent_zoom = self.chrome_percent_zoom

        num_chrome_a_row = int(self.chrome_count)

        self.handleCheckProxy()

        self.profile_id = handleCreateProfile(self)

        print("profile_id: ", self.profile_id)

        chromedriver_path = ChromeDriverManager().install()
        
        self.options.add_argument(f"webdriver.chrome.driver={chromedriver_path}")
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
        self.options.add_argument(
            fr"--user-data-dir={self.path_profile_gologin}\{self.profile_id}\Default"
        )
        
        # self.options.add_argument(f"--proxy-server={self.proxy}")

        if self.proxy_type == 2:
            proxy_helper = SeleniumAuthenticatedProxy(proxy_url=f"http://{self.proxy}")
        elif self.proxy_type == 3:
            proxy_helper = SeleniumAuthenticatedProxy(proxy_url=f"socks5://{self.proxy}")
        else:
            proxy_helper = SeleniumAuthenticatedProxy(proxy_url=f"http://{self.proxy}")

        proxy_helper.enrich_chrome_options(self.options)

        self.driver = webdriver.Chrome(options=self.options)
        AutomationThread.drivers_list.append(self.driver)
        
        # Số cột muốn sắp xếp trên màn hình
        cols = num_chrome_a_row
        x = (num_worker % cols) * 504
        y = math.floor(num_worker / cols) * 810

        self.driver.set_window_rect(x, y, 200, 800)

        self.isAutoBuyMail = self.self_main.api_hotmailbox_value.text()
        
        while not self.stop_flag:
            self.self_main.table_account_info.scrollToBottom()
            if self.random_password_account:
                self.password_account = generate_password()
            else:
                if self.self_main.password_reg_account_value.text():
                    self.password_account = self.self_main.password_reg_account_value.text()
                else:
                    self.password_account = "Abc1234@"

            if self.isAutoBuyMail:
                with open(self.input_file_path, 'r') as file:
                    content = file.read()
                if content.strip():
                    if self.is_restart:
                        if not self.username_restart or not self.password_restart:
                            self.handleGetMailAndUpdateMail()
                        else:
                            self.handleGetOldMailAndRestart()
                    else:
                       self.handleGetMailAndUpdateMail()
                else:
                    if self.is_restart:
                        if not self.username_restart or not self.password_restart:
                            self.handleAutoBuyMail()
                        else:
                            self.handleGetOldMailAndRestart()
                    else:
                        self.handleAutoBuyMail()
            else:
                if self.is_restart:
                    if not self.username_restart or not self.password_restart:
                        self.handleGetMailAndUpdateMail()
                    else:
                        self.handleGetOldMailAndRestart()
                else:
                    self.handleGetMailAndUpdateMail()

            random_five_userid = generate_random_name(5)
            random_ten_userid = generate_random_name(10)
            self.user_id = f"{random_five_userid}_{random_ten_userid}"

            self.current_row_count = self.self_main.table_account_info.rowCount()
            self.self_main.table_account_info.setRowCount(self.current_row_count + 1)
            self.self_main.table_account_info.setItem(
                self.current_row_count, 0, QTableWidgetItem(self.username_mail)
            )
            self.self_main.table_account_info.setItem(
                self.current_row_count, 1, QTableWidgetItem(self.password_mail)
            )
            self.self_main.table_account_info.setItem(
                self.current_row_count, 2, QTableWidgetItem(self.proxy)
            )

            try:
                self.driver.get("https://www.tiktok.com/signup/phone-or-email/email")
            except WebDriverException:
                self.driver.refresh()            
                self.driver.refresh()

            handleSelectMonth(self)
            handleSelectDay(self)
            handleSelectYear(self)
            handleInputUserNameAndPassword(self)
            handleGetCode(self)

            if self.captcha_type == 0:
                # Resolve captcha by Achi
                handleResolveCaptchaRotateObjectAChi(self)
                handleResolveCaptchaChooseTwoObjectsAChi(self)
               
            else:
                # Resolve captcha by Omo
                handleResolveCaptchaRotateObjectOmo(self)

                handleResolveCaptchaChooseTwoObjectsOmo(self)

            handleGetCodeFromMail(self)
            
            handleSubmitAccount(self)
            handleInsertNewUsername(self)

            if self.is_upload_avatar:
                handleUploadAvatar(self)
            else:
                wait(4, 6)
                cookies = self.driver.get_cookies()
                cookies_string = ";".join(
                    [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
                )
                account = f"{self.username_mail}|{self.password_account}|{self.password_mail}|{cookies_string}|{self.current_date}"
                with open(self.output_file_path, "a") as f:
                    f.write(account + "\n")

            wait(4, 6)
            self.driver.delete_all_cookies()
            self.driver.refresh()
        self.driver.quit()
