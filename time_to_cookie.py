from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = ""
chrome_driver_path = "C:/development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)