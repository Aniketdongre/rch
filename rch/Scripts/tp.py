




def get_page():
    print("i am inside get_page")
    from time import sleep
    from main import rchBot
    from child_actions import child_class
    sleep(3)



    # store url of currently loaded page

    page_url = rchBot.driver.current_url

    #url of 'SECTION-III(INDEX) Tracking of Children (CH-1)' page

    urlCh1 = 'https://rch.nhm.gov.in/RCH/UI/ChildDataEntry.aspx?Id_Edit='

    #compairing current page url with url of all pages by comapiring substrig method

    if urlCh1 in page_url:

        # calling corresponding page method
        child_class.Child()



    # method to set Date
