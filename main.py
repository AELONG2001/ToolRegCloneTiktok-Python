import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import threading
from selenium import webdriver
from time import sleep
import math
import requests


class AutomationThread(threading.Thread):
    def __init__(self, num_threads):
        super(AutomationThread, self).__init__()
        self.num_threads = num_threads

    def run(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--force-device-scale-factor=1")
        options.add_argument("--no-first-run")
        options.add_argument("--no-service-autorun")
        options.add_argument("--password-store-basic")
        options.add_argument("--lang=en-US")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-cpu")
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "download_restrictions": 3,
        }
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--enable-main-frame-before-activation")
        options.add_argument("--display-capture-permissions-policy-allowed")
        options.add_argument("--disabled-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-plugins-discovery")
        options.add_argument("--disabled-gpu-shader-disk-cache")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            "--user-data-dir=C:/Users/HD/AppData/Local/Temp/GoLogin/profiles/64be3436303d394f7791b045/Default"
        )
        driver = webdriver.Chrome(options=options)

        num_worker = self.num_threads
        # Số cột muốn sắp xếp trên màn hình
        cols = 5
        x = (num_worker % cols) * 510
        y = math.floor(num_worker / cols) * 810

        driver.set_window_rect(x, y, 200, 800)
        driver.get("https://www.tiktok.com/signup/phone-or-email/email")
        sleep(200)
        driver.quit()


