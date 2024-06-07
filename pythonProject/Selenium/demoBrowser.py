import time
from selenium import webdriver

#Safari driver service
driver = webdriver.Safari()

driver.get("https://add-recipe-frontend-ashen.vercel.app/") #going to a specific URL


driver.maximize_window()
print(driver.title)

















time.sleep(2) #wait for 3 seconds


