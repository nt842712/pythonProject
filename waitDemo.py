import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys("ber")
time.sleep(5)
productList = driver.find_elements(By.XPATH,'//*[@class="products"]/div')

assert len(productList) > 0
#time.sleep(3)

for product in productList:
    product.find_element(By.XPATH,'div/button').click()

#time.sleep(3)

driver.find_element(By.CSS_SELECTOR,'img[alt="Cart"]').click()
driver.find_element(By.XPATH,"//*[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(5)

driver.find_element(By.CSS_SELECTOR,'.promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,'.promoBtn').click()
#time.sleep(10)

wait = WebDriverWait(driver,10)

wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)

