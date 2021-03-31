from selenium import webdriver
import time

driver = webdriver.Chrome("D:\Stuffs\Python\LearnPython\PythonSelenium\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)
driver.switch_to.alert.accept()

time.sleep(5)

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)
driver.switch_to.alert.dismiss()

time.sleep(5)