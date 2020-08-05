from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

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

    def get_all_change_numbers(self) -> list:
        """ Get all the change number from the homepage table """
        table_of_change_numbers = []
        try:
            # get all the element object from the change table
            WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(PageLocators.ALL_CHANGE_TABLE))
            change_number_elements = self.find_elements(*PageLocators.ALL_CHANGE_TABLE)
        except TimeoutException as error:
            print(error)
        else:
            # parse the numbers from the objects and append it to the list table_of_change_numbers
            for change in change_number_elements:
                table_of_change_numbers.append(change.text)

        return table_of_change_numbers

    def go_to_home(self):
        """ Return back to IT HOME """
        try:
            WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(PageLocators.HOME_ICON_BTN))
            javascript = "document.getElementById('reg_img_304248660').click();"
            self.driver.execute_script(javascript)
        except ElementClickInterceptedException:
            home_icon = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(PageLocators.HOME_ICON_BTN))
            self.click(home_icon)
        except TimeoutException as error:
            print(error)
