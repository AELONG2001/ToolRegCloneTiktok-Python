import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class UpdateProgressDialog(QDialog):
    def __init__(self, self_main, parent=None):
        super().__init__(parent)
        self.self_main = self_main
        self.setWindowTitle("Version update")
        self.setFixedSize(300, 150)

        icon = QIcon()
        icon.addPixmap(
            QPixmap(".\\icons/logo_tiktok.png"),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.setWindowIcon(icon)

        layout = QVBoxLayout()

        current_directory_logo = os.path.dirname(__file__)
        absolute_path_logo = os.path.abspath(os.path.join(current_directory_logo, "icons/logo_tiktok.png"))
        self.pixmap = QPixmap("icons/logo_tiktok.png")
        self.pixmap = self.pixmap.scaled(28, 28, Qt.KeepAspectRatio)

        self.logo_update = QLabel()
        self.logo_update.setPixmap(self.pixmap)
        self.logo_update.setAlignment(Qt.AlignCenter)

        self.logo_update_label = QLabel("ToolRegCloneTiktok")
        self.logo_update_label.setAlignment(Qt.AlignCenter)
        self.logo_update_label.setStyleSheet('font: 600 10pt "Segoe UI";')

        self.description_update = QLabel(f"Downloading {self.self_main.latest_version}")
        self.description_update.setAlignment(Qt.AlignCenter)

        self.percent_title = QLabel()
        self.percent_title.setAlignment(Qt.AlignCenter)

        self.progress_bar = QProgressBar()
       
        layout.addWidget(self.logo_update)
        layout.addWidget(self.logo_update_label)
        layout.addWidget(self.description_update)
        layout.addWidget(self.percent_title)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)
        self.setModal(True)
        self.setAutoFillBackground(True)
        self.setAutoFillBackground(True)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

    def set_percent_title(self, text):
        self.percent_title.setText(text)

    def set_progress_dialog(self, value):
        self.progress_bar.setValue(value)

    def set_is_show_progress_dialog(self, boolean):
        self.progress_bar.setVisible(boolean)
