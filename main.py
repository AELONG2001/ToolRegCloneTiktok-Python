from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# UI
from GUI.uiMain import uiMain
from GUI.translateUi import translateUi

# handle logic
from functions.handleMultiThreads.startAutomation import startAutomation
from functions.handleMultiThreads.stopAutomation import stopAutomation
from functions.handleOpenFolder.handleOpenListAvatar import selectAvatarFolder
from functions.handleInputFileMail.getMailContent import getMailContent
from functions.handleInputFileMail.readMailFile import readMailFile
from functions.handleCheckMail.checkMail import checkMail


class Ui_ToolRegCloneTiktok(object):
    def __init__(self):
        self.success_mail_count = 0
        self.failed_mail_count = 0

    def setupUi(self, ToolRegCloneTiktok):
        uiMain(self, ToolRegCloneTiktok)

    def start(self):
        startAutomation(self)

    def stop(self):
        stopAutomation(self)

    def checkThreadsValue(self, value):
        if value > 50:
            QMessageBox.warning(None, "Warning", "Tối đa không được vượt quá 50 luồng")
            self.threads_value.setValue(50)

    def handleAvatarFolderSelection(self):
        folder = selectAvatarFolder()
        if folder:
            self.avatar_value.setText(folder)
            # image_paths = [
            #     os.path.join(folder, file_name)
            #     for file_name in os.listdir(folder)
            #     if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
            # ]

    def inputMail(self):
        self.fileName = QFileDialog.getOpenFileName(None, "Open File", "", "(*.txt)")[0]
        self.mail_value.setText(self.fileName)
        if self.fileName:
            mail_content = readMailFile(self.fileName)
            accounts = getMailContent(mail_content)
            self.fillAccountTable(accounts)

    def fillAccountTable(self, accounts):
        self.table_account_info.setRowCount(len(accounts))
        for row, (username, password) in enumerate(accounts):
            self.table_account_info.setItem(row, 0, QTableWidgetItem(username))
            self.table_account_info.setItem(row, 1, QTableWidgetItem(password))

    def getCaptchaKey(self, captcha_key):
        self.captcha_key_value = captcha_key

    def importProxy(self):
        proxy_text = self.proxy_value.toPlainText()
        proxy_list = proxy_text.splitlines()

        for row, proxy in enumerate(proxy_list):
            self.table_account_info.setItem(row, 3, QTableWidgetItem(proxy.strip()))

    def inputMailCheck(self):
        self.fileNameCheck = QFileDialog.getOpenFileName(
            None, "Open File", "", "(*.txt)"
        )[0]
        self.file_mail_check_value.setText(self.fileNameCheck)

    def handleCheckMail(self):
        if not self.file_mail_check_value.text():
            QMessageBox.warning(None, "Warning", "Vui lòng chọn file cần check")
            return

        self.success_mail_count = 0
        self.failed_mail_count = 0
        self.mail_success_box.clear()
        self.mail_failed_box.clear()

        checkMail(
            self.fileNameCheck,
            self.mail_success_box,
            self.mail_success,
            self.mail_failed_box,
            self.mail_failed,
        )

    def retranslateUi(self, ToolRegCloneTiktok):
        translateUi(self, ToolRegCloneTiktok)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ToolRegCloneTiktok = QMainWindow()
    ui = Ui_ToolRegCloneTiktok()
    ui.setupUi(ToolRegCloneTiktok)
    ToolRegCloneTiktok.show()
    sys.exit(app.exec())
