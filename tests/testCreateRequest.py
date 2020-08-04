import os

from pages.base import BasePage
from pages.createrequest import CreateRequests
from pages.home import HomePage
from pages.login import LoginPage
from utilities import make_data
from utilities.data_export import Data_Export
from utilities.read_excel_data import Read_Data
from utilities.static_data import StaticData


class CreateChangeRequest(BasePage):

    def __init__(self, driver):
        self.path = "E:\\Python Projects\\AutoBotBMCRemedy\\"
        super().__init__(driver)
        self.login = LoginPage(self.driver)
        self.homePage = HomePage(self.login.driver)
        self.createChangeRequest = CreateRequests(self.homePage.driver)
        self.read_data = Read_Data(StaticData.READ_EXCEL_FILE)
        self.export_data = Data_Export(StaticData.WRITE_EXCEL_FILE)

    def test_create_change(self):
        self.login.enter_username_textbox()
        self.login.enter_password_textbox()
        self.login.click_login_button()
        max_change = self.read_data.get_number_change() + 2
        for change in range(2, max_change):
            # ------- READ ALL THE DATA ------------ #
            m_date = self.read_data.parse_date(change)
            coordinator = self.read_data.parse_project_coordinator(change)
            project_name = self.read_data.parse_project_name(change)
            change_activity = self.read_data.parse_change_activity(change)
            impact_sites = self.read_data.parse_impact_list(change)
            service_type = self.read_data.parse_service_type(change)
            duration = self.read_data.parse_downtime_hour(change)
            company = self.read_data.get_company_group()
            region = self.read_data.get_region()
            site_group = self.read_data.parse_site_group(change)
            commercial_zone = self.read_data.parse_commercial_zone(change)
            change_manager = self.read_data.parse_change_manager(change)
            location_service = (company, region, site_group, commercial_zone)

            summary = project_name + " || " + service_type + "\n"
            notes = project_name + " || " + service_type + "\n" + change_activity + "\n"
            impact_list = make_data.make_impact_list(impact_sites, site_group)
            file_location = os.getcwd() + "/" + site_group + '.txt'

            # ---------------make_data: Task Time Calculation ---------------- #
            cr_start_time = make_data.get_change_start_time(m_date)
            start_downtime = make_data.get_service_start_downtime(m_date)
            end_downtime = make_data.get_service_end_downtime(start_downtime, duration)
            activity_hour = make_data.get_change_close_start_time(m_date)
            cr_end_time = make_data.get_change_close_end_time(m_date)
            # relation_query = None
            # ------------------------------END----------------------------- #

            # --------------------- BMCRemedy Create the Change Request as provided data ------------ #
            self.homePage.click_application_btn()
            self.homePage.click_new_change()
            self.createChangeRequest.change_location(location_service)
            self.createChangeRequest.insert_text_summary(summary)
            self.createChangeRequest.insert_text_notes(notes)
            self.createChangeRequest.insert_impact_list_in_notes(impact_list)
            change_number = self.createChangeRequest.get_change_number()
            print(f"Working On: {change - 1} \t NCR: {change_number}")
            self.createChangeRequest.select_manager_group(change_manager)
            self.createChangeRequest.select_change_manager(change_manager)
            self.createChangeRequest.insert_text_note_and_upload_files(notes, file_location)
            os.remove(file_location)
            self.createChangeRequest.insert_schedule_date_time(cr_start_time, cr_end_time)
            self.createChangeRequest.create_task_template()

            self.createChangeRequest.fill_initiation_task(cr_start_time, start_downtime)
            self.createChangeRequest.fill_service_downtime_duration_task(
                start_downtime, end_downtime)
            self.createChangeRequest.fill_system_downtime_window_task(
                start_downtime, activity_hour)
            self.createChangeRequest.fill_system_downtime_duration_task(start_downtime, end_downtime)
            self.createChangeRequest.fill_review_closure_task(
                activity_hour, cr_end_time)
            # ---------------------------------- END -------------------------------------------- #

            # ---------------------------Data_Export: Export all the data ------------------ #
            self.export_data.insert_date(change, m_date)
            self.export_data.insert_project_name(change, project_name)
            self.export_data.insert_project_coordinator(change, coordinator)
            self.export_data.insert_change_activity(change, change_activity)
            self.export_data.insert_impact_site_list(change, impact_sites)
            self.export_data.insert_service_type(change, service_type)
            self.export_data.insert_downtime_duration(change, duration)
            self.export_data.insert_site_group(change, site_group)
            self.export_data.insert_commercial_zone(change, commercial_zone)
            self.export_data.insert_change_number(change, change_number)
            self.export_data.insert_change_manager(change, change_manager)
            self.export_data.save_workbook(self.createChangeRequest, StaticData.WRITE_EXCEL_FILE)
            # ---------------------------- END -------------------------------------------------- #

            # Save and go back to home page
            self.createChangeRequest.save_change()
            self.createChangeRequest.go_back_to_homepage()
            os.chdir(self.path)
        self.homePage.click_logout_button()
        self.export_data.close_workbook()
        self.read_data.close_workbook()
