import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\Shubham\\Downloads\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")  # launch the url
    driver.maximize_window()
    request.cls.driver = driver  # now it has become a class variable in which this fixture will be used

