import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id('menu-item-40').click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()
time.sleep(4)
driver.find_element_by_css_selector('[href="/shop/?add-to-cart=180"]').click()
driver.find_element_by_css_selector('.cartcontents').click()
time.sleep(3)
#driver.find_element_by_css_selector('[data-product_id="182"]').click()
#driver.find_element_by_css_selector('.woocommerce-message a').click()
num = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
num.clear()
num.send_keys(3)
element = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
element_check = element.get_attribute("value")
element_check == "3"
time.sleep(3)
driver.find_element_by_css_selector('[value="Apply Coupon"]').click()
element2 = driver.find_element_by_css_selector(".woocommerce-error li")
element2_get_text = element2.text
assert element2_get_text == "Please enter a coupon code."
driver.quit()