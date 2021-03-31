#Site to be used - https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407

#How to get the status
#How many input boxes are there
#How to provide values into text box

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("D:\Stuffs\Python\LearnPython\PythonSelenium\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

i = 1

#How to get the status
displayed = driver.find_element_by_id('RESULT_TextField-1').is_displayed()
enabled = driver.find_element_by_id('RESULT_TextField-1').is_enabled()
if displayed == True and enabled == True:
    # Find how many input boxes are there
    allBoxes = driver.find_elements(By.CLASS_NAME, 'text_field')
    print(len(allBoxes))

    for eachBox in allBoxes:
        print(i)
        print(eachBox)
        i+=1

    # How to provide value into text box
    driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("Devraj")
    driver.find_element_by_id('RESULT_TextField-2').send_keys("Kanti")