from PySide6.QtWidgets import *

from functions.handleMultiThreads.startAutomation import startAutomation
from functions.handleMultiThreads.stopAutomation import stopAutomation
from functions.handleOpenFolder.handleOpenListAvatar import selectAvatarFolder
from functions.handleInputFileMail.getMailContent import getMailContent
from functions.handleInputFileMail.readMailFile import readMailFile
from functions.handleCheckMail.checkMail import checkMail


class AutomationController:
    def __init__(self, ui_instance):
        self.ui_instance = ui_instance

    def start(self):
        startAutomation(self.ui_instance)

    def stop(self):
        stopAutomation(self.ui_instance)

    def checkThreadsValue(self, value):
        if value > 50:
            QMessageBox.warning(None, "Warning", "Tối đa không được vượt quá 50 luồng")
            self.ui_instance.threads_value.setValue(50)

    def handleAvatarFolderSelection(self):
        folder = selectAvatarFolder()
        if folder:
            self.ui_instance.avatar_value.setText(folder)

    def inputMail(self):
        self.ui_instance.fileName = QFileDialog.getOpenFileName(
            None, "Open File", "", "(*.txt)"
        )[0]
        self.ui_instance.mail_value.setText(self.ui_instance.fileName)
        if self.ui_instance.fileName:
            mail_content = readMailFile(self.ui_instance.fileName)
            accounts = getMailContent(mail_content)

            self.ui_instance.table_account_info.setRowCount(len(accounts))
            for row, (username, password) in enumerate(accounts):
                self.ui_instance.table_account_info.setItem(
                    row, 0, QTableWidgetItem(username)
                )
                self.ui_instance.table_account_info.setItem(
                    row, 1, QTableWidgetItem(password)
                )

    def getCaptchaKey(self, captcha_key):
        self.ui_instance.captcha_key_value = captcha_key

    def importProxy(self):
        proxy_text = self.ui_instance.proxy_value.toPlainText()
        proxy_list = proxy_text.splitlines()

        for row, proxy in enumerate(proxy_list):
            self.ui_instance.table_account_info.setItem(
                row, 3, QTableWidgetItem(proxy.strip())
            )

    def inputMailCheck(self):
        self.ui_instance.fileNameCheck = QFileDialog.getOpenFileName(
            None, "Open File", "", "(*.txt)"
        )[0]
        self.ui_instance.file_mail_check_value.setText(self.ui_instance.fileNameCheck)

    def handleCheckMail(self):
        if not self.ui_instance.file_mail_check_value.text():
            QMessageBox.warning(None, "Warning", "Vui lòng chọn file cần check")
            return

        self.ui_instance.success_mail_count = 0
        self.ui_instance.failed_mail_count = 0
        self.ui_instance.mail_success_box.clear()
        self.ui_instance.mail_failed_box.clear()

        checkMail(
            self.ui_instance.fileNameCheck,
            self.ui_instance.mail_success_box,
            self.ui_instance.mail_success,
            self.ui_instance.mail_failed_box,
            self.ui_instance.mail_failed,
        )
