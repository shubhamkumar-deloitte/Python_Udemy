from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")

driver.get("https://www.google.com")  # launch the url
driver.maximize_window()
print(driver.current_url)
driver.back()  # navigate back
driver.refresh()  # refresh




