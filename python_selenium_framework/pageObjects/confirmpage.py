from selenium.webdriver.common.by import By


class confirmPage:

    def __init__(self, driver):
        self.driver = driver

    second_checkoutBtn = (By.CSS_SELECTOR, "button[class*='btn-success']")
    inputBox = (By.ID, "country")
    purchase = (By.XPATH, "//input[@type='submit']")

    def get_secondCheckout(self):
        # element = WebDriverWait(self.driver, 10).until(
        # EC.presence_of_element_located((By.CSS_SELECTOR, CheckOut.second_checkoutBtn)))
        return self.driver.find_element(*confirmPage.second_checkoutBtn)

    def get_inputField(self):
        return self.driver.find_element(*confirmPage.inputBox)

    def get_purchase(self):
        return self.driver.find_element(*confirmPage.purchase)

