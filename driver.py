from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utilities.static_data import StaticData
from tests.testCloseRequest import CloseChangeRequests
from tests.testCreateRequest import CreateChangeRequest
from tests.testCancelRequest import CancelChangeRequest

"""
Module Name: driver.py
----------------------
This is the main class for running the application. From here
all the functions can be called. This will be the user interface
from here. User's will choose the actions to do on BMC Remedy.

@Author: w4nn4b3cod3r
"""


class Driver:
    """ A independent class for calling the browser WebDriver """
    browser = None

    @classmethod
    def setUpDriver(cls):
        cls.browser = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def tearDownDriver(cls):
        cls.browser.quit()

    @classmethod
    def __del__(cls):
        del cls


class Handler(Driver):
    """ A Sub-Class of Driver for additional functionalities.
        Example: Headless Mode, Session Handle, Cookies Handle, Open Links
    """
    def __init__(self):
        super().setUpDriver()
        # Open the Link
        self.browser.get(StaticData.BASE_URL)
        # Maximize the Window
        self.browser.maximize_window()


class CreateNewChangeRequest(Handler, CreateChangeRequest):
    """ A Sub-Class of Handler and CreateChangeRequest module to create new Change Requests """

    __createChangeRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def createRequest(self):
        """ Call all the functions from CreateChangeRequest to create change requests """
        self.__createChangeRequest = CreateChangeRequest(self.browser)
        self.__createChangeRequest.test_create_change()


class CloseChangeRequest(Handler, CloseChangeRequests):
    """ A Sub-Class of Handler and CloseChangeRequest module to close Change Requests """

    __closeMyRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def closeRequest(self):
        """ Call all the functions from CloseChangeRequests to close change requests """
        self.__closeMyRequest = CloseChangeRequests(self.browser)
        self.__closeMyRequest.test_close_requests()


class CancelChangeRequests(Handler, CancelChangeRequest):
    """ A Sub-Class of Handler and CancelChangeRequest module to Cancel Change Requests """

    __cancelMyRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def cancelRequests(self):
        """ Call all teh functions from CancelChangeRequests to cancel change requests """
        self.__cancelMyRequest = CancelChangeRequest(self.browser)
        self.__cancelMyRequest.test_cancel_change()


def main():
    """ The typical main function to start the program """

    # User Choice input
    print("\tWelcome ")
    print("++++++++++++++++++++++++++++")
    while True:
        print(
              " 1. Create Change Request\n"
              " 2. Close Change Request\n"
              " 3. Cancel Change Request\n"
              " 0. Quit Application"
        )

        try:
            choice = int(input("\nEnter the Choice -> "))

            if choice == 1:
                # Create Change Request
                create = CreateNewChangeRequest()
                create.createRequest()
                create.tearDownDriver()
                break
            elif choice == 2:
                # Close Change Request
                close = CloseChangeRequest()
                close.closeRequest()
                close.tearDownDriver()
                break
            elif choice == 3:
                # Cancel Change Request
                cancel = CancelChangeRequests()
                cancel.cancelRequests()
                cancel.tearDownDriver()
                break
            elif choice == 0:
                print("Exiting Program !")
                break
            else:
                print("Invalid choice ! Try Again.")
        except ValueError:
            print("Invalid key pressed ! Please Try Again.")


if __name__ == "__main__":
    main()
