from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

#Redirect link
browser.find_element_by_xpath("//a[@href='/redirector']").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='redirect']").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='content']/div/ul/li[4]/a").click()
time.sleep(3)
browser.back()
browser.find_element_by_xpath("//*[@id='content']/div/ul/li[2]/a").click()
time.sleep(2)

browser.quit()