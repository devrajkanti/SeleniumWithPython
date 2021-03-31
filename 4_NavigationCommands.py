from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("D:\Stuffs\Python\LearnPython\PythonSelenium\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com")
print(driver.title)
time.sleep(30)

driver.get("https://www.yahoo.com")
print(driver.title)
time.sleep(30)

#Go back to the previous site
driver.back()
time.sleep(30)
print(driver.title)


#Go forward the new site
driver.forward()
time.sleep(30)
print(driver.title)