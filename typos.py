from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

#Typos
browser.find_element_by_xpath("//a[@href='/typos']").click()
time.sleep(3)
browser.refresh()
time.sleep(3)
browser.refresh()
time.sleep(2)
browser.refresh()
time.sleep(2)

browser.quit()