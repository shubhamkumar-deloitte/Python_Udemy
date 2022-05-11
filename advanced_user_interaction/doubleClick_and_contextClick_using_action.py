from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")  # launch the url
driver.maximize_window()

action = ActionChains(driver)
action.context_click(driver.find_element(by=By.ID, value="double-click")).perform()  # right click
action.double_click(driver.find_element(by=By.ID, value="double-click")).perform()
alert = driver.switch_to.alert
alert.accept()
