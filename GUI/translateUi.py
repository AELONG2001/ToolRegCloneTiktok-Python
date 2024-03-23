from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import json

def translateUi(self, ToolRegCloneTiktok):
   _translate = QCoreApplication.translate
   ToolRegCloneTiktok.setWindowTitle(
      _translate("ToolRegCloneTiktok", f"ToolRegCloneTiktok - By Long Software")
   )
   self.mail_value.setText(_translate("ToolRegCloneTiktok", ""))
   self.list_avatar.setText(_translate("ToolRegCloneTiktok", " Folder Avatar"))
   self.list_video.setText(_translate("ToolRegCloneTiktok", " Folder Video"))
   self.start_button.setWhatsThis(
      _translate(
         "ToolRegCloneTiktok", "<html><head/><body><p><br/></p></body></html>"
      )
   )
   self.start_button.setText(_translate("ToolRegCloneTiktok", "Bắt đầu"))
   self.proxy_value_ip_port.setText(_translate("ToolRegCloneTiktok", "ip:port"))
   self.proxy_value_ip_port_user_pass.setText(_translate("ToolRegCloneTiktok", "ip:port:user:pass"))
   self.proxy_value_check_live_ip_port.setText(_translate("ToolRegCloneTiktok", "ip:port"))
   self.proxy_value_check_live_ip_port_user_pass.setText(_translate("ToolRegCloneTiktok", "ip:port:user:pass"))
   self.stop_button.setText(_translate("ToolRegCloneTiktok", "Kết thúc"))
   self.threads.setText(_translate("ToolRegCloneTiktok", "Số luồng:"))
   self.table_account_info.setSortingEnabled(False)
   item = self.table_account_info.horizontalHeaderItem(0)
   item.setText(_translate("ToolRegCloneTiktok", "Username"))

   item = self.table_account_info.horizontalHeaderItem(1)
   item.setText(_translate("ToolRegCloneTiktok", "Password"))

   item = self.table_account_info.horizontalHeaderItem(2)
   item.setText(_translate("ToolRegCloneTiktok", "Proxy"))

   item = self.table_account_info.horizontalHeaderItem(3)
   item.setText(_translate("ToolRegCloneTiktok", "Status"))

   item = self.table_account_info.horizontalHeaderItem(4)
   item.setText(_translate("ToolRegCloneTiktok", "Job"))

   item = self.table_account_info.horizontalHeaderItem(5)
   item.setText(_translate("ToolRegCloneTiktok", "Xu nhận"))

   item = self.table_account_info.horizontalHeaderItem(6)
   item.setText(_translate("ToolRegCloneTiktok", "Tổng xu"))
   
   self.avatar_value.setText(_translate("ToolRegCloneTiktok", "C://images"))
   self.captcha_type.setItemText(0, _translate("ToolRegCloneTiktok", "Achicaptcha"))
   self.captcha_type.setItemText(1, _translate("ToolRegCloneTiktok", "Omocaptcha"))
   self.captcha_type.setItemText(2, _translate("ToolRegCloneTiktok", "CaptchaGuru"))
   self.proxy_type.setItemText(0, _translate("ToolRegCloneTiktok", "ShopLike"))
   self.proxy_type.setItemText(1, _translate("ToolRegCloneTiktok", "TM Proxy"))
   self.proxy_type.setItemText(2, _translate("ToolRegCloneTiktok", "Tin Proxy"))
   self.proxy_type.setItemText(3, _translate("ToolRegCloneTiktok", "Proxy No 1"))
   self.proxy_type.setItemText(4, _translate("ToolRegCloneTiktok", "HTTP Proxy"))
   self.proxy_type.setItemText(5, _translate("ToolRegCloneTiktok", "SOCKS5 Proxy"))
   self.proxy_type_check_live.setItemText(0, _translate("ToolRegCloneTiktok", "ShopLike"))
   self.proxy_type_check_live.setItemText(1, _translate("ToolRegCloneTiktok", "TM Proxy"))
   self.proxy_type_check_live.setItemText(2, _translate("ToolRegCloneTiktok", "Tin Proxy"))
   self.proxy_type_check_live.setItemText(3, _translate("ToolRegCloneTiktok", "Proxy No 1"))
   self.proxy_type_check_live.setItemText(4, _translate("ToolRegCloneTiktok", "HTTP Proxy"))
   self.proxy_type_check_live.setItemText(5, _translate("ToolRegCloneTiktok", "SOCKS5 Proxy"))

   self.list_mail.setText(_translate("ToolRegCloneTiktok", "Nhập accounts"))
   self.export_account.setText(_translate("ToolRegCloneTiktok", "Xuất tài khoản"))
   # self.update_label.setText(_translate("ToolRegCloneTiktok", "Đã có phiên bản mới, cập nhập ngay...."))
   # self.update_button.setText(_translate("ToolRegCloneTiktok", "Cập nhập"))
   self.list_proxy.setText(_translate("ToolRegCloneTiktok", "Proxys:"))
   self.list_proxy_check_live.setText(_translate("ToolRegCloneTiktok", "Proxys:"))
   # self.total_success_account.setText(
   #      _translate("ToolRegCloneTiktok", f"Số acc đã tạo thành công: 0")
   # )
   self.copyright.setText(
        _translate("ToolRegCloneTiktok", "© Bản quyền thuộc về longsoftware.vn")
   )
   self.ToolRegCloneTiktok.setTabText(
      self.ToolRegCloneTiktok.indexOf(self.home),
      _translate("ToolRegCloneTiktok", "Home"),
   )
   self.password_reg_account.setText(
      _translate("ToolRegCloneTiktok", "Mật khẩu account reg:")
   )
   self.random_password_account.setText(_translate("ToolRegCloneTiktok", "random"))
   self.is_change_username.setText(
      _translate("ToolRegCloneTiktok", "Đổi tên khi reg")
   )
   self.is_watch_live_label.setText(
      _translate("ToolRegCloneTiktok", "Xem Live")
   )
   self.is_upload_avatar_label.setText(
      _translate("ToolRegCloneTiktok", "Upload Avatar")
   )
   self.is_upload_video_label.setText(
      _translate("ToolRegCloneTiktok", "Upload Video")
   )
   self.is_run_tds_label.setText(
      _translate("ToolRegCloneTiktok", "Run TDS")
   )
   self.is_login_google_label.setText(
      _translate("ToolRegCloneTiktok", "Login google")
   )
   self.is_login_cookie_label.setText(
      _translate("ToolRegCloneTiktok", "Login Cookie")
   )
   self.change_theme.setText(
      _translate("ToolRegCloneTiktok", "DarkMode")
   )
   self.is_change_username_by_file.setText(
      _translate("ToolRegCloneTiktok", "Đổi tên khi reg theo file:")
   )
   self.list_username.setText(_translate("ToolRegCloneTiktok", "Nhập file"))
   self.list_username_value.setText(_translate("ToolRegCloneTiktok", ""))
   self.setting_tool.setTitle(_translate("ToolRegCloneTiktok", "Thiết lập thông số"))
   self.chrome_setting_line.setText(
      _translate("ToolRegCloneTiktok", "Số chrome trên 1 dòng:")
   )
   self.chrome_percent_zoom.setText(
      _translate("ToolRegCloneTiktok", "Tỉ lệ Zoom chrome:")
   )

   self.file_mail_check.setText(
      _translate("ToolRegCloneTiktok", "Nhập Mail cần check")
   )
   self.file_accounts_check.setText(
      _translate("ToolRegCloneTiktok", "Nhập File Accounts cần check")
   )
   self.chrome_delay_seconed.setText(
      _translate("ToolRegCloneTiktok", "Số giây delay sau mỗi thread:")
   )
   self.database.setText(_translate("ToolRegCloneTiktok", "Database:"))
   self.export_account_format.setText(_translate("ToolRegCloneTiktok", "Định dạng xuất accounts:"))
   self.export_account_format_value.setItemText(0, _translate("ToolRegCloneTiktok", "id | pass | mail | passMail | coookie | date"))
   self.export_account_format_value.setItemText(1, _translate("ToolRegCloneTiktok", "id | pass | mail | passMail | date"))
   self.export_account_format_value.setItemText(2, _translate("ToolRegCloneTiktok", "id | pass | mail | passMail | cookie"))
   self.export_account_format_value.setItemText(3, _translate("ToolRegCloneTiktok", "id | pass | mail | passMail"))
   self.export_account_format_value.setItemText(4, _translate("ToolRegCloneTiktok", "id | pass"))
   self.type_reg_country_label.setText(_translate("ToolRegCloneTiktok", "Chọn nước Reg:"))
   self.type_reg_country.setItemText(0, _translate("ToolRegCloneTiktok", "Việt Nam"))
   self.type_reg_country.setItemText(1, _translate("ToolRegCloneTiktok", "US"))
   self.btn_check.setText(_translate("ToolRegCloneTiktok", "Check"))
   self.btn_check_accounts.setText(_translate("ToolRegCloneTiktok", "Check"))
   self.note_mail.setText(_translate("ToolRegCloneTiktok", "Chú ý: Mail Live sẽ được tự thêm vào file mail"))
   self.note_accounts.setText(_translate("ToolRegCloneTiktok", "Chú ý:\n+ Accounts Live sẽ được tự thêm vào file LiveAccounts.txt\n+ Accouns Die sẽ được tự thêm vào file DieAccounts.txt\n+ File output sẽ bị xóa hết dữ liệu, dữ liệu sẽ được backup sang file output_backup.txt"))
   self.mail_success.setText(_translate("ToolRegCloneTiktok", "Live Mail:"))
   self.mail_failed.setText(_translate("ToolRegCloneTiktok", "Die Mail"))
   self.live_accounts.setText(_translate("ToolRegCloneTiktok", "Live:"))
   self.die_accounts.setText(_translate("ToolRegCloneTiktok", "Die:"))
   self.ToolRegCloneTiktok.setTabText(
      self.ToolRegCloneTiktok.indexOf(self.settings),
      _translate("ToolRegCloneTiktok", "Cài đặt"),
   )
   self.ToolRegCloneTiktok.setTabText(
      self.ToolRegCloneTiktok.indexOf(self.check_live),
      _translate("ToolRegCloneTiktok", "Check Live"),
   )

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

   if "url_video" in data: 
      self.video_value.setText(data["url_video"])
   else:
      self.video_value.setText("C://videos")

   if "url_mail" in data:
      self.mail_value.setText(data["url_mail"])
   else:
      self.mail_value.setText("")

   if "is_watch_live" in data:
      if data["is_watch_live"]:
         self.is_watch_live.setChecked(True)
      else:
         self.is_watch_live.setChecked(False)
   else:
      self.is_upload_avatar.setChecked(False)

   if "is_upload_avatar" in data:
      if data["is_upload_avatar"]:
         self.is_upload_avatar.setChecked(True)
      else:
         self.is_upload_avatar.setChecked(False)
   else:
      self.is_upload_avatar.setChecked(False)

   if "is_upload_video" in data:
      if data["is_upload_video"]:
         self.is_upload_video.setChecked(True)
      else:
         self.is_upload_video.setChecked(False)
   else:
      self.is_upload_video.setChecked(False)

   if "is_run_tds" in data:
      if data["is_run_tds"]:
         self.is_run_tds.setChecked(True)
      else:
         self.is_run_tds.setChecked(False)
   else:
      self.is_run_tds.setChecked(False)

   if "is_login_google" in data:
      if data["is_login_google"]:
         self.is_login_google.setChecked(True)
      else:
         self.is_login_google.setChecked(False)
   else:
      self.is_login_google.setChecked(False)

   if "is_login_cookie" in data:
      if data["is_login_cookie"]:
         self.is_login_cookie.setChecked(True)
      else:
         self.is_login_cookie.setChecked(False)
   else:
      self.is_login_cookie.setChecked(False)

   if "captcha_type" in data:
      self.captcha_type.setCurrentIndex(data["captcha_type"])
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

   if "proxys_check_live" in data:
      self.proxy_value_check_live.setPlainText("\n".join(data["proxys_check_live"]))
   else:
      self.proxy_value_check_live.setPlainText("")

   if "proxy_type" in data:
      self.proxy_type.setCurrentIndex(data["proxy_type"])
   else:
      self.proxy_type.setCurrentIndex(0)

   if "proxy_type_check_live" in data:
      self.proxy_type_check_live.setCurrentIndex(data["proxy_type_check_live"])
   else:
      self.proxy_type_check_live.setCurrentIndex(0)

   if "is_proxy_ip_port" in data:
      if data["is_proxy_ip_port"]:
         self.proxy_value_ip_port.setChecked(True)
      else:
         self.proxy_value_ip_port_user_pass.setChecked(True)
   else:
      self.proxy_value_ip_port.setChecked(True)

   if "is_proxy_ip_port_check_live" in data:
      if data["is_proxy_ip_port_check_live"]:
         self.proxy_value_check_live_ip_port.setChecked(True)
      else:
         self.proxy_value_check_live_ip_port_user_pass.setChecked(True)
   else:
      self.proxy_value_check_live_ip_port.setChecked(True)
   
   if "password_account" in data:
      self.password_reg_account_value.setText(data["password_account"])
   else:
      self.password_reg_account_value.setText("")

   if "random_password_account" in data:
      if data["random_password_account"]:
         self.random_password_account.setChecked(True)
      else:
         self.random_password_account.setChecked(False)
   else:
      self.random_password_account.setChecked(True)

   if "is_change_username_check" in data:
      if data["is_change_username_check"]:
         self.is_change_username_check.setChecked(True)
      else:
         self.is_change_username_check.setChecked(False)
   else:
      self.is_change_username_check.setChecked(True)

   if "url_username" in data:
      self.list_username_value.setText(data["url_username"])
   else:
      self.list_username_value.setText("")

   if "darkmode" in data:
      if data["darkmode"]:
        self.change_theme_switch_off.setVisible(False)
        self.change_theme_switch_on.setVisible(True)
      else:
        self.change_theme_switch_off.setVisible(True)
        self.change_theme_switch_on.setVisible(False)
   else:
      self.change_theme_switch_off.setVisible(True)
      self.change_theme_switch_on.setVisible(False)

   if "is_chrome_count" in data:
      self.chrome_setting_line_value.setValue(data["is_chrome_count"])
   else:
      self.chrome_setting_line_value.setValue(10)

   if "chrome_percent_zoom" in data:
      self.chrome_percent_zoom_value.setValue(data["chrome_percent_zoom"])
   else:
      self.chrome_percent_zoom_value.setValue(0.37)

   if "chromeValueDelay" in data:
      self.chrome_delay_second_value.setValue(data["chromeValueDelay"])
   else:
      self.chrome_delay_second_value.setValue(3)

   if "database_value" in data:
      self.database_value.setText(data["database_value"])
   else:
      self.database_value.setText("")

   if "type_reg_country" in data:
      self.type_reg_country.setCurrentIndex(data["type_reg_country"])
   else:
      self.type_reg_country.setCurrentIndex(0)

   if "typeExportAccount" in data:
      self.export_account_format_value.setCurrentIndex(data["typeExportAccount"])
   else:
      self.export_account_format_value.setCurrentIndex(0)

   if "url_mail_check" in data:
      self.file_mail_check_value.setText(data["url_mail_check"])
   else:
      self.file_mail_check_value.setText("")

   if "url_accounts_check" in data:
      self.file_accounts_check_value.setText(data["url_accounts_check"])
   else:
      self.file_accounts_check_value.setText("")

   