# import os
# import time
#
# from pages.base import BasePage
# from pages.createrequest import CreateRequests
# from pages.home import HomePage
# from pages.login import LoginPage
# from utilites import make_data
# from utilites.data_export import Data_Export
# from utilites.read_excel_data import Read_Data
# from utilites.static_data import StaticData
# from rich.live import Live
# from rich.traceback import install
# from rich import print
# from prettify.create_prettifier import get_layout, get_table, add_row_table
#
# install()
#
#
# class CreateChangeRequest(BasePage):
#
#     def __init__(self, driver):
#         self.layout = get_layout()
#         self.table = get_table()
#         self.path = os.getcwd()
#         super().__init__(driver)
#         self.login = LoginPage(self.driver)
#         self.homePage = HomePage(self.login.driver)
#         self.createChangeRequest = CreateRequests(self.homePage.driver)
#         self.read_data = Read_Data(StaticData.READ_EXCEL_FILE)
#         self.export_data = Data_Export(StaticData.WRITE_EXCEL_FILE)
#
#     def test_create_change(self):
#         print(self.layout)
#         self.login.enter_username_textbox()
#         self.login.enter_password_textbox()
#         self.login.click_login_button()
#         self.read_data.change_sheet()
#         self.export_data.change_sheet("Change_List")  # Change Sheet
#         EXCEL_ROW = 2  # Need to change if need to change the starting point in Excel
#         MAX_CHANGE = self.read_data.get_number_change() + EXCEL_ROW
#         with Live(self.table, refresh_per_second=4, vertical_overflow="visible") as live:
#             for change in range(EXCEL_ROW, MAX_CHANGE):
#
#                 # --------------------- BMCRemedy Create the Change Request as provided data ------------ #
#                 # TODO: THIS THING IS BUGGING ME > NEED A WAY TO HANDLE > DON'T WANT TO USE IMPLICIT WAIT
#                 if self.createChangeRequest.is_home_page("IT Home"):
#                     # ------- READ ALL THE DATA ------------ #
#                     date = self.read_data.parse_date(change)
#                     coordinator = self.read_data.parse_project_coordinator(change)
#                     project_name = self.read_data.parse_project_name(change)
#                     change_activity = self.read_data.parse_change_activity(change)
#                     impact_sites = self.read_data.parse_impact_list(change)
#                     service_type = self.read_data.parse_service_type(change)
#                     duration = self.read_data.parse_downtime_hour(change)
#                     company = self.read_data.get_company_group()
#                     commercial_zone = self.read_data.parse_commercial_zone(change)
#                     change_manager = self.read_data.parse_change_manager(change)
#                     location_service = (company, commercial_zone)
#
#                     summary = project_name + " // " + service_type + "\n\n"
#                     notes = summary + change_activity + "\n\n"
#                     impact_list = make_data.make_impact_list(impact_sites)
#                     details = summary + change_activity + impact_list
#
#                     # ---------------make_data: Task Time Calculation ---------------- #
#                     cr_start_time = make_data.get_change_start_time(date)
#                     start_downtime = make_data.get_service_start_downtime(date)
#                     end_downtime = make_data.get_service_end_downtime(start_downtime, duration)
#                     activity_hour = make_data.get_change_close_start_time(date)
#                     cr_end_time = make_data.get_change_close_end_time(date)
#                     # ------------------------------END----------------------------- #
#
#                     self.homePage.click_application_btn()
#                     self.homePage.click_new_change()
#                     time.sleep(3)
#                     self.createChangeRequest.insert_text_summary(summary)
#                     self.createChangeRequest.set_change_number()
#                     self.createChangeRequest.insert_text_notes(details)
#                     change_number = self.createChangeRequest.get_change_number()
#                     self.createChangeRequest.select_manager_group()
#                     self.createChangeRequest.select_change_manager(change_manager)
#                     self.createChangeRequest.insert_work_info(notes)
#                     self.createChangeRequest.change_location(location_service)
#                     self.createChangeRequest.verify_summary(summary)
#                     self.createChangeRequest.insert_schedule_date_time(cr_start_time, cr_end_time)
#                     self.createChangeRequest.create_task_template()
#
#                     self.createChangeRequest.fill_initiation_task(cr_start_time, start_downtime)
#                     self.createChangeRequest.fill_service_downtime_duration_task(
#                         start_downtime, end_downtime)
#                     self.createChangeRequest.fill_system_downtime_window_task(
#                         start_downtime, activity_hour)
#                     self.createChangeRequest.fill_system_downtime_duration_task(start_downtime, end_downtime)
#                     self.createChangeRequest.fill_review_closure_task(
#                         activity_hour, cr_end_time)
#                     # ---------------------------------- END -------------------------------------------- #
#
#                     # ---------------------------Data_Export: Export all the data ------------------ #
#                     self.export_data.insert_date(change, date)
#                     self.export_data.insert_project_name(change, project_name)
#                     self.export_data.insert_project_coordinator(change, coordinator)
#                     self.export_data.insert_change_activity(change, change_activity)
#                     self.export_data.insert_impact_site_list(change, impact_sites)
#                     self.export_data.insert_service_type(change, service_type)
#                     self.export_data.insert_downtime_duration(change, duration)
#                     self.export_data.insert_commercial_zone(change, commercial_zone)
#                     self.export_data.insert_change_number(change, change_number)
#                     self.export_data.insert_change_manager(change, change_manager)
#                     self.export_data.save_workbook(StaticData.WRITE_EXCEL_FILE)
#                     # ---------------------------- END -------------------------------------------------- #
#
#                     console_data = (str(change-1), commercial_zone, service_type, coordinator, change_number, "✅")
#
#                     # Save and go back to home page, need to tag site if service effective cr
#                     if service_type == 'Service Effective':
#                         query_formula = make_data.make_query_string(impact_sites)
#                         self.createChangeRequest.add_relationship_to_change(query_formula)
#                         # ----------------------------------------------------------
#                         # while True:
#                         #     val = input("Press q after finished")
#                         #     if val == 'q':
#                         #         break
#                         # self.createChangeRequest.save_change()
#                         # ---------------------------------------------------------
#                         self.createChangeRequest.goto_next_stage()
#                         os.chdir(self.path)
#                         add_row_table(self.table, *console_data)
#                         live.update(self.table)
#                         self.createChangeRequest.reset_change_number()
#                         self.createChangeRequest.go_back_to_homepage()
#                     else:
#                         # ----------------------------------------------------------
#                         # while True:
#                         #     val = input("Press q after finished")
#                         #     if val == 'q':
#                         #         break
#                         # self.createChangeRequest.save_change()
#                         # ----------------------------------------------------------
#                         self.createChangeRequest.goto_next_stage()
#                         os.chdir(self.path)
#                         add_row_table(self.table, *console_data)
#                         live.update(self.table)
#                         self.createChangeRequest.reset_change_number()
#                         self.createChangeRequest.go_back_to_homepage()
#         self.homePage.click_logout_button()
#         self.export_data.close_workbook()
#         self.read_data.close_workbook()
