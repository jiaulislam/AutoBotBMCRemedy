from ROC.Locators.Locator import Locator


class HomePage(Locator):

    def __init__(self, my_name):
        super().__init__(my_name)

    def __str__(self):
        return str(self.__module__)
