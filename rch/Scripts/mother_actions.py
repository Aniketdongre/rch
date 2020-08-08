import rch_actions as ra
from time import  sleep



def infant():
    print("inside infant")
    # Determined already given pnc service
    
    found = givenPNC()
    print('Found: ',found)



def givenPNC():

    # This determines last pnc visit day entry

    pncDates = ['28th Day','21st Day','14th Day','7th Day']
    for Day in pncDates:
        try:
            ra.driver.find_element_by_link_text(Day)
            break
        except Exception:
            pass
    return Day
