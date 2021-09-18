from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

#Floating Menu
browser.find_element_by_xpath("//a[@href='/floating_menu']").click()
time.sleep(3)
browser. execute_script("window. scrollTo(0,300);")
time.sleep(4)
browser.quit()