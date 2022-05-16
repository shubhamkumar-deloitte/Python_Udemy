from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    checkBox = (By.ID, "exampleCheck1")
    select = (By.ID, "exampleFormControlSelect1")
    submitBtn = (By.CSS_SELECTOR, "input[type='submit']")

    def shopItems(self):
        # self.driver.find_element(*HomePage.shop).click(), then in test class home.shopItems()
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getSelect(self):
        return self.driver.find_element(*HomePage.select)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.submitBtn)
