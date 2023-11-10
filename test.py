# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# chrome_options = webdriver.ChromeOptions()

# chromedriver_path = ChromeDriverManager().install()
# print("chromedriver_path: ", chromedriver_path)

# chrome_options.add_argument(f"webdriver.chrome.driver={chromedriver_path}")

driver = webdriver.Chrome()
driver.get("https://google.com/")