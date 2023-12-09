import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import json

def uiMain(self, ToolRegCloneTiktok):
    ToolRegCloneTiktok.setObjectName("ToolRegCloneTiktok")
    ToolRegCloneTiktok.resize(1256, 546)
    self.centralwidget = QWidget(parent=ToolRegCloneTiktok)
    self.centralwidget.setObjectName("centralwidget")
    self.ToolRegCloneTiktok = QTabWidget(parent=self.centralwidget)
    self.ToolRegCloneTiktok.setGeometry(QRect(0, 0, 1301, 1079))
    self.ToolRegCloneTiktok.setObjectName("ToolRegCloneTiktok")
    screen_geometry = QGuiApplication.primaryScreen().geometry()
    x = (screen_geometry.width() - ToolRegCloneTiktok.width()) / 2
    y = (screen_geometry.height() - ToolRegCloneTiktok.height()) / 2
    ToolRegCloneTiktok.move(x, y)

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
    self.table_account_info.setGeometry(QRect(10, 60, 860, 391))
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
    # self.captcha_type.setCurrentIndex(0)
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
    self.update_label = QLabel(parent=self.home)
    self.update_label.setGeometry(QRect(10, 50, 240, 21))
    self.update_label.setStyleSheet('font: 600 10pt "Segoe UI";')
    self.update_label.setObjectName("update_label")

    self.update_button = QPushButton(parent=self.home)
    self.update_button.setGeometry(250, 50, 100, 28)
    self.update_button.clicked.connect(self.update)
    self.update_button.setEnabled(True)
    self.update_button.setStyleSheet(
        "color: white; background-color: rgb(64, 170, 50);"
    )

   
    self.list_proxy = QLabel(parent=self.home)
    self.list_proxy.setGeometry(QRect(900, 50, 61, 41))
    self.list_proxy.setStyleSheet('font: 700 10pt "Segoe UI";')
    self.list_proxy.setObjectName("list_proxy")
    self.proxy_type = QComboBox(parent=self.home)
    self.proxy_type.setGeometry(QRect(950, 60, 121, 22))
    self.proxy_type.setObjectName("proxy_type")
    self.proxy_type.addItem("")
    self.proxy_type.addItem("")
    self.proxy_type.addItem("")
    self.proxy_type.addItem("")
    self.proxy_value = QPlainTextEdit(parent=self.home)
    self.proxy_value.setGeometry(QRect(900, 90, 211, 361))
    self.proxy_value.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
    self.proxy_value.setPlainText("")
    self.proxy_value.setPlaceholderText("Mỗi Api key một dòng")
    self.proxy_value_ip_port =QRadioButton(parent=self.home)
    self.proxy_value_ip_port.setGeometry(QRect(1120, 380, 60, 31))
    self.proxy_value_ip_port.setStyleSheet("font: 10pt \"Segoe UI\";")
    self.proxy_value_ip_port.setObjectName("proxy_value_ip_port")
    self.proxy_value_ip_port.setChecked(True)
    self.proxy_value_ip_port_user_pass =QRadioButton(parent=self.home)
    self.proxy_value_ip_port_user_pass.setGeometry(QRect(1120, 400, 124, 31))
    self.proxy_value_ip_port_user_pass.setStyleSheet("font: 10pt \"Segoe UI\";")
    self.proxy_value_ip_port_user_pass.setObjectName("proxy_value_ip_port_user_pass")
    self.proxy_value_ip_port.setVisible(False)
    self.proxy_value_ip_port_user_pass.setVisible(False)
    # self.proxy_value_ip_port_user_pass.setDisabled(True)
    self.hint = QLabel(parent=self.home)
    self.hint.setGeometry(QRect(10, 465, 500, 16))
    self.hint.setStyleSheet('font: 700 10pt "Segoe UI";')
    self.hint.setObjectName("hint")
    self.copyright = QLabel(parent=self.home)
    self.copyright.setGeometry(QRect(790, 465, 250, 16))
    self.copyright.setStyleSheet('font: 700 10pt "Segoe UI";')
    self.copyright.setObjectName("copyright")
    
    # self.check_proxy = QPushButton(parent=self.home)
    # self.check_proxy.setGeometry(QRect(1125, 420, 60, 30))
    # self.check_proxy.setStyleSheet(
    #     'font: 700 10pt "Segoe UI";\n'
    #     "color: #fff;\n"
    #     "background-color:rgb(64, 170, 15);\n"
    #     ""
    # )
    # self.check_proxy.setObjectName("import_proxy")
    # self.loading_icon_check_proxy = QLabel(parent=self.home)
    # self.loading_icon_check_proxy.setGeometry(QRect(1208, 461, 60, 30))
    # self.loading_icon_check_proxy.setText("abc")
    # relative_path_check_proxy = "icons/loading.gif"
    # absolute_path_check_proxy = os.path.abspath(relative_path_check_proxy)
    # self.loadingMovieCheckProxy = QMovie(absolute_path_check_proxy)
    # self.loading_icon_check_proxy.setMovie(self.loadingMovieCheckProxy)
    # self.loading_icon_check_proxy.setObjectName("loading_icon_check_proxy")
    # self.loading_icon_check_proxy.setVisible(False)

    if self.current_version == self.latest_version:
        self.update_label.hide()
        self.update_button.hide()
    else:
        ToolRegCloneTiktok.resize(1256, 573)
        self.table_account_info.setGeometry(QRect(10, 100, 860, 391))
        self.list_proxy.setGeometry(QRect(900, 85, 61, 41))
        self.proxy_type.setGeometry(QRect(950, 95, 121, 22))
        self.proxy_value.setGeometry(QRect(900, 130, 211, 361))
        self.hint.setGeometry(QRect(10, 500, 500, 16))
        self.copyright.setGeometry(QRect(790, 500, 250, 16))

    
    if os.path.exists("configs_account.json"):
        with open("configs_account.json", "r") as json_file:
                data = json.load(json_file)

        if "proxy_type" in data:
            if data["proxy_type"] == 2 or data["proxy_type"] == 3:
                self.proxy_value_ip_port.setVisible(True)
                self.proxy_value_ip_port_user_pass.setVisible(True)
            else:
                self.proxy_value_ip_port.setVisible(False)
                self.proxy_value_ip_port_user_pass.setVisible(False)

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
    self.ToolRegCloneTiktok.addTab(self.home, "")
    self.settings = QWidget()
    self.settings.setObjectName("settings")
    self.password_reg_account = QLabel(parent=self.settings)
    self.password_reg_account.setGeometry(QRect(20, 20, 151, 21))
    self.password_reg_account.setStyleSheet(
        'font: 600 10pt "Segoe UI";'
    )
    self.password_reg_account.setObjectName("password_reg_account")
    self.password_reg_account_value = QLineEdit(parent=self.settings)
    self.password_reg_account_value.setGeometry(QRect(160, 20, 180, 21))
    self.password_reg_account_value.setPlaceholderText("8 ký tự chữ, số và ký tự đặc biệt")
    self.password_reg_account_value.setObjectName("check_rule_password_account")
    self.check_rule_password_account = QLabel(parent=self.settings)
    self.check_rule_password_account.setGeometry(QRect(160, 40, 260, 21))
    self.check_rule_password_account.setStyleSheet(
        'color: "#d93025"'
    )
    self.check_rule_password_account.setObjectName("check_rule_password_account")
    self.check_rule_password_account.setText("")
    self.random_password_account = QCheckBox(parent=self.settings)
    self.random_password_account.setGeometry(QRect(354, 22, 72, 20))
    self.random_password_account.setStyleSheet("font: 600 10pt \"Segoe UI\";")
    self.random_password_account.setObjectName("random_password_account")
    self.random_password_account.setChecked(True)
    self.is_change_username = QLabel(parent=self.settings)
    self.is_change_username.setGeometry(QRect(500, 20, 100, 21))
    self.is_change_username.setStyleSheet(
        'font: 600 10pt "Segoe UI";'
    )
    self.is_change_username.setObjectName("is_change_username")
    self.is_change_username_check = QCheckBox(parent=self.settings)
    self.is_change_username_check.setGeometry(QRect(596, 22, 72, 20))
    self.is_change_username_check.setStyleSheet("font: 600 10pt \"Segoe UI\";")
    self.is_change_username_check.setObjectName("is_change_username_check")
    self.is_change_username_check.setChecked(True)
    self.is_change_username_by_file = QLabel(parent=self.settings)
    self.is_change_username_by_file.setGeometry(QRect(680, 20, 150, 21))
    self.is_change_username_by_file.setStyleSheet(
        'font: 600 10pt "Segoe UI";'
    )
    self.is_change_username_by_file.setObjectName("is_change_username_by_file")
    self.list_username = QPushButton(parent=self.settings)
    self.list_username.setGeometry(QRect(832, 20, 121, 24))
    icon3 = QIcon()
    icon3.addPixmap(
        QPixmap(".\\icons/txt-file.png"),
        QIcon.Mode.Normal,
        QIcon.State.Off,
    )
    self.list_username.setIcon(icon3)
    self.list_username.setObjectName("list_username")
    self.list_username_value = QLineEdit(parent=self.settings)
    self.list_username_value.setGeometry(QRect(960, 21, 150, 21))
    self.list_username_value.setReadOnly(True)
    self.list_username_value.setObjectName("list_username_value")
    self.label = QLabel(parent=self.settings)
    self.label.setGeometry(QRect(20, 70, 49, 16))
    self.label.setObjectName("label")
    self.setting_tool = QGroupBox(parent=self.settings)
    self.setting_tool.setGeometry(QRect(20, 70, 1221, 151))
    self.setting_tool.setStyleSheet('font: 600 10pt "Segoe UI";')
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
    self.chrome_delay_seconed = QLabel(parent=self.setting_tool)
    self.chrome_delay_seconed.setGeometry(QRect(10, 110, 181, 21))
    self.chrome_delay_seconed.setObjectName("chrome_delay_seconed")
    self.chrome_delay_second_value = QSpinBox(parent=self.setting_tool)
    self.chrome_delay_second_value.setGeometry(QRect(200, 110, 50, 20))
    self.chrome_delay_second_value.setStyleSheet("font: 10pt \"Segoe UI\";")
    self.chrome_delay_second_value.setProperty("value", 1)
    self.chrome_delay_second_value.setObjectName("chrome_delay_second_value")
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
    self.export_account_format.setGeometry(QRect(780, 30, 161, 21))
    self.export_account_format.setObjectName("export_account_format")
    self.export_account_format_value =QComboBox(parent=self.setting_tool)
    self.export_account_format_value.setGeometry(QRect(950, 30, 250, 22))
    self.export_account_format_value.setStyleSheet("font: 9pt \"Segoe UI\";")
    self.export_account_format_value.setObjectName("export_account_format_value")
    self.export_account_format_value.addItem("")
    self.export_account_format_value.addItem("")
    self.export_account_format_value.addItem("")
    self.export_account_format_value.addItem("")
    self.export_account_format_value.addItem("")
    self.is_upload_avatar =QLabel(parent=self.setting_tool)
    self.is_upload_avatar.setGeometry(QRect(780, 70, 101, 16))
    self.is_upload_avatar.setObjectName("is_upload_avatar")
    self.is_upload_avatar_yes =QRadioButton(parent=self.setting_tool)
    self.is_upload_avatar_yes.setGeometry(QRect(880, 70, 41, 21))
    self.is_upload_avatar_yes.setStyleSheet("font: 10pt \"Segoe UI\";")
    self.is_upload_avatar_yes.setObjectName("is_upload_avatar_yes")
    self.is_upload_avatar_yes.setChecked(True)
    self.is_upload_avatar_no =QRadioButton(parent=self.setting_tool)
    self.is_upload_avatar_no.setGeometry(QRect(920, 70, 71, 21))
    self.is_upload_avatar_no.setStyleSheet("font: 10pt \"Segoe UI\";")
    self.is_upload_avatar_no.setObjectName("is_upload_avatar_no")
    self.type_reg_country_label =QLabel(parent=self.setting_tool)
    self.type_reg_country_label.setGeometry(QRect(780, 110, 101, 21))
    self.type_reg_country_label.setObjectName("type_reg_country_label")
    self.type_reg_country =QComboBox(parent=self.setting_tool)
    self.type_reg_country.addItem("")
    self.type_reg_country.addItem("")
    self.type_reg_country.setGeometry(QRect(886, 109, 101, 24))
    self.type_reg_country.setObjectName("type_reg_country")
    self.file_mail_check = QPushButton(parent=self.settings)
    self.file_mail_check.setGeometry(QRect(20, 240, 140, 24))
    self.file_mail_check.setIcon(icon3)
    self.file_mail_check.setObjectName("file_mail_check")
    self.file_mail_check_value = QLineEdit(parent=self.settings)
    self.file_mail_check_value.setGeometry(QRect(170, 240, 261, 21))
    self.file_mail_check_value.setObjectName("file_mail_check_value")
    self.file_mail_check_value.setReadOnly(True)
    self.btn_check = QPushButton(parent=self.settings)
    self.btn_check.setGeometry(QRect(440, 240, 75, 24))
    self.btn_check.setStyleSheet(
        'font: 700 10pt "Segoe UI";\n'
        "color: #fff;\n"
        "background-color:rgb(64, 170, 15);\n"
        ""
    )
    self.btn_check.setObjectName("btn_check")
    self.loading_icon_check_mail = QLabel(parent=self.settings)
    self.loading_icon_check_mail.setGeometry(QRect(538, 246, 14, 14))
    self.loading_icon_check_mail.setText("abc")
    relative_path_check_mail = "icons/loading.gif"
    absolute_path_check_mail = os.path.abspath(relative_path_check_mail)
    self.loadingMovieCheckMail = QMovie(absolute_path_check_mail)
    self.loading_icon_check_mail.setMovie(self.loadingMovieCheckMail)
    self.loading_icon_check_mail.setObjectName("loading_icon_check_mail")
    self.loading_icon_check_mail.setVisible(False)
    self.note_mail = QLabel(parent=self.settings)
    self.note_mail.setGeometry(QRect(20, 270, 350, 24))
    self.note_mail.setStyleSheet('font: 700 10pt "Segoe UI";')
    self.note_mail.setObjectName("note_mail")
    
    self.mail_success = QLabel(parent=self.settings)
    self.mail_success.setGeometry(QRect(580, 240, 100, 16))
    self.mail_success.setStyleSheet(
        'font: 700 10pt "Segoe UI";\n' "color: rgb(0, 170, 54);"
    )
    self.mail_success.setObjectName("mail_success")
    self.mail_success_box = QTextEdit(parent=self.settings)
    self.mail_success_box.setGeometry(QRect(580, 260, 271, 236))
    self.mail_success_box.setStyleSheet("border: 1px solid rgb(0, 170, 54);")
    self.mail_success_box.setObjectName("mail_success_box")
    self.mail_failed = QLabel(parent=self.settings)
    self.mail_failed.setGeometry(QRect(890, 240, 100, 16))
    self.mail_failed.setStyleSheet(
        'font: 700 10pt "Segoe UI";\n' "color: rgb(255, 0, 0);"
    )
    self.mail_failed.setObjectName("mail_failed")
    self.mail_failed_box = QTextEdit(parent=self.settings)
    self.mail_failed_box.setGeometry(QRect(890, 260, 271, 236))
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
    self.proxy_value.textChanged.connect(self.importProxy)
    self.proxy_value_ip_port.toggled.connect(self.checkIsProxyIpPort)
    self.password_reg_account_value.textChanged.connect(self.getDefaultPassword)
    self.random_password_account.toggled.connect(self.checkRandomPassword)
    self.is_change_username_check.toggled.connect(self.checkChangeUsername)
    self.list_username.clicked.connect(self.inputFileUsername)
    self.chrome_setting_line_value.valueChanged.connect(self.getIsChromeCount)
    self.chrome_percent_zoom_value.valueChanged.connect(self.getChromePercentZoom)
    self.chrome_delay_second_value.valueChanged.connect(self.getChromeValueDelay)
    self.api_token_gologin_value.textChanged.connect(self.getTokenGologin)
    self.path_gologin_value.textChanged.connect(self.getPathGologin)
    self.api_hotmailbox_value.textChanged.connect(self.getValueApiHotmailbox)
    self.is_upload_avatar_yes.toggled.connect(self.checkIsUploadAvatar)
    self.type_reg_country.currentTextChanged.connect(self.getRegCountryType)
    self.export_account_format_value.currentTextChanged.connect(self.getTypeExportAccount)
    self.proxy_type.currentTextChanged.connect(self.getProxyType)

    # handle logic tab 2
    self.file_mail_check.clicked.connect(self.inputMailCheck)
    self.btn_check.clicked.connect(self.handleCheckMail)

    self.chrome_threads = []
    self.max_thread_count = 20
    self.threadpool = QThreadPool.globalInstance()
    self.threadpool.setMaxThreadCount(self.max_thread_count)

    ToolRegCloneTiktok.setStatusBar(self.statusbar)

    self.table_account_info.setColumnWidth(0, 220)
    self.table_account_info.setColumnWidth(1, 120)
    self.table_account_info.setColumnWidth(2, 220)
    self.table_account_info.setColumnWidth(3, 280)
