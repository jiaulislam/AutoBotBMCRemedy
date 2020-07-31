from pages.base import BasePage
from pages.login import LoginPage
from pages.home import HomePage
from pages.closerequest import CloseRequests


class CloseChangeRequests(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.close_requests = CloseRequests(self.driver)

    def test_close_requests(self):
        self.login_page.enter_username_textbox()
        self.login_page.enter_password_textbox()
        self.login_page.click_login_button()
