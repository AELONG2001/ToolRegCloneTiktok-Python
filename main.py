from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# UI
from GUI.uiMain import uiMain
from GUI.translateUi import translateUi

# Logic
from functions.handleLogicMain.logicMain import AutomationController


class Ui_ToolRegCloneTiktok(object):
    def __init__(self):
        self.success_mail_count = 0
        self.failed_mail_count = 0

    def setupUi(self, ToolRegCloneTiktok):
        uiMain(self, ToolRegCloneTiktok)
        self.automation_controller = AutomationController(self)

    def start(self):
        self.automation_controller.start()

    def stop(self):
        self.automation_controller.stop()

    def checkThreadsValue(self, value):
        self.automation_controller.checkThreadsValue(value)

    def handleAvatarFolderSelection(self):
        self.automation_controller.handleAvatarFolderSelection()

    def inputMail(self):
        self.automation_controller.inputMail()

    def getCaptchaKey(self):
        self.automation_controller.getCaptchaKey()

    def importProxy(self):
        self.automation_controller.importProxy()

    def inputMailCheck(self):
        self.automation_controller.inputMailCheck()

    def handleCheckMail(self):
        self.automation_controller.handleCheckMail()

    def retranslateUi(self, ToolRegCloneTiktok):
        translateUi(self, ToolRegCloneTiktok)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ToolRegCloneTiktok = QMainWindow()
    ui = Ui_ToolRegCloneTiktok()
    ui.setupUi(ToolRegCloneTiktok)
    ToolRegCloneTiktok.show()
    sys.exit(app.exec())
