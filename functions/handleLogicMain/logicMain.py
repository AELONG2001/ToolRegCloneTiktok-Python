from PySide6.QtWidgets import *
from PySide6.QtCore import *

from functions.handleSaveDataInputUser.handleSaveDataInputUser import handleSaveDataInputUser
from functions.handleMultiThreads.thread.startAutomation import startAutomation
from functions.handleMultiThreads.thread.stopAutomation import stopAutomation
from functions.handleOpenFolder.handleOpenListAvatar import selectFolder
from functions.handleCheckMail.checkMail import checkMail
from functions.handleCheckAccounts.checkLiveAccounts import checkLiveAccounts
from GUI.darkMode import darkMode
from GUI.lightMode import lightMode
import shutil

import os
import json
import re
import urllib.request
import zipfile
import shutil
from subprocess import run, CREATE_NO_WINDOW


class AutomationController:
    def __init__(self, ui_instance):
        self.ui_instance = ui_instance

        self.timer_check_password = QTimer()
        self.timer_check_password.timeout.connect(self.check_password)
        self.timer_check_password.setSingleShot(True)  # Đặt chế độ single shot để chỉ chạy một lần

    def update(self):
        self.ui_instance.is_update = True
        self.ui_instance.update_progress_dialog.show()
        QCoreApplication.processEvents()
        url = self.ui_instance.data["link_update"]
        print("url: ", url)
        total_size_version = int(self.ui_instance.data["size_update"])
        file_name = "./repository.zip"
        
        file_size = total_size_version / 1048576
        file_size_dl = 0
        block_sz = 8192

        u = urllib.request.urlopen(url)
        with open(file_name, 'wb') as f:
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break

                file_size_dl += len(buffer)
                f.write(buffer)
                # Tính tỷ lệ đã tải
                percent_complete = (file_size_dl * 100.0 / total_size_version)
                # print(f"Tải xong: {file_size_dl / (1024 * 1024):.2f}MB/{file_size:.2f}MB")
                # print("percent_complete: ", int(percent_complete))

                self.ui_instance.update_progress_dialog.set_percent_title(f"{file_size_dl / (1024 * 1024):.2f}MB/{file_size:.2f}MB")
                self.ui_instance.update_progress_dialog.set_progress_dialog(int(percent_complete))
                QCoreApplication.processEvents()
            print("Download completed.")

        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            # Giải nén toàn bộ nội dung vào thư mục đích
            zip_ref.extractall()

            # Lấy danh sách các tên tệp tin và thư mục trong file zip
            file_list = zip_ref.namelist()

            # Lấy tên thư mục đã giải nén
            extracted_folder_name = None
            for name in file_list:
                if name.endswith('/'):
                    extracted_folder_name = name.rstrip('/')
                    break
        
        
        os.rename(f"./{extracted_folder_name.strip()}", self.ui_instance.latest_version)
        os.remove(file_name)
        if not os.path.exists(f"{self.ui_instance.current_version}"):
            os.makedirs(f"{self.ui_instance.current_version}")
        source_file = "./ToolRegCloneTiktok.exe"
        destination_directory = f"{self.ui_instance.current_version}"
        destination_path = os.path.join(destination_directory, os.path.basename(source_file))
        # move old exe to old version folder
        os.rename(source_file, destination_path)
        os.rename(f"{self.ui_instance.latest_version}/ToolRegCloneTiktok.exe", source_file)
        # shutil.rmtree(f"{self.ui_instance.current_version}")
        shutil.rmtree(f"{self.ui_instance.latest_version}")
        QApplication.quit()
        run("./ToolRegCloneTiktok.exe", creationflags=CREATE_NO_WINDOW)
        self.ui_instance.is_update = False

    def start(self):
        startAutomation(self.ui_instance)

    def start_next_thread(self):
        if (
            self.ui_instance.thread_index < len(self.ui_instance.chrome_threads)
            and not self.ui_instance.stop_all_threads
        ):
            thread = self.ui_instance.chrome_threads[self.ui_instance.thread_index]
            thread.start()
            self.ui_instance.thread_index += 1
            self.ui_instance.start_timer.start()
        else:
            self.ui_instance.start_timer.stop()

    def stop(self):
        stopAutomation(self.ui_instance)

    def validate_password(self, password):
        password_regex = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^&*()])[A-Za-z\d@#$%^&*()]{8,}$')
        return bool(password_regex.match(password))
    
    def check_password(self):
        password_account = self.ui_instance.password_reg_account_value.text().strip()
        if self.validate_password(password_account):
            self.ui_instance.check_rule_password_account.setText("")
        else:
            random_password_account = self.ui_instance.random_password_account.isChecked()
            if not random_password_account:
                self.ui_instance.check_rule_password_account.setText("phải bao gồm 8 ký tự chữ, số và ký tự đặc biệt")


    def checkThreadsValue(self, value):
        num_threads = self.ui_instance.threads_value.value()
        
        if value < 1:
            QMessageBox.warning(None, "Warning", "Tối thiểu là 1 luồng")
            self.ui_instance.threads_value.setValue(1)
        elif value > 90:
            QMessageBox.warning(None, "Warning", "Tối đa không được vượt quá 90 luồng")
            self.ui_instance.threads_value.setValue(90)
            handleSaveDataInputUser("num_threads", 90)
            return

        handleSaveDataInputUser("num_threads", num_threads)

    def handleAvatarFolderSelection(self):
        link_avatar = selectFolder()
        if link_avatar:
            self.ui_instance.avatar_value.setText(link_avatar)
        handleSaveDataInputUser("url_avatar", link_avatar)

    def handleVideoFolderSelection(self):
        link_video = selectFolder()
        if link_video:
            self.ui_instance.video_value.setText(link_video)
        handleSaveDataInputUser("url_video", link_video)

    def inputMail(self):
        link_mail = QFileDialog.getOpenFileName(
            None, "Open File", "", "(*.txt)"
        )[0]
        self.ui_instance.mail_value.setText(link_mail)

        handleSaveDataInputUser("url_mail", link_mail)

    def checkWatchLive(self):
        is_watch_live = self.ui_instance.is_watch_live.isChecked()
        handleSaveDataInputUser("is_watch_live", is_watch_live)

    def checkUploadAvatar(self):
        is_upload_avatar = self.ui_instance.is_upload_avatar.isChecked()
        handleSaveDataInputUser("is_upload_avatar", is_upload_avatar)

    def checkUploadVideo(self):
        is_upload_video = self.ui_instance.is_upload_video.isChecked()
        handleSaveDataInputUser("is_upload_video", is_upload_video)

    def checkRunTDS(self):
        is_run_tds = self.ui_instance.is_run_tds.isChecked()
        handleSaveDataInputUser("is_run_tds", is_run_tds)

    def checkLoginGoogle(self):
        is_login_google = self.ui_instance.is_login_google.isChecked()
        handleSaveDataInputUser("is_login_google", is_login_google)

    def getCaptchaType(self):
        captcha_type = self.ui_instance.captcha_type.currentIndex()
        handleSaveDataInputUser("captcha_type", captcha_type)

    def getCaptchaKey(self):
        captcha_key = self.ui_instance.captcha_key.text().strip()
        handleSaveDataInputUser("captcha_key", captcha_key)

    def exportAccount(self):
        file_path = "data/output.txt"     
        file_path_backup = "data/output_backup.txt"     
        typeExportAccount = self.ui_instance.export_account_format_value.currentIndex()

        default_file_name = "output.txt"

        if typeExportAccount == 1:
            default_file_name = "output_without_cookie.txt"
        elif typeExportAccount == 2:
            default_file_name = "output_without_date.txt"
        elif typeExportAccount == 3:
            default_file_name = "output_without_cookie_without_date.txt"
        elif typeExportAccount == 4:
            default_file_name = "output_username_password.txt"

        file_name, _ = QFileDialog.getSaveFileName(None, "Chọn nơi lưu tệp", default_file_name, "Tệp văn bản (*.txt);;Tất cả các tệp (*)")

        if not file_name:
            return
    
        with open(file_path, "r") as file:
            accounts =  file.readlines()

        with open(file_path, "r") as file:
            full_accounts =  file.read()

        with open(file_path_backup, "w") as file:
            file.write(full_accounts)

        with open(file_path, "w") as file:
            file.write("")
        
        if typeExportAccount == 0:
            selected_data = accounts
        elif typeExportAccount == 1:
            selected_data = []
            for line in accounts:
                # check và tìm vị trí chứa cookie
                if 'msToken=' in line:
                    data = line.split("|")
                    index_cookie = next((i for i, part in enumerate(data) if 'msToken=' in part), None)
                    
                    if index_cookie is not None:
                        del data[index_cookie]
                        selected_data.append(data)
                else:
                    selected_data.append(line.split("|"))
        elif typeExportAccount == 2:
            selected_data = []
            for line in accounts:
                data = line.split("|")
                del data[len(data) - 1]
                selected_data.append(data)
        elif typeExportAccount == 3:
            selected_data = []
            for line in accounts:
                # check và tìm vị trí chứa cookie
                if 'msToken=' in line:
                    data = line.split("|")
                    index_cookie = next((i for i, part in enumerate(data) if 'msToken=' in part), None)
                    
                    if index_cookie is not None:
                        del data[len(data) - 1]
                        del data[index_cookie]
                        selected_data.append(data)
                else:
                    data = line.split("|")
                    del data[len(data) - 1]
                    selected_data.append(data)
        elif typeExportAccount == 4:
            selected_data = [line.split("|")[:2] for line in accounts]

        with open(file_name, "w") as txtfile:
            if typeExportAccount == 0:
                txtfile.writelines(selected_data)
            elif typeExportAccount == 1:
                for line in selected_data:
                    txtfile.write("|".join(line))
            elif typeExportAccount == 2 or typeExportAccount == 3 or typeExportAccount == 4:
                for line in selected_data:
                    txtfile.write("|".join(line) + "\n")
                    
        QMessageBox.information(None, "Thông báo", "Đã lưu thành công!")
            
    def getProxyType(self):
        proxy_type = self.ui_instance.proxy_type.currentIndex()
        if proxy_type == 4 or proxy_type == 5:
            self.ui_instance.proxy_value.setPlaceholderText("Mỗi proxy một dòng")
            self.ui_instance.proxy_value_ip_port.setVisible(True)
            self.ui_instance.proxy_value_ip_port_user_pass.setVisible(True)
        else:
            self.ui_instance.proxy_value.setPlaceholderText("Mỗi Api key một dòng")
            self.ui_instance.proxy_value_ip_port.setVisible(False)
            self.ui_instance.proxy_value_ip_port_user_pass.setVisible(False)

        handleSaveDataInputUser("proxy_type", proxy_type)

    def getProxyTypeCheckLive(self):
        proxy_type = self.ui_instance.proxy_type_check_live.currentIndex()
        if proxy_type == 4 or proxy_type == 5:
            self.ui_instance.proxy_value_check_live.setPlaceholderText("Mỗi proxy một dòng")
            self.ui_instance.proxy_value_check_live_ip_port.setVisible(True)
            self.ui_instance.proxy_value_check_live_ip_port_user_pass.setVisible(True)
        else:
            self.ui_instance.proxy_value_check_live.setPlaceholderText("Mỗi Api key một dòng")
            self.ui_instance.proxy_value_check_live_ip_port.setVisible(False)
            self.ui_instance.proxy_value_check_live_ip_port_user_pass.setVisible(False)

        handleSaveDataInputUser("proxy_type_check_live", proxy_type)

    def importProxy(self):
        proxy_text = self.ui_instance.proxy_value.toPlainText().strip()
        proxy_list = proxy_text.splitlines()

        handleSaveDataInputUser("proxys", proxy_list)

    def importProxyCheckLive(self):
        proxy_text = self.ui_instance.proxy_value_check_live.toPlainText().strip()
        proxy_list = proxy_text.splitlines()

        handleSaveDataInputUser("proxys_check_live", proxy_list)

    def checkIsProxyIpPort(self):
        proxy_value_ip_port = self.ui_instance.proxy_value_ip_port.isChecked()
        handleSaveDataInputUser("is_proxy_ip_port", proxy_value_ip_port)
    
    def checkAccountIsProxyIpPort(self):
        proxy_value_ip_port = self.ui_instance.proxy_value_check_live_ip_port.isChecked()
        handleSaveDataInputUser("is_proxy_ip_port_check_live", proxy_value_ip_port)
        
    def getDefaultPassword(self):
        password_account = self.ui_instance.password_reg_account_value.text().strip()
        handleSaveDataInputUser("password_account", password_account)

        if not password_account:
            self.ui_instance.random_password_account.setChecked(True)
        else:
            self.ui_instance.random_password_account.setChecked(False)

        self.timer_check_password.start(1000)

    def checkRandomPassword(self):
        random_password_account = self.ui_instance.random_password_account.isChecked()
        if self.ui_instance.random_password_account:
            self.ui_instance.check_rule_password_account.setText("")
        handleSaveDataInputUser("random_password_account", random_password_account)

    def checkChangeUsername(self):
        is_change_username_check = self.ui_instance.is_change_username_check.isChecked()
        handleSaveDataInputUser("is_change_username_check", is_change_username_check)

    def inputFileUsername(self):
        link_username = QFileDialog.getOpenFileName(
            None, "Open File", "", "(*.txt)"
        )[0]
        self.ui_instance.list_username_value.setText(link_username)

        handleSaveDataInputUser("url_username", link_username)

    def handleShowDarkMode(self, event):
        darkMode(self.ui_instance)
        handleSaveDataInputUser("darkmode", True)

    def handleHideDarkMode(self, event):
        self.ui_instance.change_theme_switch_on.setVisible(False)
        self.ui_instance.change_theme_switch_off.setVisible(True)
        lightMode(self.ui_instance)
        handleSaveDataInputUser("darkmode", False)

    def getIsChromeCount(self):
        is_chrome_count = self.ui_instance.chrome_setting_line_value.value()
        handleSaveDataInputUser("is_chrome_count", is_chrome_count)

    def getChromePercentZoom(self):

        chrome_percent_zoom = self.ui_instance.chrome_percent_zoom_value.value()
        handleSaveDataInputUser("chrome_percent_zoom", chrome_percent_zoom)

    def getChromeValueDelay(self, value):
        if value < 1:
            QMessageBox.warning(None, "Warning", "Giá trị không được nhỏ hơn 1")
            self.ui_instance.chrome_delay_second_value.setValue(1)
            handleSaveDataInputUser("chromeValueDelay", 1)
            return

        chromeValueDelay = self.ui_instance.chrome_delay_second_value.value()
        handleSaveDataInputUser("chromeValueDelay", chromeValueDelay)

    def getDatabaseValue(self):
        database_value = self.ui_instance.database_value.text().strip()
        handleSaveDataInputUser("database_value", database_value)

    def checkIsUploadAvatar(self):
        is_upload_avatar = self.ui_instance.is_upload_avatar_yes.isChecked()
        handleSaveDataInputUser("is_upload_avatar", is_upload_avatar)

    def getRegCountryType(self):
        type_reg_country = self.ui_instance.type_reg_country.currentIndex()
        handleSaveDataInputUser("type_reg_country", type_reg_country)

    def getTypeExportAccount(self):
        typeExportAccount = self.ui_instance.export_account_format_value.currentIndex()
        handleSaveDataInputUser("typeExportAccount", typeExportAccount)

    def inputMailCheck(self):
        link_mail_check = self.ui_instance.fileNameCheck = QFileDialog.getOpenFileName(
            None, "Open File", "", "(*.txt)"
        )[0]
        self.ui_instance.file_mail_check_value.setText(self.ui_instance.fileNameCheck)

        handleSaveDataInputUser("url_mail_check", link_mail_check)

    def handleCheckMail(self):
        self.ui_instance.is_check_mail = True
        
        if not self.ui_instance.file_mail_check_value.text().strip():
            QMessageBox.warning(None, "Warning", "Vui lòng chọn file cần check")
            return
        
        if os.path.exists("configs_account.json"):
            with open("configs_account.json", "r") as json_file:
                data = json.load(json_file)
            fileMailCheck = data["url_mail_check"]
        else:
            fileMailCheck = self.ui_instance.fileNameCheck        

        checkMail(self.ui_instance, fileMailCheck)

    def inputAccountsCheck(self):
        list_accounts = self.ui_instance.fileNameCheck = QFileDialog.getOpenFileName(
            None, "Open File", "", "(*.txt)"
        )[0]
        self.ui_instance.file_accounts_check_value.setText(self.ui_instance.fileNameCheck)

        handleSaveDataInputUser("url_accounts_check", list_accounts)

    def handleCheckAccounts(self):        
        if not self.ui_instance.file_accounts_check_value.text().strip():
            QMessageBox.warning(None, "Warning", "Vui lòng chọn file cần check")
            return
        
        if not self.ui_instance.proxy_value_check_live.toPlainText().strip():
            QMessageBox.warning(None, "Warning", "Vui lòng nhập proxy")
            return
        
        self.ui_instance.max_thread_count_check_accounts = len(self.ui_instance.proxy_value_check_live.toPlainText().strip().splitlines())
        self.ui_instance.threadpool_check_accounts.setMaxThreadCount(self.ui_instance.max_thread_count_check_accounts)
        
        if os.path.exists("configs_account.json"):
            with open("configs_account.json", "r") as json_file:
                data = json.load(json_file)
            fileMailCheck = data["url_accounts_check"]
        else:
            fileMailCheck = self.ui_instance.fileNameCheck        

        checkLiveAccounts(self.ui_instance, fileMailCheck)

