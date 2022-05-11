from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        # self.driver.find_element(*HomePage.shop).click(), then in test class home.shopItems()
        return self.driver.find_element(*HomePage.shop)
