from selenium.webdriver.common.by import By


class Locator(object):

    def __str__(self):
        return str(self.__module__)

    @staticmethod
    def get_by_Xpath(XPATH: str) -> tuple:
        """
        Get the XPATH Value for passed XPATH element in DOM

        Args:
            XPATH (str) : The XPATH string which to get from DOM

        Raises:
            Module Error for By Class not Found

        Returns:
            A tuple of contains the By Class & String of element to find element XPATH.
            Ex: (By.XPATH, "//input[@id='txtUsername']"

        """
        return By.XPATH, XPATH
