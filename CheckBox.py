import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkBoxList = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkBox in checkBoxList:
    if checkBox.get_attribute("value") == "option1":
        checkBox.click()
        assert checkBox.is_selected()
        break

radioList = driver.find_elements(By.XPATH,"//input[@type='radio']")
for radio in radioList:
    if radio.get_attribute("value") == "radio1":
        radio.click()
        assert radio.is_selected()
        break


assert driver.find_element(By.ID, "displayed-text").is_displayed()

# driver.find_element(By.ID,"hide-textbox").click()
#time.sleep(5)
assert driver.find_element(By.ID, "displayed-text").is_displayed()


driver.find_element(By.NAME,"enter-name").send_keys("TESTING")
driver.find_element(By.ID,"alertbtn").click()

alert = driver.switch_to.alert
print(alert.text)
assert "TESTING" in alert.text
time.sleep(5)
alert.accept()
time.sleep(5)
#alert.dismiss()



time.sleep(5)
