import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

driver.switch_to.frame(driver.find_element(By.ID,"mce_0_ifr"))

driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate")

driver.switch_to.default_content()
assert (driver.find_element(By.CSS_SELECTOR,'.example').is_displayed())

driver.quit()