import time
from rich.console import Console
from typing import Counter, List, Optional, Tuple, Union

from selenium.common.exceptions import (
    NoSuchFrameException,
    NoSuchElementException,
    TimeoutException, ElementClickInterceptedException,
)
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

''' 
The BasePage class is a base class that all the Pages that will inherit from this
BasePage class. Some most common method is written here that we're gonna need 
all over the project/Pages to work with.

written_by: jiaul_islam
'''




console = Console()

class BasePage(object):
    """
        All the Page will inherit this class BasePage Class to use the common
        functionality.
    """

    def __init__(self, driver: WebDriver, timeout: int = 30) -> None:
        self.driver: WebDriver = driver
        self.timeout = timeout

    def add_logging(func):
        def wrapper(xpath_locator):
            try:
                func(xpath_locator)
            except TimeoutException:
                console.log(
                    f"TimeoutException: [red]Related element's not visible[/red]. Source: @{BasePage.send_ctrl_plus_a.__qualname__}")
            except AttributeError:
                console.log(
                    f"Can't implement [red]Actions[/red] on 'NoneType' object. Source: [yellow]@{BasePage.send_ctrl_plus_a.__qualname__}[/yellow]")
        return wrapper

    def find_element(self, *locator):
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

    def find_elements(self, *locator) -> Union[List[WebElement], None]:
        """ Find the elements by the help of the locator that user shared """
        try:
            return self.driver.find_elements(*locator)
        except TypeError as error:
            print(f"Unexpected Value Error [base.py || Line - 47]"
                  f"\n{repr(error)}")
            pass
        except AttributeError as error:
            print(f"Unexpected Attribute Error in find_elements() ||\n{repr(error)}")
            pass
        except NoSuchElementException:
            pass

    def is_visible(self, xpath_locator) -> bool:
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

    def click(self, element_locator_xpath) -> None:
        """ Click a web element by a locator shared by the user """
        try:
            WebDriverWait(driver=self.driver,
                          timeout=self.timeout,
                          ignored_exceptions=[NoSuchElementException,
                                              NoSuchFrameException]
                          ).until(ec.visibility_of_element_located(element_locator_xpath)).click()
        except AttributeError as error:
            print(f"Unexpected Attribute Error [base.py || Line - 75]"
                  f"\n{repr(error)}")
            pass

    def write(self, xpath_locator: Tuple[By, str], text: str) -> None:
        """ Write the text in web element by a locator shared by the user """
        try:
            WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(xpath_locator)).send_keys(text)
        except NoSuchElementException as error:
            print(f"Unexpected NoSuchElementException Error [base.py || Line - 84]"
                  f"\nE{repr(error)}")
            pass

    def hover_over(self, xpath_locator: str) -> None:
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

    def switch_to_frame(self, xpath_locator) -> None:
        """ Switch to a frame by a frame locator """
        user_frame = self.driver.find_element(*xpath_locator)
        self.driver.switch_to.frame(user_frame)

    def double_click(self, xpath_locator: Tuple[By, str]) -> None:
        """ Double click on a element by a locator """
        element = WebDriverWait(self.driver, self.timeout, 2).until(
            ec.visibility_of_element_located(xpath_locator))
        ActionChains(self.driver).double_click(element).perform()

    @add_logging
    def send_ctrl_plus_a(self, xpath_locator: Tuple[By, str]) -> None:
        """ Sends CTRL + A action to a page """
        # try:
        WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(xpath_locator)).click()

        ActionChains(self.driver).key_down(
            Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        # except TimeoutException:
        #     console.log(f"TimeoutException: [red]Related element's not visible[/red]. Source: @{BasePage.send_ctrl_plus_a.__qualname__}")
        # except AttributeError:
        #     console.log(f"Can't implement [red]Actions[/red] on 'NoneType' object. Source: [yellow]@{BasePage.send_ctrl_plus_a.__qualname__}[/yellow]")

    def get_value_of_element(self, xpath_locator: Tuple[By, str]) -> str:
        """ Get the text value of a web element shared by a user """
        try:
            val_of_elem: str = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(xpath_locator)).get_attribute("value")
            return val_of_elem
        except TimeoutException as error:
            print(f"Unexpected Timeout Error [base.py || Line - 145]"
                  f"\n{repr(error)}")
            pass

    def check_for_expected_frame(self, frame_locator: str, ok_btn_locator: str) -> None:
        """ Checks for expected frames and press OK button in the frame """
        try:
            self.switch_to_frame(frame_locator)
            self.click(ok_btn_locator)
            self.driver.switch_to.default_content()
        except (NoSuchFrameException, NoSuchElementException, TimeoutException):
            pass

    def back_to_home_page(self, xpath_locator: Tuple[By, str]) -> None:
        """ Return to the homepage """
        try:
            self.click(xpath_locator)
        except NoSuchElementException as error:
            raise error
        # except TimeoutException:
        #     print("Back To Home Timeout Exception Hit")
        #     try:
        #         WebDriverWait(self.driver, 20).until(
        #             ec.visibility_of_element_located(xpath_locator)).click()
        #     except TimeoutException as error:
        #         raise Exception(f"Unexpected TimeoutException Error [base.py || Line - 172]"
        #                         f"\n{repr(error)}")
        # except ElementClickInterceptedException:
        #     try:
        #         WebDriverWait(self.driver, self.timeout).until(
        #             ec.visibility_of_element_located(xpath_locator)).click()
        #     except ElementClickInterceptedException:
        #         try:
        #             WebDriverWait(self.driver, self.timeout).until(
        #                 ec.element_to_be_clickable(xpath_locator)).click()
        #         except ElementClickInterceptedException:
        #             # TODO: Grace Period // Need to Work in this area
        #             for i in range(5):
        #                 print(".", end="")
        #                 time.sleep(1)
        #             print()
        #             WebDriverWait(self.driver, self.timeout).until(
        #                 ec.element_to_be_clickable(xpath_locator)).click()
        #         except Exception as error:
        #             print(f"Unexpected Error found ! --> {error}")
        #     except Exception as error:
        #         print(f"Unexpected error found ! --> {error}")

        
    def wait_for_loading_icon_disappear(self, *locator: Tuple[By, str]) -> None:
        """ Wait for 10 minutes for loading_icon to vanish """
        _counter = 1
        while _counter <= 600 :  # Run for 10 Minutes
            _loading_icons: list = self.driver.find_elements(*locator)
            if not len(_loading_icons):
                break
            time.sleep(1)
            _counter+=1
