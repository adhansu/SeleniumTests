from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

#ABTest
browser.find_element_by_xpath("//a[@href='/abtest']").click()
time.sleep(7)
browser.quit()
