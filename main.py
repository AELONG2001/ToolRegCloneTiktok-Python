import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from GUI.uiCheckKey import CheckKeyUser
from GUI.uiLogicMain import Ui_ToolRegCloneTiktok
from functions.handleCheckKey.handleCheckKey import handleCheckKey
import json

class MainWindow(QMainWindow):
    def __init__(self, ui_self):
        super().__init__()
        self.ui_self = ui_self
        self.ui_self.is_update = False
       
    def closeEvent(self, event):
        if self.ui_self.is_update:
            event.accept()
            return

        result = QMessageBox.question(
            self,
            "Xác nhận dừng",
            "Bạn có chắc chắn muốn dừng không.Điều này có thể gây mất mát dữ liệu?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if result == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    check_key_user = CheckKeyUser()
 
    if os.path.exists("configs_account.json"):
        with open("configs_account.json", "r") as json_file:
            data = json.load(json_file)

        key = data["key"]
        machine_code = data["machine_code"]

        response = handleCheckKey(key, machine_code)

        if response["status"]:
            ui = Ui_ToolRegCloneTiktok(response)
            ToolRegCloneTiktok = MainWindow(ui)
            ui.setupUi(ToolRegCloneTiktok)
            ToolRegCloneTiktok.show()
        else:
            check_key_user.show()
    else:
        check_key_user.show()

    sys.exit(app.exec())
