from PySide6.QtWidgets import *
from functions.handleActiveButton.setDisableStartButton import setDisableStartButton
from functions.handleCheckInitialValues.handleCheckInitialValues import handleCheckInitialValues
from functions.handleMultiThreads.thread.AutomationThread import AutomationThread
import json
import datetime
from queue import Queue

def startAutomation(self):
    setDisableStartButton(self)
    
    AutomationThread.num_quit = 0
    AutomationThread.drivers_list = []

    with open("configs_account.json", "r") as json_file:
        data = json.load(json_file)

    # input user have to includes mail
    if "url_mail" in data:
        input_file_path = data["url_mail"]
    else:
        input_file_path = "data/hotmail.txt"
    
    output_file_path = "data/output.txt"


    num_threads = self.threads_value.value()

    # with open(input_file_path, "r") as file:
    #     check_data_input_file = file.readlines()

    # non_empty_lines_input = [line.strip() for line in check_data_input_file if line.strip()]
    # with open(input_file_path, 'w') as file:
    #     file.write('\n'.join(non_empty_lines_input))

    # with open(input_file_path, 'r') as file:
    #     accounts = file.readlines()

    # self.data_queue = Queue()
    # for account in accounts:
    #     username = account.strip().split('|')[0]
    #     password = account.strip().split('|')[1]
    #     self.data_queue.put((username, password))

    chrome_count = self.chrome_setting_line_value.value()
    captcha_type = self.captcha_type.currentIndex()
    captcha_key = self.captcha_key.text()
    current_date = datetime.date.today().strftime("%d/%m/%Y")
    proxy_type = self.proxy_type.currentIndex()
    random_password_account = self.random_password_account.isChecked()
    chrome_percent_zoom = self.chrome_percent_zoom_value.value()
    type_reg_country = self.type_reg_country.currentIndex()

    self.thread_index = 0
    self.stop_all_threads = False
    self.chrome_threads = [
        AutomationThread(
            self,
            thread,
            input_file_path,
            output_file_path,
            current_date,
            chrome_count,
            captcha_type,
            captcha_key,
            proxy_type,
            random_password_account,
            chrome_percent_zoom,
            type_reg_country,
            False,
        )
        for thread in range(num_threads)
    ]


    secondTimer = self.chrome_delay_second_value.value()
    
    self.start_timer.setInterval(secondTimer * 1000)
    self.re_start_timer.setInterval((secondTimer * 1000) + 2000)
    
    self.start_timer.timeout.connect(self.start_next_thread)
    self.re_start_timer.timeout.connect(self.restart_thread)

    self.start_next_thread()
