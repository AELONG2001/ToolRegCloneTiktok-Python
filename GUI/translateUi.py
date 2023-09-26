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
    self.mail_value.setText(_translate("ToolRegCloneTiktok", ""))
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

    if os.path.exists("configs_account.json"):
        with open("configs_account.json", "r") as json_file:
            data = json.load(json_file)

        if "num_threads" in data: 
            self.threads_value.setValue(data["num_threads"])
        else:
           self.threads_value.setValue(1)

        if "url_avatar" in data: 
            self.avatar_value.setText(data["url_avatar"])
        else:
            self.avatar_value.setText("C://images")

        if "url_mail" in data:
           self.mail_value.setText(data["url_mail"])
        else:
           self.mail_value.setText("")

        if "captcha_type" in data:
          self.captcha_type.setCurrentIndex(data["captcha_type"] - 1)
        else:
          self.captcha_type.setCurrentIndex(0)

        if "captcha_key" in data:
           self.captcha_key.setText(data["captcha_key"])
        else:
           self.captcha_key.setText("")

        if "proxys" in data:
           self.proxy_value.setPlainText("\n".join(data["proxys"]))
        else:
           self.proxy_value.setPlainText("")

        if "proxy_type" in data:
           self.proxy_type.setCurrentIndex(data["proxy_type"] - 1)
        else:
           self.proxy_type.setCurrentIndex(0)
        
        
        if "default_password" in data:
           self.password_reg_account_value.setText(data["default_password"])
        else:
           self.password_reg_account_value.setText("Abc123@")

        if "is_chrome_count" in data:
           self.chrome_setting_line_value.setValue(data["is_chrome_count"])
        else:
           self.chrome_setting_line_value.setValue(10)

        if "chrome_percent_zoom" in data:
           self.chrome_percent_zoom_value.setValue(data["chrome_percent_zoom"])
        else:
           self.chrome_percent_zoom_value.setValue(0.37)

        if "chromeValueDelay" in data:
           self.chrome_delay_minute_value.setValue(data["chromeValueDelay"])
        else:
           self.chrome_delay_minute_value.setValue(3)

        if "api_token_gologin" in data:
           self.api_token_gologin_value.setText(data["api_token_gologin"])
        else:
           self.api_token_gologin_value.setText("")
        
        if "api_value_hotmailbox" in data:
            self.api_hotmailbox_value.setText(data["api_value_hotmailbox"])
        else:
           self.api_hotmailbox_value.setText("")

        if "is_upload_avatar" in data:
            if data["is_upload_avatar"]:
               self.is_upload_avatar_yes.setChecked(True)
            else:
              self.is_upload_avatar_no.setChecked(True)
        else:
            self.is_upload_avatar_yes.setChecked(True)

        if "typeExportAccount" in data:
            self.export_account_format_value.setCurrentIndex(data["typeExportAccount"] - 1)
        else:
           self.export_account_format_value.setCurrentIndex(0)

        if "url_mail_check" in data:
            self.file_mail_check_value.setText(data["url_mail_check"])
        else:
           self.file_mail_check_value.setText("")

    else:
        self.threads_value.setValue(1)
        self.avatar_value.setText("C://images")
        self.mail_value.setText("mail.txt")
        self.captcha_type.setCurrentIndex(0)
        self.captcha_key.setText("")
        self.proxy_value.setPlainText("")
        self.proxy_type.setCurrentIndex(0)
        self.password_reg_account_value.setText("Abc123@")
        self.chrome_setting_line_value.setValue(10)
        self.chrome_percent_zoom_value.setValue(0.37)
        self.chrome_delay_minute_value.setValue(3)
        self.api_token_gologin_value.setText("")
        self.api_hotmailbox_value.setText("")
        self.is_upload_avatar_yes.setChecked(True)
        self.export_account_format_value.setCurrentIndex(0)
        self.file_mail_check_value.setText("")
        