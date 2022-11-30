import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id('menu-item-40').click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()
time.sleep(3)
driver.find_element_by_css_selector('[title="View your shopping cart"]').click()
proceed = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".alt.wc-forward"))
)
proceed.click()
name = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name"))
)
name.send_keys("Tony")
last = driver.find_element_by_css_selector('[name="billing_last_name"]')
last.send_keys("Stark")
email = driver.find_element_by_css_selector('[name="billing_email"]')
email.send_keys("starkindustries@mail.com")
billing = driver.find_element_by_css_selector('[name="billing_phone"]')
billing.send_keys("+82304240023")
driver.find_element_by_id('s2id_billing_country').click()
country = driver.find_element_by_id("s2id_autogen1_search")
country.send_keys("United States")
driver.find_element_by_link_text("United States (US)").click()
address = driver.find_element_by_css_selector('[name="billing_address_1"]')
address.send_keys('Chinatown')
city = driver.find_element_by_css_selector('[name="billing_city"]')
city.send_keys('New-York')
state = driver.find_element_by_css_selector('[name="billing_state"]')
select = Select(state)
select.select_by_visible_text("New York")
postcode = driver.find_element_by_css_selector('[name="billing_postcode"]')
postcode.send_keys("10005")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
driver.find_element_by_css_selector('#payment_method_cheque.input-radio').click()
driver.find_element_by_id('place_order').click()
ty = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received.")
)
pm = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method"), "Check Payments")
)
driver.quit()