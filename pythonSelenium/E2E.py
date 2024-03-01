import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#service_obj = Service("/Users/ntalesha/Downloads/chromedriver-mac-arm64 4/chromedriver")
#driver = webdriver.Chrome(service=service_obj)


chrom_options = webdriver.ChromeOptions()
chrom_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrom_options)
driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element(By.XPATH,"//*[text()='Shop']").click()
listOfProdELe = driver.find_elements(By.XPATH,"//*[@class='card h-100']")

for ele in listOfProdELe:
    phone = ele.find_element(By.XPATH ,"div/h4/a").text
    print(phone)
    if phone == "Blackberry":
        print("Inside")
        ele.find_element(By.XPATH,"div/button").click()
        print("Clicked")


driver.find_element(By.CSS_SELECTOR,".nav-link.btn.btn-primary").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()
driver.find_element(By.CSS_SELECTOR,"#country").send_keys("Ind")
time.sleep(5)
wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))

driver.find_element(By.LINK_TEXT,"India").click()
time.sleep(5)

driver.execute_script("arguments[0].click();",driver.find_element(By.CSS_SELECTOR,"#checkbox2"))
#driver.find_element(By.CSS_SELECTOR,"#checkbox2").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()

success = driver.find_element(By.CLASS_NAME,"alert-success").text

assert "Success! Thank you! " in success
time.sleep(4)

driver.close()