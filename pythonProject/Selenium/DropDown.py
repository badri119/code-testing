import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Safari()
driver.maximize_window()


driver.get('https://rahulshettyacademy.com/loginpagePractise/')

# print(driver.title)


#automating dropdown menu
dropdown = Select(driver.find_element(By.XPATH, "//div[@class='form-group']//select[@class='form-control']")) #selecting an option in dropdown menu
# print(len(dropdown.options))
#selecting by text
dropdown.select_by_visible_text("Teacher")
time.sleep(2)
#selecting by index 
dropdown.select_by_index(0) 
time.sleep(2)
# #selecting by value
dropdown.select_by_value('consult')






time.sleep(8) 
