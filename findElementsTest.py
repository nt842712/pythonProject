import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https:rahulshettyacademy.com/dropdownsPractise")
driver.maximize_window()
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(5)

# countOfVal = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
countOfVal = driver.find_elements(By.XPATH, "//*[contains(@class,'ui-menu-item')]//a")

for val in countOfVal:
    print(val.text)
    if val.text == "India":
        val.click()
        break

getCountry=driver.find_element(By.ID, "autosuggest").get_attribute("value")

assert "Indi" == getCountry



print(len(countOfVal))
