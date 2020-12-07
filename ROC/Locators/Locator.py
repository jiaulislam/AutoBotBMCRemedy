class Locator(object):

    def __init__(self, driver):
        self.driver = driver

    def get_value(self):
        return self.driver

    def __str__(self):
        return str(self.__module__)
