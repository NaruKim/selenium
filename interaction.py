from selenium import webdriver
from selenium.webdriver.common.keys import Keys #컨트롤 클릭하면 된다.

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_driver_path = "C:/development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count.click()

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
