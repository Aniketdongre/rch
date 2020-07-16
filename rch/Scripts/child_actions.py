
import rch_actions as ra
from time import  sleep


def Child():
    print("i am inside ch1")


    # method for  'SECTION-III(INDEX) Tracking of Children (CH-1)' page

    ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_btnContinue"]').click()

    setData()

    # alert_handling

    ra.alertHandler()

    # select the id box for next id
    ra.ex_wait_xpath('//*[@id="txtRCH_MCTS_ID"]')
    
    ra.driver.find_element_by_xpath('//*[@id="txtRCH_MCTS_ID"]').click()

    #wait until next id opens

    ra.ex_wait_urlchange()

    print("waited until url changed inside wait")



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