from rich.live import Live
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base import BasePage
from pages.cancelrequest import CancelRequests
from pages.closerequest import CloseRequests
from pages.createrequest import CreateRequests
from pages.home import HomePage
from pages.login import LoginPage
from prettify.cancel_prettifier import CancelPrettify
from utilites import make_data
from utilites.static_data import StaticData


class Cancel(BasePage):

    def __init__(self, driver: WebDriver):
        """ Cancel NCR E2E Actions """
        super().__init__(driver)
        self.login_page = LoginPage(self._driver)
        self.home_page = HomePage(self.login_page._driver)
        self.closeRequest = CloseRequests(self.home_page._driver)
        self.cancel_requests = CancelRequests(self.closeRequest._driver)
        self.create_requests = CreateRequests(self.closeRequest._driver)

    def cancelRequest(self):
        """ All the functionalities in one function to mimic a user interactions to cancel a Change Request"""

        # Log in to the server
        self.login_page.enter_username_textbox()
        self.login_page.enter_password_textbox()
        self.login_page.click_login_button()

        # Parse all the change numbers from the home page
        all_changes_web = self.home_page.get_all_change_numbers()

        # Parse all the user requested change number from the source
        all_changes_file = make_data.list_of_change(StaticData.CANCEL_CHANGE_TXT_FILE_PATH)

        # Prettify tables
        CancelPrettify.make_layout()
        CancelPrettify.make_table()
        progress = CancelPrettify.progress_bar(len(all_changes_file))
        CancelPrettify.merge_layout(progress, CancelPrettify.get_table())

        with Live(CancelPrettify.show_layout(), refresh_per_second=5, vertical_overflow="visible") as live:
            while not progress.finished:
                for task in progress.tasks:
                    for _task_no, a_change in enumerate(all_changes_file):
                        # find the index of the change number from the list (custom algorithm is used).
                        #  Searching an element time complexity is O(1)
                        index = self.closeRequest.get_index_for_change_number(a_change, all_changes_web)
                        if index is not None:
                            # select the change number after found
                            self.closeRequest.find_the_change_request(a_change, index)
                            if not self.closeRequest.is_change_status_closed():
                                if not self.closeRequest.is_status_scheduled_for_approval():
                                    if not self.cancel_requests.is_change_request_opened():
                                        if not self.cancel_requests.is_cancelled():
                                            # Perform the user interactions to cancel
                                            self.cancel_requests.wait_for_loading_icon_disappear()
                                            self.cancel_requests.select_cancel()
                                            self.cancel_requests.save_status()
                                            # // Cancelled //
                                            CancelPrettify.add_row_table(str(_task_no + 1),
                                                                         self.cancel_requests.get_cancelled_cr_number(),
                                                                         "CANCELLED")
                                            live.update(CancelPrettify.show_layout())
                                            self.create_requests.go_back_to_homepage()
                                        else:
                                            #  // Already Closed //
                                            CancelPrettify.add_row_table(str(_task_no + 1),
                                                                         self.cancel_requests.get_cancelled_cr_number(),
                                                                         "A/C", style="yellow")
                                            live.update(CancelPrettify.show_layout())
                                            self.create_requests.go_back_to_homepage()
                                    else:
                                        # // Already Opened //
                                        CancelPrettify.add_row_table(str(_task_no + 1),
                                                                     self.cancel_requests.get_cancelled_cr_number(),
                                                                     "A/O", style="red")
                                        live.update(CancelPrettify.show_layout())
                                        self.create_requests.go_back_to_homepage()
                                else:
                                    # // Scheduled for Approval
                                    CancelPrettify.add_row_table(str(_task_no + 1),
                                                                 self.cancel_requests.get_cancelled_cr_number(),
                                                                 "S/F/A")
                                    live.update(CancelPrettify.show_layout())
                                    self.create_requests.go_back_to_homepage()
                            else:
                                # // Already Closed or Completed
                                CancelPrettify.add_row_table(str(_task_no + 1),
                                                             self.cancel_requests.get_cancelled_cr_number(),
                                                             "Closed/Completed")
                                live.update(CancelPrettify.show_layout())
                                self.create_requests.go_back_to_homepage()
                        if not task.finished:
                            progress.advance(task.id)

        self.home_page.click_logout_button()
