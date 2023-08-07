from selenium import webdriver
import time
import requests


# Hàm để cập nhật proxy trong WebDriver
def update_proxy(proxy):
    options = webdriver.ChromeOptions()
    options.add_argument("--proxy-server=" + proxy)
    driver = webdriver.Chrome(options=options)
    return driver


# Hàm để lấy proxy từ API
def get_new_proxy():
    api_key_tmproxy = "07abb8e50d61d34b59966335cf9cb7a0"
    api_key_list = api_key_tmproxy.splitlines()
    list_proxy = []

    url = "https://tmproxy.com/api/proxy/get-new-proxy"

    for key in api_key_list:
        response = requests.post(url, json={"api_key": f"{key}"})
        data = response.json()
        https = data["data"]["https"]
        list_proxy.append(https)

        return list_proxy


# Hàm để thực hiện việc cập nhật proxy và chạy trình duyệt
def run_with_auto_proxy():
    while True:
        proxy_list = get_new_proxy()
        print("proxy_list: ", proxy_list)
        selected_proxy = proxy_list[0]
        driver = update_proxy(selected_proxy)

        driver.refresh()
        driver.get("https://whatismyipaddress.com/vi-vn/index")

        # Đợi 5 phút trước khi bắt đầu lại vòng lặp
        time.sleep(300)  # 5 phút = 300 giây


if __name__ == "__main__":
    run_with_auto_proxy()
