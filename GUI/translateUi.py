from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os
import json

def translateUi(self, ToolRegCloneTiktok):
    _translate = QCoreApplication.translate
    ToolRegCloneTiktok.setWindowTitle(
        _translate("ToolRegCloneTiktok", "ToolRegCloneTiktok")
    )
    self.mail_value.setText(_translate("ToolRegCloneTiktok", "hotmail.txt"))
    self.list_avatar.setText(_translate("ToolRegCloneTiktok", " Folder Avatar"))
    self.start_button.setWhatsThis(
        _translate(
            "ToolRegCloneTiktok", "<html><head/><body><p><br/></p></body></html>"
        )
    )
    self.start_button.setText(_translate("ToolRegCloneTiktok", "Bắt đầu"))
    self.check_proxy.setText(_translate("ToolRegCloneTiktok", "Check"))
    self.stop_button.setText(_translate("ToolRegCloneTiktok", "Kết thúc"))
    self.threads.setText(_translate("ToolRegCloneTiktok", "Số luồng:"))
    self.table_account_info.setSortingEnabled(False)
    item = self.table_account_info.horizontalHeaderItem(0)
    item.setText(_translate("ToolRegCloneTiktok", "username"))
    item = self.table_account_info.horizontalHeaderItem(1)
    item.setText(_translate("ToolRegCloneTiktok", "passMail"))
    item = self.table_account_info.horizontalHeaderItem(2)
    item.setText(_translate("ToolRegCloneTiktok", "proxy"))
    item = self.table_account_info.horizontalHeaderItem(3)
    item.setText(_translate("ToolRegCloneTiktok", "status"))
    self.avatar_value.setText(_translate("ToolRegCloneTiktok", "C://images"))
    self.captcha_type.setItemText(0, _translate("ToolRegCloneTiktok", "Achicaptcha"))
    self.captcha_type.setItemText(1, _translate("ToolRegCloneTiktok", "Omocaptcha"))
    self.proxy_type.setItemText(0, _translate("MainWindow", "TM Proxy"))
    self.proxy_type.setItemText(1, _translate("MainWindow", "HTTP Proxy"))
    self.proxy_type.setItemText(2, _translate("MainWindow", "SOCKS5 Proxy"))

    self.list_mail.setText(_translate("ToolRegCloneTiktok", " List mail"))
    self.export_account.setText(_translate("ToolRegCloneTiktok", "Xuất tài khoản"))
    self.list_proxy.setText(_translate("ToolRegCloneTiktok", "Proxys:"))
    self.link_facebook.setText(
        _translate("ToolRegCloneTiktok", "https://www.facebook.com/longkata2001")
    )
    self.phone.setText(_translate("ToolRegCloneTiktok", "037.527.0513"))
    self.hotline.setText(_translate("ToolRegCloneTiktok", "Hotline:"))
    # self.copyright.setText(
    #     _translate("ToolRegCloneTiktok", "© Bản quyền thuộc về Long Software")
    # )
    self.ToolRegCloneTiktok.setTabText(
        self.ToolRegCloneTiktok.indexOf(self.home),
        _translate("ToolRegCloneTiktok", "Home"),
    )
    self.password_reg_account.setText(
        _translate("ToolRegCloneTiktok", "Mật khẩu account reg:")
    )
    self.password_reg_account_value.setText(_translate("MainWindow", "Abc123@"))
    self.setting_tool.setTitle(_translate("ToolRegCloneTiktok", "Thiết lập thông số"))
    self.chrome_setting_line.setText(
        _translate("ToolRegCloneTiktok", "Số chrome trên 1 dòng:")
    )
    self.chrome_percent_zoom.setText(
        _translate("ToolRegCloneTiktok", "Tỉ lệ Zoom chrome:")
    )
   

    self.file_mail_check.setText(
        _translate("ToolRegCloneTiktok", "File Mail cần check")
    )
    self.chrome_delay_minute.setText(
        _translate("MainWindow", "Số phút delay sau mỗi thread:")
    )
    self.api_token_gologin.setText(_translate("MainWindow", "API Token Gologin:"))
    self.is_upload_avatar.setText(_translate("MainWindow", "Upload avatar:"))
    self.is_upload_avatar_yes.setText(_translate("MainWindow", "Có"))
    self.is_upload_avatar_no.setText(_translate("MainWindow", "Không"))
    self.api_hotmailbox.setText(_translate("MainWindow", "API Hotmailbox:"))
    self.export_account_format.setText(_translate("MainWindow", "Định dạng xuất accounts:"))
    self.export_account_format_value.setItemText(0, _translate("MainWindow", "mail | passMail | passAccount | cookie"))
    self.export_account_format_value.setItemText(1, _translate("MainWindow", "mail | passMail | passAccount"))
    self.export_account_format_value.setItemText(2, _translate("MainWindow", "maill | passAccount"))
    self.btn_check.setText(_translate("ToolRegCloneTiktok", "Check"))
    self.mail_success.setText(_translate("ToolRegCloneTiktok", "Live Mail:"))
    self.mail_failed.setText(_translate("ToolRegCloneTiktok", "Die Mail"))
    self.ToolRegCloneTiktok.setTabText(
        self.ToolRegCloneTiktok.indexOf(self.settings),
        _translate("ToolRegCloneTiktok", "Settings"),
    )

    if os.path.exists("config_accounts.json"):
        with open("config_accounts.json", "r") as json_file:
            data = json.load(json_file)

        self.threads_value.setValue(data["num_threads"])
        self.avatar_value.setText(data["url_avatar"])
        self.mail_value.setText(data["url_mail"])
        self.captcha_type.setCurrentIndex(data["captcha_type"] - 1)
        self.captcha_key.setText(data["captcha_key"])
        self.proxy_value.setPlainText("\n".join(data["proxys"]))
        self.password_reg_account_value.setText(data["default_password"])
        self.chrome_setting_line_value.setValue(data["is_chrome_count"])
        self.chrome_percent_zoom_value.setValue(data["chrome_percent_zoom"])
        self.chrome_delay_minute_value.setValue(data["chromeValueDelay"])
        self.api_token_gologin_value.setText(data["api_token_gologin"])
        self.api_hotmailbox_value.setText(data["api_value_hotmailbox"])

        if data["is_upload_avatar"]:
          self.is_upload_avatar_yes.setChecked(True)
        else:
          self.is_upload_avatar_no.setChecked(True)        

        self.export_account_format_value.setCurrentIndex(data["typeExportAccount"] - 1)

        self.file_mail_check_value.setText(data["url_mail_check"])

        

    else:
        self.threads_value.setValue(1)
