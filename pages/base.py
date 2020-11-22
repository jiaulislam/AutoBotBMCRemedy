from selenium.common.exceptions import (
    NoSuchFrameException,
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from typing import Iterable, NoReturn
import time

''' 
The BasePage class is a base class that all the Pages that will inherit from this
BasePage class. Some most common method is written here that we're gonna need 
all over the project/pages to work with.
'''


class BasePage(object):
    """
        All the Page will inherit this class BasePage Class to use the common
        functionality.
    """

    def __init__(self, driver) -> NoReturn:
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator) -> webdriver:
        """ Find the element by the help of the locator that user shared """
        try:
            return self.driver.find_element(*locator)
        except TypeError as error:
            print(f"Unexpected Value Error [base.py || Line - 34]"
                  f"\nError Code: {error}")

    def find_elements(self, *locator) -> Iterable:
        """ Find the elements by the help of the locator that user shared """
        try:
            return self.driver.find_elements(*locator)
        except TypeError as error:
            print(f"Unexpected Value Error [base.py || Line - 41]"
                  f"\nError Code: {error}")

    def is_visible(self, by_locator) -> bool:
        """ If the element is found in the Page then return True else False """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator))
            return bool(element)
        except TimeoutException as error:
            raise Exception(f"Unexpected Timeout Error [base.py || Line - 43]"
                            f"\nError Code: {error}")

    def click(self, by_locator) -> NoReturn:
        """ Click a web element by a locator shared by the user """
        try:
            WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator)).click()
        except ElementClickInterceptedException:
            WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable(by_locator)).click()
        except NoSuchElementException as error:
            print(f"Unexpected NoSuchElementException Error [base.py || Line - 52]"
                  f"\nError Code: {error}")

    def write(self, by_locator, text) -> NoReturn:
        """ Write the text in web element by a locator shared by the user """
        try:
            WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator)).send_keys(text)
        except NoSuchElementException as error:
            print(f"Unexpected NoSuchElementException Error [base.py || Line - 59]"
                  f"\nError Code: {error}")

    def hover_over(self, by_locator) -> NoReturn:
        """ Hover over the element shared by the user locator """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator))
            ActionChains(self.driver).move_to_element(element).perform()
        except NoSuchElementException as error:
            print(f"Unexpected NoSuchElementException Error [base.py || Line - 67]"
                  f"\nError Code: {error}")
        except TimeoutException as error:
            raise Exception(f"Unexpected Timeout Error [base.py || Line - 62]"
                            f"\nError Code: {error}")

    def switch_to_frame(self, by_locator) -> NoReturn:
        """ Switch to a frame by a frame locator """
        try:
            user_frame = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator))
            self.driver.switch_to.frame(user_frame)
        except NoSuchFrameException as error:
            print(f"Unexpected NoSuchElementException Error [base.py || Line - 77]"
                  f"\nError Code: {error}")
        except TimeoutException as error:
            raise Exception(f"Unexpected Timeout Error [base.py || Line - 79]"
                            f"\nError Code: {error}")

    def double_click(self, by_locator) -> NoReturn:
        """ Double click on a element by a locator """
        element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator))
        ActionChains(self.driver).double_click(element).perform()

    def send_ctrl_plus_a(self, by_locator) -> NoReturn:
        """ Sends CTRL + A action to a page """
        try:
            WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator)).click()
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        except NoSuchElementException as error:
            print(f"Unexpected NoSuchElementException Error [base.py || Line - 92]"
                  f"\nError Code: {error}")
        except TimeoutException as error:
            raise Exception(f"Unexpected Timeout Error [base.py || Line - 94]"
                            f"\nError Code: {error}")

    def get_value_of_element(self, by_locator) -> str:
        """ Get the text value of a web element shared by a user """
        try:
            val_of_elem = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(by_locator)).get_attribute("value")
            return val_of_elem
        except TimeoutException as error:
            raise Exception(f"Unexpected Timeout Error [base.py || Line - 103]"
                            f"\nError Code: {error}")

    def check_for_expected_frame(self, frame_locator, ok_btn_locator) -> NoReturn:
        """ Checks for expected frames and press OK button in the frame """
        try:
            self.switch_to_frame(frame_locator)
            self.click(ok_btn_locator)
            self.driver.switch_to.default_content()
        except (NoSuchFrameException, TimeoutException):
            pass

    def back_to_home_page(self, by_locator) -> NoReturn:
        """ Return to the homepage """
        try:
            self.click(by_locator)
        except NoSuchElementException as errno:
            raise Exception(f"Unexpected NoSuchElementException Error [base.py || Line - 119]"
                            f"\nError Code: {errno}")
        except TimeoutException:
            try:
                time.sleep(1)
                self.click(by_locator)
            except TimeoutException as errno:
                raise Exception(f"Unexpected TimeoutException Error [base.py || Line - 125]"
                                f"\nError Code: {errno}")
