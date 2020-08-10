from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utilities.static_data import StaticData
from tests.testCloseRequest import CloseChangeRequests
from tests.testCreateRequest import CreateChangeRequest
from tests.testCancelRequest import CancelChangeRequest


class AutoBot:
    driver = None

    @classmethod
    def setUpDriver(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get(StaticData.BASE_URL)

    @classmethod
    def finishDriver(cls):
        cls.driver.quit()

    @classmethod
    def __del__(cls):
        del cls


class Handler(AutoBot):

    def __init__(self):
        super().setUpDriver()


class CreateNewChangeRequest(Handler, CreateChangeRequest):

    __createChangeRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def createRequest(self):
        self.createChangeRequest = CreateChangeRequest(self.driver)
        self.createChangeRequest.test_create_change()


class CloseChangeRequest(Handler, CloseChangeRequests):

    __closeMyRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def closeRequest(self):
        self.__closeMyRequest = CloseChangeRequests(self.driver)
        self.__closeMyRequest.test_close_requests()


class CancelChangeRequests(Handler, CancelChangeRequest):

    __cancelMyRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def cancelRequests(self):
        self.__cancelMyRequest = CancelChangeRequest(self.driver)
        self.__cancelMyRequest.test_cancel_change()


def main():
    cr = CreateNewChangeRequest()
    cr.createRequest()
    cr.finishDriver()


if __name__ == "__main__":
    main()
