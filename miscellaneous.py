import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#service_obj = Service("/Users/ntalesha/Downloads/chromedriver-mac/chromedriver")
options = Options()

# this parameter tells Chrome that
# it should be run without UI (Headless)
options.headless = True
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
#driver.get_screenshot_as_file("test.png")
# driver.execute_script("window.print();")

#driver.get_screenshot_as_png()


#driver.quit()
