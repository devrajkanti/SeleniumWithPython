#Select One Option
#Capture the options are seen
#Count the no of options

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("D:\Stuffs\Python\LearnPython\PythonSelenium\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_id('RESULT_RadioButton-9')
drop = Select(element)

drop.select_by_visible_text("Morning")
time.sleep(5)

drop.select_by_index(2)
time.sleep(5)

drop.select_by_value("Radio-2")
time.sleep(5)

#Count no of options
print(len(drop.options))

#Print each options
all_options = drop.options
for each in all_options:
    print(each.text)

driver.close()