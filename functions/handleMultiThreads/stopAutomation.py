from PySide6.QtWidgets import *


def stopAutomation(self):
    result = QMessageBox.question(
        None,
        "Xác nhận dừng",
        "Bạn có chắc chắn muốn dừng không.Điều này có thể gây mất mát dữ liệu?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No,
    )

    if result == QMessageBox.StandardButton.Yes:
        self.stop_event.set()  # Set flag stop_event để tất cả các luồng biết dừng
        # for thread in self.chrome_threads:
        #     thread.join()

        self.stop_button.setEnabled(False)
        self.stop_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")
        self.start_button.setEnabled(True)
        self.start_button.setStyleSheet(
            "color:rgb(255, 252, 252);\n" "background-color:rgb(64, 170, 15)"
        )
        # QApplication.processEvents()