import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Safari()
driver.maximize_window()
name = "Badri"

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys(name)

#for alert option
driver.find_element(By.ID, 'alertbtn').click()

#switching to alert mode
alert = driver.switch_to.alert

#will grab the text from the alert
alertText = alert.text 
# print(alertText) 

time.sleep(2)
if name == 'Badri' in alertText:
    #to click on okay
    alert.accept() 

#to cancel
# alert.dismiss() 




time.sleep(7)