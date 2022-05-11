from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")  # launch the url
driver.maximize_window()
driver.find_element_by_name("name").send_keys("shubham")
text = driver.execute_script('return document.getElementsByName("name")[0].value')  # extracting the text from inpit field
print(text)

# click using js executor
shopBtn = driver.find_element(by=By.CSS_SELECTOR, value="a[href*='shop']")
driver.execute_script("arguments[0].click();", shopBtn)  # click using js

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")  # scroll to bottom of the page
