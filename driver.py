from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utilities.static_data import StaticData, LDMAData
from tests.testCloseRequest import CloseChangeRequests
from tests.testCreateRequest import CreateChangeRequest
from tests.testCancelRequest import CancelChangeRequest
from pages.ldma import ParseLinkBudget

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
            elif choice == 4:
                # Parse LDMA LB
                browser = webdriver.Chrome(ChromeDriverManager().install())
                browser.maximize_window()
                parse_info = ParseLinkBudget(browser)
                browser.get(LDMAData.LDMA_URL)
                parse_info.login_ldma()
                link_id = ["DH23H02512", "DH23H03255"]
                for id in link_id:
                    parse_info.goto_links()
                    parse_info.insert_link_code(id)
                    parse_info.select_all_dropdown()
                    parse_info.click_search()
                    parse_info.select_found_link_code(str(id))
                parse_info.logout_ldma()
                browser.quit()
            elif choice == 0:
                print("Exiting Program !")
                break
            else:
                print("Invalid choice ! Try Again.")
        except ValueError as e:
            print(e)
            print("Invalid key pressed ! Please Try Again.")


if __name__ == "__main__":
    main()
