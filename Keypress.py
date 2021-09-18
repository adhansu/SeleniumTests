from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

#Keypress
browser.find_element_by_xpath("//a[@href='/key_presses']").click()
time.sleep(3)
key = browser.find_element_by_xpath("//*[@id='target']")
key.click()
key.send_keys(Keys.ENTER)
time.sleep(4)
browser.quit()