from PySide6.QtWidgets import *
from PySide6.QtCore import *
from functions.profilesGologin.handleDeleteProfile import handleDeleteProfile
import os
import shutil
from utils.utils import wait

def handleRestartThread(self):
    wait(4, 6)
    if os.path.exists(self.profile_fullpath):
        shutil.rmtree(self.profile_fullpath)
    handleDeleteProfile(self.profile_id)
    self.self_main.table_account_info.setItem(
        self.current_row_count,
        3,
        QTableWidgetItem("Bị chặn, đợi restart lại..."),
    )
    QCoreApplication.processEvents()
    self.self_main.restart_thread(self.num_threads, self.username_mail, self.password_mail)