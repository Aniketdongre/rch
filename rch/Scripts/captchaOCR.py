#from selenium import webdriver
import rch_actions as ra
from time import  sleep
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


#intialization of webdriver
'''driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.rch.nhm.gov.in/RCH/") '''


def captchaOCR():
    # capturing screenshot of captcha element
    img = ra.driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div/div/div[3]/div[6]/img')
    img.screenshot('ca_img.png')
    sleep(1)

    # reading captured images
    img = Image.open('ca_img.png')

    print('image read')

    # OCR - converting image into text and putting captcha field
    ca_text = pytesseract.image_to_string(img)

    ra.driver.find_element_by_xpath('//*[@id="txtimgcode"]').send_keys(ca_text)
    