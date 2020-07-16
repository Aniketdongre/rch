
import rch_actions as ra
from time import  sleep


def Child():
    print("i am inside ch1")


    # method for  'SECTION-III(INDEX) Tracking of Children (CH-1)' page

    ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_btnContinue"]').click()

    setData()

    # clicks on submit button
    ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_btnSave"]').click()
    sleep(3)

    # alert_handling

    ra.alertHandler()

    # sets child immunization options according to option selected



def setOption():

    sleep(20)
    selected_dose = ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlImmunization"]').get_attribute('value')

    print("selected value is ",selected_dose)

    if selected_dose =='23':
        ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ChkBoxImu3"]').click()
        ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ChkBoxImu5"]').click()
        sleep(3)
    else:
        sleep(2)
        pass




def setData():


    print("inside child track page and set data method")


    sleep(2) #bas yuhi

        # click on immunization selection

    ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlImmunization"]').click()

    setOption() #sets the immunization options according to selection

    ra.setDate()