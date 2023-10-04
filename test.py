import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
from selenium import webdriver

class KeyGenerator:
    def generate_key(self, days):
        # Đây là nơi bạn có thể tạo key dựa trên số ngày yêu cầu
        return f"Key_{days}_days"

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ứng dụng Key")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel("Nhập key của bạn:")
        self.layout.addWidget(self.label)

        self.key_input = QLineEdit()
        self.layout.addWidget(self.key_input)

        self.verify_button = QPushButton("Xác minh key")
        self.verify_button.clicked.connect(self.verify_key)
        self.layout.addWidget(self.verify_button)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.key_generator = KeyGenerator()

    def verify_key(self):
        input_key = self.key_input.text()
        valid_keys = [
            self.key_generator.generate_key(7),
            self.key_generator.generate_key(30),
            self.key_generator.generate_key(365)
        ]

        if input_key in valid_keys:
            self.show_message("Thông báo", "Key hợp lệ. Chào mừng bạn vào ứng dụng!")
        else:
            self.show_message("Thông báo", "Key không hợp lệ. Vui lòng thử lại hoặc liên hệ với người quản trị.")

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())
