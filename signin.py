from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "http://secure-retreat-92358.herokuapp.com/"
chrome_driver = "C:/development\chromedriver.exe" # /\섞어도 돌아간다
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(URL)

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

first_name.send_keys("Naru")
last_name.send_keys("Kim")
email.send_keys("wolfthestrider@naver.com")
email.send_keys(Keys.ENTER)

# submit = driver.find_elements_by_css_selector("form button")
# submit.click()