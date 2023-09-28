import sys
import requests
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

def handleCheckMailApi(username, password):
    url = f"https://tools.dongvanfb.net/api/check_mail"
    params = {
        "mail": username,
        "pass": password
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Xử lý lỗi HTTP
        data = response.json()
        return (username, password, data.get("status", False))
    except Exception as e:
        print(f"Error checking mail: {str(e)}")
        return (username, password, False)

class EmailCheckerTaskSignals(QObject):
    result_signal = Signal(str)  # Sửa đổi từ pyqtSignal thành Signal

class EmailCheckerTask(QRunnable):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.signals = EmailCheckerTaskSignals()

    def run(self):
        _, _, status = handleCheckMailApi(self.username, self.password)
        result_text = f"Email: {self.username} - {'Thành công' if status else 'Thất bại'}"
        self.signals.result_signal.emit(result_text)

class EmailCheckerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Email Checker")
        self.setGeometry(100, 100, 800, 600)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()

        self.selectFileButton = QPushButton("Chọn tệp danh sách email")
        self.selectFileButton.clicked.connect(self.selectFile)

        self.filePathLabel = QLabel("Tệp danh sách email:")
        self.filePathTextEdit = QTextEdit(self)
        self.filePathTextEdit.setReadOnly(True)

        self.layout.addWidget(self.selectFileButton)
        self.layout.addWidget(self.filePathLabel)
        self.layout.addWidget(self.filePathTextEdit)

        # Tạo một QLabel để hiển thị hoạt ảnh GIF
        self.loading_icon = QLabel(self)
        self.loading_icon.setGeometry(QRect(445, 221, 14, 14))
        relative_path = "icons/loading.gif"
        absolute_path = os.path.abspath(relative_path)
        self.loadingMovie = QMovie(absolute_path)
        self.loading_icon.setMovie(self.loadingMovie)

        self.checkButton = QPushButton("Kiểm tra email")
        self.checkButton.setStyleSheet(
            'font: 700 10pt "Segoe UI";\n'
            "color: #fff;\n"
            "background-color:rgb(64, 170, 15);\n"
            ""
        )
        self.checkButton.clicked.connect(self.startChecking)

        self.loading_icon.setVisible(False)

        self.layout.addWidget(self.checkButton)

        self.successLabel = QLabel("Emails thành công (0):")
        self.successTextEdit = QTextBrowser(self)
        self.successTextEdit.setReadOnly(True)

        self.failedLabel = QLabel("Emails thất bại (0):")
        self.failedTextEdit = QTextBrowser(self)
        self.failedTextEdit.setReadOnly(True)

        self.layout.addWidget(self.successLabel)
        self.layout.addWidget(self.successTextEdit)
        self.layout.addWidget(self.failedLabel)
        self.layout.addWidget(self.failedTextEdit)

        self.centralWidget.setLayout(self.layout)

        self.max_thread_count = 50
        self.threadpool = QThreadPool.globalInstance()
        self.threadpool.setMaxThreadCount(self.max_thread_count)
        self.success_count = 0
        self.failed_count = 0

    def selectFile(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_paths, _ = file_dialog.getOpenFileNames(self, "Chọn tệp danh sách email", "", "Text Files (*.txt);;All Files (*)")

        if file_paths:
            self.filePathTextEdit.setPlainText('\n'.join(file_paths))

    def startChecking(self):
        file_paths = self.filePathTextEdit.toPlainText().strip().split('\n')
        if not file_paths:
            self.successTextEdit.setPlainText("Vui lòng chọn ít nhất một tệp danh sách email.")
            return

        self.successLabel.setText(f"Emails thành công (0):")
        self.failedLabel.setText(f"Emails thất bại (0):")

        self.successTextEdit.clear()
        self.failedTextEdit.clear()

        self.success_count = 0
        self.failed_count = 0

        total_email_count = 0

        for file_path in file_paths:
            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    total_email_count += len(lines)

                    for line in lines:
                        username, password = line.strip().split('|')
                        task = EmailCheckerTask(username, password)
                        task.signals.result_signal.connect(self.updateResultText)
                        self.threadpool.start(task)
            except Exception as e:
                self.successTextEdit.setPlainText(f"Lỗi khi kiểm tra email: {str(e)}")

        self.checkButton.setEnabled(False)
        self.loading_icon.setVisible(True)
        self.loadingMovie.start()

        self.total_email_count = total_email_count

        self.checkButton.setText("Đang kiểm tra")

    def updateResultText(self, result_text):
        if "Thành công" in result_text:
            self.successTextEdit.append(result_text)
            self.success_count += 1
        else:
            self.failedTextEdit.append(result_text)
            self.failed_count += 1

        self.updateCounts()

        if self.success_count + self.failed_count == self.total_email_count:
            self.showSuccessMessage()

    def updateCounts(self):
        self.successLabel.setText(f"Emails thành công ({self.success_count}):")
        self.failedLabel.setText(f"Emails thất bại ({self.failed_count}):")

    def showSuccessMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Kiểm tra email hoàn thành.")
        msg.setWindowTitle("Thành công")
        msg.exec()

        self.checkButton.setEnabled(True)
        self.checkButton.setText("Kiểm tra")
        self.loading_icon.setVisible(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    email_checker = EmailCheckerApp()
    email_checker.show()
    sys.exit(app.exec())
