from selenium.webdriver.common.by import By
from typing import Tuple


class Locator(object):

    def __str__(self):
        return str(self.__module__)

    @staticmethod
    def get_by_Xpath(XPATH: str) -> Tuple[By, str]:
        """
        Get the XPATH Value for passed XPATH element in DOM

        Args:
            XPATH (str) : The XPATH string which to get from DOM
        return:
            A tuple of contains the By Class & String of element to find element XPATH
            Ex: (By.XPATH, //input[@id='txtUsername']
        Raises:
            Module Error for By Class not Found

        """
        return By.XPATH, XPATH
