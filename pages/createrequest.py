import time

from selenium.common.exceptions import (NoSuchFrameException, ElementClickInterceptedException,
                                        NoSuchElementException, NoSuchWindowException)
from utilities.static_data import StaticData

from pages.base import BasePage
from utilities.locators import (RelationshipQueryLocators, CommonChangeCreateLocators,
                                ChangeManagerLocators, LocationServiceLocators,
                                TaskSectionLocators, WorkInfoAttachment,
                                SummaryAndNotesBox, DateSectionSelector,
                                CommonTaskDateLocators, HomePageLocators,
                                SaveChangeLocators, FrameBoxLocators)
from utilities.terminal_colors import bcolors
"""
This Class will help to create a full new Change Request as per shared 
data in the excel by the user. It's derived from BasePage Class.
"""


class CreateRequests(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.TNR_GROUP = ['Muhammad Shahed', 'Ripan Kumar', 'Sudipta Das']
        self.ANR_GROUP = ['Faisal Mahmud Fuad', 'Sumon Kumar Biswas', 'Shahriar Mahbub', 'Md. Musfiqur  Rahman', 'Md. Rakibuzzaman', 'K.M Khairul Bashar']
        self.__change_number = ""

    def __set_change_number(self):
        """ Set the private variable of the class """
        self.__change_number = self.find_element(*CommonChangeCreateLocators.CHANGE_NUMBER_VALUE).get_attribute('value')

    def __str__(self):
        """ Set the str of the object """
        return self.__change_number

    def get_change_number(self):
        """ Get the Change number """
        return self.__change_number

    def insert_text_summary(self, summary: str) -> None:
        """ Write the excel data into Summary section """
        self.__set_change_number()
        self.write(SummaryAndNotesBox.SUMMARY_TEXTBOX, summary)

    def insert_text_notes(self, notes: str) -> None:
        """ Write the excel data into Notes section """
        self.write(SummaryAndNotesBox.NOTES_TEXTBOX, notes)

    def insert_impact_list_in_notes(self, impact_list: str) -> None:
        """ Write the impact list into the Notes Section """
        self.write(SummaryAndNotesBox.NOTES_TEXTBOX, impact_list)

    def insert_text_note_and_upload_files(self, notes: str, location_of_file: str) -> None:
        """ Write the info and attach the file in work info section """
        self.write(WorkInfoAttachment.INFO_NOTES_TEXTBOX, notes)
        self.click(WorkInfoAttachment.ATTACH_FILE_ICON_BUTTON)
        if self.__get_title_of_view_attachment_btn():
            self.switch_to_frame(WorkInfoAttachment.UPLOAD_ATTACHMENT_FRAME)
            self.write(WorkInfoAttachment.CHOOSE_ATTACHMENT_FRAME, location_of_file)
            time.sleep(1)
            self.click(WorkInfoAttachment.OK_ATTACHMENT_FRAME_BUTTON)
            # TODO: Need to do something about this implicit wait
            time.sleep(1)
            self.driver.switch_to.default_content()
        self.click(WorkInfoAttachment.ADD_NOTE_ATTACHMENT_BUTTON)

    def select_manager_group(self, change_manager: str) -> None:
        """ Select the manager domain depend on the shared change-manager name """
        self.click(ChangeManagerLocators.MANAGER_GROUP_BTN)
        self.hover_over(ChangeManagerLocators.IMPLEMENTATION_MENU)

        if change_manager in self.TNR_GROUP:
            self.hover_over(ChangeManagerLocators.TNR_GROUP_MENU)
            self.hover_over(ChangeManagerLocators.TX_OPTIMIZATION_SELECT_BTN)
            self.click(ChangeManagerLocators.TX_OPTIMIZATION_SELECT_BTN)
        elif change_manager in self.ANR_GROUP:
            self.hover_over(ChangeManagerLocators.ANR_GROUP_MENU)
            self.hover_over(ChangeManagerLocators.RADIO_ROLLOUT_SELECT_BTN)
            self.click(ChangeManagerLocators.RADIO_ROLLOUT_SELECT_BTN)
        else:
            self.hover_over(ChangeManagerLocators.TNR_GROUP_MENU)
            self.hover_over(ChangeManagerLocators.TX_OPTIMIZATION_SELECT_BTN)
            self.click(ChangeManagerLocators.TX_OPTIMIZATION_SELECT_BTN)

    def select_change_manager(self, change_manager: str) -> None:
        """ Select the change manager shared by the user """
        self.click(ChangeManagerLocators.CHANGE_MANAGER_MENU_BTN)

        if change_manager == self.TNR_GROUP[0]:
            self.click(ChangeManagerLocators.CHANGE_MANAGER_SHAHED)
        elif change_manager == self.TNR_GROUP[1]:
            self.click(ChangeManagerLocators.CHANGE_MANAGER_RIPAN)
        elif change_manager == self.TNR_GROUP[2]:
            self.click(ChangeManagerLocators.CHANGE_MANAGER_SUDIPTA)
        elif change_manager == self.ANR_GROUP[0]:
            self.click(ChangeManagerLocators.CHANGE_MANAGER_FUAD)
        elif change_manager == self.ANR_GROUP[1]:
            self.click(ChangeManagerLocators.CHANGE_MANAGER_SUMON)
        elif change_manager == self.ANR_GROUP[2]:
            self.click(ChangeManagerLocators.CHANGE_MANAGER_SHAHRIAR)
        elif change_manager == self.ANR_GROUP[3]:
            self.click(ChangeManagerLocators.CHANGE_MANAGER_MUSFIQ)
        elif change_manager == self.ANR_GROUP[4]:
            self.click(ChangeManagerLocators.CHANGE_MANAGER_RAKIB)
        elif change_manager == self.ANR_GROUP[5]:
            self.click(ChangeManagerLocators.CHANGE_MANAGER_KHAIRUL)
        else:
            raise ValueError("Manager Not Found !")

    def change_location(self, change_location_details: tuple) -> None:
        """ Change the location details of the change request """

        # Need to store Parent windows ID cause after click new Window will pop-up
        parent_window = self.driver.current_window_handle
        self.click(LocationServiceLocators.LOCATION_MENU_BTN)
        # Handle the new window of Location
        for child_window in self.driver.window_handles:
            if child_window != parent_window:
                self.driver.switch_to.window(child_window)
                self.click(LocationServiceLocators.CLEAR_BUTTON)
                self.click(LocationServiceLocators.SEARCH_ICON_IMG)
                # Another window pop-up after clicking Search button.
                for grand_child_window in self.driver.window_handles:
                    if grand_child_window != parent_window and grand_child_window != child_window:
                        # Switch to the new Child window
                        self.driver.switch_to.window(grand_child_window)
                        # Insert all the necessary info from here
                        self.write(LocationServiceLocators.COMPANY_TEXTBOX, change_location_details[0])
                        self.write(LocationServiceLocators.REGION_TEXTBOX, change_location_details[1])
                        self.write(LocationServiceLocators.SITE_GROUP_TEXTBOX, change_location_details[2])
                        self.write(LocationServiceLocators.SITE_TEXTBOX, change_location_details[3])
                        self.click(LocationServiceLocators.SEARCH_LOCATION_BTN)
                        self.click(LocationServiceLocators.SELECT_LOCATION_BTN)
                        break
                self.driver.switch_to.window(child_window)
                self.click(LocationServiceLocators.OK_LOCATION_BTN)
                break
        self.driver.switch_to.window(parent_window)

    def insert_schedule_date_time(self, start_time: str, end_time: str) -> None:
        """ Insert date into date section of the page. """

        # Click on the Date tab on the Page
        self.click(DateSectionSelector.DATE_PAGE)
        # Write the start Date on Actual Start Date Textbox
        self.write(DateSectionSelector.START_DATE_INPUT, start_time)
        # Write the End Date on Actual End Date Textbox
        self.write(DateSectionSelector.END_DATE_INPUT, end_time)

    def create_task_template(self) -> None:
        """ Create the Five-Stage Template Task """

        # Click on the Task on the page
        self.click(TaskSectionLocators.TASK_PAGE)
        # Click on the Task Request type button/input area
        self.click(TaskSectionLocators.REQUEST_TYPE_BTN)
        # Select the Task Group Template for the Change Request
        self.click(TaskSectionLocators.TASK_GROUP_TEMPLATE_BTN)
        # Click on the Relate to select the Template
        self.click(TaskSectionLocators.RELATE_BTN)
        parent_window = self.driver.current_window_handle
        # A new Windows pops up, so need the parent window later
        for new_child_window in self.driver.window_handles:
            if new_child_window != parent_window:
                # Found the New Child Window for task template selection
                self.driver.switch_to.window(new_child_window)
                # Click on the related to select the default template
                self.click(TaskSectionLocators.TASK_RELATE_BTN)
                # if all ok then should break the loop here, as after this child
                # window will be vanished automatically
                break
        # As the previous child windows vanished, default should be parent window
        self.driver.switch_to.window(parent_window)
        # Click on the Task Group template that was created
        self.click(TaskSectionLocators.TASK_GROUP_ROW_SPAN)

    def fill_initiation_task(self, start_time: str, end_time: str) -> None:
        """ Fill up the date time in Initiation Phase Task """
        task_page = self.driver.current_window_handle
        self.double_click(TaskSectionLocators.INITIATION_TASK_SPAN)
        self.__set_date_time_in_task(task_page, start_time, end_time)

    def fill_service_downtime_duration_task(self, start_downtime: str, end_downtime: str) -> None:
        """ Fill up the date time in Service Downtime duration Phase Task """
        task_page = self.driver.current_window_handle
        self.double_click(TaskSectionLocators.SERVICE_DOWNTIME_DURATION_TASK_SPAN)
        self.__set_date_time_in_task(task_page, start_downtime, end_downtime)

    def fill_system_downtime_window_task(self, work_window_begin: str, work_window_end: str) -> None:
        """ Fill up the date time in System Downtime Window Phase Task """
        task_page = self.driver.current_window_handle
        self.double_click(TaskSectionLocators.SERVICE_DOWNTIME_WINDOW_TASK_SPAN)
        self.__set_date_time_in_task(task_page, work_window_begin, work_window_end)
        # TODO: Now that the Relationship adding work is done, need a way to handle it

    def fill_system_downtime_duration_task(self, start_downtime: str, end_downtime: str) -> None:
        """ Fill up the date time in System Downtime duration Phase Task """
        task_page = self.driver.current_window_handle
        self.double_click(TaskSectionLocators.SYSTEM_DOWNTIME_TASK)
        self.__set_date_time_in_task(task_page, start_downtime, end_downtime)

    def fill_review_closure_task(self, close_start_time: str, close_end_time: str) -> None:
        """ Fill up the date time in Review & Closure Phase Task """
        task_page = self.driver.current_window_handle
        self.double_click(TaskSectionLocators.REVIEW_CLOSURE_TASK_SPAN)
        self.__set_date_time_in_task(task_page, close_start_time, close_end_time)

    def save_change(self) -> None:
        """ Save the Change Request """
        self.click(SaveChangeLocators.SAVE_CHANGE_BTN)

    def goto_next_stage(self) -> None:
        """ Take the Change request to the next stage """
        self.click(SaveChangeLocators.GOTO_NEXT_STAGE_BTN)

    def go_back_to_homepage(self) -> None:
        """ Get Back to the Homepage """
        try:
            self.back_to_home_page(HomePageLocators.IT_HOME_BUTTON)
        except ElementClickInterceptedException:
            # for click intercepted a Warning Box is available on page. Need to handle that.
            self.check_for_expected_frame(FrameBoxLocators.FRAME_OF_CONFIRMATION, FrameBoxLocators.FRAME_OK_BUTTON)
            # after then go back to home page
            self.back_to_home_page(HomePageLocators.IT_HOME_BUTTON)

    def __get_title_of_view_attachment_btn(self) -> bool:

        try:
            if self.find_element(*WorkInfoAttachment.VIEW_ATTACHMENT_BUTTON).get_attribute("title") == StaticData.VIEW_ATTACHMENT_DEFAULT_STATE:
                return True
            else:
                return False
        except NoSuchElementException:
            print(f"{bcolors.WARNING}Attachment status unable to fetch. {bcolors.ENDC}")
            pass

    def __set_date_time_in_task(self, parent_window: object, start_time: str, end_time: str) -> None:
        """ Private function for repetitive task in Filling up tasks """
        for child_window in self.driver.window_handles:
            if child_window != parent_window:
                self.driver.switch_to.window(child_window)
                self.click(CommonTaskDateLocators.DATE_SECTOR_IN_TASK)
                self.write(CommonTaskDateLocators.START_TIME_IN_TASK, start_time)
                self.write(CommonTaskDateLocators.END_TIME_IN_TASK, end_time)
                self.click(CommonTaskDateLocators.SAVE_TASK_BTN)
                break
        self.driver.switch_to.window(parent_window)

    def add_relationship_to_change(self, relationship_query_formula: str) -> None:
        """ Add the relationship to the Change request if the Change is a Service Effective Change """
        self.click(RelationshipQueryLocators.RELATIONSHIP_TAB_BTN)
        parent_window = self.driver.current_window_handle
        self.click(RelationshipQueryLocators.RECORD_TYPE_TEXTAREA)
        self.hover_over(RelationshipQueryLocators.CONFIGURATION_ITEM_LIST)
        self.click(RelationshipQueryLocators.CONFIGURATION_ITEM_LIST)
        self.click(RelationshipQueryLocators.SEARCH_BTN)

        for first_window in self.driver.window_handles:
            if first_window != parent_window:
                self.driver.switch_to.window(first_window)
                self.click(RelationshipQueryLocators.RELATIONSHIP_ADVANCE_SEARCH_LINK)
                self.write(RelationshipQueryLocators.RELATIONSHIP_QUERY_TEXTBOX, relationship_query_formula)
                self.click(RelationshipQueryLocators.RELATIONSHIP_ADVANCE_SEARCH_BTN)
                # Wait until the search is complete !  INFINITE LOOP
                while True:
                    try:
                        self.send_ctrl_plus_a(RelationshipQueryLocators.RELATIONSHIP_ROBI_AXIATA)
                        while True:
                            try:
                                self.click(RelationshipQueryLocators.RELATE_THE_RELATIONSHIP_BTN)
                                break
                            except ElementClickInterceptedException:
                                pass
                        # Wait Until the Relate button doesn't finished with the add of the relationship
                        while True:
                            try:
                                # After relationship add a frame is to be expected. handle the frame
                                self.check_for_expected_frame(FrameBoxLocators.FRAME_OF_CONFIRMATION, FrameBoxLocators.FRAME_OK_BUTTON)
                                # break the parent to this block loop
                                break
                            except NoSuchFrameException:
                                pass
                    except NoSuchElementException:
                        pass
                    except NoSuchWindowException:
                        break
        self.driver.switch_to.window(parent_window)
