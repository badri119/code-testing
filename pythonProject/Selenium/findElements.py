import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Safari()
driver.maximize_window()

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

driver.find_element(By.ID, 'autosuggest').send_keys('ind')
time.sleep(2)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a") #find_elements will give all the elements with same class
# print(len(countries))

#if country is India, make a click
for country in countries:
    if country.text == 'India':
        country.click()
        break



#will get a dynamically typed value while automating
# print(driver.find_element(By.ID, "autosuggest").get_attribute('value')) 


#assert to check if the value is matching
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"


