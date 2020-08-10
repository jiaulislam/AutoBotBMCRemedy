from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utilities.static_data import StaticData
from tests.testCreateRequest import CreateChangeRequest
from tests.testCloseRequest import CloseChangeRequests
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

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def createRequest(self):
        self.createChangeRequest = CreateChangeRequest(self.driver)
        self.createChangeRequest.test_create_change()


class CloseChangeRequest(Handler, CloseChangeRequests):

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def closeRequest(self):
        self.closeMyRequest = CloseChangeRequests(self.driver)
        self.closeMyRequest.test_close_requests()


class CancelChangeRequests(Handler, CancelChangeRequest):

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def cancelRequests(self):
        self.cancelMyRequest = CancelChangeRequest(self.driver)
        self.cancelMyRequest.test_cancel_change()


def main():
    cr = CreateNewChangeRequest()
    cr.createRequest()
    cr.finishDriver()


if __name__ == "__main__":
    main()
