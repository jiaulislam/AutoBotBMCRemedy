from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    NoSuchWindowException,
    NoSuchFrameException
)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage
from utilites.locators import (
    CommonChangeCreateLocators,
    RelationshipQueryLocators,
    LocationServiceLocators,
    CommonTaskDateLocators,
    ChangeManagerLocators,
    DateSectionSelector,
    TaskSectionLocators,
    SummaryAndNotesBox,
    SaveChangeLocators,
    WorkInfoAttachment,
    HomePageLocators,
    FrameBoxLocators
)
from utilites.static_data import StaticData
from utilites.terminal_colors import Colors

"""
This Class will help to create a full new Change Request as per shared 
data in the excel by the user. It's derived from BasePage Class.

written by: jiaul_islam
"""


class CreateRequests(BasePage):

    def __init__(self, driver):
        super().__init__(driver, timeout=30)
        self.TNR_GROUP = [
            'Muhammad Shahed',
            'Ripan Kumar',
            'Sudipta Das'
        ]
        self.ANR_GROUP = [
            'Faisal Mahmud Fuad',
            'Sumon Kumar Biswas',
            'Shahriar Mahbub',
            'Md. Musfiqur  Rahman',
            'Md. Rakibuzzaman',
            'K.M Khairul Bashar'
        ]
        self.__change_number = ""

    def set_change_number(self):
        """ Set the private variable of the class """
        while self.__change_number == "":
            try:
                self.__change_number = self.get_value_of_element(
                    CommonChangeCreateLocators.CHANGE_NUMBER_VALUE)
            except NoSuchElementException:
                raise NoSuchElementException("SET_CHANGE_NUMBER | NO SUCH ELEMENT EXCEPTION")

    def reset_change_number(self):
        """ Reset the Change Number Variable """
        if self.__change_number == "":
            pass
        else:
            self.__change_number = ""

    def __str__(self):
        """ Set the str of the object """
        return self.__change_number

    def get_change_number(self):
        """ Get the Change number """
        return self.__change_number

    def insert_text_summary(self, summary: str) -> None:
        """ Write the excel data into Summary section """
        self.write(SummaryAndNotesBox.SUMMARY_TEXTBOX, summary)

    def insert_text_notes(self, notes: str) -> None:
        """ Write the excel data into Notes section """
        self.write(SummaryAndNotesBox.NOTES_TEXTBOX, notes)

    def insert_impact_list_in_notes(self, impact_list: str) -> None:
        """ Write the impact list into the Notes Section """
        self.write(SummaryAndNotesBox.NOTES_TEXTBOX, impact_list)

    def insert_work_info(self, notes: str) -> None:
        """ Write the info and attach the file in work info section """
        self.write(WorkInfoAttachment.INFO_NOTES_TEXTBOX, notes)
        self.click(WorkInfoAttachment.ADD_NOTE_ATTACHMENT_BUTTON)

    def select_manager_group(self) -> None:
        """ Select the manager domain depend on the shared change-manager name """
        self.click(ChangeManagerLocators.MANAGER_GROUP_BTN)
        self.hover_over(ChangeManagerLocators.IMPLEMENTATION_MENU)
        self.hover_over(ChangeManagerLocators.ANR_GROUP_MENU)
        self.click(ChangeManagerLocators.RADIO_ROLLOUT_SELECT_BTN)

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
            print(f"{Colors.WARNING}Manager Not Found ! Using Default Manager: {self.TNR_GROUP[0]}{Colors.ENDC}")
            self.click(ChangeManagerLocators.CHANGE_MANAGER_SHAHED)

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
                        self.write(LocationServiceLocators.SITE_TEXTBOX, change_location_details[1])
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
        try:
            self.click(SaveChangeLocators.SAVE_CHANGE_BTN)
        except ElementClickInterceptedException:
            self.click(SaveChangeLocators.SAVE_CHANGE_BTN)

    def goto_next_stage(self) -> None:
        """ Take the Change request to the next stage """
        try:
            self.click(SaveChangeLocators.GOTO_NEXT_STAGE_BTN)
        except ElementClickInterceptedException:
            self.click(SaveChangeLocators.GOTO_NEXT_STAGE_BTN)

    def go_back_to_homepage(self) -> None:
        """ Get Back to the Homepage """
        try:
            self.wait_for_loading_icon_disappear(*CommonChangeCreateLocators.LOADING_ICON)
            self.back_to_home_page(HomePageLocators.IT_HOME_BUTTON)
        except ElementClickInterceptedException:
            # for click intercepted a Warning Box is available on page. Need to handle that.
            self.check_for_expected_frame(
                FrameBoxLocators.FRAME_OF_CONFIRMATION, FrameBoxLocators.FRAME_OK_BUTTON)
            # after then go back to home page
            self.back_to_home_page(HomePageLocators.IT_HOME_BUTTON)

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

    def verify_summary(self, summary: str):
        """ Verify if the Summary Box is empty or not """
        contents = self.driver.find_element(*SummaryAndNotesBox.SUMMARY_TEXTBOX).get_attribute('value').strip()
        if contents == "" or len(contents) == 0:
            self.driver.find_element(*SummaryAndNotesBox.SUMMARY_TEXTBOX).clear()
            self.insert_text_summary(summary)
        else:
            pass

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
                                self.check_for_expected_frame(
                                    FrameBoxLocators.FRAME_OF_CONFIRMATION, FrameBoxLocators.FRAME_OK_BUTTON)
                                # break the parent to this block loop
                                break
                            except NoSuchFrameException:
                                pass
                    except NoSuchElementException:
                        pass
                    except NoSuchWindowException:
                        break
        self.driver.switch_to.window(parent_window)

    def is_home_page(self, validating_text: str = "IT HOME"):
        """ Verify if the current page is loaded and it's home page """
        self.__verify_change()

        page_txt = None
        while self.is_visible(HomePageLocators.IT_HOME_TEXT):
            page_txt = self.find_element(*HomePageLocators.IT_HOME_TEXT).text
            break

        isVisible = self.is_visible(HomePageLocators.IT_HOME_TEXT)
        if validating_text == page_txt and isVisible:
            return True
        else:
            return False

    def __verify_change(self):
        """ Check the Change Number from current & previous. Need to meet the condition must """
        value = None

        try:
            value = self.find_element(*CommonChangeCreateLocators.CHANGE_NUMBER_VALUE).get_attribute('value')
        except NoSuchElementException:
            value = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(CommonChangeCreateLocators.CHANGE_NUMBER_VALUE)).get_attribute('value')
        except AttributeError:
            # TODO: Need to Find out why it's giving me None Type if value is changing
            pass
        while True:
            if self.get_change_number() != value:
                break
            else:
                pass
