class Locator(object):

    def __init__(self, my_name):
        self.my_name = my_name

    def get_value(self):
        return self.my_name

    def __str__(self):
        return str(self.__module__)
