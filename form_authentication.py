from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://the-internet.herokuapp.com/")

#Form authentication
browser.find_element_by_xpath("//a[@href='/login']").click()
time.sleep(3)

username = browser.find_element_by_xpath("//*[@id='username']")
username.send_keys("tomsmith")

password = browser.find_element_by_xpath("//*[@id='password']")
password.send_keys("SuperSecretPassword!")

login = browser.find_element_by_xpath("//*[@id='login']/button/i")
login.click()
time.sleep(2)
browser.quit()