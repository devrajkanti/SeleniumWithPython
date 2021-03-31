from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome("D:\Stuffs\Python\LearnPython\PythonSelenium\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.expedia.co.in/")

driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='location-field-destination-menu']/div[1]/button").click()
driver.find_element(By.ID,'location-field-destination').clear()
driver.find_element(By.ID,'location-field-destination').send_keys("BLR")
time.sleep(10)

driver.find_element(By.XPATH,'//*[@id="wizard-hotel-pwa-v2-1"]/div[2]/div[2]/button').click()

wait = WebDriverWait(driver,20)

element = wait.until(EC.element_to_be_clickable((By.ID,'popularFilter-0-HOT_TUB')))
element.click()

time.sleep(20)