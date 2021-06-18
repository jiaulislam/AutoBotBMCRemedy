from excel.excel import Excel
import os
import time
from typing import Dict

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
from utilites.static_data import StaticData

# install traceback
install()

# Starting ROW
START_ROW = 2  # Need to change if need to change the starting point in Excel
# MAX ROW USED


class Create(BasePage):
    """Create CR E2E Actions"""

    def __init__(self, driver: WebDriver):
        self._xcel: Excel = Excel(StaticData.READ_EXCEL_FILE)
        self._MAX: int = self._xcel.get_last_row()
        self._layout = get_layout()
        self._table = get_table()
        self._path = os.getcwd()
        super().__init__(driver)
        self._login = LoginPage(self._driver)
        self._home = HomePage(self._login._driver)
        self._create = CreateRequests(self._home._driver)

    def createNCR(self):
        print(self._layout)
        self._login.enter_username_textbox()
        self._login.enter_password_textbox()
        self._login.click_login_button()
        with Live(
            self._table, refresh_per_second=4, vertical_overflow="visible"
        ) as live:

            for _excel_index in range(START_ROW, self._MAX):
                # --------------------- BMCRemedy Create the Change Request as provided data ------------ #
                if self._create.is_home_page("IT Home"):
                    data: Dict[str, str] = self._xcel.get_row(_excel_index)
                    location_service = ("e.co", data.get("I"))

                    summary = f"{data.get('D')} || {data.get('G')}"
                    impact_list = make_data.make_impact_list(data.get("F"))
                    details = f"{summary}\n\n{data.get('E')}\n\n{impact_list}"

                    # ---------------make_data: Task Time Calculation ---------------- #
                    cr_start_time = make_data.get_change_start_time(data.get("B"))
                    start_downtime = make_data.get_service_start_downtime(data.get("B"))
                    end_downtime = make_data.get_service_end_downtime(
                        start_downtime, data.get("H")
                    )
                    activity_hour = make_data.get_change_close_start_time(data.get("B"))
                    cr_end_time = make_data.get_change_close_end_time(data.get("B"))
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
                    self._create.select_change_manager(data.get("K"))
                    self._create.insert_work_info(details)
                    self._create.change_location(location_service)
                    self._create.verify_summary(summary)
                    self._create.insert_schedule_date_time(cr_start_time, cr_end_time)
                    self._create.create_task_template()

                    self._create.fill_initiation_task(cr_start_time, start_downtime)
                    self._create.fill_service_downtime_duration_task(
                        start_downtime, end_downtime
                    )
                    self._create.fill_system_downtime_window_task(
                        start_downtime, activity_hour
                    )
                    self._create.fill_system_downtime_duration_task(
                        start_downtime, end_downtime
                    )
                    self._create.fill_review_closure_task(activity_hour, cr_end_time)
                    # ---------------------------------- END -------------------------------------------- #

                    # Write Data
                    self._xcel.insert_cr(_excel_index, change_number)
                    self._xcel.save()

                    # Console Data
                    console_data = (
                        str(_excel_index - 1),
                        data.get("I"),
                        data.get("G"),
                        data.get("C"),
                        change_number,
                        "✅",
                    )

                    # Save and go back to home page, need to tag site if service effective cr
                    if data.get("G") == "Service Effective":
                        query_formula = make_data.make_query_string(data.get("F"))
                        self._create.add_relationship_to_change(query_formula)
                        # ----------------------------------------------------------
                        # while True:
                        #     val = input("Press q after finished")
                        #     if val == 'q':
                        #         break
                        # self._create.save_change()
                        # ---------------------------------------------------------
                        self._create.goto_next_stage()
                        os.chdir(self._path)
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
                        # self._create.save_change()
                        # ----------------------------------------------------------
                        self._create.goto_next_stage()
                        os.chdir(self._path)
                        add_row_table(self._table, *console_data)
                        live.update(self._table)
                        self._create.reset_change_number()
                        self._create.go_back_to_homepage()
        self._home.click_logout_button()
        self._xcel.close()
