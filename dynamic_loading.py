from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

browser.find_element_by_xpath("//a[@href='/dynamic_loading']").click()
time.sleep(3)
browser.find_element_by_xpath("//a[@href='/dynamic_loading/1']").click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id=\'start\']/button').click()
time.sleep(3)
browser.back()
browser.find_element_by_xpath("//a[@href='/dynamic_loading/2']").click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id=\'start\']/button').click()
time.sleep(3)

browser.quit()

