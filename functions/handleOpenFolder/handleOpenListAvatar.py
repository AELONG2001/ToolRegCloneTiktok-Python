from PySide6.QtWidgets import QFileDialog


def selectAvatarFolder():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.Directory)
    if dialog.exec_():
        selected_folder = dialog.selectedFiles()[0]
        return selected_folder
