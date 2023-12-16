import requests
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


def handleCheckMailApi(username, password):
    url = f"https://hotmailbase.com/api/check_mail"
    params = {
        "mail": f"{username}|{password}",
    }
    response = requests.get(url, params=params)
    data = response.json()
    return (username, password, data.get("Success", False))


class EmailCheckerTaskSignals(QObject):
    result_signal = Signal(str, str, bool)

class EmailCheckerTask(QRunnable):
    def __init__(self, username, password):
        super().__init__()
        self.username_mail = username
        self.password_mail = password
        self.signals = EmailCheckerTaskSignals()

    def run(self):
        _, _, status = handleCheckMailApi(self.username_mail, self.password_mail)
        self.signals.result_signal.emit(self.username_mail, self.password_mail, status)

def checkMail(
    self, fileNameCheck
):
    is_dark_mode = self.change_theme_switch_on.isVisible()
    self.mail_success.setText(f"Live Mail (0):")
    self.mail_failed.setText(f"Die Mail (0):")


    self.mail_success_box.clear()
    self.mail_failed_box.clear()

    self.success_mail_count = 0
    self.failed_mail_count = 0

    total_email_count = 0
    
    with open(fileNameCheck, 'r') as file:
        lines = file.readlines()
        total_email_count += len(lines)

        if not lines:
            QMessageBox.warning(
            None,
            "Warning",
            "File mail không được để trống",
            )
            return

        for line in lines:
            username, password = line.strip().split('|')
            task = EmailCheckerTask(username, password)
            task.signals.result_signal.connect(self.updateResultCheckMail)
            self.threadpool.start(task)

    self.total_email_count = total_email_count
    self.btn_check.setEnabled(False)
    self.btn_check.setText("Đang check")
    self.btn_check.setGeometry(QRect(440, 240, 120, 24))
    if is_dark_mode:
        self.btn_check.setStyleSheet("color: #fff; background-color: #636e72;")
    else:
        self.btn_check.setStyleSheet("color: #000; background-color: rgba(0, 0, 0, 0.2);")
    self.loading_icon_check_mail.setVisible(True)
    self.loadingMovieCheckMail.start()

