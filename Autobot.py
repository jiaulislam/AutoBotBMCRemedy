from rich import print

from combiners.cancel import Cancel
from combiners.close import Close
from combiners.create import Create
from combiners.ldmaworker import Parser
from prettify import prettify_ldma
from drivers.chrome import Browser
from prettify.driver_prettify import MenuLayout, get_menu_choice

"""
Module Name: Autobot.py
----------------------
This is the main class for running the application. From here
all the functions can be called. This will be the user interface
from here. User's will choose the actions to do on BMC Remedy.

written by: jiaul_islam
"""


class CreateNewChangeRequest(Browser, Create):
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


class CloseChangeRequest(Browser, Close):
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


class CancelChangeRequests(Browser, Cancel):
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


class ParserLDMA(Browser, Parser):

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
