from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/shop")  # launch the url
driver.maximize_window()

mobiles = driver.find_elements(by=By.XPATH, value="//div[@class='card h-100']/div/h4/a")

for mobile in mobiles:
    print(mobile.text)
    if mobile.text == "Blackberry":
        print("found")
        mobile.find_element(by=By.XPATH, value="parent::h4/parent::div/parent::div/div[@class='card-footer']/button").click()


driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
successText = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in successText

driver.get_screenshot_as_file("screen.png")


