from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
element=driver.find_element(By.XPATH,"//div[@class='post-body entry-content']").text
print(element)
driver.implicitly_wait(5)
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH,"//a[@id='link1']").click()
print(driver.current_url)
driver.implicitly_wait(44)
driver.close()