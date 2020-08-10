from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import BasePage
from utilities.locators import PageLocators, CancelRequestLocators, CloseChangeLocators


class CancelRequests(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_change_request_opened(self) -> bool:
        """ Checks if the current working change request is opened or not """
        try:
            self.click(PageLocators.DATE_PAGE)
            status = self.is_visible(PageLocators.START_DATE_INPUT)

            if status:
                value = self.find_element(*CloseChangeLocators.ACTUAL_START_DATE_VALUE).get_attribute("value")
                if value == "":
                    return False
                else:
                    return True
        except TimeoutException as error:
            print(error)

    def is_cancelled(self):
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

    def select_cancel(self):
        """ select the Cancel Option from Status Menu """
        try:
            self.click(CancelRequestLocators.MENU_FOR_STATUS)
            self.hover_over(CancelRequestLocators.CANCEL_OPTION_SELECT)
            self.click(CancelRequestLocators.CANCEL_OPTION_SELECT)
        except TimeoutException as error:
            print(error)

    def save_status(self):
        """ Save the status to cancel """
        try:
            self.click(CancelRequestLocators.SAVE)
        except TimeoutException as error:
            print(error)
