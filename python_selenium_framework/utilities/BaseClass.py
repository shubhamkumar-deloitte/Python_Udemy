import inspect

import pytest
import  logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects import homepage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logs.log')  # file
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s : %(message)s")  # defining the format of logs messages
        fileHandler.setFormatter(formatter)  # passing the format to filehandler and passing filahandler to logger
        logger.addHandler(fileHandler)  # filehandler object into it, what format and what file

        logger.setLevel(logging.DEBUG)  # level set to INFO, it will skip all debug logs

        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectBtText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
