from logging import exception

import rch_actions as ra
from time import sleep


# start browser
ra.initialize()

# automate login
ra.login(username='PHCDewhaoi',pw="Dewhadi@123")

#wait until id page opens
#x_path of Selection Hierarchy is provided whichi is present in all entry pages
ra.ex_wait_xpath('//*[@id="DivHierarchy"]/table/tbody/tr/td')



try:
    ra.get_page()
except exception as e:
    print('Exception occurrrred :'+e)
    pass
    

# select the id box for next id

#ra.driver.find_element_by_xpath('//*[@id="txtRCH_MCTS_ID"]').click()

#wait until next id opens

ra.ex_wait_urlchange()

print("waited until url changed ")

#ra.get_page()
