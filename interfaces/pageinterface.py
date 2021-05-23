from abc import ABC, abstractmethod
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Page(ABC):
    driver: WebDriver

    @abstractmethod
    def set_driver(self, driver: WebDriver) -> None:
        pass

    @abstractmethod
    def get_driver(self) -> WebDriver:
        pass

    @abstractmethod
    def get_text(self, web_element: WebElement):
        pass

    @abstractmethod
    def click_on(self, web_element: WebElement) -> None:
        pass

    @abstractmethod
    def write_on(self, web_element: WebElement) -> None:
        pass

    @abstractmethod
    def hover_over(self, web_element: WebElement) -> None:
        pass

    @abstractmethod
    def switch_frame(self, frame_element: WebElement) -> None:
        pass

    @abstractmethod
    def is_frame_available(self, frame_element: WebElement) -> None:
        pass

    @abstractmethod
    def sleeper(self, *element: WebElement, _until: int) -> None:
        pass
