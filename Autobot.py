from rich import print

from actions.action import CreateNewChangeRequest, CloseChangeRequest, CancelChangeRequests, ParserLDMA
from prettify import prettify_ldma
from prettify.driver_prettify import MenuLayout, get_menu_choice
from logger.logger import get_logger
from sys import exit

"""
Module Name: Autobot.py
----------------------
This is the main class for running the application. From here
all the functions can be called. This will be the user interface
from here. User's will choose the actions to do on BMC Remedy.

written by: jiaul_islam
"""

main_logger = get_logger()


def main():
    """ The typical main function to start the program """

    try:
        while True:
            print(MenuLayout())
            choice: int = get_menu_choice()
            if choice == 1:
                # Create Change Request
                create = CreateNewChangeRequest()
                main_logger.info("Created instance for CreateNewChangeReqeust")
                create.createRequest()
                main_logger.info("Created NCR Successfully !")
                create.tearDownDriver()
                main_logger.info("Deleted instance Object for CreateNewChangeRequest")
                break
            elif choice == 2:
                # Close Change Request
                close = CloseChangeRequest()
                main_logger.info("Created instance of CloseChangeRequest")
                close.closeRequest()
                main_logger.info("Closed all request Succefully !")
                close.tearDownDriver()
                main_logger.info("Deleted instance of CloseChangeRequest")
                break
            elif choice == 3:
                # Cancel Change Request
                cancel = CancelChangeRequests()
                main_logger.info("Created instance of CancelChangeRequest")
                cancel.cancelRequests()
                main_logger.info("Cancelled all NCR Successfully")
                cancel.tearDownDriver()
                main_logger.info("Deleted instance of CancelChangeRequest")
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
                        main_logger.info("Created instance of LDMA Parser")
                        parse.parseLDMA(link_ids=link_ids)
                        main_logger.info("Parsed all data successfully")
                        parse.tearDownDriver()
                        main_logger.info("Deleted instance of LDMAParser")
                    elif choice == 2:
                        site_id = input("\nPlease Enter SiteID: ")
                        site_ids = site_id.split(',')
                        parse = ParserLDMA()
                        main_logger.info("Created instance of LDMAParser")
                        parse.parseLDMA(site_ids=site_ids)
                        main_logger.info("Parsed all data successfully")
                        parse.tearDownDriver()
                        main_logger.info("Deleted instance of LDMAParser")
                    elif choice == 0:
                        main_logger.info("Gracefull exit from LDMA Parser Menu")
                        break
            elif choice == 0:
                main_logger.info("Exising application gracefully")
                break
    except KeyboardInterrupt:
        main_logger.info("Exiting with KeyboardInterrupt")
        exit()


if __name__ == "__main__":
    main_logger.info("initiating main function")
    main()
    main_logger.info("Exited program gracefully")
