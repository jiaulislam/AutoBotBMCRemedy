from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException
)
from Utilites.Locators import (
    CancelRequestLocators,
    CloseChangeLocators,
    DateSectionSelector,
    CommonChangeCreateLocators
)

# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
from Pages.base import BasePage
from typing import NoReturn

"""
A class for Cancel the unused Change Requests. For cancelling a 
Request all the functions should be declared here
"""


class CancelRequests(BasePage):
    """ A class for mimicking the user interactions to cancel a Change Request """

    def __init__(self, driver):
        super().__init__(driver=driver, timeout=10)

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

        # status_Value = WebDriverWait(self.driver, self.timeout).until(
        #     ec.visibility_of_element_located(CancelRequestLocators.STATUS_AREA)).get_attribute("value")
        status_value = self.get_value_of_element(CancelRequestLocators.STATUS_AREA)
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
                return self.get_value_of_element(CommonChangeCreateLocators.CHANGE_NUMBER_VALUE)
            except NoSuchElementException:
                raise Exception("Timed out.....")
