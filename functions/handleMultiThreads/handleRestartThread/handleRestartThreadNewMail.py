from PySide6.QtWidgets import *
from PySide6.QtCore import *
from functions.profilesGologin.handleDeleteProfile import handleDeleteProfile
from utils.utils import wait

def handleRestartThreadNewMail(self):
    wait(4, 6)
    self.self_main.table_account_info.setItem(
        self.current_row_count,
        3,
        QTableWidgetItem("Bị chặn, đợi restart lại..."),
    )
    QCoreApplication.processEvents()
    self.self_main.restart_thread(self.num_threads, "", "")