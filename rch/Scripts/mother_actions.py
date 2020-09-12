import rch_actions as ra
from time import sleep
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
        setANC()


    except Exception:
        print("no previous entries found")
        pass

    setPlace()
    # click on High Risk None

    ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_chkNone"]').click()

    # After all anc entries are made and clicked on continue




def setANC():
    print("iside Set Anc")

    LMP_Date = ra.driver.find_element_by_id('SingleMainContent_DoubleMainContent_lblLMP').text
    LMP_Date = datetime.strptime(LMP_Date, '%d-%m-%Y')

    entryDate = LMP_Date + timedelta(days=56)
    # make sure its not sunday
    if entryDate.weekday() == 6:
        entryDate = entryDate + timedelta(days=1)

    if entryDate < datetime.now():

        # convert datetime object into string object
        entryDate = entryDate.strftime('%d-%m-%Y')

        # sets date in date entry field
        ra.driver.find_element_by_xpath('//*[@id="SingleMainContent_DoubleMainContent_txtAncDate"]').send_keys(
            entryDate)
    else:
        print("calculated ANC entry date is greater that todays date entry cant be made")



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

