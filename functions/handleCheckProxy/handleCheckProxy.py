from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from functions.proxy.TMProxy.handleCheckKeyTmProxy import handleCheckKeyTmProxy
from functions.proxy.TMProxy.handleGetNewTMProxyToCheckExpired import handleGetNewTMProxyToCheckExpired
from functions.proxy.TinProxy.handleGetNewTinProxyCheckCorrect import handleGetNewTinProxyCheckCorrect
from functions.proxy.TinProxy.handleGetNewTinProxyCheckExpired import handleGetNewTinProxyCheckExpired

class ProxyCheckerTaskSignals(QObject):
    result_signal = Signal(str, str)

class ProxyCheckerTask(QRunnable):
    def __init__(self, ui_instance, proxy_type, api_key_list):
        super().__init__()
        self.ui_instance = ui_instance
        self.proxy_type = proxy_type
        self.api_key_list = api_key_list
        self.signals = ProxyCheckerTaskSignals()
        
    def run(self):
        if self.proxy_type == 0:
            response_api_tm_proxy_check_correct = handleCheckKeyTmProxy(self.api_key_list)
            response_api_tm_proxy_check_expired = handleGetNewTMProxyToCheckExpired(self.api_key_list)

            self.signals.result_signal.emit(
              response_api_tm_proxy_check_correct,
              response_api_tm_proxy_check_expired
            )
        elif self.proxy_type == 1:
            response_api_tin_proxy_check_correct = handleGetNewTinProxyCheckCorrect(self.api_key_list)
            response_api_tin_proxy_check_expired = handleGetNewTinProxyCheckExpired(self.api_key_list)

            self.signals.result_signal.emit(
              response_api_tin_proxy_check_correct,
              response_api_tin_proxy_check_expired
            )
def handleCheckProxy(self):
    self.start_button.setEnabled(False)
    self.start_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.2)")

    self.check_proxy.setEnabled(False)
    if self.current_version == self.latest_version:
        self.check_proxy.setGeometry(QRect(1125, 420, 100, 30))
    else:
        self.check_proxy.setGeometry(QRect(1125, 460, 100, 30))
    self.check_proxy.setText("Đang check")
    self.check_proxy.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")

    self.loading_icon_check_proxy.setVisible(True)
    self.loadingMovieCheckProxy.start()

    proxy_type = self.proxy_type.currentIndex()
    api_key_proxy = self.proxy_value.toPlainText()
    api_key_list = api_key_proxy.splitlines()

    task = ProxyCheckerTask(self, proxy_type, api_key_list)
    task.signals.result_signal.connect(self.updateResultCheckProxy)
    self.threadpool.start(task)

    


