import time
from selenium import webdriver
from selenium.webdriver.common.by import By


#Safari driver service
driver = webdriver.Safari()
driver.maximize_window()
driver.implicitly_wait(20) #takes time to load the webpage, and hence the detection of webelement wasn't happening so I had to add this via stackoverflow /27112731

driver.get('https://rahulshettyacademy.com/client') #going to a specific URL
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

driver.find_element(By.XPATH, "//form/div[1]/input").send_keys('demo@gmail.com') #getting the input via tags
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys('Hello@1234') #getting the input via css
driver.find_element(By.XPATH, "//input[@placeholder='Confirm Passsword']").send_keys('Hello@1234')
driver.find_element(By.XPATH, "//button[@type='submit']").click()






















time.sleep(10) #wait for 3 seconds


