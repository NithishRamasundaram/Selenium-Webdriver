import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(15)

driver.get("https://www.amazon.in/s?k=watches+for+men&crid=2Z5OTAZR1S8TD&sprefix=%2Caps%2C260&ref=nb_sb_ss_recent_1_0_recent")
driver.maximize_window()
driver.find_element(By.XPATH,"(//span[text()='Stainless Steel Analog Watch'])[1]").click()
driver.switch_to.frame(0)
driver.switch_to.frame(driver.find_element(By.XPATH,"//input[@id='buy-now-button']").click())
time.sleep(10)
driver.close()