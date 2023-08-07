from PySide6.QtWidgets import *
from functions.handleMultiThreads.thread.AutomationThread import AutomationThread


def startAutomation(self):
    AutomationThread.num_quit = 0
    AutomationThread.drivers_list = []
    # username = self.table_account_info.item(0, 0)
    # if username is not None:
    num_threads = self.threads_value.value()

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
    # else:
    #     QMessageBox.warning(None, "Warning", "Vui lòng nhập mail")
