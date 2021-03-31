from selenium import webdriver
import time

driver = webdriver.Chrome("D:\Stuffs\Python\LearnPython\PythonSelenium\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
alltabs = driver.window_handles

for each in alltabs:
    print(each)
    driver.switch_to.window(each)
    print(driver.title)

time.sleep(5)
driver.close() 