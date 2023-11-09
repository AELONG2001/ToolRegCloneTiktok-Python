from PySide6.QtWidgets import *
from PySide6.QtCore import *

from functions.handleSaveDataInputUser.handleSaveDataInputUser import handleSaveDataInputUser
from functions.handleMultiThreads.thread.startAutomation import startAutomation
from functions.handleMultiThreads.thread.stopAutomation import stopAutomation
from functions.handleOpenFolder.handleOpenListAvatar import selectAvatarFolder
from functions.handleCheckMail.checkMail import checkMail
from functions.proxy.TMProxy.handleCheckKeyTmProxy import handleCheckKeyTmProxy
from functions.proxy.TMProxy.handleGetNewTMProxyToCheckExpired import handleGetNewTMProxyToCheckExpired
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
        print("Update")
        url = self.ui_instance.data["link_update"]
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
        shutil.rmtree(f"{self.ui_instance.current_version}")
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
            self.ui_instance.start_timer.start()  # Khởi động lại timer để tạo khoảng thời gian cho lần khởi động luồng tiếp theo
        else:
            self.ui_instance.start_timer.stop()

    def stop(self):
        stopAutomation(self.ui_instance)

    def validate_password(self, password):
        password_regex = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^&*()])[A-Za-z\d@#$%^&*()]{8,}$')
        return bool(password_regex.match(password))
    
    def check_password(self):
        password_account = self.ui_instance.password_reg_account_value.text()
        if self.validate_password(password_account):
            self.ui_instance.check_rule_password_account.setText("")
        else:
            random_password_account = self.ui_instance.random_password_account.isChecked()
            if not random_password_account:
                self.ui_instance.check_rule_password_account.setText("Mật khẩu phải bao gồm ít nhất 8 ký tự bao gồm chữ, số và ký tự đặc biệt")


    def checkThreadsValue(self, value):
        num_threads = self.ui_instance.threads_value.value()
        
        if value < 1:
            QMessageBox.warning(None, "Warning", "Tối thiểu là 1 luồng")
            self.ui_instance.threads_value.setValue(1)
        elif value > 50:
            QMessageBox.warning(None, "Warning", "Tối đa không được vượt quá 50 luồng")
            self.ui_instance.threads_value.setValue(50)

        handleSaveDataInputUser("num_threads", num_threads)

    def handleAvatarFolderSelection(self):
        link_avatar = selectAvatarFolder()
        if link_avatar:
            self.ui_instance.avatar_value.setText(link_avatar)
        handleSaveDataInputUser("url_avatar", link_avatar)

    def inputMail(self):
        link_mail = self.ui_instance.fileName = QFileDialog.getOpenFileName(
            None, "Open File", "", "(*.txt)"
        )[0]
        self.ui_instance.mail_value.setText(self.ui_instance.fileName)

        handleSaveDataInputUser("url_mail", link_mail)

    def getCaptchaType(self):
        captcha_type = self.ui_instance.captcha_type.currentIndex()
        handleSaveDataInputUser("captcha_type", captcha_type + 1)

    def getCaptchaKey(self):
        captcha_key = self.ui_instance.captcha_key.text()
        handleSaveDataInputUser("captcha_key", captcha_key)

    def exportAccount(self):
        file_path = "data/output.txt"     
        typeExportAccount = self.ui_instance.export_account_format_value.currentIndex()

        default_file_name = "output.txt"

        if typeExportAccount == 1:
            default_file_name = "output_without_cookie.txt"
        elif typeExportAccount == 2:
            default_file_name = "output_username_password.txt"

        file_name, _ = QFileDialog.getSaveFileName(None, "Chọn nơi lưu tệp", default_file_name, "Tệp văn bản (*.txt);;Tất cả các tệp (*)")

        if not file_name:
            return
    
        with open(file_path, "r") as file:
                accounts =  file.readlines()

        if typeExportAccount == 0:
                selected_data = accounts
        elif typeExportAccount == 1:
                selected_data = [line.split("|")[:4] + line.split("|")[5:] for line in accounts]
        elif typeExportAccount == 2:
                selected_data = [line.split("|")[:2] for line in accounts]
        else:
            return

        with open(file_name, "w") as txtfile:
            if typeExportAccount == 1:
                for line in selected_data:
                    txtfile.write("|".join(line))
            elif typeExportAccount == 2:
                for line in selected_data:
                    txtfile.write("|".join(line) + "\n")
            else:
                txtfile.writelines(selected_data)

        QMessageBox.information(None, "Thông báo", "Đã lưu thành công!")
            

    def getProxyType(self):
        proxy_type = self.ui_instance.proxy_type.currentIndex()
        if proxy_type == 2 or proxy_type == 3:
            self.ui_instance.proxy_value_ip_port.setVisible(True)
            self.ui_instance.proxy_value_ip_port_user_pass.setVisible(True)
        else:
            self.ui_instance.proxy_value_ip_port.setVisible(False)
            self.ui_instance.proxy_value_ip_port_user_pass.setVisible(False)

        handleSaveDataInputUser("proxy_type", proxy_type + 1)

    def importProxy(self):
        proxy_text = self.ui_instance.proxy_value.toPlainText()
        proxy_list = proxy_text.splitlines()

        handleSaveDataInputUser("proxys", proxy_list)

    def checkProxy(self):
        api_key_proxy = self.ui_instance.proxy_value.toPlainText()
        api_key_list = api_key_proxy.splitlines()

        response_api_tm_proxy_check_correct = handleCheckKeyTmProxy(api_key_list)
        response_api_tm_proxy_check_expired = handleGetNewTMProxyToCheckExpired(api_key_list)

        if response_api_tm_proxy_check_expired:
           QMessageBox.warning(None, "Warning", f"{response_api_tm_proxy_check_expired}Vui lòng kiểm tra lại")

        if response_api_tm_proxy_check_correct:
           QMessageBox.warning(None, "Warning", f"{response_api_tm_proxy_check_correct}Vui lòng kiểm tra lại")
        else:
            QMessageBox.information(None, "Thông báo", f"Proxy live.Hãy bắt đầu chạy tool")
        

    def getDefaultPassword(self):
        password_account = self.ui_instance.password_reg_account_value.text()
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

    def getIsChromeCount(self):
        is_chrome_count = self.ui_instance.chrome_setting_line_value.value()
        handleSaveDataInputUser("is_chrome_count", is_chrome_count)

    def getChromePercentZoom(self):
        chrome_percent_zoom = self.ui_instance.chrome_percent_zoom_value.value()
        handleSaveDataInputUser("chrome_percent_zoom", chrome_percent_zoom)

    def getChromeValueDelay(self):
        chromeValueDelay = self.ui_instance.chrome_delay_minute_value.value()
        handleSaveDataInputUser("chromeValueDelay", chromeValueDelay)

    def getTokenGologin(self):
        api_token_gologin = self.ui_instance.api_token_gologin_value.text()
        handleSaveDataInputUser("api_token_gologin", api_token_gologin)

    def getPathGologin(self):
        path_gologin = self.ui_instance.path_gologin_value.text()
        handleSaveDataInputUser("path_gologin", path_gologin)    

    def getValueApiHotmailbox(self):
        api_value_hotmailbox = self.ui_instance.api_hotmailbox_value.text()
        handleSaveDataInputUser("api_value_hotmailbox", api_value_hotmailbox)

    def checkIsUploadAvatar(self):
        is_upload_avatar = self.ui_instance.is_upload_avatar_yes.isChecked()
        handleSaveDataInputUser("is_upload_avatar", is_upload_avatar)

    def getTypeExportAccount(self):
        typeExportAccount = self.ui_instance.export_account_format_value.currentIndex()
        handleSaveDataInputUser("typeExportAccount", typeExportAccount + 1)

    def inputMailCheck(self):
        link_mail_check = self.ui_instance.fileNameCheck = QFileDialog.getOpenFileName(
            None, "Open File", "", "(*.txt)"
        )[0]
        self.ui_instance.file_mail_check_value.setText(self.ui_instance.fileNameCheck)

        handleSaveDataInputUser("url_mail_check", link_mail_check)

    def handleCheckMail(self):
        if not self.ui_instance.file_mail_check_value.text():
            QMessageBox.warning(None, "Warning", "Vui lòng chọn file cần check")
            return
        
        if os.path.exists("configs_account.json"):
            with open("configs_account.json", "r") as json_file:
                data = json.load(json_file)
            fileMailCheck = data["url_mail_check"]
        else:
            fileMailCheck = self.ui_instance.fileNameCheck        

        checkMail(self.ui_instance, fileMailCheck)
