from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

#Inputs
browser.find_element_by_xpath("//a[@href='/inputs']").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='content']/div/div/div/input").send_keys(25)
time.sleep(3)
browser.quit()