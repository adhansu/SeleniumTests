from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

#Javascript alerts
browser.find_element_by_xpath("//a[@href='/javascript_alerts']").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='content']/div/ul/li[1]/button").click()
time.sleep(2)
browser.switch_to.alert.accept()
time.sleep(2)
browser.find_element_by_xpath("//*[@id='content']/div/ul/li[2]/button").click()
time.sleep(2)
browser.switch_to.alert.dismiss()
time.sleep(2)
browser.find_element_by_xpath("//*[@id='content']/div/ul/li[3]/button").click()
time.sleep(2)
browser.switch_to.alert.send_keys('nirnay')
time.sleep(2)
browser.switch_to.alert.accept()
time.sleep(2)
browser.quit()