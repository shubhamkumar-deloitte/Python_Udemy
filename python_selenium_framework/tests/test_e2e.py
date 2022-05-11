import time

import pytest
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass

from pageObjects.homepage import HomePage

from pageObjects.checkoutpage import CheckOut


class TestOne(BaseClass):

    def test_homepage(self):
        print("inside homepage")

        # home page object
        home = HomePage(self.driver)
        home.shopItems().click()

    def test_checkoutpage(self):
        print("inside checkout")
        # checkout page object

        checkout = CheckOut(self.driver)
        checkout.selectPhone().click()
        checkout.get_checkoutBtn().click()  # clicking on checkout btn










