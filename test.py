from selenium import webdriver
from selenium_authenticated_proxy import SeleniumAuthenticatedProxy
from time import sleep

chrome_options = webdriver.ChromeOptions()

proxy_helper = SeleniumAuthenticatedProxy(proxy_url="http://116.96.146.110:22471")

proxy_helper.enrich_chrome_options(chrome_options)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.facebook.com/')


sleep(10000000)
