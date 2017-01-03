from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#user data to sign in form 
first_name = "user_first_name"
last_name = "user_last_name"
email = 'user_email'
pwd = "password"

#initializing webdriver
driver = webdriver.Chrome()

#loading site
driver.get("https://www.xing.com/")

elem = driver.find_element_by_id('signup_minireg_first_name')
elem.send_keys(first_name)
elem = driver.find_element_by_id('signup_minireg_last_name')
elem.send_keys(last_name, Keys.ARROW_DOWN)
elem = driver.find_element_by_id('signup_minireg_email')
elem.send_keys(email,  Keys.ARROW_DOWN)
elem = driver.find_element_by_id('signup_minireg_password')
elem.send_keys(pwd)
elem = driver.find_element_by_id('signup_minireg_tandc_check')
elem.click()

##driver.switch_to_window("")

elem = driver.find_element_by_name("send")
elem.click()

#recaptcha-anchor
time.sleep(10)
driver.forward()
##driver.switch_to_default_content()
    
elem = driver.find_element_by_id('recaptcha-anchor')
elem.click()


time.sleep(2000)
driver.close()
