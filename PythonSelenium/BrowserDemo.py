from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\shubhamkumar32\\Downloads\\chromedriver.exe")

driver.get("https://www.google.com")  # launch the url
driver.maximize_window()
print(driver.current_url)
driver.back()  # navigate back
driver.refresh()  # refresh
driver.quit()



