from selenium import webdriver
from time import sleep
import pyautogui

# Khởi tạo trình duyệt Chrome
options = webdriver.ChromeOptions()
options.add_extension("TM_chrome.crx")
driver = webdriver.Chrome(options=options)


# Hàm để cập nhật proxy trong phiên driver hiện có
def update_proxy(driver):
    driver.get("chrome-extension://pmdlifofgdjcolhfjjfkojibiimoahlc/popup.html")
    sleep(2)
    inputApiKey = driver.find_element("css selector", ".js-api-key")
    current_value = inputApiKey.get_attribute("value")
    if not current_value:
        inputApiKey.send_keys("4e7eeadaa41d83285838285edd60e3e5")

    sleep(2)
    autoChangeIp = driver.find_element("css selector", ".slider")
    autoChangeIp.click()

    sleep(2)
    minute = driver.find_element("css selector", ".js-time-reset-input")
    minute.send_keys("10")

    # sleep(2)
    # http_proxy = driver.find_element("css selector", ".js-radio-proxy")
    # http_proxy.click()

    sleep(2)
    connectButton = driver.find_element("css selector", ".js-connect-current-ip")
    connectButton.click()


# Hàm để thực hiện việc cập nhật proxy và chạy trình duyệt
def run_with_auto_proxy(driver):
    while True:
        update_proxy(driver)

        sleep(2)
        driver.get("https://whoer.net/")
        sleep(200000)


if __name__ == "__main__":
    run_with_auto_proxy(driver)
