from PySide6.QtWidgets import *
from PySide6.QtCore import *
from functions.handleActiveButton.setEnableStartButton import setEnableStartButton
from functions.handleMultiThreads.thread.AutomationThread import AutomationThread


def stopAutomation(self):
    result = QMessageBox.question(
        None,
        "Xác nhận dừng",
        "Bạn có chắc chắn muốn dừng không.Điều này có thể gây mất mát dữ liệu?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No,
    )

   
    self.stop_all_threads = True
    for thread in self.chrome_threads:
        thread.stop()

    self.chrome_threads.clear()
    setEnableStartButton(self)
    self.startAutomation_called = False

       
