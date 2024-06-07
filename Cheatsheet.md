# Selenium Cheatsheet

## List:

### 1. To get an element using element tags use //<first tag>/<second tag>... (locatorExtensions.py)

#### This goes inside form tag -> first div tag (that's why I specified the indiex [1]) -> input

Example: //form/div[1]/input
Another way is to use classname:

#### Example using a mix of tags and class:

#This goes inside li tag -> check's for class name with 'ui-menu-item' -> a
Example: //li[@class='ui-menu-item']/a

### 2. If selected element has multiple values with same attributes, you can store it in a variable and loop it to find a specific value (findElements.py)

#### Example:

#countries has a list of values with same attributes and we're checking if the text == India:
for country in countries:
if country.text == 'India':
country.click()
break

### 3. To get dynamically typed values, we cannot use .text as we're typing the values while automating. For that, we will need to use a special function called get_attribute (findElements.py)

#### Example:

#will get a dynamically typed value while automating

#print(driver.find_element(By.ID, "autosuggest").get_attribute('value'))

#Adding assert to check if the value entered is matching (A sample test case)
#assert to check if the value is matching
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"

### 4.
