from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

browser.find_element_by_xpath("//a[@href='/checkboxes']").click()
time.sleep(3)
browser.find_element_by_id("checkboxes").click()
time.sleep(3)
# To find whether the element is a checkbox or not
if browser.find_element_by_id("checkboxes").get_attribute("type") == "checkbox":
    print("Element is a checkbox")
else:
    print("Element is not a checkbox")

# To find whether the checkbox element is selected or not
isChecked = browser.find_element_by_id("checkboxes").get_attribute("checked")
if isChecked is not None:
    print("Element checked - ", isChecked)
else:
    print("Element checked - false")
