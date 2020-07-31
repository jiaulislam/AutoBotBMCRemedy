from pages.base import BasePage
from utilities.locators import PageLocators

"""
This is the most important class file here. Home page will have the 
all the functions and classes or inside work in BMC Remedy. This class
will be responsible for Creating NCR, Closing NCR, Parsing the NCR information
also the logout from account will also be here.
"""


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_home_page(self) -> str:
        """ Check if the 'IT Home' text is available or not in the DOM """
        return self.find_element(*PageLocators.IT_HOME_TEXT).text

    def click_application_btn(self) -> None:
        """ Click the Application Button on Home Page """
        self.click(PageLocators.APPLICATION_BUTTON)

    def click_new_change(self) -> None:
        """ Find and Click the New Change Menu Button """
        self.hover_over(PageLocators.CHANGE_MANAGEMENT_LIST)
        self.hover_over(PageLocators.NEW_CHANGE_LIST)
        self.click(PageLocators.NEW_CHANGE_LIST)

    def click_logout_button(self) -> None:
        """ Click the Logout Button on home page """
        self.click(PageLocators.LOGOUT_BUTTON)
