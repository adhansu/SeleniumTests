from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

browser.find_element_by_xpath("//a[@href='/disappearing_elements']").click()
time.sleep(3)
browser.find_element_by_xpath("//a[@href='/about/']").click()
time.sleep(3)
browser.back()
browser.find_element_by_xpath("//a[@href='/contact-us/']").click()
time.sleep(3)
browser.back()
browser.find_element_by_xpath("//a[@href='/gallery/']").click()
time.sleep(3)

browser.quit()