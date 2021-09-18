from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

browser.find_element_by_xpath("//a[@href='/dynamic_controls']").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@onclick='swapCheckbox()']").click()
time.sleep(7)
browser.find_element_by_xpath("//*[@autocomplete='off']").click()
time.sleep(7)
browser.find_element_by_xpath("//*[@onclick='swapInput()']").click()
time.sleep(7)
browser.quit()