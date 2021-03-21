from selenium import webdriver
import time

chrome_driver_path = "C:/development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
# for i in upgrades:
#     print(i.text.split('-')[-1].replace(',',''))

timeout = time.time() + 5

while True:
    cookie.click()
    if time.time() > timeout:
        driver.find_element_by_id("buyGrandma").click()
        timeout = time.time() + 5