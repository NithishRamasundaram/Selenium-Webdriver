from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=best+urls+for+testing+purpose&rlz=1C1CHBF_enIN1031IN1031&oq=best+urls+for+tes&gs_lcrp=EgZjaHJvbWUqBwgCECEYnwUyBggAEEUYOTIJCAEQIRgKGKABMgcIAhAhGJ8FMgcIAxAhGJ8FMgcIBBAhGJ8FMgcIBRAhGJ8F0gEKMTE1NjBqMGoxNagCCLACAQ&sourceid=chrome&ie=UTF-8")
driver.maximize_window()
driver.find_element(By.XPATH, "//h3[text()='Need a good website URL to test against']").click()
if driver.find_element(By.XPATH,"//a[@class='s-topbar--item s-topbar--item__unset s-btn s-btn__outlined ws-nowrap js-gps-track']").is_displayed():
    print("login")
else:
    print("Failed")
driver.implicitly_wait(12)
driver.close()
