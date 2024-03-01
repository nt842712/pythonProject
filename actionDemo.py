import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()

action=ActionChains(driver)

#action.double_click()

action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()


action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()

time.sleep(10)