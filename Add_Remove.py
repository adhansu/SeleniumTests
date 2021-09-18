from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

browser.find_element_by_xpath("//a[@href='/add_remove_elements/']").click()
time.sleep(3)
browser.find_element_by_xpath("//button[@onclick='addElement()']").click()
time.sleep(3)
browser.find_element_by_xpath("//button[@onclick='deleteElement()']").click()
time.sleep(2)
browser.quit()