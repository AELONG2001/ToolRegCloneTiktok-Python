from PySide6.QtWidgets import *
from PySide6.QtCore import *

from functions.handleSaveDataInputUser.handleSaveDataInputUser import handleSaveDataInputUser
from functions.handleMultiThreads.thread.startAutomation import startAutomation
from functions.handleMultiThreads.thread.stopAutomation import stopAutomation
from functions.handleOpenFolder.handleOpenListAvatar import selectAvatarFolder
from functions.handleCheckMail.checkMail import checkMail
import os
import json


class AutomationController:
    def __init__(self, ui_instance):
        self.ui_instance = ui_instance

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
      file_name, _ = QFileDialog.getSaveFileName(None, "Chọn nơi lưu tệp", file_path, "Tệp văn bản (*.txt);;Tất cả các tệp (*)")
      if file_name:
        try:
            with open(file_name, 'w') as file:
                # Đọc nội dung từ file cần lưu và ghi vào file mới
                with open(file_path, 'r') as source_file:
                    file.write(source_file.read())
        except Exception:
            pass

    def getProxyType(self):
        proxy_type = self.ui_instance.proxy_type.currentIndex()
        handleSaveDataInputUser("proxy_type", proxy_type + 1)

    def importProxy(self):
        proxy_text = self.ui_instance.proxy_value.toPlainText()
        proxy_list = proxy_text.splitlines()

        for row, proxy in enumerate(proxy_list):
            self.ui_instance.table_account_info.setItem(
                row, 2, QTableWidgetItem(proxy.strip())
            )

        handleSaveDataInputUser("proxys", proxy_list)

    def getDefaultPassword(self):
        default_password = self.ui_instance.password_reg_account_value.text()
        handleSaveDataInputUser("default_password", default_password)

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

        self.ui_instance.success_mail_count = 0
        self.ui_instance.failed_mail_count = 0
        self.ui_instance.mail_success_box.clear()
        self.ui_instance.mail_failed_box.clear()

        if os.path.exists("configs_account.json"):
            with open("configs_account.json", "r") as json_file:
                data = json.load(json_file)
            fileMailCheck = data["url_mail_check"]
        else:
            fileMailCheck = self.ui_instance.fileNameCheck
        

        checkMail(
            fileMailCheck,
            self.ui_instance.mail_success_box,
            self.ui_instance.mail_success,
            self.ui_instance.mail_failed_box,
            self.ui_instance.mail_failed,
        )
