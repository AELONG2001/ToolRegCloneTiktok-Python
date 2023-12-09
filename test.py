from threading import Thread
import pyautogui
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep

hostname = "rp.proxyscrape.com"
port = "6060"
proxy_username = "33v7bu4ahf7ultp-country-us-session-8z2x1mev4b-lifetime-10"
proxy_password = "x97zud5m4en4q5f"

chrome_options = Options()
chrome_options.add_argument('--proxy-server={}'.format(hostname + ":" + port))
driver = webdriver.Chrome(options=chrome_options)


def enter_proxy_auth(proxy_username, proxy_password):
    sleep(1)
    pyautogui.typewrite(proxy_username)
    pyautogui.press('tab')
    pyautogui.typewrite(proxy_password)
    pyautogui.press('enter')

def open_a_page(driver, url):
    driver.get(url)


Thread(target=open_a_page, args=(driver, "https://www.tiktok.com/signup/phone-or-email/email")).start()
Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()
sleep(100000)