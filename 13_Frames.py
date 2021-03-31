from selenium import webdriver

driver = webdriver.Chrome("D:\Stuffs\Python\LearnPython\PythonSelenium\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/package-summary.html")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium.devtools").click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("DevTools").click()

driver.switch_to.parent_frame()

driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()

#driver.close()