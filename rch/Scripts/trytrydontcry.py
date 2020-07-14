from selenium import webdriver
import requests
from time import  sleep

class captcha:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.rch.nhm.gov.in/RCH/")
        sleep(1)
        # Auto login
        self.driver.find_element_by_xpath('//*[@id="form1"]/header/div[2]/div[2]/div[3]').click()
        sleep(5)
        self.get_img()



    def get_img(self):
        img = self.driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div/div/div[3]/div[6]/img')
        src = img.get_attribute('src')
        img = requests.get(src)
        with open('captcha.jpg', 'wb') as f:
            f.write(img.content)

        sleep(10)

captcha()