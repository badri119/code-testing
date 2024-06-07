import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Safari()
driver.maximize_window()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

checkbox = driver.find_elements(By.XPATH, "//div[@id='checkbox-example']//input[@type='checkbox']")

# print(len(checkbox))

#selecting option2 which was an attribute for value called option2
#use for loop if options don't change
for cb in checkbox:
    if cb.get_attribute('value') == 'option2':
        cb.click()
        print("checkbox:", cb.is_selected()) #checks if the selected option is selected (True or False)
        break



#For radio button
radio = driver.find_elements(By.XPATH, "//div[@id='radio-btn-example']//input[@type='radio']")

#selecting 3rd radio option

for r in radio:
    if r.get_attribute('value') == 'radio3':
        r.click()
        print("Radio: ", r.is_selected())
        break
    
#or, if radio options don't change:
# radio[2].click()



# To display text:
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, 'displayed-text').is_displayed()


time.sleep(8)