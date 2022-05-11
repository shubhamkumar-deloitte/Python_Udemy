from selenium import webdriver


chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe", options=chrome_option)

driver.get("https://rahulshettyacademy.com/angularpractice/")  # launch the url


