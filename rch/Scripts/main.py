import rch_actions as ra

ra.login(username='PHCDewhaoi',pw="Dewhadi@123")

#wait until id page opens

ra.ex_wait_xpath('//*[@id="SingleMainContent_DoubleMainContent_btnContinue"]')

ra.get_page()