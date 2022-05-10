import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")

driver.get("http://3.110.88.201/dropdownsPractise/")  # launch the url
driver.maximize_window()

driver.find_element(by=By.ID, value="autosuggest").send_keys("ind")
time.sleep(2)

names = driver.find_elements(by=By.CLASS_NAME, value="ui-corner-all")  # saving in variable names which is a list

for name in names:  # iterating over the list and clicking on India
    if name.text == "India":
        name.click()
        break

selected_country = driver.find_element(by=By.ID, value="autosuggest").get_attribute("value")
assert "India" == selected_country  # asserting whether the India has been selected or not
