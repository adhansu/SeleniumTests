from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

#Multiple windows
browser.find_element_by_xpath("//a[@href='/windows']").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='content']/div/a").click()
time.sleep(5)
print(browser.current_window_handle)
handles = browser.window_handles
for handle in handles:
    browser.switch_to.window(handle)
    print(browser.title)

    if browser.title == "The Internet":
        browser.close()

browser.quit()