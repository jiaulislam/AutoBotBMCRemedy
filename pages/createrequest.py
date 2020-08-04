from selenium.common.exceptions import (NoSuchFrameException, ElementClickInterceptedException,
                                        NoSuchElementException, NoSuchWindowException)

from pages.base import BasePage
from utilities.locators import PageLocators

"""
This Class will help to create a full new Change Request as per shared 
data in the excel by the user. It's derived from BasePage Class.
"""


class CreateRequests(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.TNR_GROUP = ['Muhammad Shahed', 'Ripan Kumar']
        self.ANR_GROUP = ['Faisal Mahmud Fuad', 'Sumon Kumar Biswas', 'Shahriar Mahbub', 'Md. Musfiqur Rahman']
        self.__change_number = None

    def __set_change_number(self):
        """ Set the private variable of the class """
        self.__change_number = self.find_element(*PageLocators.CHANGE_NUMBER_VALUE).get_attribute("value")

    def __str__(self):
        """ Set the str of the object """
        return self.__change_number

    def get_change_number(self):
        """ Get the Change number """
        return self.__change_number

    def insert_text_summary(self, summary: str) -> None:
        """ Write the excel data into Summary section """
        self.write(PageLocators.SUMMARY_TEXTBOX, summary)

    def insert_text_notes(self, notes: str) -> None:
        """ Write the excel data into Notes section """
        self.write(PageLocators.NOTES_TEXTBOX, notes)

    def insert_impact_list_in_notes(self, impact_list: str) -> None:
        """ Write the impact list into the Notes Section """
        self.write(PageLocators.NOTES_TEXTBOX, impact_list)

    def insert_text_note_and_upload_files(self, notes: str, location_of_file: str) -> None:
        """ Write the info and attach the file in work info section """
        self.write(PageLocators.INFO_NOTES_TEXTBOX, notes)
        self.click(PageLocators.ATTACH_FILE_ICON_BUTTON)
        self.switch_to_frame(PageLocators.UPLOAD_ATTACHMENT_FRAME)
        self.write(PageLocators.CHOOSE_ATTACHMENT_FRAME, location_of_file)
        self.click(PageLocators.OK_ATTACHMENT_FRAME_BUTTON)
        self.driver.switch_to.default_content()
        self.click(PageLocators.ADD_NOTE_ATTACHMENT_BUTTON)

    def select_manager_group(self, change_manager: str) -> None:
        """ Select the manager domain depend on the shared change-manager name """
        self.click(PageLocators.MANAGER_GROUP_BTN)
        self.hover_over(PageLocators.IMPLEMENTATION_MENU)

        if change_manager in self.TNR_GROUP:
            self.hover_over(PageLocators.TNR_GROUP_MENU)
            self.hover_over(PageLocators.TX_OPTIMIZATION_SELECT_BTN)
            self.click(PageLocators.TX_OPTIMIZATION_SELECT_BTN)
        elif change_manager in self.ANR_GROUP:
            self.hover_over(PageLocators.ANR_GROUP_MENU)
            self.hover_over(PageLocators.RADIO_ROLLOUT_SELECT_BTN)
            self.click(PageLocators.RADIO_ROLLOUT_SELECT_BTN)
        else:
            self.hover_over(PageLocators.TNR_GROUP_MENU)
            self.hover_over(PageLocators.TX_OPTIMIZATION_SELECT_BTN)
            self.click(PageLocators.TX_OPTIMIZATION_SELECT_BTN)

    def select_change_manager(self, change_manager: str) -> None:
        """ Select the change manager shared by the user """
        self.click(PageLocators.CHANGE_MANAGER_MENU_BTN)

        if change_manager == self.TNR_GROUP[0]:
            self.click(PageLocators.CHANGE_MANAGER_SHAHED)
        elif change_manager == self.TNR_GROUP[1]:
            self.click(PageLocators.CHANGE_MANAGER_RIPAN)
        elif change_manager == self.ANR_GROUP[0]:
            self.click(PageLocators.CHANGE_MANAGER_FUAD)
        elif change_manager == self.ANR_GROUP[1]:
            self.click(PageLocators.CHANGE_MANAGER_SUMON)
        elif change_manager == self.ANR_GROUP[2]:
            self.click(PageLocators.CHANGE_MANAGER_SHAHRIAR)
        elif change_manager == self.ANR_GROUP[3]:
            self.click(PageLocators.CHANGE_MANAGER_MUSFIQ)
        else:
            raise ValueError("Manager Not Found !")

    def change_location(self, location_details: tuple) -> None:

        # Need to store Parent windows ID cause after click new Window will pop-up
        print()
        parent_window = self.driver.current_window_handle
        self.click(PageLocators.LOCATION_MENU_BTN)
        for child_window in self.driver.window_handles:
            if child_window != parent_window:
                self.driver.switch_to.window(child_window)
                self.click(PageLocators.CLEAR_BUTTON)
                self.click(PageLocators.SEARCH_ICON_IMG)
                # Another window pop-up after clicking Search button.
                for grand_child_window in self.driver.window_handles:
                    if grand_child_window != parent_window and grand_child_window != child_window:
                        # Switch to the new Child window
                        self.driver.switch_to.window(grand_child_window)
                        # Insert all the necessary info from here
                        self.write(PageLocators.COMPANY_TEXTBOX, location_details[0])
                        self.write(PageLocators.REGION_TEXTBOX, location_details[1])
                        self.write(PageLocators.SITE_GROUP_TEXTBOX, location_details[2])
                        self.write(PageLocators.SITE_TEXTBOX, location_details[3])
                        self.click(PageLocators.SEARCH_LOCATION_BTN)
                        self.click(PageLocators.SELECT_LOCATION_BTN)
                        break
                self.driver.switch_to.window(child_window)
                self.click(PageLocators.OK_LOCATION_BTN)
                break
        self.driver.switch_to.window(parent_window)

    def insert_schedule_date_time(self, start_time: str, end_time: str) -> None:
        """ Insert date into date section of the page. """

        # Click on the Date tab on the Page
        self.click(PageLocators.DATE_PAGE)
        # Write the start Date on Actual Start Date Textbox
        self.write(PageLocators.START_DATE_INPUT, start_time)
        # Write the End Date on Actual End Date Textbox
        self.write(PageLocators.END_DATE_INPUT, end_time)

    def create_task_template(self) -> None:
        """ Create the Five-Stage Template Task """

        # Click on the Task on the page
        self.click(PageLocators.TASK_PAGE)
        # Click on the Task Request type button/input area
        self.click(PageLocators.REQUEST_TYPE_BTN)
        # Select the Task Group Template for the Change Request
        self.click(PageLocators.TASK_GROUP_TEMPLATE_BTN)
        # Click on the Relate to select the Template
        self.click(PageLocators.RELATE_BTN)
        parent_window = self.driver.current_window_handle
        # A new Windows pops up, so need the parent window later
        for new_child_window in self.driver.window_handles:
            if new_child_window != parent_window:
                # Found the New Child Window for task template selection
                self.driver.switch_to.window(new_child_window)
                # Click on the related to select the default template
                self.click(PageLocators.TASK_RELATE_BTN)
                # if all ok then should break the loop here, as after this child
                # window will be vanished automatically
                break
        # As the previous child windows vanished, default should be parent window
        self.driver.switch_to.window(parent_window)
        # Click on the Task Group template that was created
        self.click(PageLocators.TASK_GROUP_ROW_SPAN)

    def fill_initiation_task(self, start_time: str, end_time: str) -> None:
        """ Fill up the date time in Initiation Phase Task """
        task_page = self.driver.current_window_handle
        self.double_click(PageLocators.INITIATION_TASK_SPAN)
        self.__set_date_time_in_task(task_page, start_time, end_time)

    def fill_service_downtime_duration_task(self, start_downtime: str, end_downtime: str) -> None:
        """ Fill up the date time in Service Downtime duration Phase Task """
        task_page = self.driver.current_window_handle
        self.double_click(PageLocators.SERVICE_DOWNTIME_DURATION_TASK_SPAN)
        self.__set_date_time_in_task(task_page, start_downtime, end_downtime)

    def fill_system_downtime_window_task(self, work_window_begin: str, work_window_end: str) -> None:
        """ Fill up the date time in System Downtime Window Phase Task """
        task_page = self.driver.current_window_handle
        self.double_click(PageLocators.SERVICE_DOWNTIME_WINDOW_TASK_SPAN)
        self.__set_date_time_in_task(task_page, work_window_begin, work_window_end)
        # TODO: Now that the Relationship adding work is done, need a way to handle it

    def fill_system_downtime_duration_task(self, start_downtime: str, end_downtime: str) -> None:
        """ Fill up the date time in System Downtime duration Phase Task """
        task_page = self.driver.current_window_handle
        self.double_click(PageLocators.SYSTEM_DOWNTIME_TASK)
        self.__set_date_time_in_task(task_page, start_downtime, end_downtime)

    def fill_review_closure_task(self, close_start_time: str, close_end_time: str) -> None:
        """ Fill up the date time in Review & Closure Phase Task """
        task_page = self.driver.current_window_handle
        self.double_click(PageLocators.REVIEW_CLOSURE_TASK_SPAN)
        self.__set_date_time_in_task(task_page, close_start_time, close_end_time)

    def save_change(self) -> None:
        """ Save the Change Request """
        self.click(PageLocators.SAVE_CHANGE_BTN)

    def go_back_to_homepage(self) -> None:
        """ Get Back to the Homepage """
        self.back_to_home_page(PageLocators.IT_HOME_BUTTON)

    def __set_date_time_in_task(self, parent_window: object, start_time: str, end_time: str) -> None:
        """ Private function for repetitive task in Filling up tasks """
        for child_window in self.driver.window_handles:
            if child_window != parent_window:
                self.driver.switch_to.window(child_window)
                self.click(PageLocators.DATE_SECTOR_IN_TASK)
                self.write(PageLocators.START_TIME_IN_TASK, start_time)
                self.write(PageLocators.END_TIME_IN_TASK, end_time)
                self.click(PageLocators.SAVE_TASK_BTN)
                break
        self.driver.switch_to.window(parent_window)

    def __add_relationship_to_change(self, main_task_page: object, relationship_query_formula: str) -> None:
        """ Add the relationship to the Change request if the Change is a Service Effective Change """
        # WARNING: EXPERIMENTAL OPTION
        parent_window = self.driver.current_window_handle

        for first_window in self.driver.window_handles:
            if first_window != parent_window:
                self.driver.switch_to.window(first_window)
                self.click(PageLocators.RELATIONSHIP_TAB)
                self.click(PageLocators.RELATIONSHIP_TYPE_LIST)
                self.hover_over(PageLocators.CONFIGURATION_ITEM)
                self.click(PageLocators.RELATIONSHIP_TYPE_SELECT)
                self.click(PageLocators.RELATIONSHIP_WINDOW_SEARCH_BTN)
                for second_window in self.driver.window_handles:
                    if second_window != parent_window and second_window != first_window:
                        self.driver.switch_to.window(second_window)
                        self.click(PageLocators.RELATIONSHIP_ADVANCE_SEARCH_LINK)
                        self.write(PageLocators.RELATIONSHIP_QUERY_TEXTBOX, relationship_query_formula)
                        self.click(PageLocators.RELATIONSHIP_ADVANCE_SEARCH_BTN)
                        # Wait until the search is complete !  INFINITE LOOP
                        while True:
                            try:
                                self.send_ctrl_plus_a(PageLocators.RELATIONSHIP_ROBI_AXIATA)
                                self.click(PageLocators.RELATE_THE_RELATIONSHIP_BTN)
                                # Wait Until the Relate button doesn't finished with the add of the relationship
                                while True:
                                    try:
                                        # After relationship add a frame is to be expected. handle the frame
                                        self.check_for_expected_frame(PageLocators.FRAME_OK_BUTTON)
                                        # break the parent to this block loop
                                        break
                                    except NoSuchFrameException:
                                        pass
                                try:
                                    for third_window in self.driver.window_handles:
                                        if third_window != parent_window and third_window != second_window and third_window != first_window and third_window != main_task_page:
                                            self.driver.switch_to.window(third_window)
                                            self.click(PageLocators.RELATION_NEW_WINDOW_CLOSE_BTN)
                                            self.driver.switch_to.window(parent_window)
                                            self.click(PageLocators.SAVE_TASK_BTN)
                                            # break the parent to this block loop
                                            break
                                    # Break the Whole while loop
                                    break
                                except NoSuchWindowException:
                                    pass
                            except (NoSuchElementException, ElementClickInterceptedException):
                                pass
        self.driver.switch_to.window(main_task_page)
