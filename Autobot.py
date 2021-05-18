import os

from rich import print
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from combiners.cancel import Cancel
from combiners.close import Close
from combiners.create import Create
from combiners.ldmaworker import Parser
from prettify import prettify_ldma
from prettify.driver_prettify import MenuLayout, get_menu_choice
from utilites.static_data import LDMAData, BMCData

"""
Module Name: Autobot.py
----------------------
This is the main class for running the application. From here
all the functions can be called. This will be the user interface
from here. User's will choose the actions to do on BMC Remedy.

written by: jiaul_islam
"""


class Browser:
    """ A independent class for calling the browser WebDriver """
    browser: WebDriver = None

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
        cls.browser: WebDriver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    @classmethod
    def tearDownDriver(cls):
        cls.browser.quit()

    @classmethod
    def __del__(cls):
        del cls


class Handler(Browser):
    """ A Sub-Class of Driver for additional functionalities.
        Example: Headless Mode, Session Handle, Cookies Handle, Open Links
    """

    def __init__(self):
        super().setUpDriver()

    def get_bmc_website(self):
        """ Get the BMC Remedy URL """
        self.browser.get(BMCData.BMC_URL)

    def get_ldma_website(self):
        """ Get the LDMA URL """
        self.browser.get(LDMAData.LDMA_URL)

    def get_maximize_window(self):
        """ Maximize the current window of driver """
        self.browser.maximize_window()


class CreateNewChangeRequest(Handler, Create):
    """ A Sub-Class of Handler and CreateChangeRequest module to create new Change Requests """

    __createChangeRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def createRequest(self):
        """ Call all the functions from CreateChangeRequest to create change requests """
        self.get_bmc_website()
        self.__createChangeRequest = Create(self.browser)
        self.__createChangeRequest.CreateNCR()


class CloseChangeRequest(Handler, Close):
    """ A Sub-Class of Handler and CloseChangeRequest module to close Change Requests """

    __closeMyRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def closeRequest(self):
        """ Call all the functions from CloseChangeRequests to close change requests """
        self.get_bmc_website()
        self.__closeMyRequest = Close(self.browser)
        self.__closeMyRequest.CloseRequest()


class CancelChangeRequests(Handler, Cancel):
    """ A Sub-Class of Handler and CancelChangeRequest module to Cancel Change Requests """

    __cancelMyRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def cancelRequests(self):
        """ Call all the functions from CancelChangeRequests to cancel change requests """
        self.get_bmc_website()
        self.__cancelMyRequest = Cancel(self.browser)
        self.__cancelMyRequest.CancelRequest()


class ParserLDMA(Handler, Parser):

    __parser = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def test_parse_ldma(self, link_ids: list[str] = None, site_ids: list[str] = None):
        self.get_ldma_website()
        self.__parser = Parser(self.browser)
        self.__parser.ParseLinkBudget(link_ids, site_ids)


def main():
    """ The typical main function to start the program """

    while True:
        print(MenuLayout())
        choice: int = get_menu_choice()
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
            while True:
                print(prettify_ldma.MainMenuLayout())
                choice: int = prettify_ldma.get_choice()
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
                elif choice == 0:
                    break
        elif choice == 0:
            break


if __name__ == "__main__":
    main()
