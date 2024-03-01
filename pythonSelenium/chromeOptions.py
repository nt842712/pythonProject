import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#service_obj = Service("/Users/ntalesha/Downloads/chromedriver-mac-arm64 4/chromedriver")
#driver = webdriver.Chrome(service=service_obj)


chrom_options = webdriver.ChromeOptions()
chrom_options.add_argument("--start-maximized")

chrom_options.add_argument("headless")
chrom_options.add_argument('--ignore-certificate-errors')
# chrome driver services
driver = webdriver.Chrome(options=chrom_options)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

print(driver.title)