class Ui_ToolRegCloneTiktok(object):
    def setupUi(self, ToolRegCloneTiktok):
        ToolRegCloneTiktok.setObjectName("ToolRegCloneTiktok")
        ToolRegCloneTiktok.resize(1256, 573)
        self.centralwidget = QWidget(parent=ToolRegCloneTiktok)
        self.centralwidget.setObjectName("centralwidget")
        self.ToolRegCloneTiktok = QTabWidget(parent=self.centralwidget)
        self.ToolRegCloneTiktok.setGeometry(QRect(-4, -1, 1301, 1079))
        self.ToolRegCloneTiktok.setObjectName("ToolRegCloneTiktok")
        self.home = QWidget()
        self.home.setObjectName("home")
        self.mail_value = QLineEdit(parent=self.home)
        self.mail_value.setGeometry(QRect(720, 10, 113, 21))
        self.mail_value.setObjectName("mail_value")
        self.list_avatar = QPushButton(parent=self.home)
        self.list_avatar.setGeometry(QRect(340, 10, 121, 24))
        icon = QIcon()
        icon.addPixmap(
            QPixmap(".\\../../../../../Downloads/icon-qt/tik-tok_4782345.png"),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        ToolRegCloneTiktok.setWindowIcon(icon)
        icon.addPixmap(
            QPixmap(".\\../../../../../Downloads/icon-qt/folder_3767094.png"),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.list_avatar.setIcon(icon)
        self.list_avatar.setObjectName("list_avatar")
        self.list_proxy = QLabel(parent=self.home)
        self.list_proxy.setGeometry(QRect(1311, 130, 61, 31))
        self.list_proxy.setStyleSheet('font: 700 10pt "Segoe UI";')
        self.list_proxy.setObjectName("list_proxy")
        self.proxy_value = QPlainTextEdit(parent=self.home)
        self.proxy_value.setGeometry(QRect(1311, 167, 211, 371))
        self.proxy_value.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn
        )
        self.proxy_value.setObjectName("proxy_value")
        self.captcha_key = QLineEdit(parent=self.home)
        self.captcha_key.setGeometry(QRect(1348, 80, 141, 20))
        self.captcha_key.setText("")
        self.captcha_key.setObjectName("captcha_key")
        self.start = QPushButton(parent=self.home)
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
        self.threads_value = QSpinBox(parent=self.home)
        self.threads_value.setGeometry(QRect(280, 10, 51, 22))
        font = QFont()
        font.setBold(True)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.threads_value.setFont(font)
        self.threads_value.setProperty("value", 1)
        self.threads_value.setObjectName("threads_value")
        self.export_excel = QPushButton(parent=self.home)
        self.export_excel.setGeometry(QRect(1536, 80, 75, 21))
        self.export_excel.setStyleSheet(
            "color:#fff;\n" "background-color: rgb(19, 170, 24);"
        )
        self.export_excel.setObjectName("export_excel")
        self.import_proxy = QPushButton(parent=self.home)
        self.import_proxy.setGeometry(QRect(1150, 420, 61, 31))
        self.import_proxy.setObjectName("import_proxy")
        self.stop = QPushButton(parent=self.home)
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
        self.threads = QLabel(parent=self.home)
        self.threads.setGeometry(QRect(220, 10, 61, 21))
        self.threads.setStyleSheet('font: 600 11pt "Segoe UI";')
        self.threads.setObjectName("threads")
        self.table_account_info = QTableWidget(parent=self.home)
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
        self.table_account_info.setColumnCount(6)
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
        self.avatar_value = QLineEdit(parent=self.home)
        self.avatar_value.setGeometry(QRect(470, 10, 113, 21))
        self.avatar_value.setObjectName("avatar_value")
        self.omocaptcha = QLabel(parent=self.home)
        self.omocaptcha.setGeometry(QRect(850, 10, 121, 21))
        self.omocaptcha.setStyleSheet('font: 11pt "Sans Serif Collection";')
        self.omocaptcha.setObjectName("omocaptcha")
        self.list_mail = QPushButton(parent=self.home)
        self.list_mail.setGeometry(QRect(590, 10, 121, 24))
        icon3 = QIcon()
        icon3.addPixmap(
            QPixmap(".\\../../../../../Downloads/icon-qt/txt_8361365.png"),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.list_mail.setIcon(icon3)
        self.list_mail.setObjectName("list_mail")
        self.captcha_key = QLineEdit(parent=self.home)
        self.captcha_key.setGeometry(QRect(970, 10, 141, 20))
        self.captcha_key.setText("")
        self.captcha_key.setObjectName("captcha_key")
        self.export_excel = QPushButton(parent=self.home)
        self.export_excel.setGeometry(QRect(1130, 10, 75, 21))
        self.export_excel.setStyleSheet(
            "color:#fff;\n" "background-color: rgb(19, 170, 24);"
        )
        self.export_excel.setObjectName("export_excel")
        self.list_proxy = QLabel(parent=self.home)
        self.list_proxy.setGeometry(QRect(920, 50, 61, 31))
        self.list_proxy.setStyleSheet('font: 700 10pt "Segoe UI";')
        self.list_proxy.setObjectName("list_proxy")
        self.proxy_value = QPlainTextEdit(parent=self.home)
        self.proxy_value.setGeometry(QRect(920, 80, 211, 371))
        self.proxy_value.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn
        )
        self.proxy_value.setObjectName("proxy_value")
        self.label_3 = QLabel(parent=self.home)
        self.label_3.setGeometry(QRect(70, 470, 81, 16))
        self.label_3.setStyleSheet(
            "color:rgb(16, 170, 16);\n"
            'font: 600 9pt "Segoe UI Variable Display Semib";\n'
            'font: 700 10pt "Segoe UI";'
        )
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.link_facebook = QLabel(parent=self.home)
        self.link_facebook.setGeometry(QRect(50, 490, 301, 31))
        self.link_facebook.setStyleSheet(
            "color:#0000ff;\n"
            "text-decoration: underline;\n"
            'font: 9pt "Segoe UI";\n'
            'font: 600 9pt "Segoe UI Variable Display Semib";\n'
            'font: 700 10pt "Segoe UI";'
        )
        self.link_facebook.setObjectName("link_facebook")
        self.phone = QLabel(parent=self.home)
        self.phone.setGeometry(QRect(70, 460, 81, 31))
        self.phone.setStyleSheet("color:#00557f;\n" 'font: 700 10pt "Segoe UI";')
        self.phone.setObjectName("phone")
        self.hotline = QLabel(parent=self.home)
        self.hotline.setGeometry(QRect(10, 455, 49, 41))
        self.hotline.setStyleSheet('font: 700 10pt "Segoe UI";')
        self.hotline.setObjectName("hotline")
        self.icon_facebook = QPushButton(parent=self.home)
        self.icon_facebook.setGeometry(QRect(10, 490, 31, 31))
        self.icon_facebook.setText("")
        icon4 = QIcon()
        icon4.addPixmap(
            QPixmap(".\\../../../../../Downloads/icon-qt/facebook_5968764.png"),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.icon_facebook.setIcon(icon4)
        self.icon_facebook.setIconSize(QSize(20, 20))
        self.icon_facebook.setObjectName("icon_facebook")
        self.copyright = QLabel(parent=self.home)
        self.copyright.setGeometry(QRect(790, 490, 231, 16))
        self.copyright.setStyleSheet('font: 700 10pt "Segoe UI";')
        self.copyright.setObjectName("copyright")
        self.ToolRegCloneTiktok.addTab(self.home, "")
        self.settings = QWidget()
        self.settings.setObjectName("settings")
        self.password_reg_account = QLabel(parent=self.settings)
        self.password_reg_account.setGeometry(QRect(20, 20, 151, 21))
        self.password_reg_account.setStyleSheet(
            'font: 700 10pt "Segoe UI";\n' 'font: 11pt "Sans Serif Collection";'
        )
        self.password_reg_account.setObjectName("password_reg_account")
        self.password_reg_account_value = QLineEdit(parent=self.settings)
        self.password_reg_account_value.setGeometry(QRect(170, 20, 161, 21))
        self.password_reg_account_value.setObjectName("password_reg_account_value")
        self.label = QLabel(parent=self.settings)
        self.label.setGeometry(QRect(20, 70, 49, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.chome_setting = QGroupBox(parent=self.settings)
        self.chome_setting.setGeometry(QRect(20, 70, 491, 151))
        self.chome_setting.setStyleSheet('font: 700 10pt "Segoe UI";')
        self.chome_setting.setObjectName("chome_setting")
        self.chrome_setting_line = QLabel(parent=self.chome_setting)
        self.chrome_setting_line.setGeometry(QRect(10, 30, 151, 21))
        self.chrome_setting_line.setObjectName("chrome_setting_line")
        self.chrome_setting_line_value = QComboBox(parent=self.chome_setting)
        self.chrome_setting_line_value.setGeometry(QRect(170, 31, 68, 21))
        self.chrome_setting_line_value.setObjectName("chrome_setting_line_value")
        self.chrome_setting_line_value.addItem("")
        self.chrome_setting_line_value.addItem("")
        self.chrome_setting_line_value.addItem("")
        self.chrome_setting_line_value.addItem("")
        self.chrome_setting_line_value.addItem("")
        self.chrome_setting_line_value.addItem("")
        self.chrome_setting_line_value.addItem("")
        self.chrome_setting_line_value.addItem("")
        self.chrome_setting_line_value.addItem("")
        self.chrome_setting_line_value.addItem("")
        self.chrome_setting_radio = QLabel(parent=self.chome_setting)
        self.chrome_setting_radio.setGeometry(QRect(10, 70, 171, 16))
        self.chrome_setting_radio.setObjectName("chrome_setting_radio")
        self.chrome_setting_radio_yes = QRadioButton(parent=self.chome_setting)
        self.chrome_setting_radio_yes.setGeometry(QRect(200, 70, 41, 20))
        self.chrome_setting_radio_yes.setObjectName("chrome_setting_radio_yes")
        self.chrome_setting_radio_no = QRadioButton(parent=self.chome_setting)
        self.chrome_setting_radio_no.setGeometry(QRect(250, 70, 71, 20))
        self.chrome_setting_radio_no.setObjectName("chrome_setting_radio_no")
        self.file_mail_check = QPushButton(parent=self.settings)
        self.file_mail_check.setGeometry(QRect(20, 240, 131, 24))
        self.file_mail_check.setIcon(icon3)
        self.file_mail_check.setObjectName("file_mail_check")
        self.file_mail_check_value = QLineEdit(parent=self.settings)
        self.file_mail_check_value.setGeometry(QRect(160, 240, 261, 21))
        self.file_mail_check_value.setObjectName("file_mail_check_value")
        self.btn_check = QPushButton(parent=self.settings)
        self.btn_check.setGeometry(QRect(430, 240, 81, 24))
        self.btn_check.setStyleSheet(
            'font: 700 10pt "Segoe UI";\n'
            "color: #fff;\n"
            "background-color:rgb(64, 170, 15);\n"
            ""
        )
        self.btn_check.setObjectName("btn_check")
        self.mail_success = QLabel(parent=self.settings)
        self.mail_success.setGeometry(QRect(550, 220, 61, 16))
        self.mail_success.setStyleSheet(
            'font: 700 10pt "Segoe UI";\n' "color: rgb(0, 170, 54);"
        )
        self.mail_success.setObjectName("mail_success")
        self.mail_success_box = QTextEdit(parent=self.settings)
        self.mail_success_box.setGeometry(QRect(550, 240, 191, 281))
        self.mail_success_box.setStyleSheet("border: 1px solid rgb(0, 170, 54);")
        self.mail_success_box.setObjectName("mail_success_box")
        self.mail_failed = QLabel(parent=self.settings)
        self.mail_failed.setGeometry(QRect(790, 220, 61, 16))
        self.mail_failed.setStyleSheet(
            'font: 700 10pt "Segoe UI";\n' "color: rgb(255, 0, 0);"
        )
        self.mail_failed.setObjectName("mail_failed")
        self.mail_failed_box = QTextEdit(parent=self.settings)
        self.mail_failed_box.setGeometry(QRect(790, 240, 191, 281))
        self.mail_failed_box.setStyleSheet("border: 1px solid rgb(255, 0, 0);")
        self.mail_failed_box.setObjectName("mail_failed_box")
        self.ToolRegCloneTiktok.addTab(self.settings, "")
        ToolRegCloneTiktok.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(parent=ToolRegCloneTiktok)
        self.statusbar.setObjectName("statusbar")
        ToolRegCloneTiktok.setStatusBar(self.statusbar)

        self.retranslateUi(ToolRegCloneTiktok)
        self.ToolRegCloneTiktok.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(ToolRegCloneTiktok)

        # handle logic tab 1
        self.start.clicked.connect(self.startAutomation)
        self.threads_value.valueChanged.connect(self.checkThreadsValue)
        self.list_avatar.clicked.connect(self.selectAvatarFolder)
        self.list_mail.clicked.connect(self.inputMail)
        self.captcha_key.textChanged.connect(self.getCaptchaKey)
        self.import_proxy.clicked.connect(self.importProxy)

        # handle logic tab 2
        self.file_mail_check.clicked.connect(self.inputMailCheck)

        ToolRegCloneTiktok.setStatusBar(self.statusbar)

        self.table_account_info.setColumnWidth(0, 200)
        self.table_account_info.setColumnWidth(1, 100)
        self.table_account_info.setColumnWidth(2, 180)
        self.table_account_info.setColumnWidth(3, 200)
        self.table_account_info.setColumnWidth(4, 160)

    def startAutomation(self):
        num_threads = self.threads_value.value()
        self.automation_threads = []

        for thread in range(num_threads):
            automation_thread = AutomationThread(thread)
            self.automation_threads.append(automation_thread)
            automation_thread.start()

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

    def processMailContent(self, mail_content):
        accounts = []
        for line in mail_content.splitlines():
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

    def inputMailCheck(self):
        self.fileNameCheck = QFileDialog.getOpenFileName(
            None, "Open File", "", "(*.txt)"
        )[0]
        self.file_mail_check_value.setText(self.fileNameCheck)
        if self.fileNameCheck:
            mail_content = self.readMailFile(self.fileNameCheck)
            self.content_file_mail_check = mail_content

    def retranslateUi(self, ToolRegCloneTiktok):
        _translate = QCoreApplication.translate
        ToolRegCloneTiktok.setWindowTitle(
            _translate("ToolRegCloneTiktok", "ToolRegCloneTiktok")
        )
        self.mail_value.setText(_translate("ToolRegCloneTiktok", "hotmail.txt"))
        self.list_avatar.setText(_translate("ToolRegCloneTiktok", " Folder Avatar"))
        self.list_proxy.setText(_translate("ToolRegCloneTiktok", "List Proxy"))
        self.start.setWhatsThis(
            _translate(
                "ToolRegCloneTiktok", "<html><head/><body><p><br/></p></body></html>"
            )
        )
        self.start.setText(_translate("ToolRegCloneTiktok", "Start"))
        self.export_excel.setText(_translate("ToolRegCloneTiktok", "Export excel"))
        self.import_proxy.setText(_translate("ToolRegCloneTiktok", "Import"))
        self.stop.setText(_translate("ToolRegCloneTiktok", "Stop"))
        self.threads.setText(_translate("ToolRegCloneTiktok", "Threads"))
        self.table_account_info.setSortingEnabled(False)
        item = self.table_account_info.horizontalHeaderItem(0)
        item.setText(_translate("ToolRegCloneTiktok", "username"))
        item = self.table_account_info.horizontalHeaderItem(1)
        item.setText(_translate("ToolRegCloneTiktok", "password"))
        item = self.table_account_info.horizontalHeaderItem(2)
        item.setText(_translate("ToolRegCloneTiktok", "passMail"))
        item = self.table_account_info.horizontalHeaderItem(3)
        item.setText(_translate("ToolRegCloneTiktok", "cookie"))
        item = self.table_account_info.horizontalHeaderItem(4)
        item.setText(_translate("ToolRegCloneTiktok", "proxy"))
        item = self.table_account_info.horizontalHeaderItem(5)
        item.setText(_translate("ToolRegCloneTiktok", "status"))
        self.avatar_value.setText(_translate("ToolRegCloneTiktok", "C://images"))
        self.omocaptcha.setText(_translate("ToolRegCloneTiktok", "omocaptcha.com"))
        self.list_mail.setText(_translate("ToolRegCloneTiktok", " List mail"))
        self.export_excel.setText(_translate("ToolRegCloneTiktok", "Export excel"))
        self.list_proxy.setText(_translate("ToolRegCloneTiktok", "List Proxy"))
        self.link_facebook.setText(
            _translate("ToolRegCloneTiktok", "https://www.facebook.com/100093720346445")
        )
        self.phone.setText(_translate("ToolRegCloneTiktok", "037.527.0513"))
        self.hotline.setText(_translate("ToolRegCloneTiktok", "Hotline:"))
        self.copyright.setText(
            _translate("ToolRegCloneTiktok", "© Bản quyền thuộc về Long Software")
        )
        self.ToolRegCloneTiktok.setTabText(
            self.ToolRegCloneTiktok.indexOf(self.home),
            _translate("ToolRegCloneTiktok", "Home"),
        )
        self.password_reg_account.setText(
            _translate("ToolRegCloneTiktok", "Mật khẩu account reg:")
        )
        self.chome_setting.setTitle(
            _translate("ToolRegCloneTiktok", "Thiết lập chrome")
        )
        self.chrome_setting_line.setText(
            _translate("ToolRegCloneTiktok", "Số chrome trên 1 dòng:")
        )
        self.chrome_setting_line_value.setItemText(
            0, _translate("ToolRegCloneTiktok", "1")
        )
        self.chrome_setting_line_value.setItemText(
            1, _translate("ToolRegCloneTiktok", "2")
        )
        self.chrome_setting_line_value.setItemText(
            2, _translate("ToolRegCloneTiktok", "3")
        )
        self.chrome_setting_line_value.setItemText(
            3, _translate("ToolRegCloneTiktok", "4")
        )
        self.chrome_setting_line_value.setItemText(
            4, _translate("ToolRegCloneTiktok", "5")
        )
        self.chrome_setting_line_value.setItemText(
            5, _translate("ToolRegCloneTiktok", "6")
        )
        self.chrome_setting_line_value.setItemText(
            6, _translate("ToolRegCloneTiktok", "7")
        )
        self.chrome_setting_line_value.setItemText(
            7, _translate("ToolRegCloneTiktok", "8")
        )
        self.chrome_setting_line_value.setItemText(
            8, _translate("ToolRegCloneTiktok", "9")
        )
        self.chrome_setting_line_value.setItemText(
            9, _translate("ToolRegCloneTiktok", "10")
        )
        self.chrome_setting_radio.setText(
            _translate("ToolRegCloneTiktok", "Chạy mà không mở chrome:")
        )
        self.chrome_setting_radio_yes.setText(_translate("ToolRegCloneTiktok", "Có"))
        self.chrome_setting_radio_no.setText(_translate("ToolRegCloneTiktok", "Không"))
        self.file_mail_check.setText(
            _translate("ToolRegCloneTiktok", "File Mail cần check")
        )
        self.btn_check.setText(_translate("ToolRegCloneTiktok", "Check"))
        self.mail_success.setText(_translate("ToolRegCloneTiktok", "Live Mail:"))
        self.mail_failed.setText(_translate("ToolRegCloneTiktok", "Die Mail"))
        self.ToolRegCloneTiktok.setTabText(
            self.ToolRegCloneTiktok.indexOf(self.settings),
            _translate("ToolRegCloneTiktok", "Settings"),
        )


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ToolRegCloneTiktok = QMainWindow()
    ui = Ui_ToolRegCloneTiktok()
    ui.setupUi(ToolRegCloneTiktok)
    ToolRegCloneTiktok.show()
    sys.exit(app.exec())
