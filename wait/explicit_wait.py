

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")  # launch the url
driver.maximize_window()

driver.find_element(by=By.CLASS_NAME, value="search-keyword").send_keys("ber")

wait = WebDriverWait(driver, 7)

time.sleep(2)
add_to_cart_buttons = driver.find_elements(by=By.CSS_SELECTOR, value="div.products div.product div.product-action button")

print(len(add_to_cart_buttons))
# explicit wait
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.products div.product div.product-action button")))
for button in add_to_cart_buttons:  # iterating over all the product and clicking on add to cart
    button.click()

driver.find_element(by=By.CSS_SELECTOR, value="a.cart-icon").click()  # clicking on cart icon
driver.find_element(by=By.CSS_SELECTOR, value="div.cart-preview  div.action-block button").click()  # clicking on proceed to checkout button


driver.find_element(by=By.CLASS_NAME, value="promoCode").send_keys("rahulshettyacademy")
driver.find_element(by=By.CLASS_NAME, value="promoBtn").click()

# explicit wait till element is visible
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

assert driver.find_element(by=By.CLASS_NAME, value="promoInfo").text == "Code applied ..!"
