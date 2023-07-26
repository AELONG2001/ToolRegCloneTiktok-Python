from PySide6.QtWidgets import QFileDialog, QLineEdit


def selectAvatarFolder():
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly
    folder = QFileDialog.getExistingDirectory(
        None,
        "Select Avatar Folder",
        "",
        QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
    )
    return folder
