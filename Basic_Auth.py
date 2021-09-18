from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/basic_auth")
time.sleep(3)
browser.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)

browser.quit()