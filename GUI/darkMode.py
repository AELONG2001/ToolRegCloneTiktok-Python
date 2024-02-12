def darkMode(self):
    background_element_dark_mode = "#636e72"
    self.change_theme_switch_off.setVisible(False)
    self.change_theme_switch_on.setVisible(True)
    self.stop_button.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}")
    self.threads_value.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.table_account_info.setStyleSheet(f"color: green; background-color: #dfe6e9")
    self.list_avatar.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.avatar_value.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.list_video.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.video_value.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.list_mail.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.mail_value.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.captcha_type.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.captcha_key.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.proxy_type.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.proxy_value.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.proxy_value_ip_port.setStyleSheet(f"color: #fff;")
    self.proxy_value_ip_port_user_pass.setStyleSheet(f"color: #fff;")
    self.random_password_account.setStyleSheet("color: #fff")
    self.password_reg_account_value.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.setting_tool.setStyleSheet("color: #fff")
    self.list_username.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.list_username_value.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.chrome_setting_line_value.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.chrome_percent_zoom_value.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.chrome_delay_second_value.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.database_value.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.export_account_format_value.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.type_reg_country.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.file_mail_check.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.file_mail_check_value.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}")
    self.mail_success_box.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}; border: 1px solid rgb(0, 170, 54);")
    self.mail_failed_box.setStyleSheet(f"color: #fff; background-color: {background_element_dark_mode}; border: 1px solid rgb(255, 0, 0);")
    stylesheet = """ 
    QTabBar::tab:selected {color: '#fff'; background: '#636e72';}
    QTabWidget QStackedWidget {
    background: #000;
    }

    QTabWidget QStackedWidget QLabel {
        color: #fff;
    }
    """
    self.ToolRegCloneTiktok.setStyleSheet(stylesheet)