from selenium import webdriver
import time
from selenium.webdriver import ActionChains

#horizontal slider
class Sliders():
    @staticmethod
    def sliders_demo():
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(options=chrome_options)
        browser.get("http://the-internet.herokuapp.com/horizontal_slider")
        browser.maximize_window()
        elem = browser.find_element_by_xpath("//*[@id='content']/div/div/input")
        ActionChains(browser).drag_and_drop_by_offset(elem, 50, 0).perform()
        time.sleep(3)

s = Sliders()
s.sliders_demo()









