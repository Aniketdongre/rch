
from rch_actions import *
from time import  sleep


def Child():
    print("i am inside ch1")
    from main import rchBot

    # method for  'SECTION-III(INDEX) Tracking of Children (CH-1)' page

    driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_btnContinue"]').click()

    self.setData()

    # clicks on submit button
    rchBot.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_btnSave"]').click()
    sleep(3)

    # alert_handling

    alertHandler()

    # sets child immunization options according to option selected



def setOption(self):

    sleep(20)
    self.selected_dose = driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlImmunization"]').get_attribute('value')

    print("selected value is ",self.selected_dose)

    if self.selected_dose =='23':
        driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ChkBoxImu3"]').click()
        driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ChkBoxImu5"]').click()
        sleep(3)
    else:
        sleep(2)
        pass




def setData(self):


    print("inside child track page and set data method")


    sleep(2) #bas yuhi

        # click on immunization selection

    driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlImmunization"]').click()

    self.setOption() #sets the immunization options according to selection

    rch_actions.setDate()