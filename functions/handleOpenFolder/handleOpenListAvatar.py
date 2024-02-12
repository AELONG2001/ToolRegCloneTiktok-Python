from PySide6.QtWidgets import QFileDialog


def selectFolder():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.Directory)
    if dialog.exec_():
        selected_folder = dialog.selectedFiles()[0]
        return selected_folder
