import os
import time

from rich import print
from rich.live import Live
from rich.traceback import install
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base import BasePage
from pages.createrequest import CreateRequests
from pages.home import HomePage
from pages.login import LoginPage
from prettify.create_prettifier import get_layout, get_table, add_row_table
from utilites import make_data
from utilites.data_export import Data_Export
from utilites.read_excel_data import Read_Data
from utilites.static_data import StaticData

# install traceback
install()


class Create(BasePage):
    """ Create CR E2E Actions"""

    def __init__(self, driver: WebDriver):
        self._layout = get_layout()
        self._table = get_table()
        self.path = os.getcwd()
        super().__init__(driver)
        self._login = LoginPage(self._driver)
        self._home = HomePage(self._login._driver)
        self._create = CreateRequests(self._home._driver)
        self._read = Read_Data(StaticData.READ_EXCEL_FILE)
        self._write = Data_Export(StaticData.WRITE_EXCEL_FILE)

    def createNCR(self):
        print(self._layout)
        self._login.enter_username_textbox()
        self._login.enter_password_textbox()
        self._login.click_login_button()
        self._read.change_sheet()
        self._write.change_sheet("Main")  # Change Sheet
        EXCEL_ROW = 2  # Need to change if need to change the starting point in Excel
        MAX_CHANGE = self._read.get_number_change() + EXCEL_ROW
        with Live(self._table, refresh_per_second=4, vertical_overflow="visible") as live:
            for _excel_index in range(EXCEL_ROW, MAX_CHANGE):

                # --------------------- BMCRemedy Create the Change Request as provided data ------------ #
                if self._create.is_home_page("IT Home"):
                    # ------- READ ALL THE DATA ------------ #
                    date = self._read.parse_date(_excel_index)
                    coordinator = self._read.parse_project_coordinator(_excel_index)
                    project_name = self._read.parse_project_name(_excel_index)
                    change_activity = self._read.parse_change_activity(_excel_index)
                    impact_sites = self._read.parse_impact_list(_excel_index)
                    service_type = self._read.parse_service_type(_excel_index)
                    duration = self._read.parse_downtime_hour(_excel_index)
                    company = self._read.get_company_group()
                    commercial_zone = self._read.parse_commercial_zone(_excel_index)
                    change_manager = self._read.parse_change_manager(_excel_index)
                    location_service = (company, commercial_zone)

                    summary = project_name + " // " + service_type + "\n\n"
                    notes = summary + change_activity + "\n\n"
                    impact_list = make_data.make_impact_list(impact_sites)
                    details = summary + change_activity + impact_list

                    # ---------------make_data: Task Time Calculation ---------------- #
                    cr_start_time = make_data.get_change_start_time(date)
                    start_downtime = make_data.get_service_start_downtime(date)
                    end_downtime = make_data.get_service_end_downtime(start_downtime, duration)
                    activity_hour = make_data.get_change_close_start_time(date)
                    cr_end_time = make_data.get_change_close_end_time(date)
                    # ------------------------------END----------------------------- #

                    self._home.click_application_btn()
                    self._home.click_new_change()
                    # TODO: THIS THING IS BUGGING ME > NEED A WAY TO HANDLE > DON'T WANT TO USE IMPLICIT WAIT
                    time.sleep(3)
                    self._create.insert_text_summary(summary)
                    self._create.set_change_number()
                    self._create.insert_text_notes(details)
                    change_number = self._create.get_change_number()
                    live.console.print(f"Working on: [green]{change_number}")
                    self._create.select_manager_group()
                    self._create.select_change_manager(change_manager)
                    self._create.insert_work_info(notes)
                    self._create.change_location(location_service)
                    self._create.verify_summary(summary)
                    self._create.insert_schedule_date_time(cr_start_time, cr_end_time)
                    self._create.create_task_template()

                    self._create.fill_initiation_task(cr_start_time, start_downtime)
                    self._create.fill_service_downtime_duration_task(
                        start_downtime, end_downtime)
                    self._create.fill_system_downtime_window_task(
                        start_downtime, activity_hour)
                    self._create.fill_system_downtime_duration_task(start_downtime, end_downtime)
                    self._create.fill_review_closure_task(
                        activity_hour, cr_end_time)
                    # ---------------------------------- END -------------------------------------------- #

                    # ---------------------------Data_Export: Export all the data ------------------ #
                    self._write.insert_date(_excel_index, date)
                    self._write.insert_project_name(_excel_index, project_name)
                    self._write.insert_project_coordinator(_excel_index, coordinator)
                    self._write.insert_change_activity(_excel_index, change_activity)
                    self._write.insert_impact_site_list(_excel_index, impact_sites)
                    self._write.insert_service_type(_excel_index, service_type)
                    self._write.insert_downtime_duration(_excel_index, duration)
                    self._write.insert_commercial_zone(_excel_index, commercial_zone)
                    self._write.insert_change_number(_excel_index, change_number)
                    self._write.insert_change_manager(_excel_index, change_manager)
                    self._write.save_workbook(StaticData.WRITE_EXCEL_FILE)
                    # ---------------------------- END -------------------------------------------------- #

                    console_data = (
                        str(_excel_index - 1), commercial_zone, service_type, coordinator, change_number, "✅")

                    # Save and go back to home page, need to tag site if service effective cr
                    if service_type == 'Service Effective':
                        query_formula = make_data.make_query_string(impact_sites)
                        self._create.add_relationship_to_change(query_formula)
                        # ----------------------------------------------------------
                        # while True:
                        #     val = input("Press q after finished")
                        #     if val == 'q':
                        #         break
                        # self.createChangeRequest.save_change()
                        # ---------------------------------------------------------
                        self._create.goto_next_stage()
                        os.chdir(self.path)
                        add_row_table(self._table, *console_data)
                        live.update(self._table)
                        self._create.reset_change_number()
                        self._create.go_back_to_homepage()
                    else:
                        # ----------------------------------------------------------
                        # while True:
                        #     val = input("Press q after finished")
                        #     if val == 'q':
                        #         break
                        # self.createChangeRequest.save_change()
                        # ----------------------------------------------------------
                        self._create.goto_next_stage()
                        os.chdir(self.path)
                        add_row_table(self._table, *console_data)
                        live.update(self._table)
                        self._create.reset_change_number()
                        self._create.go_back_to_homepage()
        self._home.click_logout_button()
        self._write.close_workbook()
        self._read.close_workbook()
