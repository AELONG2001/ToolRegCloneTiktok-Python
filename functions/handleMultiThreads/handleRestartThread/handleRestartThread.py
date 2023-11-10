from PySide6.QtWidgets import *
from functions.profilesGologin.handleDeleteProfile import (
    handleDeleteProfile,
)

def handleRestartThread(self):
    self.driver.quit()
    handleDeleteProfile(self.profile_id)
    self.self_main.table_account_info.setItem(
        self.current_row_count,
        3,
        QTableWidgetItem("Bị chặn, đợi restart lại..."),
    )
    self.self_main.restart_thread(self.num_threads, self.username_mail, self.password_mail)