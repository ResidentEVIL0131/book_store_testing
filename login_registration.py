from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id('menu-item-50').click()
email = driver.find_element_by_id('reg_email')
email.send_keys("starkindustries@mail.com")
password = driver.find_element_by_id('reg_password')
password.send_keys("012kIsAkD12")
driver.find_element_by_name("register").click()
driver.quit()