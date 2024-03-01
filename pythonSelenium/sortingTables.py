import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#service_obj = Service("/Users/ntalesha/Downloads/chromedriver-mac-arm64 4/chromedriver")
#driver = webdriver.Chrome(service=service_obj)

# chrome driver services
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")


driver.find_element(By.XPATH,"//*[span='Veg/fruit name']").click()

fruitName = driver.find_elements(By.XPATH,"//tr//td[1]")

arrayOfFruit=[]

for ele in fruitName:
    arrayOfFruit.append(ele.text)

originalSortedList = arrayOfFruit.copy()

arrayOfFruit.sort()

assert arrayOfFruit == originalSortedList

time.sleep(10)
