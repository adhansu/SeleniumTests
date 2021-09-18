from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
browser.get("http://the-internet.herokuapp.com/")


browser.find_element_by_xpath("//a[@href='/drag_and_drop']").click()
time.sleep(7)
action = ActionChains(browser)
src = browser.find_element_by_xpath("//*[@id='column-a']")
trgt = browser.find_element_by_xpath("//*[@id='column-b']")
action.drag_and_drop(src, trgt).perform()
time.sleep(3)
browser.quit()
