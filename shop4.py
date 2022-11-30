from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
driver.find_element_by_css_selector('[title="Android Quick Start Guide"]').click()
price = driver.find_element_by_css_selector('del')
price_get_text = price.text
assert price_get_text == "₹600.00"
pricecell = driver.find_element_by_css_selector('ins .amount')
pricecell_get_text = pricecell.text
assert pricecell_get_text == "₹450.00"
book = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Android Quick Start Guide']"))
)
book.click()
close = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close"))
)
close.click()
driver.quit()