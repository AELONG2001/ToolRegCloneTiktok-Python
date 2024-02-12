import requests
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from time import sleep
from functions.proxy.ShopLike.handleGetNewShopLikeProxy import handleGetNewShopLikeProxy
from functions.proxy.ShopLike.handleGetCurrentShopLikeProxy import handleGetCurrentShopLikeProxy

from functions.proxy.TMProxy.handleGetNewTMProxy import handleGetNewTMProxy
from functions.proxy.TMProxy.handleGetCurrentTMProxy import handleGetCurrentTMProxy

from functions.proxy.TinProxy.handleGetNewTinProxy import handleGetNewTinProxy
from functions.proxy.TinProxy.handleGetCurrentTinProxy import handleGetCurrentTinProxy
from functions.proxy.ProxyNo1.handleGetCurrentProxyNo1Proxy import handleGetCurrentProxyNo1Proxy
import random

def handleCheckAccountsApi(self, user_id):
    all_indices = list(range(self.max_thread_count_check_accounts))
    proxy = ""
    index = random.choice(all_indices)
    if self.proxy_type_check_live.currentIndex() == 0:
            isGetShopLikeProxyAgain = True
            while isGetShopLikeProxyAgain:
                api_key_list = self.proxy_value_check_live.toPlainText().splitlines()
                
                new_proxy = handleGetNewShopLikeProxy(api_key_list[index])
                current_proxy = handleGetCurrentShopLikeProxy(api_key_list[index])

                if not new_proxy:
                    proxy = current_proxy
                else:
                    proxy = new_proxy
                    
                if ':' in proxy:
                    isGetShopLikeProxyAgain = False
                else:
                    isGetShopLikeProxyAgain = True
    elif self.proxy_type_check_live.currentIndex() == 1:
        isGetTMProxyAgain = True
        while isGetTMProxyAgain:
            api_key_list = self.proxy_value_check_live.toPlainText().splitlines()
            
            new_proxy = handleGetNewTMProxy(api_key_list[index])
            current_proxy = handleGetCurrentTMProxy(api_key_list[index])
            sleep(2)

            if not new_proxy:
                proxy = current_proxy
            else:
                proxy = new_proxy
                
            if ':' in proxy:
                isGetTMProxyAgain = False
            else:
                isGetTMProxyAgain = True
    elif self.proxy_type_check_live.currentIndex() == 2:
            api_key_tinproxy = self.proxy_value_check_live.toPlainText()
            api_key_list = api_key_tinproxy.splitlines()

            new_proxy = handleGetNewTinProxy(api_key_list[index])
            current_proxy = handleGetCurrentTinProxy(api_key_list[index])

            if not new_proxy:
                proxy = current_proxy
            else:
                proxy = new_proxy
    elif self.proxy_type_check_live.currentIndex() == 3:
            proxys = self.proxy_value_check_live.toPlainText().splitlines()

            proxy = proxys[index]         
    elif self.proxy_type_check_live.currentIndex() == 4 or self.proxy_type_check_live.currentIndex() == 5:
            self.type_ip_port = self.proxy_value_check_live_ip_port.isChecked()

            get_list_proxy = self.proxy_value_check_live.toPlainText()
            proxys = get_list_proxy.splitlines()

            if self.type_ip_port:
                proxy = proxys[index]
            else:
                ip,port,user_proxy,password_proxy = proxys[index].split(":")
                proxy = f"{ip}:{port}:{user_proxy}:{password_proxy}"
    
    if not proxy:
        return
    
    proxy_http = {
        "http": f"http://{proxy}",
    }
                    
    status = False
    url = f"https://www.tiktok.com/@{user_id}"
    head = {"Host":"www.tiktok.com","user-agent":"Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","accept-encoding":"gzip, deflate","accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"}
    response = requests.get(url, headers=head, proxies=proxy_http).text
    sleep(1)

    if "userInfo" in response:
        status = True
    elif "Access Denied" in response:
        while True:
            response = requests.get(url, headers=head).text
            if "Access Denied" in response:
                continue
            else:
                break
        if "userInfo" in response:
            status = True
        else:
            status = False
    else:
        while True:
            response = requests.get(url, headers=head).text
            if "Access Denied" in response:
                continue
            else:
                break
        if "userInfo" in response:
            status = True
        else:
            status = False
    
    all_indices.remove(index)

    return user_id, status
    

class AccountsCheckerTaskSignals(QObject):
    result_signal = Signal(str, str, bool)

class AccountsCheckerTask(QRunnable):
    def __init__(self, self_main, user, user_id):
        super().__init__()
        self.self_main = self_main
        self.user = user
        self.user_id = user_id
        self.signals = AccountsCheckerTaskSignals()

    def run(self):
        _, status = handleCheckAccountsApi(self.self_main, self.user_id)
        self.signals.result_signal.emit(self.user, self.user_id, status)

def checkLiveAccounts(
    self, fileNameCheck
):
    self.live_accounts.setText(f"Live (0):")
    self.die_accounts.setText(f"Die (0):")

    self.live_accounts_box.clear()
    self.die_accounts_box.clear()

    self.success_account_live_count = 0
    self.failed_accounts_live_count = 0

    total_accounts_check_live_count = 0

    with open("data/LiveAccounts.txt", "w", encoding="utf-8") as f:
        f.write("")

    with open("data/DieAccounts.txt", "w", encoding="utf-8") as f:
                f.write("")
    
    with open(fileNameCheck, 'r', encoding="utf-8") as file:
        users = file.readlines()
        total_accounts_check_live_count += len(users)

        if not users:
            QMessageBox.warning(
            None,
            "Warning",
            "File accounts không được để trống",
            )
            return

        for user in users:
            user_id = user.strip().split("|")[0]
            task = AccountsCheckerTask(self, user, user_id)
            task.signals.result_signal.connect(self.updateResultCheckAccounts)
            self.threadpool_check_accounts.start(task)

    self.total_accounts_check_live_count = total_accounts_check_live_count
    self.btn_check_accounts.setEnabled(False)
    self.btn_check_accounts.setText("Đang check")
    self.btn_check_accounts.setGeometry(QRect(480, 40, 100, 24))
    self.btn_check_accounts.setStyleSheet("color: #fff; background-color: #636e72;")
    self.loading_icon_check_accounts.setVisible(True)
    self.loadingMovieCheckAccounts.start()

