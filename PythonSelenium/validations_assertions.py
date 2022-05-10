from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")  # launch the url
driver.maximize_window()
print(driver.current_url)

driver.refresh()  # refresh

# select class to handle dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown = Select(driver.find_element(by=By.ID, value="exampleFormControlSelect1"))  # select object
dropdown.select_by_visible_text("Female")  # selecting in dropdown
# dropdown.select_by_value(), the dropdown should have value attribute

# driver.find_element_by_css_selector("input.btn-success").click()
driver.find_element(by=By.CSS_SELECTOR, value="input.btn-success").click()
# success_message = driver.find_element_by_css_selector("div.alert-success").text
success_message = driver.find_element(by=By.CSS_SELECTOR, value="div.alert-success").text
assert "success" in success_message  # asserting the success message

# assert "success" == message , if we want to compare entire string

