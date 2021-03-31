from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome("D:\Stuffs\Python\LearnPython\PythonSelenium\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#Working with Radio Button

status = driver.find_element_by_id('RESULT_RadioButton-7_1').is_selected()
print(status) #Returns False

driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').click() #Clicks the radio button

status1 = radiobutton_male = driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()
print(status1) #Returns true

#Working with check boxes
driver.find_element_by_id('RESULT_CheckBox-8_5').click()
# driver.find_element_by_xpath('//*[@id="RESULT_CheckBox-8_5"]').click()