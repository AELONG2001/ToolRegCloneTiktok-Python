from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class StopProgressDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Quá trình này có thể mất thời gian...")
        self.setFixedSize(300, 100)

        layout = QVBoxLayout()
        self.progress_label = QLabel("Quá trình này có thể mất thời gian...")
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_label)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)
        self.setModal(True)
        self.setAutoFillBackground(True)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

    def set_progress(self, value):
        self.progress_bar.setValue(value)

    def set_progress_text(self, text):
        self.progress_label.setText(text)