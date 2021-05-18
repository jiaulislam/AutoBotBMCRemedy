from rich import print

from actions.action import CreateNewChangeRequest, CloseChangeRequest, CancelChangeRequests, ParserLDMA
from prettify import prettify_ldma
from prettify.driver_prettify import MenuLayout, get_menu_choice

"""
Module Name: Autobot.py
----------------------
This is the main class for running the application. From here
all the functions can be called. This will be the user interface
from here. User's will choose the actions to do on BMC Remedy.

written by: jiaul_islam
"""


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
