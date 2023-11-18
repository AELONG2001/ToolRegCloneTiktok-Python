from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from functions.hdcklsfw.handleGetMachineCode import handleGetMachineCode
from functions.hdcklsfw.hdcklsfw import hdcklsfw
from functions.handleSaveDataInputUser.handleSaveDataInputUser import handleSaveDataInputUser
from subprocess import run, CREATE_NO_WINDOW
import webbrowser

class ckuslsw(QMainWindow):
    def __init__(self):
        super().__init__()
        self.machine_code = handleGetMachineCode()

        self.setWindowTitle("ToolRegCloneTiktok")
        self.setGeometry(0, 0, 450, 250)

        screen_geometry = QGuiApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) / 2
        y = (screen_geometry.height() - self.height()) / 2
        self.move(x, y)

        icon = QIcon()
        icon.addPixmap(
            QPixmap(".\\icons/logo_tiktok.png"),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.setWindowIcon(icon)
        
        self.zalo_icon = QPixmap("icons/zalo.png")
        self.facebook_icon = QPixmap("icons/facebook.png")
        self.hotline_icon = QPixmap("icons/call_phone.png")
        self.web_icon = QPixmap("icons/web.png")

        self.check_key = QLabel("Nhập Key của bạn:", self)
        self.check_key.setGeometry(10, 10, 160, 28)
        self.key_input = QLineEdit(self)
        self.key_input.setGeometry(10, 40, 430, 30)
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setGeometry(180, 76, 100, 30)
        self.submit_button.setStyleSheet("color: white; background-color: rgb(64, 170, 15)")
        self.key_input.returnPressed.connect(self.hckuslfw)
        self.submit_button.clicked.connect(self.hckuslfw)

        self.zalo = QLabel(self)
        self.zalo.setGeometry(10, 136, 28, 28)
        self.zalo.setPixmap(self.zalo_icon)
        self.zalo_value = QLabel('<a style="color: #0068FF;" href="https://zalo.me/0375270513">https://zalo.me/0375270513</a>', self)
        self.zalo_value.setGeometry(42, 136, 200, 28)
        self.zalo_value.setStyleSheet('font: 700 9pt "Segoe UI"')
        self.zalo_value.setCursor(Qt.PointingHandCursor)
        self.zalo_value.setOpenExternalLinks(True)
        self.zalo_value.linkActivated.connect(self.open_link)

        self.facebook = QLabel(self)
        self.facebook.setGeometry(10, 168, 28, 28)
        self.facebook.setPixmap(self.facebook_icon)
        self.facebook_value = QLabel('<a style="color: #000;" href="https://facebook.com/longdevzz">https://facebook.com/longdevzz</a>', self)
        self.facebook_value.setGeometry(42, 168, 220, 28)
        self.facebook_value.setStyleSheet('font: 700 9pt "Segoe UI"')
        self.facebook_value.setCursor(Qt.PointingHandCursor)
        self.facebook_value.setOpenExternalLinks(True)
        self.facebook_value.linkActivated.connect(self.open_link)

        self.hotline = QLabel(self)
        self.hotline.setGeometry(270, 136, 28, 28)
        self.hotline.setPixmap(self.hotline_icon)
        self.hotline_value = QLabel("037.527.0513", self)
        self.hotline_value.setGeometry(302, 136, 100, 28)
        self.hotline_value.setStyleSheet('color: #000; font: 700 9pt "Segoe UI";')

        self.web = QLabel(self)
        self.web.setGeometry(272, 170, 24, 24)
        self.web.setPixmap(self.web_icon)
        self.web_value = QLabel('<a style="color: #000;" href="http://longsoftware.vn">http://longsoftware.vn</a>', self)
        self.web_value.setGeometry(302, 168, 220, 28)
        self.web_value.setStyleSheet('font: 700 9pt "Segoe UI"')
        self.web_value.setCursor(Qt.PointingHandCursor)
        self.web_value.setOpenExternalLinks(True)
        self.web_value.linkActivated.connect(self.open_link)

        self.attention = QLabel("Chú ý: Mọi hành vi cố tình crack sẽ không được support và cập nhập\n phiên bản mới", self)
        self.attention.setGeometry(15, 205, 400, 36)
        self.attention.setStyleSheet('font: 600 italic 8pt "Segoe UI";')

    def open_link(url):
        webbrowser.open(url)

    def hckuslfw(self):
        input_key = self.key_input.text().strip()
        response = hdcklsfw(input_key, self.machine_code)

        if response["status"]:
            handleSaveDataInputUser("klsfw", input_key)
            handleSaveDataInputUser("mclsfw", self.machine_code)
            QApplication.quit()
            run("./ToolRegCloneTiktok.exe", creationflags=CREATE_NO_WINDOW)
        else:
            QMessageBox.critical(self, "Xác nhận", "Key không đúng hoặc đã hết hạn.\nVui lòng kiểm tra lại", QMessageBox.Ok)