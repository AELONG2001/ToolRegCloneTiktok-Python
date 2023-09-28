import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

def uiMain(self, ToolRegCloneTiktok):
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
    self.mail_value.setReadOnly(True)
    self.mail_value.setObjectName("mail_value")
    self.list_avatar = QPushButton(parent=self.home)
    self.list_avatar.setGeometry(QRect(340, 10, 121, 24))
    icon = QIcon()
    icon.addPixmap(
        QPixmap(".\\icons/logo_tiktok.png"),
        QIcon.Mode.Normal,
        QIcon.State.Off,
    )
    ToolRegCloneTiktok.setWindowIcon(icon)
    icon.addPixmap(
        QPixmap(".\\icons/folder.png"),
        QIcon.Mode.Normal,
        QIcon.State.Off,
    )
    self.list_avatar.setIcon(icon)
    self.list_avatar.setObjectName("list_avatar")
    self.captcha_key = QLineEdit(parent=self.home)
    self.captcha_key.setGeometry(QRect(1348, 80, 141, 20))
    self.captcha_key.setObjectName("captcha_key")
    self.start_button = QPushButton(parent=self.home)
    self.start_button.setGeometry(QRect(10, 10, 91, 24))
    self.start_button.setMouseTracking(False)
    self.start_button.setStyleSheet(
        "color:rgb(255, 252, 252);\n" "background-color:rgb(64, 170, 15)"
    )
    icon1 = QIcon()
    icon1.addPixmap(
        QPixmap(".\\icons/play-button.png"),
        QIcon.Mode.Normal,
        QIcon.State.Off,
    )
    self.start_button.setIcon(icon1)
    self.start_button.setAutoRepeat(False)
    self.start_button.setObjectName("start_button")
    self.start_button.setCursor(Qt.CursorShape.PointingHandCursor)
    self.threads_value = QSpinBox(parent=self.home)
    self.threads_value.setGeometry(QRect(280, 10, 51, 22))
    font = QFont()
    font.setBold(True)
    font.setStrikeOut(False)
    font.setKerning(False)
    self.threads_value.setFont(font)
    self.threads_value.setProperty("value", 1)
    self.threads_value.setObjectName("threads_value")
    self.export_account = QPushButton(parent=self.home)
    self.export_account.setGeometry(QRect(1536, 80, 75, 21))
    self.export_account.setStyleSheet(
        "color:#fff;\n" "background-color: rgb(19, 170, 24);"
    )
    self.export_account.setObjectName("export_account")
    self.check_proxy = QPushButton(parent=self.home)
    self.check_proxy.setGeometry(QRect(1150, 420, 61, 31))
    self.check_proxy.setStyleSheet(
        'font: 700 10pt "Segoe UI";\n'
        "color: #fff;\n"
        "background-color:rgb(64, 170, 15);\n"
        ""
    )
    self.check_proxy.setObjectName("import_proxy")
    self.stop_button = QPushButton(parent=self.home)
    self.stop_button.setGeometry(QRect(110, 10, 91, 24))
    self.stop_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")
    self.stop_button.setCursor(Qt.CursorShape.PointingHandCursor)
    icon2 = QIcon()
    icon2.addPixmap(
        QPixmap(
            ".\\icons/pause-button.png"
        ),
        QIcon.Mode.Normal,
        QIcon.State.Off,
    )
    self.stop_button.setIcon(icon2)
    self.stop_button.setObjectName("stop_button")
    self.threads = QLabel(parent=self.home)
    self.threads.setGeometry(QRect(210, 10, 80, 21))
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
    self.table_account_info.setRowCount(0)
    self.table_account_info.setObjectName("table_account_info")
    self.table_account_info.setColumnCount(4)
    item = QTableWidgetItem()
    self.table_account_info.setHorizontalHeaderItem(0, item)
    item = QTableWidgetItem()
    self.table_account_info.setHorizontalHeaderItem(1, item)
    item = QTableWidgetItem()
    self.table_account_info.setHorizontalHeaderItem(2, item)
    item = QTableWidgetItem()
    self.table_account_info.setHorizontalHeaderItem(3, item)
    self.table_account_info.horizontalHeader().setVisible(True)
    self.table_account_info.horizontalHeader().setCascadingSectionResizes(False)
    self.avatar_value = QLineEdit(parent=self.home)
    self.avatar_value.setGeometry(QRect(470, 10, 113, 21))
    self.avatar_value.setObjectName("avatar_value")
    self.avatar_value.setReadOnly(True)
    self.captcha_type = QComboBox(parent=self.home)
    self.captcha_type.setObjectName("comboBox")
    self.captcha_type.setGeometry(QRect(860, 10, 101, 21))
    self.captcha_type.addItem("")
    self.captcha_type.addItem("")
    self.list_mail = QPushButton(parent=self.home)
    self.list_mail.setGeometry(QRect(590, 10, 121, 24))
    icon3 = QIcon()
    icon3.addPixmap(
        QPixmap(".\\icons/list-mail.png"),
        QIcon.Mode.Normal,
        QIcon.State.Off,
    )
    self.list_mail.setIcon(icon3)
    self.list_mail.setObjectName("list_mail")
    self.captcha_key = QLineEdit(parent=self.home)
    self.captcha_key.setGeometry(QRect(970, 10, 141, 20))
    self.captcha_key.setObjectName("captcha_key")
    self.export_account = QPushButton(parent=self.home)
    self.export_account.setGeometry(QRect(1130, 10, 100, 21))
    self.export_account.setStyleSheet(
        "color:#fff;\n" "background-color: rgb(19, 170, 24);"
    )
    self.export_account.setObjectName("export_account")
    self.list_proxy = QLabel(parent=self.home)
    self.list_proxy.setGeometry(QRect(920, 50, 61, 41))
    self.list_proxy.setStyleSheet('font: 700 10pt "Segoe UI";')
    self.list_proxy.setObjectName("list_proxy")
    self.proxy_type = QComboBox(parent=self.home)
    self.proxy_type.setGeometry(QRect(970, 60, 121, 22))
    self.proxy_type.setObjectName("proxy_type")
    self.proxy_type.addItem("")
    self.proxy_type.addItem("")
    self.proxy_type.addItem("")
    self.proxy_type.addItem("")
    self.proxy_value = QPlainTextEdit(parent=self.home)
    self.proxy_value.setGeometry(QRect(920, 90, 211, 361))
    self.proxy_value.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
    self.proxy_value.setPlainText("")
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
    icon4 = QIcon()
    icon4.addPixmap(
        QPixmap(".\\icons/facebook.png"),
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
    self.password_reg_account_value.setGeometry(QRect(170, 20, 405, 21))
    self.password_reg_account_value.setPlaceholderText("Mật khẩu phải bao gồm ít nhất 8 ký tự bao gồm chữ, số và ký tự đặc biệt,...")
    self.password_reg_account_value.setObjectName("check_rule_password_account")
    self.check_rule_password_account = QLabel(parent=self.settings)
    self.check_rule_password_account.setGeometry(QRect(170, 40, 405, 21))
    self.check_rule_password_account.setStyleSheet(
        'color: "#d93025"'
    )
    self.check_rule_password_account.setObjectName("check_rule_password_account")
    self.check_rule_password_account.setText("")
    self.random_password_account = QCheckBox(parent=self.settings)
    self.random_password_account.setGeometry(QRect(585, 20, 72, 20))
    self.random_password_account.setStyleSheet("font: 600 10pt \"Segoe UI\";")
    self.random_password_account.setObjectName("random_password_account")
    self.random_password_account.setChecked(True)
    self.label = QLabel(parent=self.settings)
    self.label.setGeometry(QRect(20, 70, 49, 16))
    self.label.setObjectName("label")
    self.setting_tool = QGroupBox(parent=self.settings)
    self.setting_tool.setGeometry(QRect(20, 70, 1221, 151))
    self.setting_tool.setStyleSheet('font: 700 10pt "Segoe UI";')
    self.setting_tool.setObjectName("setting_tool")
    self.chrome_setting_line = QLabel(parent=self.setting_tool)
    self.chrome_setting_line.setGeometry(QRect(10, 30, 151, 21))
    self.chrome_setting_line.setObjectName("chrome_setting_line")
    self.chrome_setting_line_value = QSpinBox(parent=self.setting_tool)
    self.chrome_setting_line_value.setGeometry(QRect(170, 31, 50, 20))
    self.chrome_setting_line_value.setStyleSheet("font: 10pt \"Segoe UI\";")
    self.chrome_setting_line_value.setProperty("value", 1)
    self.chrome_setting_line_value.setObjectName("chrome_setting_line_value")
    self.chrome_percent_zoom = QLabel(parent=self.setting_tool)
    self.chrome_percent_zoom.setGeometry(QRect(10, 70, 121, 21))
    self.chrome_percent_zoom.setObjectName("chrome_percent_zoom")
    self.chrome_percent_zoom_value = QDoubleSpinBox(parent=self.setting_tool)
    self.chrome_percent_zoom_value.setGeometry(QRect(140, 70, 61, 22))
    self.chrome_percent_zoom_value.setStyleSheet("font: 10pt \"Segoe UI\";")
    self.chrome_percent_zoom_value.setObjectName("chrome_percent_zoom_value")
    self.chrome_percent_zoom_value.setValue(1)
    self.chrome_delay_minute = QLabel(parent=self.setting_tool)
    self.chrome_delay_minute.setGeometry(QRect(10, 110, 181, 21))
    self.chrome_delay_minute.setObjectName("chrome_delay_minute")
    self.chrome_delay_minute_value = QSpinBox(parent=self.setting_tool)
    self.chrome_delay_minute_value.setGeometry(QRect(200, 110, 50, 20))
    self.chrome_delay_minute_value.setStyleSheet("font: 10pt \"Segoe UI\";")
    self.chrome_delay_minute_value.setProperty("value", 1)
    self.chrome_delay_minute_value.setObjectName("chrome_delay_minute_value")
    self.api_token_gologin = QLabel(parent=self.setting_tool)
    self.api_token_gologin.setGeometry(QRect(380, 30, 121, 21))
    self.api_token_gologin.setObjectName("api_token_gologin")
    self.api_token_gologin_value =QLineEdit(parent=self.setting_tool)
    self.api_token_gologin_value.setGeometry(QRect(510, 30, 161, 21))
    self.api_token_gologin_value.setStyleSheet("font: 10pt \"Segoe UI\";")
    self.api_token_gologin_value.setObjectName("api_token_gologin_value")
    self.path_gologin = QLabel(parent=self.setting_tool)
    self.path_gologin.setGeometry(QRect(380, 70, 91, 21))
    self.path_gologin.setObjectName("path_gologin")
    self.path_gologin_value = QLineEdit(parent=self.setting_tool)
    self.path_gologin_value.setGeometry(QRect(470, 70, 201, 21))
    self.path_gologin_value.setStyleSheet("font: 10pt \"Segoe UI\";")
    self.path_gologin_value.setObjectName("path_gologin_value")
    self.api_hotmailbox =QLabel(parent=self.setting_tool)
    self.api_hotmailbox.setGeometry(QRect(380, 110, 111, 21))
    self.api_hotmailbox.setObjectName("api_hotmailbox")
    self.api_hotmailbox_value =QLineEdit(parent=self.setting_tool)
    self.api_hotmailbox_value.setGeometry(QRect(490, 110, 181, 21))
    self.api_hotmailbox_value.setStyleSheet("font: 10pt \"Segoe UI\";")
    self.api_hotmailbox_value.setObjectName("api_hotmailbox_value")
    self.export_account_format =QLabel(parent=self.setting_tool)
    self.export_account_format.setGeometry(QRect(800, 30, 161, 21))
    self.export_account_format.setObjectName("export_account_format")
    self.export_account_format_value =QComboBox(parent=self.setting_tool)
    self.export_account_format_value.setGeometry(QRect(970, 30, 231, 22))
    self.export_account_format_value.setStyleSheet("font: 9pt \"Segoe UI\";")
    self.export_account_format_value.setObjectName("export_account_format_value")
    self.export_account_format_value.addItem("")
    self.export_account_format_value.addItem("")
    self.export_account_format_value.addItem("")
    self.is_upload_avatar =QLabel(parent=self.setting_tool)
    self.is_upload_avatar.setGeometry(QRect(800, 70, 101, 16))
    self.is_upload_avatar.setObjectName("is_upload_avatar")
    self.is_upload_avatar_yes =QRadioButton(parent=self.setting_tool)
    self.is_upload_avatar_yes.setGeometry(QRect(900, 70, 41, 21))
    self.is_upload_avatar_yes.setStyleSheet("font: 10pt \"Segoe UI\";")
    self.is_upload_avatar_yes.setObjectName("is_upload_avatar_yes")
    self.is_upload_avatar_yes.setChecked(True)
    self.is_upload_avatar_no =QRadioButton(parent=self.setting_tool)
    self.is_upload_avatar_no.setGeometry(QRect(950, 70, 71, 21))
    self.is_upload_avatar_no.setStyleSheet("font: 10pt \"Segoe UI\";")
    self.is_upload_avatar_no.setObjectName("is_upload_avatar_no")
    self.file_mail_check = QPushButton(parent=self.settings)
    self.file_mail_check.setGeometry(QRect(20, 240, 131, 24))
    self.file_mail_check.setIcon(icon3)
    self.file_mail_check.setObjectName("file_mail_check")
    self.file_mail_check_value = QLineEdit(parent=self.settings)
    self.file_mail_check_value.setGeometry(QRect(160, 240, 261, 21))
    self.file_mail_check_value.setObjectName("file_mail_check_value")
    self.file_mail_check_value.setReadOnly(True)
    self.btn_check = QPushButton(parent=self.settings)
    self.btn_check.setGeometry(QRect(430, 240, 120, 24))
    self.btn_check.setStyleSheet(
        'font: 700 10pt "Segoe UI";\n'
        "color: #fff;\n"
        "background-color:rgb(64, 170, 15);\n"
        ""
    )
    self.btn_check.setObjectName("btn_check")
    self.loading_icon = QLabel(parent=self.settings)
    self.loading_icon.setGeometry(QRect(528, 246, 14, 14))
    self.loading_icon.setText("abc")
    relative_path = "icons/loading.gif"
    absolute_path = os.path.abspath(relative_path)
    self.loadingMovie = QMovie(absolute_path)
    self.loading_icon.setMovie(self.loadingMovie)
    self.loading_icon.setObjectName("loading_icon")

    self.loading_icon.setVisible(False)
    
    self.mail_success = QLabel(parent=self.settings)
    self.mail_success.setGeometry(QRect(580, 240, 100, 16))
    self.mail_success.setStyleSheet(
        'font: 700 10pt "Segoe UI";\n' "color: rgb(0, 170, 54);"
    )
    self.mail_success.setObjectName("mail_success")
    self.mail_success_box = QTextEdit(parent=self.settings)
    self.mail_success_box.setGeometry(QRect(580, 260, 271, 260))
    self.mail_success_box.setStyleSheet("border: 1px solid rgb(0, 170, 54);")
    self.mail_success_box.setObjectName("mail_success_box")
    self.mail_failed = QLabel(parent=self.settings)
    self.mail_failed.setGeometry(QRect(890, 240, 100, 16))
    self.mail_failed.setStyleSheet(
        'font: 700 10pt "Segoe UI";\n' "color: rgb(255, 0, 0);"
    )
    self.mail_failed.setObjectName("mail_failed")
    self.mail_failed_box = QTextEdit(parent=self.settings)
    self.mail_failed_box.setGeometry(QRect(890, 260, 271, 260))
    self.mail_failed_box.setStyleSheet("border: 1px solid rgb(255, 0, 0);")
    self.mail_failed_box.setObjectName("mail_failed_box")
    self.ToolRegCloneTiktok.addTab(self.settings, "")
    ToolRegCloneTiktok.setCentralWidget(self.centralwidget)
    self.statusbar = QStatusBar(parent=ToolRegCloneTiktok)
    self.statusbar.setObjectName("statusbar")
    ToolRegCloneTiktok.setStatusBar(self.statusbar)

    self.retranslateUi(ToolRegCloneTiktok)
    self.ToolRegCloneTiktok.setCurrentIndex(0)
    QMetaObject.connectSlotsByName(ToolRegCloneTiktok)

    # handle logic tab 1
    self.start_button.clicked.connect(self.start)
    self.stop_button.clicked.connect(self.stop)
    self.threads_value.valueChanged.connect(self.checkThreadsValue)
    self.list_avatar.clicked.connect(self.handleAvatarFolderSelection)
    self.list_mail.clicked.connect(self.inputMail)
    self.captcha_type.currentTextChanged.connect(self.getCaptchaType)
    self.captcha_key.textChanged.connect(self.getCaptchaKey)
    self.export_account.clicked.connect(self.exportAccount)
    self.check_proxy.clicked.connect(self.importProxy)
    self.password_reg_account_value.textChanged.connect(self.getDefaultPassword)
    self.random_password_account.toggled.connect(self.checkRandomPassword)
    self.chrome_setting_line_value.valueChanged.connect(self.getIsChromeCount)
    self.chrome_percent_zoom_value.valueChanged.connect(self.getChromePercentZoom)
    self.chrome_delay_minute_value.valueChanged.connect(self.getChromeValueDelay)
    self.api_token_gologin_value.textChanged.connect(self.getTokenGologin)
    self.path_gologin_value.textChanged.connect(self.getPathGologin)
    self.api_hotmailbox_value.textChanged.connect(self.getValueApiHotmailbox)
    self.is_upload_avatar_yes.toggled.connect(self.checkIsUploadAvatar)
    self.export_account_format_value.currentTextChanged.connect(self.getTypeExportAccount)
    self.proxy_type.currentTextChanged.connect(self.getProxyType)

    # handle logic tab 2
    self.file_mail_check.clicked.connect(self.inputMailCheck)
    self.btn_check.clicked.connect(self.handleCheckMail)

    self.chrome_threads = []
    self.max_thread_count = 30
    self.threadpool = QThreadPool.globalInstance()
    self.threadpool.setMaxThreadCount(self.max_thread_count)

    ToolRegCloneTiktok.setStatusBar(self.statusbar)

    self.table_account_info.setColumnWidth(0, 220)
    self.table_account_info.setColumnWidth(1, 120)
    self.table_account_info.setColumnWidth(2, 220)
    self.table_account_info.setColumnWidth(3, 280)
