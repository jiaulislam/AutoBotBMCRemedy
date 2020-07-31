from pages.base import BasePage
from utilities.locators import PageLocators
from utilities.static_data import StaticData

"""
This Login Page Class File in responsible for login into the home page.
So this will require username & password from the PageLocators Class.
"""


class LoginPage(BasePage):
    def __init(self, driver) -> None:
        super().__init__(driver)
        # self.driver.get(StaticData.BASE_URL)

    def enter_username_textbox(self) -> None:
        """ Search & Enter the data in username textbox """
        self.driver.find_element(*PageLocators.USERNAME_TEXTBOX).clear()
        self.write(PageLocators.USERNAME_TEXTBOX, StaticData.USERNAME)

    def enter_password_textbox(self) -> None:
        """ Search & Enter the data in password textbox """
        self.driver.find_element(*PageLocators.PASSWORD_TEXTBOX).clear()
        self.write(PageLocators.PASSWORD_TEXTBOX, StaticData.PASSWORD)

    def click_login_button(self) -> None:
        """ Click the Login Button on login page """
        self.click(PageLocators.LOGIN_BUTTON)
