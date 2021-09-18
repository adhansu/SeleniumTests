from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

#File Download
browser.find_element_by_xpath("//a[@href='/download']").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='content']/div/a[1]").click()
time.sleep(5)
browser.quit()