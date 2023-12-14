import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from GUI.uckuslsfw import ckuslsw
from GUI.uiLogicMain import utrclttlsfw
from functions.hdcklsfw.hdcklsfw import hdcklsfw
import json

class hmlsfw(QMainWindow):
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
    ackuslsfw = ckuslsw()
 
    if os.path.exists("configs_account.json"):
        with open("configs_account.json", "r") as json_file:
            data = json.load(json_file)

        klsfw = data["klsfw"]
        mclsfw = data["mclsfw"]

        response_text = hdcklsfw(klsfw, mclsfw)
        response = json.loads(response_text)

        if response["sfad23sewf32ewdds47rfd"]:
            ui = utrclttlsfw(response)
            trgclttlsfw = hmlsfw(ui)
            ui.setupUi(trgclttlsfw)
            trgclttlsfw.show()
        else:
            ackuslsfw.show()
    else:
        ackuslsfw.show()

    sys.exit(app.exec())
