from selenium import webdriver

driver = webdriver.Chrome("D:\Stuffs\Python\LearnPython\PythonSelenium\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com")
print(driver.title) #Returns the title
print(driver.current_url) #Returns the title
print(driver.page_source) #Returns the page source

# driver = webdriver.Edge("D:\Stuffs\Python\LearnPython\PythonSelenium\Drivers\edgedriver_win64\msedgedriver.exe")
# driver.get("https://www.google.com")
# print(driver.title)