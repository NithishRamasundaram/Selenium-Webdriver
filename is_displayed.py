from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://omayo.blogspot.com/")
driver.maximize_window()
if driver.find_element(By.ID,"hbutton").is_displayed():
    print("login")
else:
    print('failed')
driver.implicitly_wait(10)
driver.close()