import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

file_path="/Users/ntalesha/Downloads/download.xlsx"

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.CSS_SELECTOR,"#downloadButton").click()

#edit excel


file_input = driver.find_element(By.CSS_SELECTOR,"#fileinput")
file_input.send_keys(file_path)

WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[text()='Updated Excel Data Successfully.']")))
print(driver.find_element(By.XPATH,"//div[text()='Updated Excel Data Successfully.']").text)

priceColID = driver.find_element(By.XPATH,"//*[text()='Price']").get_attribute("data-column-id")
fruit_name = "Apple"
priceval = driver.find_element(By.XPATH,"//*[text()='"+fruit_name+"']/../..//div[@id='cell-"+priceColID+"-undefined']/div").text
print(priceval)


time.sleep(7)