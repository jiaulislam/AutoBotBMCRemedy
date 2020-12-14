from Pages.base import BasePage
from Utilites.Locators import LoginPageLocators
from Utilites.static_data import StaticData

"""
This Login Page Class File in responsible for login into the home page.
So this will require username & password from the PageLocators Class.

written by: jiaul_islam
"""


class LoginPage(BasePage):
    def __init(self, driver) -> None:
        super().__init__(driver)
        # self.driver.get(StaticData.BASE_URL)

    def enter_username_textbox(self) -> None:
        """ Search & Enter the data in username textbox """
        self.driver.find_element(*LoginPageLocators.USERNAME_TEXTBOX).clear()
        self.write(LoginPageLocators.USERNAME_TEXTBOX, StaticData.USERNAME)

    def enter_password_textbox(self) -> None:
        """ Search & Enter the data in password textbox """
        self.driver.find_element(*LoginPageLocators.PASSWORD_TEXTBOX).clear()
        self.write(LoginPageLocators.PASSWORD_TEXTBOX, StaticData.PASSWORD)

    def click_login_button(self) -> None:
        """ Click the Login Button on login page """
        self.click(LoginPageLocators.LOGIN_BUTTON)
