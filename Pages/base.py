from selenium.common.exceptions import (
    NoSuchFrameException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from typing import Iterable, NoReturn
from selenium import webdriver
import time

''' 
The BasePage class is a base class that all the Pages that will inherit from this
BasePage class. Some most common method is written here that we're gonna need 
all over the project/Pages to work with.
'''


class BasePage(object):
    """
        All the Page will inherit this class BasePage Class to use the common
        functionality.
    """

    def __init__(self, driver: webdriver, timeout: int = 30) -> NoReturn:
        self.driver = driver
        self.timeout = timeout

    def find_element(self, *locator: tuple):
        """ Find the element by the help of the locator that user shared """
        try:
            return self.driver.find_element(*locator)
        except TypeError as error:
            print(f"Unexpected Type Error [base.py || Line - 37]"
                  f"\n{repr(error)}")
            pass
        except AttributeError as error:
            print(f"Unexpected Attribute Error in find_element() ||\n{repr(error)}")
            pass
        except NoSuchElementException:
            pass

    def find_elements(self, *locator: tuple) -> Iterable[object]:
        """ Find the elements by the help of the locator that user shared """
        try:
            return self.driver.find_elements(*locator)
        except TypeError as error:
            print(f"Unexpected Value Error [base.py || Line - 47]"
                  f"\n{repr(error)}")
            pass
        except AttributeError as error:
            print(f"Unexpected Attribute Error in find_element() ||\n{repr(error)}")
            pass
        except NoSuchElementException:
            pass

    def is_visible(self, xpath_locator: str) -> bool:
        """ If the element is found in the Page then return True else False """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(xpath_locator))
            return bool(element)
        except TimeoutException:
            pass
        except AttributeError as error:
            print(f"Unexpected Attribute Error [base.py || Line - 60]"
                  f"\n{repr(error)}")
            pass

    def click(self, element_locator_xpath: webdriver) -> NoReturn:
        """ Click a web element by a locator shared by the user """
        try:
            WebDriverWait(driver=self.driver,
                          timeout=self.timeout,
                          poll_frequency=1,
                          ignored_exceptions=[NoSuchElementException,
                                              NoSuchFrameException]
                          ).until(ec.visibility_of_element_located(element_locator_xpath)).click()
        except AttributeError as error:
            print(f"Unexpected Attribute Error [base.py || Line - 75]"
                  f"\n{repr(error)}")
            pass

    def write(self, xpath_locator: str, text: str) -> NoReturn:
        """ Write the text in web element by a locator shared by the user """
        try:
            WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(xpath_locator)).send_keys(text)
        except NoSuchElementException as error:
            print(f"Unexpected NoSuchElementException Error [base.py || Line - 84]"
                  f"\nE{repr(error)}")
            pass

    def hover_over(self, xpath_locator: str) -> NoReturn:
        """ Hover over the element shared by the user locator """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(xpath_locator))
            ActionChains(self.driver).move_to_element(element).perform()
        except NoSuchElementException as error:
            print(f"Unexpected NoSuchElementException Error [base.py || Line - 94]"
                  f"\n{repr(error)}")
            pass
        except TimeoutException as error:
            print(f"Unexpected Timeout Error [base.py || Line - 98]"
                  f"\n{repr(error)}")
            pass

    def switch_to_frame(self, xpath_locator: str) -> NoReturn:
        """ Switch to a frame by a frame locator """
        try:
            user_frame = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(xpath_locator))
            self.driver.switch_to.frame(user_frame)
        except NoSuchFrameException:
            pass
        except TimeoutException:
            pass

    def double_click(self, xpath_locator: str) -> NoReturn:
        """ Double click on a element by a locator """
        element = WebDriverWait(self.driver, self.timeout, 2).until(
            ec.visibility_of_element_located(xpath_locator))
        ActionChains(self.driver).double_click(element).perform()

    def send_ctrl_plus_a(self, xpath_locator: str) -> NoReturn:
        """ Sends CTRL + A action to a page """
        try:
            WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(xpath_locator)).click()

            ActionChains(self.driver).key_down(
                Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

        except NoSuchElementException as error:
            print(f"Unexpected NoSuchElementException Error [base.py || Line - 130]"
                  f"\n{repr(error)}")
            pass
        except TimeoutException as error:
            print(f"Unexpected Timeout Error [base.py || Line - 135]"
                  f"\n{repr(error)}")
            pass

    def get_value_of_element(self, xpath_locator: str) -> str:
        """ Get the text value of a web element shared by a user """
        try:
            val_of_elem = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(xpath_locator)).get_attribute("value")
            return val_of_elem
        except TimeoutException as error:
            print(f"Unexpected Timeout Error [base.py || Line - 145]"
                  f"\n{repr(error)}")
            pass

    def check_for_expected_frame(self, frame_locator: str, ok_btn_locator: str) -> NoReturn:
        """ Checks for expected frames and press OK button in the frame """
        try:
            self.switch_to_frame(frame_locator)
            self.click(ok_btn_locator)
            self.driver.switch_to.default_content()
        except (NoSuchFrameException, TimeoutException):
            pass

    def back_to_home_page(self, xpath_locator: str) -> NoReturn:
        """ Return to the homepage """
        try:
            self.click(xpath_locator)
        except NoSuchElementException as error:
            print(f"Unexpected NoSuchElementException Error [base.py || Line - 164]"
                  f"\n{repr(error)}")
            pass
        except TimeoutException:
            try:
                time.sleep(1)
                self.click(xpath_locator)
            except TimeoutException as error:
                raise Exception(f"Unexpected TimeoutException Error [base.py || Line - 172]"
                                f"\n{repr(error)}")