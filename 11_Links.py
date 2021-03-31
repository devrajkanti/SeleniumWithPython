from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("D:\Stuffs\Python\LearnPython\PythonSelenium\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.google.com/")
links = driver.find_elements(By.TAG_NAME,"a")

for each in (links):
    print(each.text)

print("Hello World")
driver.find_element(By.LINK_TEXT,"Gmail").click()
driver.back()
driver.find_element(By.PARTIAL_LINK_TEXT,"Search").click()

time.sleep(20)

driver.close()