from selenium import webdriver
import time

driver = webdriver.Chrome("D:\Stuffs\Python\LearnPython\PythonSelenium\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.linkedin.com/")

print(driver.title)

driver.implicitly_wait(30)
driver.find_element_by_class_name('nav__button-secondary').click()

time.sleep(30)

driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys("devraj_kanti@yahoo.com")
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('Dell@15R')

driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()