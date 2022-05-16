import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageObjects.homepage import HomePage

from utilities.BaseClass import BaseClass

from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        # driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")
        # driver.get("https://rahulshettyacademy.com/angularpractice/")  # launch the url
        # driver.maximize_window()

        homepage = HomePage(self.driver)

        # homepage.getName().send_keys("shubham")
        # homepage.getEmail().send_keys("email")

        homepage.getName().send_keys(getData["firstName"])
        homepage.getEmail().send_keys(getData["lastName"])
        homepage.getCheckBox().click()
        # sel = Select(homepage.getSelect())
        # sel.select_by_visible_text("Male")
        self.selectBtText(homepage.getSelect(), getData["gender"])
        homepage.getSubmitBtn().click()
        self.driver.refresh()

        # driver.find_element_by_css_selector("[name='name']").send_keys("shubham")
        # driver.find_element_by_name("email").send_keys("Shubham")
        # driver.find_element_by_id("exampleCheck1").click()
        # time.sleep(4)
        #
        # sel = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        # sel.select_by_visible_text("Male")
        # driver.find_element_by_css_selector("input[type='submit']").click()
        # time.sleep(4)

    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    # in the first iteration ("Shubham", "Kumar", "Male") will be passed and if we do getdata[0] we will get shubham
    # in the second iteration ("lady", "lady", "Female") will be passed and if we do getdata[0], we will get lady
    def getData(self, request):
        return request.param

