from typing import NoReturn

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException
)

from pages.base import BasePage
from utilites.locators import (
    CancelRequestLocators,
    CloseChangeLocators,
    DateSectionSelector,
    CommonChangeCreateLocators
)

"""
A class for Cancel the unused Change Requests. For cancelling a 
Request all the functions should be declared here

written by: jiaul_islam
"""


class CancelRequests(BasePage):
    """ A class for mimicking the user interactions to cancel a Change Request """

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_change_request_opened(self) -> bool:
        """ Checks if the current working change request is opened or not """
        try:
            self.click(DateSectionSelector.DATE_PAGE)
            status = self.is_visible(DateSectionSelector.START_DATE_INPUT)

            if status:
                value = self.find_element(*CloseChangeLocators.ACTUAL_OPEN_DATE).get_attribute("value")
                if value == "":
                    return False
                else:
                    return True
        except TimeoutException as error:
            print(error)

    def is_cancelled(self) -> bool:
        """ Checks if the Cancellation is successful or not """
        status_value = self.get_text(CancelRequestLocators.STATUS_AREA)
        if status_value == 'Cancelled':
            return True
        else:
            return False

    def select_cancel(self) -> NoReturn:
        """ select the Cancel Option from Status Menu """
        self.click(CancelRequestLocators.MENU_FOR_STATUS)
        self.hover_over(CancelRequestLocators.CANCEL_OPTION_SELECT)
        self.click(CancelRequestLocators.CANCEL_OPTION_SELECT)

    def save_status(self) -> NoReturn:
        """ Save the change status to cancelled """
        self.click(CancelRequestLocators.SAVE)

    def get_cancelled_cr_number(self):
        """ Get the Cancelled Changed Number """
        change_number = ""
        while change_number == "" or None:
            try:
                return self.get_text(CommonChangeCreateLocators.CHANGE_NUMBER_VALUE)
            except NoSuchElementException:
                raise Exception("Timed out.....")
