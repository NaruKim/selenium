from selenium import webdriver

chrome_driver_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")

# price = driver.find_element_by_id("priceblock_ourprice")
# title = driver.find_element_by_id("productTitle")
# print(price.text)
# print(title.text)

# link = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[4]/a')
# print(link.text)

events_dict = {}

times = driver.find_elements_by_css_selector(".menu time")

names = driver.find_elements_by_css_selector(".shrubbery .menu a")

for i in range(5,10):
    events_dict[i - 5] = {'time':times[i].text, 'name':names[i].text}









# driver.close() #close the tab
driver.quit() #quit the browser