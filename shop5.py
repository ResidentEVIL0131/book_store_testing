from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id('menu-item-40').click()
driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()
item = driver.find_element_by_css_selector(".cartcontents")
item_get_text = item.text
assert item_get_text == "1 Item"
price = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
price_get_text = price.text
assert price_get_text == "₹180.00"
cart = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/basket/"]')
cart.click()
subtotal = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal"), "₹180.00")
)
total = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total"), "₹183.60")
)
driver.quit()