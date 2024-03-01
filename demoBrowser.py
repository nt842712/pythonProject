import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service_obj = Service("/Users/ntalesha/Downloads/chromedriver-mac-arm64 4/chromedriver")
#driver = webdriver.Chrome(service=service_obj)

# chrome driver services
driver = webdriver.Edge()
driver.get("https:rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)























time.sleep(3)