import time

import pytest
from selenium.webdriver.common.by import By


from pageObjects.homepage import HomePage
from utilities.BaseClass import BaseClass
from pageObjects.checkoutpage import CheckOut
from pageObjects.confirmpage import confirmPage


class TestOne(BaseClass):

    def test_homepage(self):

        log = self.getLogger()
        log.info("inside homepage")

        # home page object
        home = HomePage(self.driver)
        home.shopItems().click()
        log.info("clicked on shop link")

    def test_checkoutpage(self):
        log = self.getLogger()
        log.info("inside checkout")
        # checkout page object

        checkout = CheckOut(self.driver)
        checkout.selectPhone().click()
        log.info("clicked on phone to be bought")
        checkout.get_checkoutBtn().click()  # clicking on checkout btn
        log.info("clicked on first checkout ")

    def test_confirm(self):

        confirmpage = confirmPage(self.driver)
        confirmpage.get_secondCheckout().click()
        time.sleep(3)
        confirmpage.get_inputField().send_keys("ind")
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        confirmpage.get_purchase().click()















