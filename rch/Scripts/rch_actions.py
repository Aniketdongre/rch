from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import  sleep


    #method for explicit wait until element located by xpath, xpath is given to constructor

def ex_wait(xpath):
    from main import rchBot
    try:
        element = WebDriverWait(rchBot.driver,30).until(EC.presence_of_element_located((By.XPATH,xpath))
        )
        return element
    finally:
        pass



    #method for checing url of loaded page and calling corresponding page methods


def setDate():
    from main import rchBot

    sleep(4)
    self.date = '20-05-2020'
    print('inside set date')

    rchBot.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_txtImmu_Date"]').send_keys(self.date) #sets date in immunization date field


    #method to handle alerts according to alert message


def alertHandler():

    from main import rchBot

    #get Alert_text

    alert_text = rchBot.driver.switch_to_alert().text

    print("Alert text is : ",alert_text)

    self.success = 'Successfully'
    # checks if alert is of successfull

    if success in alert_text:
        #clicks on on alert
        rchBot.driver.switch_to_alert().accept()


    #method to set Data Entry Data i.e Doses or ANC visits

  #  def setData(self):


    #    print("inside child track page and set data method")


    #    sleep(2) #bas yuhi

    #    # click on immunization selection

    #    driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlImmunization"]').click()

     #   self.setOption() #sets the immunization options according to selection

     #   self.setDate()