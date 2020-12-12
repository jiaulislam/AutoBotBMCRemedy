from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

from Pages.base import BasePage
from roc.locators.homelocator import HomeLocator as HL
from roc.locators.loginlocator import LoginLocator as LL


class Logout(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):

        try:
            self.click(LL.get_by_Xpath(HL.LOGOUT_IMG_BTN))
            self.click(LL.get_by_Xpath(HL.LOGOUT_BTN))
        except (ElementClickInterceptedException, NoSuchElementException) as e:
            print(e)
