from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

#Frames
browser.find_element_by_xpath("//a[@href='/frames']").click()
time.sleep(3)
browser.find_element_by_xpath("//a[@href='/nested_frames']").click()
time.sleep(3)
browser.back()
browser.find_element_by_xpath("//a[@href='/iframe']").click()
time.sleep(3)
action = ActionChains(browser)
source = browser.find_element_by_xpath("//*[@id='content']/div/div/div[1]/div[1]/div[1]/button[1]/span")
action.double_click(source)
time.sleep(2)
browser.quit()