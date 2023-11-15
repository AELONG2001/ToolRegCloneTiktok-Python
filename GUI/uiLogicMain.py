from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# UI
from GUI.uiUpdateVersion import UpdateProgressDialog
from GUI.uiStopThread import StopProgressDialog

# Logic
from functions.handleLogicMain.logicMain import AutomationController
from functions.handleMultiThreads.thread.AutomationThread import AutomationThread
from GUI.uiMain import uiMain
from GUI.translateUi import translateUi
from utils.utils import wait, generate_random_name

import json
import datetime

class Ui_ToolRegCloneTiktok(QObject):
    def __init__(self, data):
        super().__init__()

        self.data = data
        self.current_version = "1.0.0"
        self.latest_version = self.data["latest_version"]
        self.remaining_days = self.data["remaining_days"]
        self.is_start = False
        self.startAutomation_called = False
        self.is_check_mail = False
        self.stop_flag = False
        self.chrome_threads = []
        self.thread_index = 0
        self.stop_all_threads = False
        self.success_mail_count = 0
        self.failed_mail_count = 0

        self.start_timer = QTimer(self)
        self.re_start_timer = QTimer(self)
    
        self.update_progress_dialog = UpdateProgressDialog(self)
        self.stop_progress_dialog = StopProgressDialog(self)

    def setupUi(self, ToolRegCloneTiktok):
        uiMain(self, ToolRegCloneTiktok)
        self.automation_controller = AutomationController(self)

    def update(self):
        self.automation_controller.update()
         
    def start(self):
        self.automation_controller.start()

    def start_next_thread(self):
        self.automation_controller.start_next_thread()
    
    def restart_thread(self, thread, username, password):
        with open("configs_account.json", "r") as json_file:
            data = json.load(json_file)

        input_file_path = data["url_mail"]
        output_file_path = "data/output.txt"
        current_date = datetime.date.today().strftime("%d/%m/%Y")
        chrome_count = self.chrome_setting_line_value.value()
        captcha_type = self.captcha_type.currentIndex()
        captcha_key = self.captcha_key.text()
        proxy_type = self.proxy_type.currentIndex()
        random_password_account = self.random_password_account.isChecked()
        chrome_percent_zoom = self.chrome_percent_zoom_value.value()
        path_profile_gologin = self.path_gologin_value.text()
        if "api_value_hotmailbox" in data:
            api_key_hotmailbox = data["api_value_hotmailbox"]
        else:
            api_key_hotmailbox = ""
        is_upload_avatar = self.is_upload_avatar_yes.isChecked()
        
        self.chrome_threads[thread] = AutomationThread(
            self, 
            thread,
            input_file_path,
            output_file_path,
            current_date,
            chrome_count,
            captcha_type,
            captcha_key,
            proxy_type,
            random_password_account,
            chrome_percent_zoom,
            path_profile_gologin,
            api_key_hotmailbox,
            is_upload_avatar,
            # self.data_queue,
            username,
            password,
            True
        )  # Khởi tạo thread mới
        self.chrome_threads[thread].start()

    def stop(self):
        self.automation_controller.stop()

    def checkThreadsValue(self, value):
        self.automation_controller.checkThreadsValue(value)

    def handleAvatarFolderSelection(self):
        self.automation_controller.handleAvatarFolderSelection()

    def inputMail(self):
        self.automation_controller.inputMail()

    def getCaptchaType(self):
        self.automation_controller.getCaptchaType()

    def getCaptchaKey(self):
        self.automation_controller.getCaptchaKey()

    def exportAccount(self):
        self.automation_controller.exportAccount()

    def getProxyType(self):
        self.automation_controller.getProxyType()

    def importProxy(self):
        self.automation_controller.importProxy()

    def checkIsProxyIpPort(self):
        self.automation_controller.checkIsProxyIpPort()

    def getDefaultPassword(self):
        self.automation_controller.getDefaultPassword()

    def checkRandomPassword(self):
        self.automation_controller.checkRandomPassword()

    def getIsChromeCount(self):
        self.automation_controller.getIsChromeCount()

    def getChromePercentZoom(self, value):
        self.automation_controller.getChromePercentZoom(value)

    def getChromeValueDelay(self, value):
        self.automation_controller.getChromeValueDelay(value)

    def getTokenGologin(self):
        self.automation_controller.getTokenGologin()

    def getPathGologin(self):
        self.automation_controller.getPathGologin()

    def getValueApiHotmailbox(self):
        self.automation_controller.getValueApiHotmailbox()

    def checkIsUploadAvatar(self):
        self.automation_controller.checkIsUploadAvatar()
    
    def getTypeExportAccount(self):
        self.automation_controller.getTypeExportAccount()

    def inputMailCheck(self):
        self.automation_controller.inputMailCheck()

    def handleCheckMail(self):
        self.automation_controller.handleCheckMail()

    def updateResultCheckInitalValues(self, can_continue, message):
        if can_continue:
            self.is_start = True
            self.start()
        else:
            self.is_start = False
            QMessageBox.warning(None, "Warning", f"{message}")

    def updateResultCheckMail(self, username, password, status):
        if status:
            self.mail_success_box.append(f"{username}|{password}")
            self.success_mail_count += 1

        else:
            self.mail_failed_box.append(f"{username}|{password}")
            self.failed_mail_count += 1

        self.mail_success.setText(f"Live Mail ({self.success_mail_count}):")
        self.mail_failed.setText(f"Die Mail ({self.failed_mail_count}):")

        if self.success_mail_count + self.failed_mail_count == self.total_email_count:
            self.btn_check.setEnabled(True)
            self.btn_check.setText("Check")
            self.btn_check.setGeometry(QRect(430, 240, 75, 24))
            self.btn_check.setStyleSheet("color: #fff; background-color: rgb(64, 170, 15)")
            self.loading_icon_check_mail.setVisible(False)

            input_file_path = "data/hotmail.txt"
            total_mail_success = self.mail_success_box.toPlainText()

            with open(input_file_path, "w") as file:
                file.write("")

            with open(input_file_path, "w") as file:
                file.write(total_mail_success)

            self.is_check_mail = False

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Kiểm tra email hoàn thành.")
            msg.setWindowTitle("Thành công")
            msg.exec()

    def retranslateUi(self, ToolRegCloneTiktok):
        translateUi(self, ToolRegCloneTiktok, self.current_version, self.remaining_days)