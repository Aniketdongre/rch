from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import  sleep
from time import  sleep

#from child_actions import *








class rchBot:

    def __init__(self):
        pass



    driver = ''
    def login(self,username,pw):

        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.rch.nhm.gov.in/RCH/")
        sleep(1)
        #Auto login
        driver.find_element_by_xpath('//*[@id="form1"]/header/div[2]/div[2]/div[3]').click()
        sleep(1)

        # selects state Maharastra
        driver.find_element_by_xpath('//*[@id="ddlStateName"]/option[21]').click()

        #sets usaername
        driver.find_element_by_xpath('//*[@id="txtUserName"]')\
        .send_keys(username)
        sleep(1)

        #sets Password
        driver.find_element_by_xpath('//*[@id="txtPassword"]')\
        .send_keys(pw)
        sleep(10)
       # self.captcha = self.driver.find_element_by_xpath('//*[@id="txtimgcode"]').get_attribute('value')

        #clicks on login
        driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

        driver.find_element_by_xpath('//*[@id="SMSMenu"]/span').click()


        sleep(5)

        driver.find_element_by_xpath('//*[@id="SingleMainContent_UserInfoBoxControl2_ddlSubCentre"]/option[5]').click()


        sleep(3)
        driver.find_element_by_xpath('//*[@id="SingleMainContent_UserInfoBoxControl2_ddlVillage"]/option[3]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="SingleMainContent_UserInfoBoxControl2_btnSave"]').click()
        sleep(4)

        print("location selected")
        #home button click
        driver.find_element_by_xpath('//*[@id="HomeMenu"]/span').click()

        sleep(30)

    def get_page(self):
        print("i am inside get_page")

        from child_actions import Child
        sleep(3)

        # store url of currently loaded page

        page_url = driver.current_url

        # url of 'SECTION-III(INDEX) Tracking of Children (CH-1)' page

        urlCh1 = 'https://rch.nhm.gov.in/RCH/UI/ChildDataEntry.aspx?Id_Edit='

        # compairing current page url with url of all pages by comapiring substrig method

        if urlCh1 in page_url:
            # calling corresponding page method
            Child()


mybot = rchBot()

mybot.login(username='PHCDewhaoi',pw="Dewhadi@123")
mybot.get_page()