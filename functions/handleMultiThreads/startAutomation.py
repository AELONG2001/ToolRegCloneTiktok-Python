from PySide6.QtWidgets import *
from time import sleep
from functions.handleMultiThreads.AutomationThread import AutomationThread


def startAutomation(self):
    num_threads = self.threads_value.value()
    self.start_button.setEnabled(False)
    self.start_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")
    self.stop_button.setEnabled(True)
    self.stop_button.setStyleSheet(
        "color:rgb(255, 252, 252);\n" "background-color:rgb(255, 0, 0)"
    )
    # QApplication.processEvents()
    self.stop_event.clear()
    chrome_count = self.chrome_setting_line_value.currentText()
    chrome_delay_minute = int(self.chrome_delay_minute_value.currentText())
    chrome_percent_zoom = self.chrome_percent_zoom_value.value()
    is_show_chrome = self.chrome_setting_radio_yes.isChecked()

    self.chrome_threads = [
        AutomationThread(
            self.stop_event,
            thread,
            chrome_count,
            chrome_percent_zoom,
            is_show_chrome,
        )
        for thread in range(num_threads)
    ]
    for thread in self.chrome_threads:
        sleep(chrome_delay_minute)
        thread.start()