from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)

browser.get("http://the-internet.herokuapp.com/")
browser.find_element_by_xpath("//a[@href='/checkboxes']").click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id=\'checkboxes\']/input[1]').click()
time.sleep(3)
browser.quit()