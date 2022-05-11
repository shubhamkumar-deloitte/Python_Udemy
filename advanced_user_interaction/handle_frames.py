from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/iframe")  # launch the url
driver.maximize_window()
# give frame id, frame name or index value
driver.switch_to.frame("mce_0_ifr")  # switched to frame

driver.find_element(by=By.ID, value="tinymce").clear()
driver.find_element(by=By.ID, value="tinymce").send_keys("Hello")

driver.switch_to.default_content()  # switched out of frame, very important to do
