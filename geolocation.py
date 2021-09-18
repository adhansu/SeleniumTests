from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://the-internet.herokuapp.com/')

#geolocation
browser.find_element_by_xpath("//a[@href='/geolocation']").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='content']/div/button").click()
time.sleep(2)

browser.quit()