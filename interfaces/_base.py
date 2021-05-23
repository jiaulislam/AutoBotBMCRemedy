from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pageinterface import Page


class BasePage(Page):
    def set_driver(self, driver: WebDriver) -> None:
        pass

    def get_driver(self) -> WebDriver:
        pass

    def click_on(self, web_element: WebElement) -> None:
        pass

    def write_on(self, web_element: WebElement) -> None:
        pass

    def hover_over(self, web_element: WebElement) -> None:
        pass

    def switch_frame(self, frame_element: WebElement) -> None:
        pass

    def is_frame_available(self, frame_element: WebElement) -> None:
        pass

    def get_text(self, web_element: WebElement) -> str:
        return web_element.text

    def sleeper(self, *element: WebElement, _until: int = 600) -> None:
        _counter = 1
        while _counter <= _until:
            _loading_icons: list[WebElement] = self.driver.find_elements(*element)
            if not len(_loading_icons):
                break
            sleep(1)
            _counter += 1
