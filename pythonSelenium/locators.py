import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#service_obj = Service("/Users/ntalesha/Downloads/chromedriver-mac-arm64 4/chromedriver")
#driver = webdriver.Chrome(service=service_obj)

# chrome driver services
driver = webdriver.Chrome()
driver.get("https:rahulshettyacademy.com/angularpractice")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.NAME,"name").send_keys("TESTING")
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Password@123")
driver.find_element(By.ID,"exampleCheck1").click()
dropDown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))

dropDown.select_by_visible_text("Female")
time.sleep(5)
dropDown.select_by_index(0)

message = driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/div[1]/label").text
driver.find_element(By.NAME,"name").clear()
assert "Name" in message
print(message)


time.sleep(3)