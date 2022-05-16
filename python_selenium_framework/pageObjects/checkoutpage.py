import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class CheckOut:

    def __init__(self, driver):
        self.driver = driver

    # mobiles = driver.find_elements(by=By.XPATH, value="//div[@class='card h-100']/div/h4/a")

    mobile = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    mobile_link_to_be_clicked = (By.XPATH, "parent::h4/parent::div/parent::div/div[@class='card-footer']/button")
    checkout_btn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    second_checkoutBtn = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def selectPhone(self):
        mobiles = self.driver.find_elements(*CheckOut.mobile)
        for mobile in mobiles:
            print(mobile.text)
            if mobile.text == "Blackberry":
                print("found")
                return mobile.find_element(*CheckOut.mobile_link_to_be_clicked)

    def get_checkoutBtn(self):
        return self.driver.find_element(*CheckOut.checkout_btn)

    def get_secondCheckout(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, CheckOut.second_checkoutBtn)))
        return self.driver.find_element(*CheckOut.second_checkoutBtn)





