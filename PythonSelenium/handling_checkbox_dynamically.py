from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")  # launch the url
driver.maximize_window()


checkboxes = driver.find_elements(by=By.XPATH, value="//input[@type='checkbox']")
for checkbox in checkboxes:  # iterating over the list and clicking on all checkboxes
    checkbox.click()
    assert checkbox.is_selected()  # checking whether checkbox is selected or not

for checkbox in checkboxes:  # clicking on a particular checkbox by its value
    if checkbox.get_attribute("value") == "option1":
        checkbox.click()
        assert checkbox.is_selected()  # checking whether checkbox is selected or not,
        # it will fail bcz we have already iterated over all the
        # checkboxes and clicked and if we click again then it will get unselected



