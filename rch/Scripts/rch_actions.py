from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from time import  sleep
import child_actions as ca



driver = ''


def login(username, pw):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.rch.nhm.gov.in/RCH/")
    sleep(1)
    # Auto login
    driver.find_element_by_xpath('//*[@id="form1"]/header/div[2]/div[2]/div[3]').click()
    sleep(1)

    # selects state Maharastra
    driver.find_element_by_xpath('//*[@id="ddlStateName"]/option[21]').click()

    # sets usaername
    driver.find_element_by_xpath('//*[@id="txtUserName"]') \
        .send_keys(username)
    sleep(1)

    # sets Password
    driver.find_element_by_xpath('//*[@id="txtPassword"]') \
        .send_keys(pw)
    sleep(10)
    # self.captcha = self.driver.find_element_by_xpath('//*[@id="txtimgcode"]').get_attribute('value')

    # clicks on login
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
    # home button click
    driver.find_element_by_xpath('//*[@id="HomeMenu"]/span').click()

    




def get_page():
    print("i am inside get_page")

    sleep(3)

    # store url of currently loaded page

    page_url = driver.current_url

    # url of 'SECTION-III(INDEX) Tracking of Children (CH-1)' page

    urlCh1 = 'https://rch.nhm.gov.in/RCH/UI/ChildDataEntry.aspx?Id_Edit='

    # compairing current page url with url of all pages by comapiring substrig method

    if urlCh1 in page_url:
        # calling corresponding page method
        ca.Child()




    #method for explicit wait until element located by xpath, xpath is given to constructor

def ex_wait_xpath(xpath):
    try:
        element = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH,xpath))
        )
        return element
    finally:
        pass

        #method for explicit wait until url changed

def ex_wait_urlchange():
    try:
        element = WebDriverWait(driver,30).until(EC.url_changes)
        print("waited until url changed inside wait")
        return element
    finally:
        pass



    #method for checing url of loaded page and calling corresponding page methods


def setDate():

    sleep(4)
    date = '20-05-2020'
    print('inside set date')

    driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_txtImmu_Date"]').send_keys(date) #sets date in immunization date field


    #method to handle alerts according to alert message


def alertHandler():
    #wait until Alert is present

    try:
        element = WebDriverWait(driver,30).until(EC.alert_is_present())
        print("Alert Detected")
        return element
    except:
        pass
    finally:
        pass



    #get Alert_text
    try:
        sleep(2)
        alert_text = driver.switch_to_alert().text

        print("Alert text is : ",alert_text)

        success = 'Successfully'
        # checks if alert is of successfull

        if success in alert_text:
            #clicks on on alert
            driver.switch_to_alert().accept()
            print("Alert is accepted")
            sleep(5)
    except:
        pass


