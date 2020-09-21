import rch_actions as ra
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from datetime import datetime
from datetime import timedelta

#global variable declaration
add_days = ''
deliveryDate = ''


#Delivery Method









# Function to work on Mother ANC


def ANC():
    print('inside Anc')
    # Scroll to bottom of webpage
    ra.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        ra.driver.find_element_by_link_text(1)
        print("element Found")


    except Exception:
        print("no previous entries found")
        pass

    setPlace()
    # click on urin test donte
    ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlUrineTest"]/option[3]').click()
    # click on High Risk None
    ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_chkNone"]').click()

    # After all anc entries are made and clicked on continue






def setPlace():

    village_data = ra.driver.find_element_by_xpath('//*[@id="lblHierarchy"]').text

    village_id = {'(11749)': 'Madagi','(11750)': 'Chargaon', '(11751)':'Dhorwada'}

    for village in village_id:
        if village in village_data:
            place =  village_id[village]


    if place=='Chargoan':
        select = Select(ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlFPforANCDone"]'))
        select.select_by_visible_text('Village')

        ra.ex_wait_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlFacilityPlaceId"]')


        ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlFacilityPlaceId"]').click()
        sleep(2)

        ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlFacilityPlaceId"]/option[1]').click()


    elif place == 'Dhorwada':

        select = Select(ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlFPforANCDone"]'))
        select.select_by_visible_text('Village')

        ra.ex_wait_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlFacilityPlaceId"]')

        ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlFacilityPlaceId"]').click()
        sleep(2)

        ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlFacilityPlaceId"]/option[2]').click()




    else:
        select = Select(ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlFPforANCDone"]'))
        select.select_by_visible_text('SubCentre')

        ra.ex_wait_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlFacilityPlaceId"]/option[5]')

        select = Select(ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlFacilityPlaceId"]'))
        select.select_by_visible_text('Madagi (Bhandara)')



def DeliveryOut():

    print("inside deliver out")
    # it makes delivery outcome page automatic

    # wait for drop down is selected and sub drop drown is appeared

    ra.ex_wait_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlReffralFacility"]/option[1]')

    # selecting the place of dilivery
    # slecting using option value attribute of drop down
    # dictiory = {value:who conducted delivery}

    select = Select(ra.driver.find_element_by_id('SingleMainContent_DoubleMainContent_ddlReffralFacility'))
    del_location_id  = {'3801': 'Staff Nurse','2188':'ANM','10731':'ANM','3713':'Staff Nurse'}

    for id in del_location_id :
        try:
            select.select_by_value(id) # selecting place of del
            # selecting who conducted delivery
            select = Select(ra.driver.find_element_by_id('SingleMainContent_DoubleMainContent_ddlDeliveryConducted'))
            select.select_by_visible_text(del_location_id[id])
            break
        except NoSuchElementException:
            pass

    # selecting delivery complication as none

    ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_chkNone"]').click()
    print('cliked on none')

    # set delivery outcome and live birth as 1 child
    select = Select(ra.driver.find_element_by_id('SingleMainContent_DoubleMainContent_ddlDeliveryOutcomes'))
    select.select_by_visible_text('1')

    select = Select(ra.driver.find_element_by_id('SingleMainContent_DoubleMainContent_ddlLiveBirth'))
    select.select_by_visible_text('1')












def infant():
    print("inside infant")

    #Scroll to bottom of webpage
    ra.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    setPncDate()

    sleep(4)
    #Scroll to top of webpage
    ra.driver.execute_script("scrollBy(0,-500);")

    # clicks on next id entry field
    ra.driver.find_element_by_xpath('//*[@id="txtRCH_MCTS_ID"]').click()
    ra.alertHandler()
    sleep(50)

    # click on Danger sign None
    ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_chkInfantNone"]').click()


def setPncDate():

    # This manipulates date to set date for entry

    pncday = PNC_ToEnter()

    if pncday!=None:
        # Make entry
        #selecting pncday to enter from drop down
        select = Select(ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_ddlPNCPeriod"]'))
        select.select_by_visible_text(pncday)


        #geting delivery date
        global deliveryDate
        deliveryDate = ra.driver.find_element_by_id('SingleMainContent_DoubleMainContent_lblDeliverydate').text

        # Determine days to add in delivery date to get Entry Date
        global add_days
        add_days = int(''.join(i for i in pncday if i.isdigit())) # get digits and then join to get number
    



        DateManipulate()
    else:
        # 28th day is enter that means all four entries are done
        #dont make any entry
        #for mother pnc click on continue
        # for child entry click on new id field
        print('All entries are done')
        pass

    # Next id all the entries till the current sys date are made
    # select entry field for next id


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



    if entryDate < datetime.now() :

        #convert datetime object into string object
        entryDate = entryDate.strftime('%d-%m-%Y')

        #sets date in date entry field
        ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_txtPncDate"]').send_keys(entryDate)
    else:
        print("calculated entry date is greater that todays date entry cant be made")




def PNC_ToEnter():

    # This determines last given pnc visit day entry
    # and returns Next pnc to enter


    pncDates = ['28th Day','21st Day','14th Day','7th Day']

    for index, Day in enumerate(pncDates) :
        
        try:
            ra.driver.find_element_by_link_text(Day)
            if index == 0:
                break
                return None
            else:
                return pncDates[index-1]

        except Exception:
            if index == 3 :
                break
                return pncDates[index]

