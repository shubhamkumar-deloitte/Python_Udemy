from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")  # launch the url
driver.maximize_window()

driver.find_element(by=By.LINK_TEXT, value="Click Here").click()  # opens a new window
childWindow = driver.window_handles[1]

driver.switch_to.window(childWindow)  # switched to child window
print(driver.find_element(by=By.TAG_NAME, value="h3").text)
driver.close()  # closed child window

driver.switch_to.window(driver.window_handles[0])  # switched to parent window
driver.close()  # closed parent window

