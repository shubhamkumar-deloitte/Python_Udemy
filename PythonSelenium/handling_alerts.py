from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")  # launch the url
driver.maximize_window()

driver.find_element(by=By.ID, value="name").send_keys("Shubham")
driver.find_element(by=By.ID, value="alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
assert "Shubham" in alert.text
alert.accept()  # it will click on Ok in alert body
# alert.dismiss()  # click on cancel in the alert body
