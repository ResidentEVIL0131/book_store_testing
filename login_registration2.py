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
logout = driver.find_element_by_class_name("woocommerce-MyAccount-navigation-link--customer-logout")
logout_get_text = logout.text
assert logout_get_text == "Logout"
driver.quit()