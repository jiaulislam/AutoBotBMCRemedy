from abc import ABC, abstractmethod
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement as WE
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Element(ABC):
    """ Represet abstraction of Element """
    @abstractmethod
    def click(self) -> None:
        pass

    @abstractmethod
    def write(self, value: str) -> None:
        pass

    @abstractmethod
    def text(self, _by: str, value: str) -> str:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def select_all_elements(self, _driver: WebDriver) -> None:
        pass

    @abstractmethod
    def double_click(self, _driver: WebDriver) -> None:
        pass

    @abstractmethod
    def element(self) -> WE:
        pass

    @abstractmethod
    def is_visible(self) -> bool:
        pass

    @abstractmethod
    def hover(self, _driver: WebDriver) -> None:
        pass


class WebElement(Element):
    """ Represent concrete web element """
    def __init__(self, element: WE) -> None:
        self._element = element

    def click(self) -> None:
        self._element.click()

    def write(self, value: str) -> None:
        self._element.send_keys(value)

    def text(self, _by: str, value: str) -> str:
        return self._element.find_element(_by, value).get_attribute('value')

    def clear(self) -> None:
        self._element.clear()

    def select_all_elements(self, _driver: WebDriver) -> None:
        ActionChains(_driver).key_down(
            Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

    def double_click(self, _driver: WebDriver) -> None:
        ActionChains(_driver).double_click(self._element)

    def element(self) -> WE:
        return self._element

    def is_visible(self) -> bool:
        return bool(self._element)

    def hover(self, _driver: WebDriver) -> None:
        ActionChains(_driver).move_to_element(self._element).perform()

