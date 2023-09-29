from PySide6.QtWidgets import *
from functions.handleInputFileMail.getMailContent import getMailContent
from functions.handleMultiThreads.thread.AutomationThread import AutomationThread
import os
import json


def startAutomation(self):
    AutomationThread.num_quit = 0
    AutomationThread.drivers_list = []

    if os.path.exists("configs_account.json"):
        with open("configs_account.json", "r") as json_file:
            data = json.load(json_file)

        # input user have to includes mail
        if "url_mail" in data:
           input_file_path = data["url_mail"]
           output_file_path = "data/output.txt"
        else:
            QMessageBox.warning(None, "Warning", "Vui lòng nhập mail")
            return
        
        # input user have to includes captcha_key
        if not "captcha_key" in data:
            QMessageBox.warning(None, "Warning", "Vui lòng nhập captcha key")
            return
        else:
            if not data["captcha_key"]:
               QMessageBox.warning(None, "Warning", "Vui lòng nhập captcha key")
               return
        
        # input user have to includes proxys
        if not "proxys" in data:
            QMessageBox.warning(None, "Warning", "Vui lòng nhập proxys")
            return
        else:
            if not data["proxys"]:
               QMessageBox.warning(None, "Warning", "Vui lòng nhập proxys")
               return
        
        # input user have to includes api_token_gologin
        if not "api_token_gologin" in data:
            QMessageBox.warning(None, "Warning", "Vui lòng nhập api_token_gologin")
            return
        else:
            if not data["api_token_gologin"]:
               QMessageBox.warning(None, "Warning", "Vui lòng nhập api_token_gologin")
               return

    else:
        QMessageBox.warning(None, "Warning", "Vui lòng cập nhập các thông tin cần thiết trước khi bắt đầu chạy tool.\nVD: nhập mail, api captcha key,proxy,token và path của gologin...")
    
    # with open(input_file_path, "r") as f:
    #     mail_content = f.read()

    # accounts = getMailContent(mail_content)

    # if len(accounts) > 0:
    num_threads = self.threads_value.value()
    # else:
    #     num_threads = 1

    chrome_count = self.chrome_setting_line_value.value()
    captcha_type = self.captcha_type.currentIndex()
    captcha_key = self.captcha_key.text()
    proxy_type = self.proxy_type.currentIndex()
    random_password_account = self.random_password_account.isChecked()
    chrome_percent_zoom = self.chrome_percent_zoom_value.value()
    path_profile_gologin = self.path_gologin_value.text()
    is_upload_avatar = self.is_upload_avatar_yes.isChecked()

    self.thread_index = 0
    self.stop_all_threads = False
    self.chrome_threads = [
        AutomationThread(
            self,
            thread,
            input_file_path,
            output_file_path,
            chrome_count,
            captcha_type,
            captcha_key,
            proxy_type,
            random_password_account,
            chrome_percent_zoom,
            path_profile_gologin,
            is_upload_avatar
        )
        for thread in range(num_threads)
    ]
    self.start_next_thread()

    self.start_button.setEnabled(False)
    self.start_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.2)")
    self.stop_button.setEnabled(True)
    self.stop_button.setStyleSheet(
        "color:rgb(255, 252, 252);\n" "background-color:rgb(255, 0, 0)"
    )
