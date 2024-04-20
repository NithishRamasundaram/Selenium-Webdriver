import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(
    "https://www.google.com/search?q=amazon&rlz=1C1CHBF_enIN1031IN1031&oq=a&gs_lcrp=EgZjaHJvbWUqDAgAECMYJxiABBiKBTIMCAAQIxgnGIAEGIoFMhgIARAuGEMYgwEYxwEYsQMY0QMYgAQYigUyBggCEEUYQDIGCAMQRRg8MgYIBBBFGD0yBggFEEUYPDIGCAYQRRg8MgYIBxAFGEDSAQgxMjgyajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")
driver.maximize_window()
driver.implicitly_wait(5)
try:
    driver.find_element(By.XPATH, "//span[text()='Shop online at Amazon India']").click()
except:
    print("exceptional handles")
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("Watches for men")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
driver.implicitly_wait(6)
driver.find_element(By.XPATH,"//span[@class='a-size-base-plus a-color-base a-text-normal']").click()
driver.implicitly_wait(15)
switch_windows = driver.window_handles
driver.switch_to.window(switch_windows[1])
driver.find_element(By.XPATH,"//input[@id='buy-now-button']").click()
driver.implicitly_wait(10)
driver.close()
