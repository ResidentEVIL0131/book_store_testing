from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id('menu-item-50').click()
username = driver.find_element_by_id('username')
username.send_keys("starkindustries@mail.com")
password = driver.find_element_by_id('password')
password.send_keys("012kIsAkD12")
driver.find_element_by_name("login").click()
driver.find_element_by_id('menu-item-40').click()
sorting = driver.find_element_by_css_selector(".orderby")
sorting_check = sorting.get_attribute("value")
assert sorting_check == "menu_order"
sorting = driver.find_element_by_css_selector(".orderby")
select = Select(sorting)
select.select_by_value("price")
sorting2 = driver.find_element_by_css_selector(".orderby")
sorting2_check = sorting2.get_attribute("value")
assert sorting2_check == "price"
driver.quit()