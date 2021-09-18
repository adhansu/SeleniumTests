from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

browser.find_element_by_xpath("//a[@href='/context_menu']").click()
time.sleep(3)
actionChains = ActionChains(browser)
elementLocator = browser.find_element_by_id("hot-spot")
actionChains.context_click(elementLocator).perform()
time.sleep(3)
browser.quit()