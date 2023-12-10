def lightMode(self):
    background_element_dark_mode = "#fff"
    border_element_dark_mode = "#636e72"
    self.change_theme_switch_on.setVisible(False)
    self.change_theme_switch_off.setVisible(True)
    self.stop_button.setStyleSheet(f"color: #000; background-color: rgba(0, 0, 0, 0.2)")
    self.random_password_account.setStyleSheet("color: #000")
    self.is_upload_avatar_yes.setStyleSheet("color: #000")
    self.is_upload_avatar_no.setStyleSheet("color: #000")
    self.setting_tool.setStyleSheet("color: #000")
    self.chrome_setting_line_value.setStyleSheet("color: #000")
    self.chrome_percent_zoom_value.setStyleSheet("color: #000")
    self.chrome_delay_second_value.setStyleSheet("color: #000")
    self.api_token_gologin_value.setStyleSheet("color: #000")
    self.path_gologin_value.setStyleSheet("color: #000")
    self.api_hotmailbox_value.setStyleSheet("color: #000")
    self.export_account_format_value.setStyleSheet("color: #000")
    self.type_reg_country.setStyleSheet("color: #000")
    self.threads_value.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid {border_element_dark_mode}")
    self.table_account_info.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}")
    self.list_avatar.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid {border_element_dark_mode}")
    self.avatar_value.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid {border_element_dark_mode}")
    self.list_mail.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid {border_element_dark_mode}")
    self.mail_value.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid {border_element_dark_mode}")
    self.captcha_type.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid {border_element_dark_mode}")
    self.captcha_key.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid {border_element_dark_mode}")
    self.proxy_type.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid {border_element_dark_mode}")
    self.proxy_value.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid {border_element_dark_mode}")
    self.proxy_value_ip_port.setStyleSheet(f"color: #000;")
    self.proxy_value_ip_port_user_pass.setStyleSheet(f"color: #000;")
    self.password_reg_account_value.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}")
    self.list_username.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid {border_element_dark_mode}")
    self.list_username_value.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}")
    self.api_token_gologin_value.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}")
    self.path_gologin_value.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}")
    self.api_hotmailbox_value.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}")
    self.export_account_format_value.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid {border_element_dark_mode}")
    self.type_reg_country.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid {border_element_dark_mode}")
    self.file_mail_check.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid {border_element_dark_mode}")
    self.file_mail_check_value.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}")
    self.mail_success_box.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid rgb(0, 170, 54);")
    self.mail_failed_box.setStyleSheet(f"color: #000; background-color: {background_element_dark_mode}; border: 1px solid rgb(255, 0, 0);")
    stylesheet = """ 
    QTabBar::tab:selected {color: '#000'; background: '#fff';}
    QTabWidget QStackedWidget {
    background: #fff;
    }

    QTabWidget QStackedWidget QLabel {
        color: #000;
    }
    """
    self.ToolRegCloneTiktok.setStyleSheet(stylesheet)