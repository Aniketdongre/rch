import rch_actions as ra
from time import  sleep
from selenium.webdriver.support.ui import Select
from datetime import datetime
from datetime import timedelta

#global variable declaration
add_days = ''
deliveryDate = ''


def infant():
    print("inside infant")
    

    setPncDate()

    # click on Danger sign None
    ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_chkInfantNone"]').click()


def setPncDate():

    # This manipulates date to set date for entry

    pncday = PNC_ToEnter()
    #selecting pncday to enter from drop down
    select = Select(ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlPNCPeriod"]'))
    select.select_by_visible_text(pncday)


    #geting delivery date
    global deliveryDate
    deliveryDate = ra.driver.find_element_by_id('SingleMainContent_DoubleMainContent_lblDeliverydate').text

    # Determine days to add in delivery date to get Entry Date
    global add_days
    add_days = int(''.join(i for i in pncday if i.isdigit())) # get digits and then join to get number
    

    print(add_days)
    print(type(add_days))

    DateManipulate()


def DateManipulate():

    # it adds pnc days to dilvery date

    # converting dilvery date from string to datetime object
    global deliveryDate
    deliveryDate = datetime.strptime(deliveryDate, '%d-%m-%Y')
    print(deliveryDate)
    

    # adding days to dilvery date
    global add_days
    entryDate = deliveryDate + timedelta(days = add_days)
    # make sure its not sunday
    if entryDate.weekday() == 6:
        entryDate = entryDate + timedelta(days = 1) 

    #convert datetime object into string object
    entryDate = entryDate.strftime('%d-%m-%Y')

    

    #sets date in date entry field
    ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_txtPncDate"]').send_keys(entryDate)
    



def PNC_ToEnter():

    # This determines last given pnc visit day entry
    # and returns Next pnc to enter


    pncDates = ['28th Day','21st Day','14th Day','7th Day']
    for index, Day in enumerate(pncDates) :
        flag = 0
        try:
            ra.driver.find_element_by_link_text(Day)
            flag = 1
            break
        except Exception:
            pass
    if flag == 1:
        return pncDates[index-1]
    elif flag == 0:
        return pncDates[index]
