import os

from alive_progress import alive_bar
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.ldma import ParseLinkBudget
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
        """ Call all teh functions from CancelChangeRequests to cancel change requests """
        self.get_bmc_website()
        self.__cancelMyRequest = CancelChangeRequest(self.browser)
        self.__cancelMyRequest.test_cancel_change()


class ParserLDMA(Handler, LDMA_Parser):

    __parser = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def parse_ldma(self):
        self.get_ldma_website()
        self.__parser = LDMA_Parser(self.browser)
        self.__parser.parse_link_budget()

    pass


class ParseLB(Handler):
    """ LinkBudget Parser """

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def parse_link_budget(self, link_ids: list = 0, site_ids: list = 0):
        if len(link_ids) > 0:
            self.get_ldma_website()
            parse_info = ParseLinkBudget(self.browser)
            parse_info.login_ldma()
            parse_info.make_dir()
            with alive_bar(len(link_ids)) as bar:
                try:
                    for ID in link_ids:
                        parse_info.goto_links()
                        parse_info.insert_link_code(ID)
                        parse_info.select_all_dropdown()
                        parse_info.click_search()
                        try:
                            parse_info.select_found_link_code(ID)
                            bar()
                        except TimeoutException:
                            print(f"{bcolors.WARNING}Invalid Link ID --> {ID}{bcolors.WARNING}")
                            bar()
                            continue
                        # parse_info.export_pdf_file(id) # Export As PDF
                        parse_info.export_file(ID)  # Export As HTML
                        # parse_info.export_word_file(id) # Export As DOC
                        # parse_info.delete_html_file(id) # Delete the Exported HTML file
                    parse_info.logout_ldma()
                    self.browser.quit()
                except Exception as e:
                    print(e)
        else:
            self.get_ldma_website()
            parse_info = ParseLinkBudget(self.browser)
            parse_info.login_ldma()
            parse_info.make_dir()

            with alive_bar(len(site_ids)) as bar:
                for site in site_ids:
                    parse_info.goto_links()
                    parse_info.select_all_dropdown()
                    parse_info.insert_site_code_1(site)
                    parse_info.click_search()
                    if parse_info.is_lb_found():
                        LINK_ID = parse_info.get_link_id()
                        parse_info.search_lb_with_sitecode(site)
                        parse_info.export_file(LINK_ID)
                        bar()
                        continue
                    parse_info.clear_site_code_1()
                    parse_info.insert_site_code_2(site)
                    parse_info.click_search()
                    if parse_info.is_lb_found():
                        LINK_ID = parse_info.get_link_id()
                        parse_info.search_lb_with_sitecode(site)
                        parse_info.export_file(LINK_ID)
                        bar()
                        continue
                    else:
                        print(f"{site} LB not closed.")
                        bar()
                parse_info.logout_ldma()
                self.browser.quit()


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
                print("==>Press 1 for parse with Link ID\n==>Press 2 for parse with Site ID\n")
                choice = int(input("Press: "))
                if choice == 1:
                    LinkID = input("\nPlease Enter LinkID: ")
                    link_ids = LinkID.split(",")
                    parse = ParseLB()
                    parse.parse_link_budget(link_ids=link_ids)
                    parse.tearDownDriver()
                elif choice == 2:
                    site_id = input("\nPlease Enter SiteID: ")
                    site_ids = site_id.split(',')
                    parse = ParseLB()
                    parse.parse_link_budget(site_ids=site_ids)
                    parse.tearDownDriver()
                else:
                    print(f"Invalid input {choice}. Please use 1 or 2")
                break
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
