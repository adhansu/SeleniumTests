from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

#Notification messages
browser.find_element_by_xpath("//a[@href='/notification_message']").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='content']/div/p/a").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='flash']/a").click()
time.sleep(3)
browser.quit()