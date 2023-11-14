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

    if result == QMessageBox.StandardButton.Yes:
        self.stop_progress_dialog.show()
        self.stop_progress_dialog.set_progress(0)
        self.stop_progress_dialog.set_progress_text("Đang tiến hành stop...")
        QCoreApplication.processEvents()
        QCoreApplication.processEvents()

        self.stop_all_threads = True
        for thread in self.chrome_threads:
            if AutomationThread.num_quit == len(AutomationThread.drivers_list):
                break
            thread.stop()

        self.chrome_threads.clear()  # Xóa danh sách các luồng đã dừng

        self.stop_progress_dialog.close()
        setEnableStartButton(self)
        self.startAutomation_called = False

       
