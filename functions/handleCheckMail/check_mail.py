from PySide6.QtWidgets import *
from PySide6.QtGui import *
import requests
from concurrent.futures import ThreadPoolExecutor


def handleCheckMailApi(username, password):
    url = f"https://tools.dongvanfb.net/api/check_mail?mail={username}&pass={password}"
    response = requests.get(url)
    data = response.json()
    return (username, password, data.get("status", False))


def checkMail(
    fileNameCheck, mail_success_box, mail_success, mail_failed_box, mail_failed
):
    with open(fileNameCheck, "r") as file:
        mail_content = file.read()
        mail_lines = mail_content.splitlines()

    listMailFilterSpace = []
    for item in mail_lines:
        if item.strip():
            listMailFilterSpace.append(item)

    num_threads = 50
    valid_mails = []
    invalid_mails = []
    for line in listMailFilterSpace:
        if "|" in line:
            try:
                username, password = line.split("|", 1)
                valid_mails.append((username, password))
            except ValueError:
                # Nếu xảy ra lỗi khi tách dòng thành username và password, xem như là "invalid_mails"
                invalid_mails.append(line)
        else:
            # Nếu không tìm thấy "|", xem như là "invalid_mails"
            invalid_mails.append(line)

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(handleCheckMailApi, username, password)
            for username, password in valid_mails
        ]

        success_mail_count = 0
        failed_mail_count = 0
        for future in futures:
            username, password, is_live = future.result()
            if is_live:
                success_mail_count += 1
                mail_success_box.moveCursor(QTextCursor.End)
                mail_success_box.insertPlainText(f"{username}|{password}\n")
                mail_success.setText(f"Live Mail ({success_mail_count}):")
                QApplication.processEvents()
            else:
                invalid_mails_str = "\n".join(invalid_mails)
                failed_mail_count += 1
                mail_failed_box.moveCursor(QTextCursor.End)
                mail_failed_box.insertPlainText(f"{username}|{password}\n")
                mail_failed_box.insertPlainText(invalid_mails_str)
                mail_failed.setText(f"Die Mail ({failed_mail_count}):")
                QApplication.processEvents()

    # All tasks are finished, display a message
    QMessageBox.information(None, "Thông báo", "Hoàn thành kiểm tra email!")
