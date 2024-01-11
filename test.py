from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from time import sleep

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

stealth(driver,
    languages=["vi"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

driver.get("https://www.tiktok.com/signup/phone-or-email/email")
sleep(100000)