from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from functions.handleActiveButton.setEnableStartButton import setEnableStartButton
from functions.handleMultiThreads.selenium.ResolveCaptcha.AchiCaptcha.handleCheckApiKeyAChi import handleCheckApiKeyAChi
from functions.handleMultiThreads.selenium.ResolveCaptcha.OmoCaptcha.handleCheckApiKeyOmo import handleCheckApiKeyOmo
from functions.proxy.TMProxy.handleCheckKeyTmProxy import handleCheckKeyTmProxy
from functions.proxy.TMProxy.handleGetNewTMProxyToCheckExpired import handleGetNewTMProxyToCheckExpired
from functions.proxy.TinProxy.handleGetNewTinProxyCheckCorrect import handleGetNewTinProxyCheckCorrect
from functions.proxy.TinProxy.handleGetNewTinProxyCheckExpired import handleGetNewTinProxyCheckExpired
from functions.profilesGologin.handleCheckTokenGologin import handleCheckTokenGologin
from functions.autoBuyHotmail.handleCheckBalance import handleCheckBalance
from functions.autoBuyHotmail.handleCheckInstock import handleCheckInstock
import json

class InitalValuesCheckerTaskSignals(QObject):
    result_signal = Signal(bool, str)

class InitalValuesCheckerTask(QRunnable):
    def __init__(self, ui_instance):
        super().__init__()
        self.ui_instance = ui_instance
        self.signals = InitalValuesCheckerTaskSignals()
        
    def run(self):
        message = ""
        if self.ui_instance.is_check_mail:
            message = "Vui lòng đợi quá trình check mail hoàn thành"
            setEnableStartButton(self.ui_instance)
            self.signals.result_signal.emit(False, message)
            return
            
        with open("configs_account.json", "r") as json_file:
            data = json.load(json_file)

        if not "url_mail" in data or not data["url_mail"]:
            if not data["api_value_hotmailbox"]:
                message = "Vui lòng nhập mail"
                setEnableStartButton(self.ui_instance)
                self.signals.result_signal.emit(False, message)
                return

        # input user have to includes captcha_key
        if not "captcha_key" in data or not data["captcha_key"]:
            message = "Vui lòng nhập captcha key"
            setEnableStartButton(self.ui_instance)
            self.signals.result_signal.emit(False, message)
            return
            
        else:
            if self.ui_instance.captcha_type.currentIndex() == 0:
                response_api_achi = handleCheckApiKeyAChi(data["captcha_key"])

                if "errorDescription" in response_api_achi and response_api_achi["errorDescription"] == "client key not correct":
                    message = "Api key AchiCaptcha không chính xác.Vui lòng kiểm tra lại"
                    setEnableStartButton(self.ui_instance)
                    self.signals.result_signal.emit(False, message)
                    return
                    
                
                if "errorDescription" in response_api_achi and response_api_achi["errorDescription"] == "not enough funds":
                    message = "Tài khoản AchiCaptcha đã hết tiền.Vui lòng kiểm tra lại"
                    setEnableStartButton(self.ui_instance)
                    self.signals.result_signal.emit(False, message)
                    return
                    
            else:
                response_api_omo = handleCheckApiKeyOmo(data["captcha_key"])

                if response_api_omo == "api key not correct":
                    message = "Api key OmoCaptcha không chính xác.Vui lòng kiểm tra lại"
                    setEnableStartButton(self.ui_instance)
                    self.signals.result_signal.emit(False, message)
                    return
                    
                
                if "balance" in response_api_omo and response_api_omo["balance"] == "0.00000":
                    message = "Tài khoản OmoCaptcha đã hết tiền.Vui lòng kiểm tra lại"
                    setEnableStartButton(self.ui_instance)
                    self.signals.result_signal.emit(False, message)
                    return
                    

            if not data["captcha_key"]:
                message = "Vui lòng nhập captcha key"
                setEnableStartButton(self.ui_instance)
                self.signals.result_signal.emit(False, message)
                return
                        
        # input user have to includes api_token_gologin
        if not "api_token_gologin" in data or not data["api_token_gologin"]:
            message = "Vui lòng nhập Token Gologin"
            setEnableStartButton(self.ui_instance)
            self.signals.result_signal.emit(False, message)
            return
        else:
            response_api_gologin = handleCheckTokenGologin(data["api_token_gologin"])

            if "statusCode" in response_api_gologin and response_api_gologin["statusCode"] == 401:
                message = "Token Gologin không chính xác.Vui lòng kiểm tra lại"
                setEnableStartButton(self.ui_instance)
                self.signals.result_signal.emit(False, message)
                return
                
            
            if "plan" in response_api_gologin and response_api_gologin["plan"]["name"] == "Unpaid":
                message = "Token Gologin đã hết hạn.Vui lòng kiểm tra lại"
                setEnableStartButton(self.ui_instance)
                self.signals.result_signal.emit(False, message)
                return
        
        # input user have to includes path_gologin
        if not "path_gologin" in data or not data["path_gologin"]:
            message = "Vui lòng nhập Path Profile Gologin"
            setEnableStartButton(self.ui_instance)
            self.signals.result_signal.emit(False, message)
            return
            
        if "api_value_hotmailbox" in data and data["api_value_hotmailbox"]:
            response_api_hotmailbox_check_balance = handleCheckBalance(data["api_value_hotmailbox"])
            response_api_hotmailbox_check_instock = handleCheckInstock(data["api_value_hotmailbox"])

            if "Code" in response_api_hotmailbox_check_balance and response_api_hotmailbox_check_balance["Code"] == 401:
                message = "Api hotmailbox không chính xác.Vui lòng kiểm tra lại"
                setEnableStartButton(self.ui_instance)
                self.signals.result_signal.emit(False, message)
                return
                

            if int(response_api_hotmailbox_check_balance["Balance"]) == 0:
                message = "Tài khoản Hotmailbox đã hết tiền.Vui lòng kiểm tra lại"
                setEnableStartButton(self.ui_instance)
                self.signals.result_signal.emit(False, message)
                return
                
            
            if response_api_hotmailbox_check_instock < 2000:
                message = "Số lượng hotmail trên Hotmailbox đang ít hơn 2000.Vui lòng mua tay và tiếp tục chạy"
                setEnableStartButton(self.ui_instance)
                self.signals.result_signal.emit(False, message)
                return
            
        # input user have to includes proxys
        if not "proxys" in data or not data["proxys"]:
            message = "Vui lòng nhập proxys"
            setEnableStartButton(self.ui_instance)
            self.signals.result_signal.emit(False, message)
            return
            
        else:
            if "proxys" in data:
                proxy_type = self.ui_instance.proxy_type.currentIndex()
                api_key_list = data["proxys"]
                 
                if proxy_type == 0:
                    response_api_tm_proxy_check_correct = handleCheckKeyTmProxy(api_key_list)
                    if response_api_tm_proxy_check_correct:
                        message = response_api_tm_proxy_check_correct
                        setEnableStartButton(self.ui_instance)
                        self.signals.result_signal.emit(False, message)
                        return
                    
                    response_api_tm_proxy_check_expired = handleGetNewTMProxyToCheckExpired(api_key_list)
                    if response_api_tm_proxy_check_expired:
                        message = response_api_tm_proxy_check_expired
                        setEnableStartButton(self.ui_instance)
                        self.signals.result_signal.emit(False, message)
                        return
                elif proxy_type == 2:
                    response_api_tin_proxy_check_correct = handleGetNewTinProxyCheckCorrect(api_key_list)
                    if response_api_tin_proxy_check_correct:
                        message = response_api_tin_proxy_check_correct
                        setEnableStartButton(self.ui_instance)
                        self.signals.result_signal.emit(False, message)
                        return
                    
                    response_api_tin_proxy_check_expired = handleGetNewTinProxyCheckExpired(api_key_list)
                    if response_api_tin_proxy_check_expired:
                        message = response_api_tin_proxy_check_expired
                        setEnableStartButton(self.ui_instance)
                        self.signals.result_signal.emit(False, message)
                        return

                    self.signals.result_signal.emit(False, message)
                    return
        self.signals.result_signal.emit(True, message)
       

def handleCheckInitialValues(self):
    task = InitalValuesCheckerTask(self)
    task.signals.result_signal.connect(self.updateResultCheckInitalValues)
    self.threadpool.start(task)


