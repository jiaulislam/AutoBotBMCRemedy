import time
from typing import List, Tuple, Union

from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from utilites.decorators import add_logger
import logging

logger = logging.getLogger(__name__)

''' 
The BasePage class is a base class that all the Pages that will inherit from this
BasePage class. Some most common method is written here that we're gonna need 
all over the project/Pages to work with.

written_by: jiaul_islam
'''


class BasePage(object):
    """
        All the Page will inherit this class BasePage Class to use the common
        functionality.
    """

    def __init__(self, driver: WebDriver, timeout: int = 30) -> None:
        self._driver: WebDriver = driver
        self.timeout = timeout

    def find_element(self, *locator) -> WebElement:
        """ Find the element by the help of the locator that user shared """
        try:
            return self._driver.find_element(*locator)
        except TypeError as error:
            print(f"Unexpected Type Error [base.py || Line - 37]"
                  f"\n{repr(error)}")
        except AttributeError as error:
            print(f"Unexpected Attribute Error in find_element() ||\n{repr(error)}")
        except NoSuchElementException:
            pass

    def find_elements(self, *locator) -> Union[List[WebElement], None]:
        """ Find the elements by the help of the locator that user shared """
        try:
            return self._driver.find_elements(*locator)
        except TypeError as error:
            print(f"Unexpected Value Error [base.py || Line - 47]"
                  f"\n{repr(error)}")
        except AttributeError as error:
            print(f"Unexpected Attribute Error in find_elements() ||\n{repr(error)}")
        except NoSuchElementException:
            pass

    def is_visible(self, xpath_locator) -> bool:
        """ If the element is found in the Page then return True else False """
        try:
            _element = WebDriverWait(self._driver, self.timeout).until(
                ec.visibility_of_element_located(xpath_locator))
        except TimeoutException:
            pass
        except AttributeError as error:
            print(f"Unexpected Attribute Error [base.py || Line - 60]"
                  f"\n{repr(error)}")
        else:
            return bool(_element)

    @add_logger
    def click(self, element_locator_xpath) -> None:
        """ Click a web element by a locator shared by the user """
        WebDriverWait(driver=self._driver,
                      timeout=self.timeout,
                      ignored_exceptions=None
                      ).until(ec.visibility_of_element_located(element_locator_xpath)).click()

    @add_logger
    def write(self, xpath_locator: Tuple[By, str], text: str) -> None:
        """ Write the text in web element by a locator shared by the user """
        WebDriverWait(self._driver, self.timeout).until(
            ec.visibility_of_element_located(xpath_locator)).send_keys(text)

    @add_logger
    def hover_over(self, xpath_locator: str) -> None:
        """ Hover over the element shared by the user locator """
        _element: Union[WebElement, None] = WebDriverWait(self._driver, self.timeout).until(
            ec.visibility_of_element_located(xpath_locator))
        if _element is not None:
            ActionChains(self._driver).move_to_element(_element).perform()
        else:
            raise AttributeError

    @add_logger
    def switch_to_frame(self, xpath_locator) -> None:
        """ Switch to a frame by a frame locator """
        _frame: Union[WebElement, None] = self._driver.find_element(*xpath_locator)
        self._driver.switch_to.frame(_frame)

    @add_logger
    def double_click(self, xpath_locator: Tuple[By, str]) -> None:
        """ Double click on a element by a locator """
        _element: Union[WebElement, None] = WebDriverWait(self._driver, self.timeout, 2).until(
            ec.visibility_of_element_located(xpath_locator))
        ActionChains(self._driver).double_click(_element).perform()

    @add_logger
    def select_all(self, xpath_locator: Tuple[By, str]) -> None:
        """ Sends CTRL + A action to a page """
        WebDriverWait(self._driver, self.timeout).until(
            ec.visibility_of_element_located(xpath_locator)).click()

        ActionChains(self._driver).key_down(
            Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

    def get_text(self, xpath_locator: Tuple[By, str]) -> str:
        """ Get the text value of a web element shared by a user """
        try:
            _val_of_elem: str = WebDriverWait(self._driver, self.timeout).until(
                ec.visibility_of_element_located(xpath_locator)).get_attribute("value")
        except TimeoutException as error:
            print(f"Unexpected Timeout Error [base.py || Line - 145]"
                  f"\n{repr(error)}")
        else:
            return _val_of_elem

    @add_logger
    def handle_frame_alert(self, frame_locator: str, ok_btn_locator: str) -> None:
        """ Checks for expected frames and press OK button in the frame """
        self.switch_to_frame(frame_locator)
        self.click(ok_btn_locator)
        self._driver.switch_to.default_content()

    @add_logger
    def back_to_home_page(self, xpath_locator: Tuple[By, str]) -> None:
        """ Return to the homepage """
        self.click(xpath_locator)

    def wait_for_loading_icon_disappear(self, *locator: Tuple[By, str], _time: float = 1, _range: int = 600) -> None:
        """ Wait for loading_icon to vanish """
        _counter = 1
        while _counter <= _range:
            _loading_icons: list = self._driver.find_elements(*locator)
            if not len(_loading_icons):
                break
            time.sleep(_time)
            _counter += 1
