from select import select

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")  # launch the url
driver.maximize_window()
print(driver.current_url)

driver.refresh()  # refresh

# select class to handle dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
# dropdown.select_by_value(), the dropdown should have value attribute


