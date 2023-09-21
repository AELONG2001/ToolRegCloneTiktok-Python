from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


def translateUi(self, ToolRegCloneTiktok):
    _translate = QCoreApplication.translate
    ToolRegCloneTiktok.setWindowTitle(
        _translate("ToolRegCloneTiktok", "ToolRegCloneTiktok")
    )
    self.mail_value.setText(_translate("ToolRegCloneTiktok", "hotmail.txt"))
    self.list_avatar.setText(_translate("ToolRegCloneTiktok", " Folder Avatar"))
    self.list_proxy.setText(_translate("ToolRegCloneTiktok", "List Proxy"))
    self.start_button.setWhatsThis(
        _translate(
            "ToolRegCloneTiktok", "<html><head/><body><p><br/></p></body></html>"
        )
    )
    self.start_button.setText(_translate("ToolRegCloneTiktok", "Bắt đầu"))
    self.export_account.setText(_translate("ToolRegCloneTiktok", "Xuất tài khoản"))
    self.import_proxy.setText(_translate("ToolRegCloneTiktok", "Nhập"))
    self.stop_button.setText(_translate("ToolRegCloneTiktok", "Kết thúc"))
    self.threads.setText(_translate("ToolRegCloneTiktok", "Số luồng:"))
    self.threads_value.setValue(3)
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

    self.list_mail.setText(_translate("ToolRegCloneTiktok", " List mail"))
    self.export_account.setText(_translate("ToolRegCloneTiktok", "Xuất tài khoản"))
    self.list_proxy.setText(_translate("ToolRegCloneTiktok", "List Proxy"))
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
    self.chome_setting.setTitle(_translate("ToolRegCloneTiktok", "Thiết lập chrome"))
    self.chrome_setting_line.setText(
        _translate("ToolRegCloneTiktok", "Số chrome trên 1 dòng:")
    )
    self.chrome_setting_line_value.setItemText(0, _translate("ToolRegCloneTiktok", "1"))
    self.chrome_setting_line_value.setItemText(1, _translate("ToolRegCloneTiktok", "2"))
    self.chrome_setting_line_value.setItemText(2, _translate("ToolRegCloneTiktok", "3"))
    self.chrome_setting_line_value.setItemText(3, _translate("ToolRegCloneTiktok", "4"))
    self.chrome_setting_line_value.setItemText(4, _translate("ToolRegCloneTiktok", "5"))
    self.chrome_setting_line_value.setItemText(5, _translate("ToolRegCloneTiktok", "6"))
    self.chrome_setting_line_value.setItemText(6, _translate("ToolRegCloneTiktok", "7"))
    self.chrome_setting_line_value.setItemText(7, _translate("ToolRegCloneTiktok", "8"))
    self.chrome_setting_line_value.setItemText(8, _translate("ToolRegCloneTiktok", "9"))
    self.chrome_setting_line_value.setItemText(
        9, _translate("ToolRegCloneTiktok", "10")
    )
    self.chrome_setting_line_value.setCurrentText("10")
    self.chrome_setting_radio.setText(
        _translate("ToolRegCloneTiktok", "Mở chrome khi chạy:")
    )
    self.chrome_setting_radio_yes.setText(_translate("ToolRegCloneTiktok", "Có"))
    self.chrome_setting_radio_no.setText(_translate("ToolRegCloneTiktok", "Không"))
    self.chrome_percent_zoom.setText(
        _translate("ToolRegCloneTiktok", "Tỉ lệ Zoom chrome:")
    )
    self.chrome_delay_minute_value.setItemText(0, _translate("ToolRegCloneTiktok", "1"))
    self.chrome_delay_minute_value.setItemText(1, _translate("ToolRegCloneTiktok", "2"))
    self.chrome_delay_minute_value.setItemText(2, _translate("ToolRegCloneTiktok", "3"))
    self.chrome_delay_minute_value.setItemText(3, _translate("ToolRegCloneTiktok", "4"))
    self.chrome_delay_minute_value.setItemText(4, _translate("ToolRegCloneTiktok", "5"))
    self.chrome_delay_minute_value.setItemText(5, _translate("ToolRegCloneTiktok", "6"))
    self.chrome_delay_minute_value.setItemText(6, _translate("ToolRegCloneTiktok", "7"))
    self.chrome_delay_minute_value.setItemText(7, _translate("ToolRegCloneTiktok", "8"))
    self.chrome_delay_minute_value.setItemText(8, _translate("ToolRegCloneTiktok", "9"))
    self.chrome_delay_minute_value.setItemText(
        9, _translate("ToolRegCloneTiktok", "10")
    )
    self.chrome_delay_minute_value.setCurrentText("3")

    self.file_mail_check.setText(
        _translate("ToolRegCloneTiktok", "File Mail cần check")
    )
    self.chrome_delay_minute.setText(
        _translate("MainWindow", "Số phút delay sau mỗi thread")
    )
    self.btn_check.setText(_translate("ToolRegCloneTiktok", "Check"))
    self.mail_success.setText(_translate("ToolRegCloneTiktok", "Live Mail:"))
    self.mail_failed.setText(_translate("ToolRegCloneTiktok", "Die Mail"))
    self.ToolRegCloneTiktok.setTabText(
        self.ToolRegCloneTiktok.indexOf(self.settings),
        _translate("ToolRegCloneTiktok", "Settings"),
    )
