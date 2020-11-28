import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from tests.testCancelRequest import CancelChangeRequest
from tests.testCloseRequest import CloseChangeRequests
from tests.testCreateRequest import CreateChangeRequest
from utilities.static_data import StaticData, LDMAData
from tests.testLDMA import LDMA_Parser
from utilities.terminal_colors import bcolors

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
        options = Options()
        # options.headless = True # Run the Chrome driver in headless mode
        # options.add_argument("--disable-gpu") # It's recommended to turn of GPU while headless mode
        options.add_argument("--log-level=3")  # disable Info/Error/Warning in Chrome Driver
        options.add_experimental_option('excludeSwitches',
                                        ['enable-logging'])  # disable Dev Info info while running app
        options.add_argument("--start-maximized")  # start the chrome with maximized window
        os.environ['WDM_LOG_LEVEL'] = '0'  # Disable the logging of ChromeDriverManager()
        cls.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

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

    def get_bmc_website(self):
        """ Get the BMC Remedy URL """
        self.browser.get(StaticData.BMC_URL)

    def get_ldma_website(self):
        """ Get the LDMA URL """
        self.browser.get(LDMAData.LDMA_URL)

    def get_maximize_window(self):
        """ Maximize the current window of driver """
        self.browser.maximize_window()


class CreateNewChangeRequest(Handler, CreateChangeRequest):
    """ A Sub-Class of Handler and CreateChangeRequest module to create new Change Requests """

    __createChangeRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def createRequest(self):
        """ Call all the functions from CreateChangeRequest to create change requests """
        self.get_bmc_website()
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
        self.get_bmc_website()
        self.__closeMyRequest = CloseChangeRequests(self.browser)
        self.__closeMyRequest.test_close_requests()


class CancelChangeRequests(Handler, CancelChangeRequest):
    """ A Sub-Class of Handler and CancelChangeRequest module to Cancel Change Requests """

    __cancelMyRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def cancelRequests(self):
        """ Call all the functions from CancelChangeRequests to cancel change requests """
        self.get_bmc_website()
        self.__cancelMyRequest = CancelChangeRequest(self.browser)
        self.__cancelMyRequest.test_cancel_change()


class ParserLDMA(Handler, LDMA_Parser):

    __parser = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def test_parse_ldma(self, link_ids: list = None, site_ids: list = None):
        self.get_ldma_website()
        self.__parser = LDMA_Parser(self.browser)
        self.__parser.parse_link_budget(link_ids, site_ids)


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
            " 4. Parse Link Budget\n"
            " 0. Quit Application\n"
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
                # Parse Link Budget from LDMA
                print("==>Press 1 for parse with Link ID\n==>Press 2 for parse with Site ID\n==>Press 3 for go-back\n")
                while True:
                    try:
                        choice = int(input("Press: "))
                        if choice == 1:
                            LinkID = input("\nPlease Enter LinkID: ")
                            link_ids = LinkID.split(",")
                            parse = ParserLDMA()
                            parse.test_parse_ldma(link_ids=link_ids)
                            parse.tearDownDriver()
                        elif choice == 2:
                            site_id = input("\nPlease Enter SiteID: ")
                            site_ids = site_id.split(',')
                            parse = ParserLDMA()
                            parse.test_parse_ldma(site_ids=site_ids)
                            parse.tearDownDriver()
                        elif choice == 3:
                            break
                        else:
                            print(f"Invalid input {choice}. Please use 1 or 2")
                    except ValueError as error:
                        print(f"\n{bcolors.FAIL}{error}{bcolors.ENDC}\n")
            elif choice == 5:
                # Expedited CR
                # TODO: EXPERIMENTAL 
                create = CreateNewChangeRequest()
                create.createRequest()
                create.tearDownDriver()
            elif choice == 0:
                print("\nExiting Program !\n")
                break
            else:
                print("\nInvalid choice ! Try Again.\n")
        except ValueError as e:
            print(f"\n{bcolors.FAIL}{e}{bcolors.ENDC}\n")


if __name__ == "__main__":
    main()
