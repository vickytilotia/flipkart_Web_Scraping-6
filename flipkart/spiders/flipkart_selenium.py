"""
from selenium import webdriver
from shutil import which

# To use headless browser: chrome will not popup
'''from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")

chrome_path = which("./chromedriver.exe")
driver  = webdriver.Chrome(executable_path= chrome_path, options=chrome_options)
'''

chrome_path = which("./chromedriver.exe")

driver  = webdriver.Chrome(executable_path= chrome_path)
driver.get("https://www.flipkart.com")  

# check_useragent = browser.execute.script()

#search_bar = driver.find_element_by_id("search_form_input_homepage")
# search_input = driver.find_element_by_xpath("//div[@class = 'nav-search-field ']")
search_input = driver.find_element_by_xpath("//div[@class='_3OO5Xc']/input")
search_input.send_keys("laptop")

login_box = driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']")
login_box.click()

search_btn = driver.find_element_by_xpath("//button[@class='L0Z3Pu']")
search_btn.click()

# to use enter instead of mouse click
# from selenium.webdriver.common.keys import Keys
# search_input.send_keys(Keys.ENTER)

#to print html in terminal
# print(driver.page_source)

#always close your driver to save ram
# driver.close()

"""