# from pages.base import BasePage
# from pages.cancelrequest import CancelRequests
# from pages.closerequest import CloseRequests
# from pages.createrequest import CreateRequests
# from pages.home import HomePage
# from pages.login import LoginPage
# from utilites import make_data
# from utilites.static_data import StaticData
# from alive_progress import alive_bar
# from utilites.terminal_colors import Colors
#
# class CancelChangeRequest(BasePage):
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.login_page = LoginPage(self.driver)
#         self.home_page = HomePage(self.login_page.driver)
#         self.closeRequest = CloseRequests(self.home_page.driver)
#         self.cancel_requests = CancelRequests(self.closeRequest.driver)
#         self.create_requests = CreateRequests(self.closeRequest.driver)
#
#     def test_cancel_change(self):
#         """ All the functionalities in one function to mimic a user interactions to cancel a Change Request"""
#
#         # Log in to the server
#         self.login_page.enter_username_textbox()
#         self.login_page.enter_password_textbox()
#         self.login_page.click_login_button()
#
#         # Parse all the change numbers from the home page
#         all_changes_web = self.home_page.get_all_change_numbers()
#
#         # Parse all the user requested change number from the source
#         all_changes_file = make_data.list_of_change(StaticData.CANCEL_CHANGE_TXT_FILE_PATH)
#         with alive_bar(len(all_changes_file)) as bar:
#             for a_change in all_changes_file:
#                 # find the index of the change number from the list (custom algorithm is used).
#                 #  Searching an element time complexity is O(1)
#                 index = self.closeRequest.get_index_for_change_number(a_change, all_changes_web)
#                 if index is not None:
#                     # select the change number after found
#                     self.closeRequest.find_the_change_request(a_change, index)
#                     if not self.closeRequest.is_change_status_closed():
#                         if not self.closeRequest.is_status_scheduled_for_approval():
#                             if not self.cancel_requests.is_change_request_opened():
#                                 if not self.cancel_requests.is_cancelled():
#                                     # Perform the user interactions to cancel
#                                     self.cancel_requests.select_cancel()
#                                     self.cancel_requests.save_status()
#                                     print(f"{Colors.OKGREEN}===>STAT: CANCELLED ===> "
#                                           f"{self.cancel_requests.get_cancelled_cr_number()}{Colors.ENDC}")
#                                     bar()
#                                     self.create_requests.go_back_to_homepage()
#                                 else:
#                                     print(f"{Colors.OKGREEN}===>STAT: ALREADY CANCELLED ===> "
#                                           f"{self.cancel_requests.get_cancelled_cr_number()}{Colors.ENDC}")
#                                     self.create_requests.go_back_to_homepage()
#                                     bar()
#                             else:
#                                 print(f"{Colors.FAIL}===>STAT: ALREADY OPENED ===> "
#                                       f"{self.cancel_requests.get_cancelled_cr_number()}{Colors.ENDC}")
#                                 self.create_requests.go_back_to_homepage()
#                                 bar()
#                         else:
#                             print(f"{Colors.OKCYAN}===>STAT: SCHEDULED FOR APPROVAL ===> "
#                                   f"{self.cancel_requests.get_cancelled_cr_number()}{Colors.ENDC}")
#                             self.create_requests.go_back_to_homepage()
#                             bar()
#                     else:
#                         print(f"{Colors.OKBLUE}===>STAT: CLOSED OR COMPLETED ===> "
#                               f"{self.cancel_requests.get_cancelled_cr_number()}{Colors.ENDC}")
#                         bar()
#
#         self.home_page.click_logout_button()
