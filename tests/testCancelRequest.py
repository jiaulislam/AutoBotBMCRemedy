from pages.base import BasePage
from pages.cancelrequest import CancelRequests
from pages.closerequest import CloseRequests
from pages.home import HomePage
from pages.login import LoginPage
from utilities import make_data
from utilities.static_data import StaticData


class CancelChangeRequest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.login_page.driver)
        self.closeRequest = CloseRequests(self.home_page.driver)
        self.cancel_requests = CancelRequests(self.closeRequest.driver)

    def test_cancel_change(self):
        self.login_page.enter_username_textbox()
        self.login_page.enter_password_textbox()
        self.login_page.click_login_button()

        all_changes_web = self.home_page.get_all_change_numbers()
        all_changes_file = make_data.list_of_change(StaticData.CANCEL_CHANGE_TXT_FILE_PATH)

        for a_change in all_changes_file:
            index = self.closeRequest.get_index_for_change_number(a_change, all_changes_web)
            if index is not None:
                self.closeRequest.find_the_change_request(a_change, index)
                if not self.cancel_requests.is_change_request_opened():
                    if not self.cancel_requests.is_cancelled():
                        self.cancel_requests.select_cancel()
                        self.cancel_requests.save_status()
                        self.cancel_requests.go_to_home()
                    else:
                        self.cancel_requests.go_to_home()
                else:
                    self.cancel_requests.go_to_home()
        self.home_page.click_logout_button()
