from threading import Thread
import pyautogui
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep

hostname = "115.73.197.184"
port = "10005"
proxy_username = "8eyE8CzO"
proxy_password = "JEDX50dd"

chrome_options = Options()
chrome_options.add_argument('--proxy-server={}'.format(hostname + ":" + port))
driver = webdriver.Chrome(options=chrome_options)


def enter_proxy_auth(proxy_username, proxy_password):
    pyautogui.typewrite(proxy_username)
    pyautogui.press('tab')
    pyautogui.typewrite(proxy_password)
    pyautogui.press('enter')
    

def open_a_page(driver, url):
    driver.get(url)


Thread(target=open_a_page, args=(driver, "https://whatismyipaddress.com/vi-vn/index")).start()
Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

sleep(100000)