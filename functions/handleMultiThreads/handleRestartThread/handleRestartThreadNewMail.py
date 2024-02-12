from PySide6.QtWidgets import *
from PySide6.QtCore import *
from utils.utils import wait
# from functions.database.updateMail import updateMail

def handleRestartThreadNewMail(self):
    self.self_main.chrome_threads[self.num_threads].quit()
    self.self_main.chrome_threads[self.num_threads].wait()
    wait(4, 6)
    self.self_main.table_account_info.setItem(
        self.current_row_count,
        3,
        QTableWidgetItem("Bị chặn, đợi restart lại..."),
    )
    QCoreApplication.processEvents()
    # updateMail(self.username_mail, False)
    self.self_main.restart_thread(self.num_threads)