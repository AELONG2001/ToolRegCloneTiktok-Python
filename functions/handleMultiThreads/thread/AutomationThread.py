import os
import json
import math
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from utils.utils import wait, random_number, generate_random_name, generate_password
from functions.profilesGologin.handleDeleteProfile import handleDeleteProfile
from functions.proxy.Authentication.AuthenticationForProxy import create_proxyauth_extension
from functions.handleMultiThreads.handleRestartThread.handleRestartThread import handleRestartThread

from functions.profilesGologin.handleCreateProfile import (
    handleCreateProfile,
)

from functions.proxy.ShopLike.handleGetNewShopLikeProxy import handleGetNewShopLikeProxy
from functions.proxy.ShopLike.handleGetCurrentShopLikeProxy import handleGetCurrentShopLikeProxy

from functions.proxy.TMProxy.handleGetNewTMProxy import handleGetNewTMProxy
from functions.proxy.TMProxy.handleGetCurrentTMProxy import handleGetCurrentTMProxy

from functions.proxy.TinProxy.handleGetNewTinProxy import handleGetNewTinProxy
from functions.proxy.TinProxy.handleGetCurrentTinProxy import handleGetCurrentTinProxy

from functions.proxy.ProxyNo1.handleGetCurrentProxyNo1Proxy import handleGetCurrentProxyNo1Proxy
from functions.proxy.ProxyNo1.handleGetNewProxyNo1Proxy import handleGetNewProxyNo1Proxy

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
from functions.handleMultiThreads.selenium.ResolveCaptcha.AchiCaptcha.captchaSliderObjectAChi import (
    handleResolveCaptchaSliderObjectAChi,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.CaptchaGuru.captchaRotateObjectGuru import (
    handleResolveCaptchaRotateObjectGuru,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.CaptchaGuru.captchaChooseTwoObjectsGuru import (
    handleResolveCaptchaChooseTwoObjectsGuru,
)
from functions.handleMultiThreads.selenium.ResolveCaptcha.CaptchaGuru.captchaSliderObjectGuru import (
    handleResolveCaptchaSliderObjectGuru,
)

from functions.HandleUploadAvatar.handleUploadAvatar import handleUploadAvatar
from functions.apiTDSTiktok.handleGetTask import handleGetTask
from functions.apiTDSTiktok.handleConfirmTask import handleConfirmTask
from functions.apiTDSTiktok.handleReceiveCoin import handleReceiveCoin
from gologin import GoLogin
import keyboard


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
        self.type_reg_country = type_reg_country
        self.is_upload_avatar = is_upload_avatar
        self.username_restart = username_restart
        self.password_restart = password_restart
        self.is_restart = is_restart

        self.username = ""
        self.password = ""

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

    def handleGetAccounts(self):
        # hotmails = readMail()
        # self.username_mail = hotmails[self.num_threads]["username"]
        # self.password_mail = hotmails[self.num_threads]["password"]
        with open("data/accounts.txt", "r") as f:
            accounts = f.read()

        # self.accounts = getMailContent(mail_content)
        # # Lấy nội dung mail
        # # self.username_mail, self.password_mail = self.data_queue.get()
        # self.username_mail, self.password_mail = self.accounts[self.num_threads]

        # # update lại file mail
        # with open(self.input_file_path, 'r') as file:
        #     lines = file.readlines()

        # new_lines = [line for line in lines if not line.startswith(f"{self.username_mail}|{self.password_mail}")]

        # with open(self.input_file_path, 'w') as file:
        #     file.writelines(new_lines)

    def handleGetOldMailAndRestart(self):
        self.username_mail = self.username_restart
        self.password_mail = self.password_restart

    def handleAutoBuyMail(self):
        wait(1, 2)
        self.mail = handleAutoBuyHotmail(self)
        print("Mail: ", self.mail)
        if self.mail:
            self.username_mail, self.password_mail =  self.mail.split("|")
        # else:
        #     self.stop_flag = True
        #     QMessageBox.warning(None, "Warning", "Hệ thống Hotmailbase đang không đủ mail hãy đợi một lúc rồi chạy lại.")
        #     return
        
    def handleCheckProxy(self):
        if self.proxy_type == 0:
            api_key_shoplike_proxy = self.self_main.proxy_value.toPlainText()
            api_key_list = api_key_shoplike_proxy.splitlines()

            new_proxy = handleGetNewShopLikeProxy(api_key_list[self.num_threads])
            current_proxy = handleGetCurrentShopLikeProxy(api_key_list[self.num_threads])

            if not new_proxy:
                self.proxy = current_proxy
            else:
                self.proxy = new_proxy
                
        elif self.proxy_type == 1:
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
        elif self.proxy_type == 2:
            api_key_tinproxy = self.self_main.proxy_value.toPlainText()
            api_key_list = api_key_tinproxy.splitlines()

            new_proxy = handleGetNewTinProxy(api_key_list[self.num_threads])
            current_proxy = handleGetCurrentTinProxy(api_key_list[self.num_threads])

            if not new_proxy:
                self.proxy = current_proxy
            else:
                self.proxy = new_proxy
        elif self.proxy_type == 3:
            api_key_proxy_no_1 = self.self_main.proxy_value.toPlainText()
            api_key_list = api_key_proxy_no_1.splitlines()
            
            # handleGetNewProxyNo1Proxy(api_key_list[self.num_threads])
            # wait(6, 8)
            current_proxy = handleGetCurrentProxyNo1Proxy(api_key_list[self.num_threads])

            self.proxy = current_proxy
            
        elif self.proxy_type == 4 or self.proxy_type == 5:
            self.type_ip_port = self.self_main.proxy_value_ip_port.isChecked()

            get_list_proxy = self.self_main.proxy_value.toPlainText()
            proxys = get_list_proxy.splitlines()

            if self.type_ip_port:
                self.proxy = proxys[self.num_threads]
            else:
                ip,port,user_proxy,password_proxy = proxys[self.num_threads].split(":")
                self.proxy = f"{ip}:{port}:{user_proxy}:{password_proxy}"


                self.proxy_auth = create_proxyauth_extension(
                    proxy_host = ip,
                    proxy_port = port,
                    proxy_username = user_proxy,
                    proxy_password = password_proxy
                )
        
        print("Proxy: ", self.proxy)

    def stop(self):
        print("Stop")
        
        self.stop_flag = True
        account = f"{self.username}|{self.password}"
        with open(self.input_file_path, "a", encoding="utf-8") as f:
            f.write(account + "\n")

        for thread in self.self_main.chrome_threads:
            thread.terminate()

        self.driver.quit()

    def run(self):
            # while not self.stop_flag:
            with open(self.input_file_path, 'r') as file:
                accounts = file.readlines()

            if len(accounts) == 0:
                return
            
            print("run")
            # self.options.add_argument(
            #     f"--user-data-dir={self.profile_fullpath}\Default"
            # 

            # AutomationThread.drivers_list.append(self.driver)
            
            # Số cột muốn sắp xếp trên màn hình
            # self.isAutoBuyMail = self.self_main.api_hotmailbox_value.text()
        
        
            self.self_main.table_account_info.scrollToBottom()
            if self.random_password_account:
                self.password_account = generate_password()
            else:
                if self.self_main.password_reg_account_value.text():
                    self.password_account = self.self_main.password_reg_account_value.text()
                else:
                    self.password_account = "Abc1234@"
            
            # while True:
            num_worker = self.num_threads
            chrome_percent_zoom = self.chrome_percent_zoom

            num_chrome_a_row = int(self.chrome_count)

            self.handleCheckProxy()

            # self.profile_id = handleCreateProfile(self)
            # print(self.profile_id)

            # wait(200000, 4000000)
            
            # with open("configs_account.json", "r") as json_file:
            #     data = json.load(json_file)

            # gl = GoLogin({
            #     "token": data["api_token_gologin"],
            #     "profile_id": self.profile_id,
            #     "port": f"350{self.num_threads}"
            # })
        
            # debugger_address = gl.start()
            # self.options.add_experimental_option("debuggerAddress", debugger_address)
            chromedriver_path = ChromeDriverManager().install()
            self.options.add_argument(f"webdriver.chrome.driver={chromedriver_path}")
            self.options.add_argument(
                f"--force-device-scale-factor={chrome_percent_zoom}"
            )
            self.options.add_argument("--log-level=3")
            self.options.add_argument("start-maximized")
            self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
            self.options.add_experimental_option('useAutomationExtension', False)
            
            
            self.options.add_argument("--mute-audio")
            self.options.add_argument('--no-first-run')
            self.options.add_argument('--no-service-autorun')
            self.options.add_argument('--password-store-basic')
            self.options.add_argument('--lang=vi')
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
            self.options.add_argument(f"--proxy-server=http://{self.proxy}")
            
            # self.options.add_experimental_option("prefs", prefs)
            # if self.proxy_type == 4:
            #     if self.type_ip_port:
            #         self.options.add_argument(f"--proxy-server=http://{self.proxy}")
            #     else:
            #         self.options.add_extension(self.proxy_auth)
            # elif self.proxy_type == 5:
            #     if self.type_ip_port:
            #         self.options.add_argument(f"--proxy-server=socks5://{self.proxy}")
            #     else:
            #         self.options.add_extension(self.proxy_auth)
            # else:
            #     self.options.add_argument(f"--proxy-server=http://{self.proxy}")
            self.driver = webdriver.Chrome(options=self.options)

            cols = num_chrome_a_row
            x = (num_worker % cols) * 504
            y = math.floor(num_worker / cols) * 810

            self.driver.set_window_rect(x, y, 200, 800)

            with open(self.input_file_path, "r", encoding="utf-8") as f:
                accounts = f.readlines()

            self.username = accounts[self.num_threads].split('|')[0]
            self.password = accounts[self.num_threads].split('|')[1]
            
            # if self.username_restart and self.password_restart:
            #     self.username = self.username_restart
            #     self.password = self.password_restart
            # else:
            #     self.username, self.password = self.self_main.data_queue.get()

            # with open("data/accounts.txt", 'r') as file:
            #     lines = file.readlines()
                
            # new_lines = [line for line in lines if not line.startswith(f"{self.username}")]

            # with open("data/accounts.txt", 'w') as file:
            #     file.writelines(new_lines)

            random_five_userid = generate_random_name(5)
            random_ten_userid = generate_random_name(10)
            self.user_id = f"{random_five_userid}_{random_ten_userid}"

            self.current_row_count = self.self_main.table_account_info.rowCount()
            self.self_main.table_account_info.setRowCount(self.current_row_count + 1)
            self.self_main.table_account_info.setItem(
                self.current_row_count, 0, QTableWidgetItem(self.username)
            )
            self.self_main.table_account_info.setItem(
                self.current_row_count, 1, QTableWidgetItem(self.password)
            )

            is_watch_live = self.self_main.is_watch_live.isChecked()
            is_upload_avatar = self.self_main.is_upload_avatar.isChecked()
            is_upload_video = self.self_main.is_upload_video.isChecked()
            is_run_tds = self.self_main.is_run_tds.isChecked()
            is_login_google = self.self_main.is_login_google.isChecked()
            
            main_window_handle = self.driver.current_window_handle
            if is_login_google:
                try:
                    self.driver.get("https://www.tiktok.com/signup")
                except:
                    self.driver.refresh()

                wait(2, 3)
                btn_google_login = self.driver.find_element("xpath", "//div[text()='Tiếp tục với Google']")
                btn_google_login.click()

                wait(3, 4)
                window_handles = self.driver.window_handles
                self.driver.switch_to.window(window_handles[-1])

                wait(4, 6)
                emailElement = self.driver.find_element("css selector", "input[type='email']")
                emailElement.send_keys(self.username)
                emailElement.send_keys(Keys.ENTER)

                wait(4, 6)
                passwordElement = self.driver.find_element("css selector", "input[type='password']")
                passwordElement.send_keys(self.password)
                passwordElement.send_keys(Keys.ENTER)

                wait(8, 10)
                continueElement = self.driver.find_elements("css selector", "button[type='button']")
                try:
                    continueElement[2].click()
                except IndexError:
                    with open("data/failed.txt", "a", encoding="utf-8") as f:
                        f.write(f"{self.username.strip()}|{self.password.strip()}" + "\n")
                
                    with open("data/accounts.txt", 'r') as file:
                        lines = file.readlines()
                        
                    new_lines = [line for line in lines if not line.startswith(f"{self.username}")]

                    with open("data/accounts.txt", 'w') as file:
                        file.writelines(new_lines)

                    self.driver.switch_to.window(main_window_handle)

                    self.driver.quit()    
                    self.self_main.chrome_threads[self.num_threads].quit()
                    self.self_main.chrome_threads[self.num_threads].wait()
                    
                
            else:
                try:
                    self.driver.get("https://www.tiktok.com/login/phone-or-email/email")
                except:
                    self.driver.refresh()
            
                waitForNavigation = WebDriverWait(self.driver, 30)
                usernameElement = waitForNavigation.until(
                    EC.presence_of_element_located(
                        ("css selector", "input[type='text']")
                    )
                )
                usernameElement.send_keys(self.username)
                wait(1, 2)

                passwordElement = self.driver.find_element("xpath", '//input[@autocomplete="new-password"]')
                passwordElement.send_keys(self.password)
                wait(1, 2)
                passwordElement.send_keys(Keys.ENTER)

                if self.captcha_type == 0:
                    handleResolveCaptchaRotateObjectAChi(self)
                    handleResolveCaptchaChooseTwoObjectsAChi(self)
                    handleResolveCaptchaSliderObjectAChi(self)
                elif self.captcha_type == 1:
                    handleResolveCaptchaRotateObjectOmo(self)
                    handleResolveCaptchaChooseTwoObjectsOmo(self)
                else:
                    handleResolveCaptchaRotateObjectGuru(self)
                    handleResolveCaptchaChooseTwoObjectsGuru(self)
                    handleResolveCaptchaSliderObjectGuru(self)
            
            self.driver.switch_to.window(main_window_handle)
            
            is_login_again = True
            while is_login_again:
                wait(8, 10)
                self.driver.switch_to.window(main_window_handle)
                self.driver.refresh()
                wait(6, 8)
                if self.driver.current_url == "https://www.tiktok.com/signup":
                    is_login_again = True
                    wait(4, 6)
                    btn_google_login = self.driver.find_element("xpath", "//div[text()='Tiếp tục với Google']")
                    btn_google_login.click()

                    wait(4, 6)
                    window_handles = self.driver.window_handles
                    self.driver.switch_to.window(window_handles[-1])
                    user_google = self.driver.find_element("xpath", "//div[@data-authuser='0']")
                    user_google.click()

                    wait(8, 10)
                    continueElement = self.driver.find_elements("css selector", "button[type='button']")
                    continueElement[2].click()
                else:
                    is_login_again = False

            cookies = self.driver.get_cookies()
            self.cookies = ";".join(
                [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
            )

            with open("configs_account.json", "r") as json_file:
                data = json.load(json_file)


            if is_upload_avatar:
                list_avatar_folder = data["url_avatar"]
                list_avatar = os.listdir(list_avatar_folder)
                
                if is_login_google:
                    pageContent = self.driver.page_source
                    try:
                        self.userId = pageContent.split('"uniqueId":"')[1].split('"')[0]
                    except IndexError:
                        with open("data/failed.txt", "a", encoding="utf-8") as f:
                            f.write(f"{self.username.strip()}|{self.password.strip()}" + "\n")
                    
                        with open("data/accounts.txt", 'r') as file:
                            lines = file.readlines()
                            
                        new_lines = [line for line in lines if not line.startswith(f"{self.username}")]

                        with open("data/accounts.txt", 'w') as file:
                            file.writelines(new_lines)

                        self.driver.switch_to.window(main_window_handle)

                        self.driver.quit()    
                        self.self_main.chrome_threads[self.num_threads].quit()
                        self.self_main.chrome_threads[self.num_threads].wait()

                    try:
                        self.driver.get(f"https://www.tiktok.com/@{self.userId}")
                    except:
                        self.driver.refresh()
                        self.driver.refresh()
                else:
                    try:
                        self.driver.get(f"https://www.tiktok.com/@{self.username}")
                    except:
                        self.driver.refresh()
                        self.driver.refresh()

                try:
                    waitForNavigation = WebDriverWait(self.driver, 20)
                    editProfile = waitForNavigation.until(
                        EC.presence_of_element_located(("xpath", '//span[text()="Sửa hồ sơ"]'))
                    )
                    editProfile.click()
                except TimeoutException:
                    return
                except ElementClickInterceptedException:
                    return
                
                wait(4, 6)
                inputUploadAvatar = self.driver.find_elements("css selector", "input[type='file']")
                inputUploadAvatar[0].send_keys(
                    f"{list_avatar_folder}/{list_avatar[random_number(0, len(list_avatar) - 1)]}"
                )
                
                wait(6, 8)
                try:
                    waitForNavigation = WebDriverWait(self.driver, 20)
                    applyAvatarBtn = waitForNavigation.until(
                        EC.presence_of_element_located(("xpath", '//button[text()="Đăng ký"]'))
                    )
                    self.driver.execute_script("arguments[0].scrollIntoView();", applyAvatarBtn)
                    applyAvatarBtn.click()
                except NoSuchElementException:
                    return
                except TimeoutException:
                    return
                
                wait(4, 6)
                saveElement = self.driver.find_elements("xpath", '//*[@data-e2e="edit-profile-save"]')
                
                try:
                    saveElement[0].click()
                except ElementClickInterceptedException:
                    return
                
                wait(4, 6)
                                
            if is_upload_video:
                list_video_folder = data["url_video"]
                list_video = os.listdir(list_video_folder)
                wait(1, 2)
                try:
                    self.driver.get("https://www.tiktok.com/creator-center/upload?from=upload")
                except:
                    self.driver.refresh()
                
                iframe = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(("xpath", "//*[@data-tt='Upload_index_iframe']"))
                )
            
                self.driver.switch_to.frame(iframe)
                wait(4, 6)
                inputUploadVideo = self.driver.find_element("css selector", "input[type='file']")
                self.driver.execute_script("arguments[0].style.display = 'block';", inputUploadVideo)
                inputUploadVideo.send_keys(f"{list_video_folder}/{list_video[random_number(0, len(list_video) - 1)]}")

                wait(18, 20)
                btnPostVideo = self.driver.find_elements("xpath", "//*[text()='Đăng']")
                self.driver.execute_script("arguments[0].scrollIntoView();", btnPostVideo[0])
                btnPostVideo[0].click()
                
                try:
                    waitForNavigation = WebDriverWait(self.driver, 30)
                    manager_post_video = waitForNavigation.until(
                        EC.presence_of_element_located(
                            ("xpath", "//*[text()='Quản lý bài đăng của bạn']")
                        )
                    )
                    manager_post_video.click()
                except TimeoutException:
                    return

                wait(4, 6)
                try:
                    self.driver.get("https://www.tiktok.com")
                except:
                    self.driver.refresh()
                    self.driver.refresh()
            
            if is_watch_live:
                if is_login_google:
                    for _ in range(2):
                        wait(4, 6)
                        try:
                            self.driver.get("https://www.tiktok.com/live")
                        except:
                            self.driver.refresh()
                        
                        wait(4, 6)
                        try:
                            btnMoveLiveAction = self.driver.find_element("xpath", "//button[text()='Nhấp để xem LIVE']")
                            btnMoveLiveAction.click()
                        except NoSuchElementException:
                           pass

                        bodyElement = self.driver.find_element("tag name", "body")

                        wait(1, 2)
                        bodyElement.send_keys(Keys.ARROW_DOWN)

                        wait(1, 2)
                        bodyElement.send_keys(Keys.ARROW_DOWN)

                        wait(36, 40)
                        followBtn = self.driver.find_elements("xpath", "//span[text()='Follow']")
                        try:
                            self.driver.execute_script("arguments[0].scrollIntoView();", followBtn[0])
                            followBtn[0].click()
                        except:
                            pass
                        
                        wait(4, 6)
                        try:
                            self.driver.get(f"https://www.tiktok.com/@{self.userId}")
                        except:
                            self.driver.refresh()

                        wait(2, 3)

                    cookies = f"{self.cookies}"
                    with open("data/cookies.txt", "a", encoding="utf-8") as f:
                        f.write(cookies + "\n")
                    
                    with open("data/accounts.txt", 'r') as file:
                        lines = file.readlines()
                        
                    new_lines = [line for line in lines if not line.startswith(f"{self.username}")]

                    with open("data/accounts.txt", 'w') as file:
                        file.writelines(new_lines)

                    self.driver.quit()    
                    self.self_main.chrome_threads[self.num_threads].quit()
                    self.self_main.chrome_threads[self.num_threads].wait()
                    
                else:
                    wait(4, 6)
                    try:
                        self.driver.get("https://www.tiktok.com/live")
                    except:
                        self.driver.refresh()
                        self.driver.refresh()
                    
                    wait(4, 6)
                    try:
                        btnMoveLiveAction = self.driver.find_element("xpath", "//button[text()='Nhấp để xem LIVE']")
                        btnMoveLiveAction.click()
                    except NoSuchElementException:
                        pass

                    bodyElement = self.driver.find_element("tag name", "body")

                    wait(1, 2)
                    bodyElement.send_keys(Keys.ARROW_DOWN)

                    wait(1, 2)
                    bodyElement.send_keys(Keys.ARROW_DOWN)

                    wait(36, 40)
                    followBtn = self.driver.find_elements("xpath", "//span[text()='Follow']")
                    try:
                        self.driver.execute_script("arguments[0].scrollIntoView();", followBtn[0])
                        followBtn[0].click()
                    except:
                        pass
                    
                    wait(4, 6)
                    try:
                        self.driver.get(f"https://www.tiktok.com/@{self.username}")
                    except:
                        self.driver.refresh()
                        self.driver.refresh()

                    wait(4, 6)
                    try:
                        self.driver.get("https://www.tiktok.com/live")
                    except:
                        self.driver.refresh()
                        self.driver.refresh()

                    wait(4, 6)
                    bodyElement = self.driver.find_element("tag name", "body")
                    bodyElement.send_keys(Keys.ARROW_DOWN)

                    wait(36, 40)
                    followBtn = self.driver.find_elements("xpath", "//span[text()='Follow']")
                    try:
                        self.driver.execute_script("arguments[0].scrollIntoView();", followBtn[0])
                        followBtn[0].click()
                    except:
                        pass

                    wait(4, 6)
                    try:
                        self.driver.get(f"https://www.tiktok.com/@{self.username}")
                    except:
                        self.driver.refresh()
                        self.driver.refresh()

                    wait(4, 6)
                    countFollow = self.driver.find_element("xpath", "//*[@data-e2e='following-count']").text

                    if int(countFollow) >= 1:
                        accountKicked = f"{self.username.strip()}|{self.password.strip()}|{self.cookies.strip()}"
                        with open("data/account_kicked.txt", "a", encoding="utf-8") as f:
                            f.write(accountKicked + "\n")
                        
                        with open("data/accounts.txt", 'r') as file:
                            lines = file.readlines()
                            
                        new_lines = [line for line in lines if not line.startswith(f"{self.username}")]

                        with open("data/accounts.txt", 'w') as file:
                            file.writelines(new_lines)

                        self.driver.quit()    
                        self.self_main.chrome_threads[self.num_threads].quit()
                        self.self_main.chrome_threads[self.num_threads].wait()    
                    else:
                        wait(4, 6)
                        try:
                            self.driver.get("https://www.tiktok.com/live")
                        except:
                            self.driver.refresh()
                            self.driver.refresh()

                        wait(4, 6)
                        bodyElement = self.driver.find_element("tag name", "body")
                        bodyElement.send_keys(Keys.ARROW_DOWN)

                        wait(36, 40)
                        followBtn = self.driver.find_elements("xpath", "//span[text()='Follow']")
                        try:
                            self.driver.execute_script("arguments[0].scrollIntoView();", followBtn[0])
                            followBtn[0].click()
                        except:
                            pass
                        
                        wait(4, 6)
                        try:
                            self.driver.get(f"https://www.tiktok.com/@{self.username}")
                        except:
                            self.driver.refresh()

                        wait(4, 6)
                        try:
                            countFollow = self.driver.find_element("xpath", "//*[@data-e2e='following-count']").text
                        except:
                            pass 

                        if int(countFollow) >= 1:
                            accountKicked = f"{self.username.strip()}|{self.password.strip()}|{self.cookies.strip()}"
                            with open("data/account_kicked.txt", "a", encoding="utf-8") as f:
                                f.write(accountKicked + "\n")

                            
                            with open("data/accounts.txt", 'r') as file:
                                lines = file.readlines()
                                
                            new_lines = [line for line in lines if not line.startswith(f"{self.username}")]

                            with open("data/accounts.txt", 'w') as file:
                                file.writelines(new_lines)
                            
                            self.driver.quit()
                            self.self_main.chrome_threads[self.num_threads].quit()
                            self.self_main.chrome_threads[self.num_threads].wait()    
                        else:
                            accountWaitKickAgain = f"{self.username}|{self.password}|{self.cookies}"
                            with open("data/account_wait_kick_again.txt", "a", encoding="utf-8") as f:
                                f.write(accountWaitKickAgain + "\n")

                            
                            with open("data/accounts.txt", 'r') as file:
                                lines = file.readlines()
                                
                            new_lines = [line for line in lines if not line.startswith(f"{self.username}")]

                            with open("data/accounts.txt", 'w') as file:
                                file.writelines(new_lines)

                            self.driver.quit()
                            self.self_main.chrome_threads[self.num_threads].quit()
                            self.self_main.chrome_threads[self.num_threads].wait()
                
            if is_run_tds:
                self.tokenTds = "TDSQfiUjclZXZzJiOiIXZ2V2ciwiIxADMy8mcwtmeiojIyV2c1Jye"
                wait(4, 6)
                try:
                    self.driver.get(f"https://traodoisub.com/api/autoclick/abcd/3491/?access_token={self.tokenTds}&type=tiktok_like")
                    wait(4, 6)
                    configBtn = self.driver.find_element("xpath", "//*[@data-target='#exampleModal']")      
                    configBtn.click()       
                    wait(4, 6)
                    inputIdTiktok = self.driver.find_element("css selector", "#id_run")
                    inputIdTiktok.send_keys(self.username)

                    wait(2, 3)
                    confirmBtn = self.driver.find_element("css selector", "#chbutton")
                    confirmBtn.click()
                    wait(4, 6)
                    self.driver.get(f"https://www.tiktok.com/live")
                except:
                    self.driver.refresh()
                
                while True:
                    coin = 0
                    totalCoin = 0
                    list_task = handleGetTask(self.tokenTds)
                    for task in list_task:
                        taskId = task["id"]
                        uniqueID = task["uniqueID"]
                        link = task["link"]
                        
                        try:
                           
                            self.driver.get(f"https://www.tiktok.com")
                            wait(2, 3)
                            inputSearchTiktokId = self.driver.find_element("xpath", "//*[@data-e2e='search-user-input']")
                            inputSearchTiktokId.send_keys(uniqueID)
                            wait(2, 3)
                            btnSearch = self.driver.find_element("xpath", "//*[@data-e2e='search-box-button']")
                            btnSearch.click()
                            wait(6, 8)
                            waitForNavigation = WebDriverWait(self.driver, 10)
                            try:
                                tiktokIdClick = waitForNavigation.until(
                                EC.presence_of_element_located(
                                    ('xpath', f'//p[text()="{uniqueID}"]')
                                )
                                )
                                tiktokIdClick.click()
                            except TimeoutException:
                                self.driver.get(link)
                        except:
                            self.driver.refresh()
                        try:
                            wait(4, 6)
                            try:
                                waitForNavigation = WebDriverWait(self.driver, 10)
                                followBtnTask = waitForNavigation.until(
                                    EC.presence_of_element_located(
                                        ("xpath", "//*[@data-e2e='follow-button']")
                                    )
                                )
                                followBtnTask.click()
                            except Exception as e:
                                pass
                            handleResolveCaptchaChooseTwoObjectsGuru(self)
                            # self.driver.close()
                            # self.driver.switch_to.window(self.driver.window_handles[-1])
                        except TimeoutException:
                            pass
                        
                        try:
                            cache = handleConfirmTask(taskId, self.tokenTds)
                            print(f"cache for {self.username}: ", cache)
                            self.self_main.table_account_info.setItem(
                                self.current_row_count, 4, QTableWidgetItem(cache)
                            )
                            QCoreApplication.processEvents()
                        except Exception as e:
                            pass

                        if int(cache) >= 10:
                            wait(4, 6)
                            data = handleReceiveCoin(self.tokenTds)
                            if "msg" in data:
                                coin = int(''.join(filter(str.isdigit, data["msg"])))
                                print(f"coin for {self.username}: ", coin)

                                if coin == 0:
                                    with open("data/accounts.txt", 'r', encoding="utf-8") as file:
                                        lines = file.readlines()
                                        
                                    new_lines = [line for line in lines if not line.startswith(f"{self.username}")]

                                    with open("data/accounts.txt", 'w', encoding="utf-8") as file:
                                        file.writelines(new_lines)

                                    self.driver.quit()
                                    self.self_main.chrome_threads[self.num_threads].quit()
                                    self.self_main.chrome_threads[self.num_threads].wait()
                                self.self_main.table_account_info.setItem(
                                    self.current_row_count, 5, QTableWidgetItem(coin)
                                )
                                QCoreApplication.processEvents()
                                totalCoin += coin
                        wait(4, 6)
                            
                    print(f"totalCoin {self.username}: ", totalCoin)
                    self.self_main.table_account_info.setItem(
                        self.current_row_count, 6, QTableWidgetItem(totalCoin)
                    )
                    QCoreApplication.processEvents()
            
            if not is_watch_live:
                cookies = f"{self.cookies}"
                with open("data/cookies.txt", "a", encoding="utf-8") as f:
                    f.write(cookies + "\n")
                
                with open("data/accounts.txt", 'r') as file:
                    lines = file.readlines()
                    
                new_lines = [line for line in lines if not line.startswith(f"{self.username}")]

                with open("data/accounts.txt", 'w') as file:
                    file.writelines(new_lines)

                self.driver.quit()    
                self.self_main.chrome_threads[self.num_threads].quit()
                self.self_main.chrome_threads[self.num_threads].wait()   

            # try:
            #     self.driver.get("https://www.tiktok.com/signup/phone-or-email/email")
            # except WebDriverException:
            #     self.driver.refresh()            
            #     self.driver.refresh()

            # handleSelectMonth(self)
            # handleSelectDay(self)
            # handleSelectYear(self)
            # handleInputUserNameAndPassword(self)
            # handleGetCode(self)
            # handleGetCodeFromMail(self)
            
            # handleSubmitAccount(self)
            # handleInsertNewUsername(self)

            # if self.is_upload_avatar:
            #     handleUploadAvatar(self)
            # else:
            #     wait(4, 6)
            #     pageContent = self.driver.page_source
            #     if '"nickName":"' in pageContent:
            #         try:
            #             userId = pageContent.split('"nickName":"')[1].split('"')[0]
            #         except IndexError:
            #             userId = ""
            #     else:
            #         userId = ""
            #     cookies = self.driver.get_cookies()
            #     cookies_string = ";".join(
            #         [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
            #     )
            #     account = ""
            #     if userId:
            #         account = f"{userId}|{self.password_account}|{self.username_mail}|{self.password_mail}|{cookies_string}|{self.current_date}"
            #     else:
            #         account2 = f"{self.username_mail}|{self.password_account}|{self.password_mail}|{cookies_string}|{self.current_date}"
            #         with open("data/output_not_user_id.txt", "a") as f:
            #             f.write(account2 + "\n")
                    
            #             self.self_main.total_success += 1
            #             self.self_main.total_success_account.setText(f"Số acc đã tạo thành công: {self.self_main.total_success}")
            #             QCoreApplication.processEvents()
            #     with open(self.output_file_path, "a") as f:
            #         f.write(account + "\n")

            #     self.self_main.total_success += 1
            #     self.self_main.total_success_account.setText(f"Số acc đã tạo thành công: {self.self_main.total_success}")
            #     QCoreApplication.processEvents()