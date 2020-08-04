from pages.base import BasePage
from pages.login import LoginPage
from pages.home import HomePage
from utilities import make_data
from utilities.static_data import StaticData
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
        
        all_changes_list = self.home_page.get_all_change_numbers()
        user_list_for_close = make_data.list_of_change(StaticData.CLOSE_CHANGE_TXT_FILE_PATH)

        for a_change in user_list_for_close:
            if a_change in all_changes_list:
                index = self.close_requests.get_index_for_change_number(a_change, all_changes_list)
                if index is not None:
                    self.close_requests.find_the_change_request(a_change, index)
                    if not self.close_requests.is_change_status_closed():
                        actual_open_time = self.close_requests.get_actual_start_date()
                        if actual_open_time is not None:
                            actual_closing_time = make_data.make_downtime_from_open_time(actual_open_time)
                            current_sys_time = make_data.get_current_system_time()
                            self.close_requests.goto_task_page()
                            self.close_requests.close_service_downtime_duration_task(actual_open_time, actual_closing_time)
                            self.close_requests.close_service_downtime_window_task(actual_open_time, current_sys_time)
                            self.close_requests.close_system_downtime_duration_task(actual_open_time, actual_closing_time)
                            self.close_requests.goto_next_stage()
                            self.home_page.go_to_home()
                        else:
                            print(f"{self.close_requests.get_change_number()} is not Opened !")
                            self.close_requests.add_change_to_invalid_list(a_change)
                            self.home_page.go_to_home()
                    else:
                        print(f"{self.close_requests.get_change_number()} change already closed !")
                        self.home_page.go_to_home()
                else:
                    print(f"{a_change} change not found !")
                    self.close_requests.add_change_to_invalid_list(a_change)
            else:
                print(f"{a_change} change not found !")
                self.close_requests.add_change_to_invalid_list(a_change)
        self.home_page.click_logout_button()


