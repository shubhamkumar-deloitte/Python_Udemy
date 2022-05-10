import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")  # launch the url
driver.maximize_window()

driver.find_element(by=By.CLASS_NAME, value="search-keyword").send_keys("ber")

time.sleep(2)
add_to_cart_buttons = driver.find_elements(by=By.CSS_SELECTOR, value="div.product div.product-action button")

print(len(add_to_cart_buttons))

for button in add_to_cart_buttons:  # iterating over all the product and clicking on add to cart
    button.click()

driver.find_element(by=By.CSS_SELECTOR, value="a.cart-icon").click()  # clicking on cart icon
driver.find_element(by=By.CSS_SELECTOR, value="div.cart-preview  div.action-block button").click()  # clicking on proceed to checkout button

time.sleep(2)
driver.find_element(by=By.CLASS_NAME, value="promoCode").send_keys("rahulshettyacademy")
driver.find_element(by=By.CLASS_NAME, value="promoBtn").click()

time.sleep(6)

assert driver.find_element(by=By.CLASS_NAME, value="promoInfo").text == "Code applied ..!"
