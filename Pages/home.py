from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException
)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from Utilites.Locators import HomePageLocators
from Utilites.terminal_colors import bcolors
from Pages.base import BasePage
import time

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
        return self.find_element(*HomePageLocators.IT_HOME_TEXT).text

    def click_application_btn(self) -> None:
        """ Click the Application Button on Home Page """
        try:
            self.click(HomePageLocators.APPLICATION_BUTTON)
        except ElementClickInterceptedException:
            self.click(HomePageLocators.APPLICATION_BUTTON)

    def click_new_change(self) -> None:
        """ Find and Click the New Change Menu Button """
        self.hover_over(HomePageLocators.CHANGE_MANAGEMENT_LIST)
        self.hover_over(HomePageLocators.NEW_CHANGE_LIST)
        self.click(HomePageLocators.NEW_CHANGE_LIST)

    def click_logout_button(self) -> None:
        """ Click the Logout Button on home page """
        self.click(HomePageLocators.LOGOUT_BUTTON)
        print(f"{bcolors.OKGREEN}\nLogged out Successfully.\n{bcolors.ENDC}")

    def get_all_change_numbers(self) -> list:
        """ Get all the change number from the homepage table """
        table_of_change_numbers = []
        try:
            # get all the element object from the change table
            WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(HomePageLocators.ALL_CHANGE_TABLE))
            change_number_elements = self.find_elements(*HomePageLocators.ALL_CHANGE_TABLE)
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
            home_icon = WebDriverWait(driver=self.driver, timeout=self.timeout, poll_frequency=3).until(
                ec.element_to_be_clickable(HomePageLocators.HOME_ICON_BTN))
            self.click(home_icon)
            # get_state = "document.readyState"
            # status = self.driver.execute_script(get_state)
            # print(status)
            # while status != 'complete':
            #     home_icon = WebDriverWait(driver=self.driver, timeout=self.timeout, poll_frequency=3.5).until(
            #         ec.visibility_of_element_located(HomePageLocators.HOME_ICON_BTN))
            #     self.click(home_icon)
            #     print("working")
        # except ElementClickInterceptedException:
        #     home_icon = WebDriverWait(driver=self.driver, timeout=self.timeout, poll_frequency=3).until(
        #         ec.visibility_of_element_located(HomePageLocators.HOME_ICON_BTN))
        #     self.click(home_icon)
        except TimeoutException:
            pass
        except ElementClickInterceptedException:
            time.sleep(10)
            home_icon = WebDriverWait(driver=self.driver, timeout=self.timeout, poll_frequency=3).until(
                ec.visibility_of_element_located(HomePageLocators.HOME_ICON_BTN))
            self.click(home_icon)
