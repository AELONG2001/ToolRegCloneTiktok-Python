from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from time import sleep

# UI
from GUI.uiMain import uiMain
from GUI.translateUi import translateUi

# Logic
from functions.handleLogicMain.logicMain import AutomationController


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
        self.ui_self.setupUi(self)

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

        self.stop_flag = False
        self.chrome_threads = []
        self.thread_index = 0
        self.stop_all_threads = False
        self.success_mail_count = 0
        self.failed_mail_count = 0

        self.start_timer = QTimer(self)
        self.start_timer.setInterval(2000)  # Thời gian chờ giữa các lần khởi động luồng
        self.start_timer.timeout.connect(self.start_next_thread)

        self.stop_progress_dialog = StopProgressDialog()

    def setupUi(self, ToolRegCloneTiktok):
        uiMain(self, ToolRegCloneTiktok)
        self.automation_controller = AutomationController(self)

    def start(self):
        self.automation_controller.start()

    def start_next_thread(self):
        self.automation_controller.start_next_thread()

    def stop(self):
        self.automation_controller.stop()

    def checkThreadsValue(self, value):
        self.automation_controller.checkThreadsValue(value)

    def handleAvatarFolderSelection(self):
        self.automation_controller.handleAvatarFolderSelection()

    def inputMail(self):
        self.automation_controller.inputMail()

    def getCaptchaKey(self):
        self.automation_controller.getCaptchaKey()

    def importProxy(self):
        self.automation_controller.importProxy()

    def inputMailCheck(self):
        self.automation_controller.inputMailCheck()

    def handleCheckMail(self):
        self.automation_controller.handleCheckMail()

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
