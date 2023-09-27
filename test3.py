import sys
import re
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QLabel
from PyQt6.QtCore import QTimer

def validate_password(password):
    # Biểu thức chính quy kiểm tra mật khẩu
    password_regex = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^&*()])[A-Za-z\d@#$%^&*()]{8,}$')
    return bool(password_regex.match(password))

def on_text_changed():
    input_text = line_edit.text()

    # Hủy timer trước đó (nếu có)
    if timer.isActive():
        timer.stop()

    # Bắt đầu lại timer
    timer.start(1000)  # Chờ 1 giây trước khi kiểm tra mật khẩu

def check_password():
    input_text = line_edit.text()
    if validate_password(input_text):
        result_label.setText("")
    else:
        result_label.setText("Mật khẩu không hợp lệ")
        result_label.setStyleSheet("color: red;")

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Password Validation Example")

    global line_edit
    line_edit = QLineEdit()
    line_edit.setPlaceholderText("Nhập mật khẩu")
    line_edit.setEchoMode(QLineEdit.EchoMode.Password)  # Ẩn ký tự khi nhập mật khẩu
    line_edit.textChanged.connect(on_text_changed)

    global result_label
    result_label = QLabel()

    global timer
    timer = QTimer()
    timer.timeout.connect(check_password)

    layout = QVBoxLayout()
    layout.addWidget(line_edit)
    layout.addWidget(result_label)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
