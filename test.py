from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Tạo một QTabWidget
        tab_widget = QTabWidget(self)

        # Tạo các tab
        self.home = QWidget()
        self.setting = QWidget()

        # Tạo một QVBoxLayout cho mỗi tab và thêm các phần tử vào đó
        home_layout = QVBoxLayout(self.home)
        home_label = QLabel("Hello, this is the home tab!", self.home)
        home_layout.addWidget(home_label)
        self.home.setLayout(home_layout)

        setting_layout = QVBoxLayout(self.setting)
        setting_label = QLabel("Hello, this is the setting tab!", self.setting)
        setting_layout.addWidget(setting_label)
        self.setting.setLayout(setting_layout)

        # Thêm các tab vào QTabWidget
        tab_widget.addTab(self.home, "Home")
        tab_widget.addTab(self.setting, "Setting")

        # Đặt màu nền cho tiêu đề của từng tab
        self.set_tab_header_background_color(tab_widget, 0, "#green")  # Màu nền cho tab Home
        self.set_tab_header_background_color(tab_widget, 1, "#green")  # Màu nền cho tab Setting

        # Hiển thị QTabWidget
        tab_widget.show()

    def set_tab_header_background_color(self, tab_widget, index, color):
        # Kiểm tra index hợp lệ
        if 0 <= index < tab_widget.count():
            # Truy cập QTabBar và đặt màu nền cho tiêu đề tab tại index
            tab_bar = tab_widget.findChild(QTabBar)
            if tab_bar:
                tab_bar.setStyleSheet(f'QTabBar::tab:{index} {{ background-color: {color}; }}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
