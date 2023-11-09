from selenium import webdriver
from selenium_authenticated_proxy import SeleniumAuthenticatedProxy
from time import sleep

chrome_options = webdriver.ChromeOptions()

proxy_helper = SeleniumAuthenticatedProxy(proxy_url="http://jJENO0wvFX:YFvmYcy14f:91.192.81.213:40250")

proxy_helper.enrich_chrome_options(chrome_options)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.facebook.com/')


sleep(10000000)
