import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_ToolRegCloneTiktok(object):
    def setupUi(self, ToolRegCloneTiktok):
        ToolRegCloneTiktok.setObjectName("ToolRegCloneTiktok")
        ToolRegCloneTiktok.setEnabled(True)
        ToolRegCloneTiktok.resize(1210, 488)
        font = QFont()
        font.setBold(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        ToolRegCloneTiktok.setFont(font)
        icon = QIcon()
        icon.addPixmap(
            QPixmap(".\\../../../../../Downloads/icon-qt/tik-tok_4782345.png"),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        ToolRegCloneTiktok.setWindowIcon(icon)
        ToolRegCloneTiktok.setAnimated(False)
        ToolRegCloneTiktok.setTabShape(QTabWidget.TabShape.Triangular)
        self.centralwidget = QWidget(parent=ToolRegCloneTiktok)
        self.centralwidget.setObjectName("centralwidget")
        self.start = QPushButton(parent=self.centralwidget)
        self.start.setGeometry(QRect(10, 10, 91, 24))
        self.start.setMouseTracking(False)
        self.start.setStyleSheet(
            "color:rgb(255, 252, 252);\n" "background-color:rgb(64, 170, 15)"
        )
        icon1 = QIcon()
        icon1.addPixmap(
            QPixmap(".\\../../../../../Downloads/icon-qt/right_4162041.png"),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.start.setIcon(icon1)
        self.start.setAutoRepeat(False)
        self.start.setObjectName("start")
        self.stop = QPushButton(parent=self.centralwidget)
        self.stop.setGeometry(QRect(110, 10, 91, 24))
        self.stop.setStyleSheet(
            "color:rgb(255, 252, 252);\n" "background-color:rgb(255, 0, 0)"
        )
        icon2 = QIcon()
        icon2.addPixmap(
            QPixmap(".\\../../../../../Downloads/icon-qt/stop-button_4340168.png"),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.stop.setIcon(icon2)
        self.stop.setObjectName("stop")
        self.threads_value = QSpinBox(parent=self.centralwidget)
        self.threads_value.setGeometry(QRect(280, 10, 41, 22))
        font = QFont()
        font.setBold(True)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.threads_value.setFont(font)
        self.threads_value.setProperty("value", 1)
        self.threads_value.setObjectName("threads_value")
        self.threads_value.setMinimum(1)
        self.threads = QLabel(parent=self.centralwidget)
        self.threads.setGeometry(QRect(220, 10, 61, 21))
        self.threads.setStyleSheet('font: 600 11pt "Segoe UI";')
        self.threads.setObjectName("threads")
        self.list_avatar = QPushButton(parent=self.centralwidget)
        self.list_avatar.setGeometry(QRect(330, 10, 121, 24))
        icon3 = QIcon()
        icon3.addPixmap(
            QPixmap(".\\../../../../../Downloads/icon-qt/folder_3767094.png"),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.list_avatar.setIcon(icon3)
        self.list_avatar.setObjectName("list_avatar")
        self.avatar_value = QLineEdit(parent=self.centralwidget)
        self.avatar_value.setGeometry(QRect(460, 10, 113, 21))
        self.avatar_value.setObjectName("avatar_value")
        self.list_mail = QLineEdit(parent=self.centralwidget)
        self.list_mail.setGeometry(QRect(710, 10, 113, 21))
        self.list_mail.setObjectName("list_mail")
        self.open_mail_btn = QPushButton(parent=self.centralwidget)
        self.open_mail_btn.setGeometry(QRect(580, 10, 121, 24))
        icon4 = QIcon()
        icon4.addPixmap(
            QPixmap(".\\../../../../../Downloads/icon-qt/txt_8361365.png"),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.open_mail_btn.setIcon(icon4)
        self.open_mail_btn.setObjectName("open_mail_btn")
        self.captcha_key = QLineEdit(parent=self.centralwidget)
        self.captcha_key.setGeometry(QRect(950, 10, 141, 20))
        self.captcha_key.setText("")
        self.captcha_key.setObjectName("captcha_key")
        self.omocaptcha = QLabel(parent=self.centralwidget)
        self.omocaptcha.setGeometry(QRect(840, 10, 111, 21))
        self.omocaptcha.setStyleSheet('font: 700 10pt "Segoe UI";')
        self.omocaptcha.setObjectName("omocaptcha")
        self.export_excel = QPushButton(parent=self.centralwidget)
        self.export_excel.setGeometry(QRect(1100, 10, 75, 21))
        self.export_excel.setStyleSheet(
            "color:#fff;\n" "background-color: rgb(19, 170, 24);"
        )
        self.export_excel.setObjectName("export_excel")
        self.table_account_info = QTableWidget(parent=self.centralwidget)
        self.table_account_info.setEnabled(True)
        self.table_account_info.setGeometry(QRect(10, 60, 881, 391))
        self.table_account_info.setAutoFillBackground(False)
        self.table_account_info.setLineWidth(1)
        self.table_account_info.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn
        )
        self.table_account_info.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.table_account_info.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.table_account_info.setTabKeyNavigation(True)
        self.table_account_info.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.table_account_info.setShowGrid(True)
        self.table_account_info.setRowCount(10)
        self.table_account_info.setObjectName("table_account_info")
        self.table_account_info.setColumnCount(5)
        item = QTableWidgetItem()
        self.table_account_info.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.table_account_info.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.table_account_info.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.table_account_info.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.table_account_info.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.table_account_info.setHorizontalHeaderItem(5, item)
        self.table_account_info.horizontalHeader().setVisible(True)
        self.table_account_info.horizontalHeader().setCascadingSectionResizes(False)
        self.proxy_value = QPlainTextEdit(parent=self.centralwidget)
        self.proxy_value.setGeometry(QRect(920, 80, 211, 371))
        self.proxy_value.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn
        )
        self.proxy_value.setObjectName("proxy_value")
        self.list_proxy = QLabel(parent=self.centralwidget)
        self.list_proxy.setGeometry(QRect(920, 50, 61, 31))
        self.list_proxy.setStyleSheet('font: 700 10pt "Segoe UI";')
        self.list_proxy.setObjectName("list_proxy")
        self.import_proxy = QPushButton(parent=self.centralwidget)
        self.import_proxy.setGeometry(QRect(1140, 420, 61, 31))
        self.import_proxy.setObjectName("import_proxy")
        ToolRegCloneTiktok.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(parent=ToolRegCloneTiktok)
        self.statusbar.setObjectName("statusbar")
        self.threads_value.valueChanged.connect(self.checkThreadsValue)
        self.list_avatar.clicked.connect(self.selectAvatarFolder)
        self.open_mail_btn.clicked.connect(self.inputMail)
        self.captcha_key.textChanged.connect(self.getCaptchaKey)
        self.import_proxy.clicked.connect(self.importProxy)
        ToolRegCloneTiktok.setStatusBar(self.statusbar)

        self.retranslateUi(ToolRegCloneTiktok)
        QMetaObject.connectSlotsByName(ToolRegCloneTiktok)

        self.table_account_info.setColumnWidth(0, 200)
        self.table_account_info.setColumnWidth(1, 100)
        self.table_account_info.setColumnWidth(2, 180)
        self.table_account_info.setColumnWidth(3, 200)
        self.table_account_info.setColumnWidth(4, 160)

    def checkThreadsValue(self, value):
        if value > 50:
            QMessageBox.warning(None, "Warning", "Tối đa không được vượt quá 50 luồng")
            self.threads_value.setValue(50)

    def selectAvatarFolder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder = QFileDialog.getExistingDirectory(
            None,
            "Select Avatar Folder",
            "",
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
        )
        if folder:
            self.avatar_value.setText(folder)
            image_paths = [
                os.path.join(folder, file_name)
                for file_name in os.listdir(folder)
                if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
            ]

    def processMailContent(self, mail_conent):
        accounts = []
        for line in mail_conent.splitlines():
            if "|" in line:
                username, password = line.split("|", 1)
                accounts.append((username.strip(), password.strip()))
        return accounts

    def readMailFile(self, file_path):
        with open(file_path, "r") as file:
            mail_content = file.read()
            return mail_content

    def inputMail(self):
        self.fileName = QFileDialog.getOpenFileName(None, "Open File", "", "(*.txt)")[0]
        self.list_mail.setText(self.fileName)
        if self.fileName:
            mail_content = self.readMailFile(self.fileName)
            accounts = self.processMailContent(mail_content)
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

    def retranslateUi(self, ToolRegCloneTiktok):
        _translate = QCoreApplication.translate
        ToolRegCloneTiktok.setWindowTitle(
            _translate("ToolRegCloneTiktok", "ToolRegCloneTiktok")
        )
        self.start.setWhatsThis(
            _translate(
                "ToolRegCloneTiktok", "<html><head/><body><p><br/></p></body></html>"
            )
        )
        self.start.setText(_translate("ToolRegCloneTiktok", "Start"))
        self.stop.setText(_translate("ToolRegCloneTiktok", "Stop"))
        self.threads.setText(_translate("ToolRegCloneTiktok", "Threads"))
        self.list_avatar.setText(_translate("ToolRegCloneTiktok", " Folder Avatar"))
        self.avatar_value.setText(_translate("ToolRegCloneTiktok", "C://images"))
        self.list_mail.setText(_translate("ToolRegCloneTiktok", "hotmail.txt"))
        self.open_mail_btn.setText(_translate("ToolRegCloneTiktok", " List mail"))
        self.omocaptcha.setText(_translate("ToolRegCloneTiktok", "omocaptcha.com"))
        self.export_excel.setText(_translate("ToolRegCloneTiktok", "Export excel"))
        self.table_account_info.setSortingEnabled(False)
        item = self.table_account_info.horizontalHeaderItem(0)
        item.setText(_translate("ToolRegCloneTiktok", "username"))
        item = self.table_account_info.horizontalHeaderItem(1)
        item.setText(_translate("ToolRegCloneTiktok", "passMail"))
        item = self.table_account_info.horizontalHeaderItem(2)
        item.setText(_translate("ToolRegCloneTiktok", "cookie"))
        item = self.table_account_info.horizontalHeaderItem(3)
        item.setText(_translate("ToolRegCloneTiktok", "proxy"))
        item = self.table_account_info.horizontalHeaderItem(4)
        item.setText(_translate("ToolRegCloneTiktok", "status"))
        self.list_proxy.setText(_translate("ToolRegCloneTiktok", "List Proxy"))
        self.import_proxy.setText(_translate("ToolRegCloneTiktok", "Import"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ToolRegCloneTiktok = QMainWindow()
    ui = Ui_ToolRegCloneTiktok()
    ui.setupUi(ToolRegCloneTiktok)
    ToolRegCloneTiktok.show()
    sys.exit(app.exec())
