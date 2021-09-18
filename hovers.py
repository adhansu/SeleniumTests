from selenium import webdriver
import time
from selenium.webdriver import ActionChains

#hovers
class hovers():
    @staticmethod
    def hovers_demo():
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(options=chrome_options)
        browser.get("http://the-internet.herokuapp.com/hovers")
        browser.maximize_window()
        pic = browser.find_element_by_xpath("//*[@id='content']/div/div[1]/img")
        achains = ActionChains(browser)
        achains.move_to_element(pic).perform()
        time.sleep(4)
        browser.find_element_by_xpath("//*[@id='content']/div/div[1]/div/a").click()
        time.sleep(3)

h = hovers()
h.hovers_demo()