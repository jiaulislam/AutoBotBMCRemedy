from typing import NoReturn

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base import BasePage
from utilities.locators import (CancelRequestLocators, CloseChangeLocators, DateSectionSelector)

"""
A class for Cancel the unused Change Requests. For cancelling a 
Request all the functions should be declared here
"""


class CancelRequests(BasePage):
    """ A class for mimicking the user interactions to cancel a Change Request """
    def __init__(self, driver):
        super().__init__(driver)

    def is_change_request_opened(self) -> bool:
        """ Checks if the current working change request is opened or not """
        try:
            self.click(DateSectionSelector.DATE_PAGE)
            status = self.is_visible(DateSectionSelector.START_DATE_INPUT)

            if status:
                value = self.find_element(*CloseChangeLocators.CHANGE_REQUEST_OPEN).get_attribute("value")
                if value == "":
                    return False
                else:
                    return True
        except TimeoutException as error:
            print(error)

    def is_cancelled(self) -> bool:
        """ Checks if the Cancellation is successful or not """
        try:
            status_Value = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(CancelRequestLocators.STATUS_AREA)).get_attribute("value")
            if status_Value == 'Cancelled':
                return True
            else:
                return False
        except TimeoutException as error:
            print(error)

    def select_cancel(self) -> NoReturn:
        """ select the Cancel Option from Status Menu """
        try:
            self.click(CancelRequestLocators.MENU_FOR_STATUS)
            self.hover_over(CancelRequestLocators.CANCEL_OPTION_SELECT)
            self.click(CancelRequestLocators.CANCEL_OPTION_SELECT)
        except TimeoutException as error:
            print(error)

    def is_scheduled_for_approval(self) -> bool:
        """ Check if the given CR status is schedule for approval """
        # TODO: Need to Implement
        pass

    def save_status(self) -> NoReturn:
        """ Save the change status to cancelled """
        try:
            self.click(CancelRequestLocators.SAVE)
        except TimeoutException as error:
            print(error)
