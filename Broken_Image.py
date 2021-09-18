from pip._vendor import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
URL = "http://the-internet.herokuapp.com/broken_images"

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get(URL)

#Broken Image
image_list = browser.find_elements(By.TAG_NAME, "img")
print('Total number of images on '+ URL + ' are ' + str(len(image_list)))
for img in image_list:
    try:
        response = requests.get(img.get_attribute('src'), stream=True)
        if response.status_code != 200:
            print(img.get_attribute('outerHTML') + " is broken.")
            iBrokenImageCount = (iBrokenImageCount + 1)

    except requests.exceptions.MissingSchema:
        print("Encountered MissingSchema Exception")
    except requests.exceptions.InvalidSchema:
        print("Encountered InvalidSchema Exception")
    except:
        print("Encountered Some other Exception")

browser.quit()
