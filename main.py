from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from time import sleep
from dotenv import load_dotenv

# UI
from GUI.uiMain import uiMain
from GUI.translateUi import translateUi

# Logic
from functions.handleLogicMain.logicMain import AutomationController
from functions.handleMultiThreads.thread.AutomationThread import AutomationThread
import json

load_dotenv()

class StopProgressDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Quá trình này có thể mất thời gian...")
        self.setFixedSize(300, 100)

        layout = QVBoxLayout()
        self.progress_label = QLabel("Quá trình này có thể mất thời gian...")
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_label)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)
        self.setModal(True)
        self.setAutoFillBackground(True)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

    def set_progress(self, value):
        self.progress_bar.setValue(value)

    def set_progress_text(self, text):
        self.progress_label.setText(text)

class MainWindow(QMainWindow):
    def __init__(self, ui_self):
        super().__init__()
        self.ui_self = ui_self

    def closeEvent(self, event):
        result = QMessageBox.question(
            self,
            "Xác nhận dừng",
            "Bạn có chắc chắn muốn dừng không.Điều này có thể gây mất mát dữ liệu?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if result == QMessageBox.StandardButton.Yes:
            self.ui_self.stop_all_threads = True
            for thread in self.ui_self.chrome_threads:
                thread.stop()

            sleep(5)
            event.accept()
        else:
            event.ignore()


class Ui_ToolRegCloneTiktok(QObject):
    def __init__(self):
        super().__init__()
       
        self.mutex = QMutex()
        self.stop_flag = False
        self.chrome_threads = []
        self.thread_index = 0
        self.stop_all_threads = False
        self.success_mail_count = 0
        self.failed_mail_count = 0

        self.start_timer = QTimer(self)
        self.start_timer.setInterval(3000)  # Thời gian chờ giữa các lần khởi động luồng
       
        self.start_timer.timeout.connect(self.start_next_thread)

        self.stop_progress_dialog = StopProgressDialog()

    def setupUi(self, ToolRegCloneTiktok):
        uiMain(self, ToolRegCloneTiktok)
        self.automation_controller = AutomationController(self)
    def start(self):
        self.automation_controller.start()

    def start_next_thread(self):
        self.automation_controller.start_next_thread()
    
    def restart_thread(self, thread, username, password):
        print("Restart")
        with open("configs_account.json", "r") as json_file:
            data = json.load(json_file)

        input_file_path = data["url_mail"]
        output_file_path = "data/output.txt"
        chrome_count = self.chrome_setting_line_value.value()
        captcha_type = self.captcha_type.currentIndex()
        captcha_key = self.captcha_key.text()
        proxy_type = self.proxy_type.currentIndex()
        random_password_account = self.random_password_account.isChecked()
        chrome_percent_zoom = self.chrome_percent_zoom_value.value()
        path_profile_gologin = self.path_gologin_value.text()
        is_upload_avatar = self.is_upload_avatar_yes.isChecked()
        
        self.chrome_threads[thread] = AutomationThread(
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
            is_upload_avatar,
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

    def getDefaultPassword(self):
        self.automation_controller.getDefaultPassword()

    def checkRandomPassword(self):
        self.automation_controller.checkRandomPassword()

    def getIsChromeCount(self):
        self.automation_controller.getIsChromeCount()

    def getChromePercentZoom(self):
        self.automation_controller.getChromePercentZoom()

    def getChromeValueDelay(self):
        self.automation_controller.getChromeValueDelay()

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

    def updateResultText(self, username, status):
        if status:
            self.mail_success_box.append(username)
            self.success_mail_count += 1
        else:
            self.mail_failed_box.append(username)
            self.failed_mail_count += 1

        self.updateCounts()

        if self.success_mail_count + self.failed_mail_count == self.total_email_count:
            self.showSuccessMessage()

    def updateCounts(self):
        self.mail_success.setText(f"Live Mail ({self.success_mail_count}):")
        self.mail_failed.setText(f"Die Mail ({self.failed_mail_count}):")

    def showSuccessMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Kiểm tra email hoàn thành.")
        msg.setWindowTitle("Thành công")
        msg.exec()

        self.btn_check.setEnabled(True)
        self.btn_check.setStyleSheet("color: #fff; background-color: rgb(64, 170, 15)")
        self.btn_check.setText("Check")
        self.loading_icon.setVisible(False)

    
    def retranslateUi(self, ToolRegCloneTiktok):
        translateUi(self, ToolRegCloneTiktok)


if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    ui = Ui_ToolRegCloneTiktok()
    ToolRegCloneTiktok = MainWindow(ui)
    ui.setupUi(ToolRegCloneTiktok)
    ToolRegCloneTiktok.show()
    sys.exit(app.exec())
