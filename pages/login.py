from pages.base import BasePage
from utilites.locators import LoginPageLocators
from utilites.static_data import BMCData

"""
This Login Page Class File in responsible for login into the home page.
So this will require username & password from the PageLocators Class.

written by: jiaul_islam
"""


class LoginPage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def enter_username_textbox(self) -> None:
        """ Search & Enter the data in username textbox """
        self._driver.find_element(*LoginPageLocators.USERNAME_TEXTBOX).clear()
        self.write(LoginPageLocators.USERNAME_TEXTBOX, BMCData.USERNAME)

    def enter_password_textbox(self) -> None:
        """ Search & Enter the data in password textbox """
        self._driver.find_element(*LoginPageLocators.PASSWORD_TEXTBOX).clear()
        self.write(LoginPageLocators.PASSWORD_TEXTBOX, BMCData.PASSWORD)

    def click_login_button(self) -> None:
        """ Click the Login Button on login page """
        self.click(LoginPageLocators.LOGIN_BUTTON)
