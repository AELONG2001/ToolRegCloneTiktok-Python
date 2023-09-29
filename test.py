import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog

class AccountExporter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        export_full_button = QPushButton("Xuất toàn bộ nội dung")
        export_full_button.clicked.connect(self.export_full)
        layout.addWidget(export_full_button)

        export_without_cookie_button = QPushButton("Xuất username|password|passmail (loại bỏ cookie)")
        export_without_cookie_button.clicked.connect(self.export_without_cookie)
        layout.addWidget(export_without_cookie_button)

        export_username_password_button = QPushButton("Xuất username|password")
        export_username_password_button.clicked.connect(self.export_username_password)
        layout.addWidget(export_username_password_button)

        self.setLayout(layout)
        self.setWindowTitle("Xuất Accounts")

    def export_full(self):
        self.export("full")

    def export_without_cookie(self):
        self.export("without_cookie")

    def export_username_password(self):
        self.export("username_password")

    def export(self, export_type):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("Tệp văn bản (*.txt);;Tất cả các tệp (*)")
        
        default_file_name = "output.txt"  # Tên tệp mặc định
        
        if export_type == "without_cookie":
            default_file_name = "output_without_cookie.txt"
        elif export_type == "username_password":
            default_file_name = "output_username_password.txt"
        
        file_name, _ = QFileDialog.getSaveFileName(None, "Chọn nơi lưu tệp", default_file_name, "Tệp văn bản (*.txt);;Tất cả các tệp (*)")

        if not file_name:
            return  # Không làm gì nếu người dùng không chọn tên tệp

        with open("data/accounts.txt", "r") as file:
            accounts =  file.readlines()

        if export_type == "full":
            selected_data = accounts
        elif export_type == "without_cookie":
            selected_data = [line.split("|")[:3] for line in accounts]
        elif export_type == "username_password":
            selected_data = [line.split("|")[:2] for line in accounts]
        else:
            return

        with open(file_name, "w") as txtfile:
            if export_type in ["without_cookie", "username_password"]:
                for line in selected_data:
                    txtfile.write("|".join(line) + "\n")
            else:
                txtfile.writelines(selected_data)
       

def main():
    app = QApplication(sys.argv)
    window = AccountExporter()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
