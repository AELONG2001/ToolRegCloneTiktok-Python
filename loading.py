import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

class LoadingIcon(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.loading_label = QLabel(self)
        self.loading_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.loading_label)

        self.setLayout(layout)

        # Tạo QTimer để cập nhật biểu tượng quay 180 độ
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateLoadingIcon)
        self.timer.start(100)  # Cập nhật mỗi 100ms

        # Tải biểu tượng mặc định
        self.loading_pixmap = QPixmap('loading.png')
        self.loading_label.setPixmap(self.loading_pixmap)

        # Góc quay ban đầu
        self.rotation_angle = 0

    def updateLoadingIcon(self):
        # Tạo một bản sao của biểu tượng và xoay nó
        rotated_pixmap = self.loading_pixmap.copy()
        transform = QTransform()
        self.rotation_angle += 10  # Góc xoay 10 độ mỗi lần cập nhật
        transform.rotate(self.rotation_angle)
        rotated_pixmap = rotated_pixmap.transformed(transform)

        # Cập nhật biểu tượng đã xoay
        self.loading_label.setPixmap(rotated_pixmap)

def main():
    app = QApplication(sys.argv)
    window = LoadingIcon()
    window.setWindowTitle('Loading Icon')
    window.setGeometry(100, 100, 100, 100)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
