from selenium import webdriver
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
driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product-category/html/"]').click()
amount = driver.find_element_by_css_selector('.cat-item-19 .count')
amount_get_text = amount.text
assert amount_get_text == "(3)"
driver.quit()