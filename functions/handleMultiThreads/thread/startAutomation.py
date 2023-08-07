from PySide6.QtWidgets import *
from functions.handleInputFileMail.getMailContent import getMailContent
from functions.handleMultiThreads.thread.AutomationThread import AutomationThread


def startAutomation(self):
    AutomationThread.num_quit = 0
    AutomationThread.drivers_list = []

    input_file_path = r"C:\Users\HD\OneDrive\Documents\WorkSpace\Tools\Python\ToolRegCloneTiktok\data\hotmail.txt"

    with open(input_file_path, "r") as f:
        mail_content = f.read()

    accounts = getMailContent(mail_content)

    if len(accounts) > 0:
        num_threads = self.threads_value.value()
    else:
        num_threads = 1

    self.stop_event.clear()
    chrome_count = self.chrome_setting_line_value.currentText()
    chrome_delay_minute = int(self.chrome_delay_minute_value.currentText())
    chrome_percent_zoom = self.chrome_percent_zoom_value.value()
    is_show_chrome = self.chrome_setting_radio_yes.isChecked()

    self.thread_index = 0
    self.stop_all_threads = False
    self.chrome_threads = [
        AutomationThread(
            self,
            self.stop_event,
            thread,
            chrome_count,
            chrome_percent_zoom,
            is_show_chrome,
        )
        for thread in range(num_threads)
    ]
    self.start_next_thread()

    self.start_button.setEnabled(False)
    self.start_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")
    self.stop_button.setEnabled(True)
    self.stop_button.setStyleSheet(
        "color:rgb(255, 252, 252);\n" "background-color:rgb(255, 0, 0)"
    )
