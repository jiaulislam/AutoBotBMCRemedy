from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    TimeoutException
)
from utilities.locators import (
    CloseChangeLocators,
    CancelRequestLocators,
    TaskSectionLocators,
    DateSectionSelector,
    CommonTaskDateLocators,
    FrameBoxLocators
)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base import BasePage
from typing import NoReturn
import time
"""
This class will help us to close the Change Request as per user requirement.
it will inherit the base page class for the basic functionality.
"""


class CloseRequests(BasePage):
    """ Close the Change Request in BMC Remedy """

    def __init__(self, driver):
        super().__init__(driver)
        self.__change_type: bool = False
        self.__change_number: str = ""
        self.__invalid_change_numbers: list = []

    def __set_change_number(self, change_number: str) -> NoReturn:
        """ Set the value of Change Number """
        self.__change_number = change_number

    def get_change_number(self) -> str:
        """ Get the Value of Change Number """
        return self.__change_number

    def __set_change_type(self) -> NoReturn:
        """ Set the Value of Change Type """
        self.__change_type = self.__is_service_effective()

    def get_change_type(self) -> bool:
        """ Get the Change Request type """
        return self.__change_type

    def get_actual_start_date(self) -> (str, None):
        """ Get the Closing Change Request Date & Time """
        self.click(DateSectionSelector.DATE_PAGE)
        if self.get_value_of_element(CloseChangeLocators.CHANGE_REQUEST_OPEN) != "":
            return self.get_value_of_element(CloseChangeLocators.CHANGE_REQUEST_OPEN)
        else:
            return None

    @staticmethod
    def get_index_for_change_number(change_number: str, list_of_change_number: list) -> (int, None):
        """ returns the correct position of the change number from the list """
        try:
            return list_of_change_number.index(change_number) + 2
        except ValueError:
            return None

    def add_change_to_invalid_list(self, change_number: str):
        """ append the invalid change_number found the the invalid list """
        self.__invalid_change_numbers.append(change_number)

    def find_the_change_request(self, change_number: str, index: int):
        """ Find the Change Request with respect to user shared number"""

        final_xpath = "//table[@id='T301444200']//tr[" + str(index) + "]//td[1]/nobr[1]/span"

        dynamicXPATH = CloseChangeLocators.get_changeable_xpath(final_xpath)  # get the tuple

        try:
            self.double_click(dynamicXPATH)
            self.__set_change_number(change_number)  # set the change number for future use
        except NoSuchElementException as error:
            print(error)

    def get_invalid_change_numbers(self) -> NoReturn:
        """ Fetch all the invalid change numbers from the list """
        if len(self.__invalid_change_numbers):
            print("Below change request number not found:")
            for inv in self.__invalid_change_numbers:
                print(inv)
            print("\n")
        else:
            pass

    def __is_task_closed_already(self) -> bool:
        """ Check if the task is already closed or not """
        if self.get_value_of_element(CloseChangeLocators.TASK_INIT_STATUS) == "Closed":
            return True
        else:
            return False

    def is_change_status_closed(self) -> bool:
        """
        Check if the Change status is already closed or completed
        """
        status = self.get_value_of_element(CancelRequestLocators.STATUS_AREA)

        if status == 'Closed' or status == 'Completed':
            return True
        else:
            return False

    def __is_service_effective(self) -> bool:
        """Check if the current working Change is service effective or not.
            :rtype: bool
        """
        try:
            if self.is_visible(CloseChangeLocators.START_TIME_IN_TASK):
                if self.get_value_of_element(CloseChangeLocators.START_TIME_IN_TASK) != self.get_value_of_element(
                        CloseChangeLocators.END_TIME_IN_TASK):
                    return True
                else:
                    pass
        except NoSuchElementException as error:
            print(error)

    def __back_to_change_task_page(self) -> NoReturn:
        """ Go back to the Change request control page """
        makeXPATH = f"//a[@class='btn'][contains(text(),'{self.__change_number}')]"
        dynamicXPATH = CloseChangeLocators.get_changeable_xpath(makeXPATH)
        self.back_to_home_page(dynamicXPATH)

    def close_service_downtime_duration_task(self, actual_start_time: str, actual_end_time: str) -> NoReturn:
        """
        Close the Task for: Service_Downtime_Duration_Task(2) ,
        If CR Task Status is already closed then will go back to
        the task page.
        """
        self.double_click(TaskSectionLocators.SERVICE_DOWNTIME_DURATION_TASK_SPAN)

        if not self.__is_task_closed_already():
            self.click(CommonTaskDateLocators.DATE_SECTOR_IN_TASK)
            self.__set_change_type()
            self.__common_closing_activity(actual_start_time, actual_end_time)
        else:
            print("WARN: Service Downtime Duration Task is closed already !")
            self.__back_to_change_task_page()
            time.sleep(2)

    def close_service_downtime_window_task(self, actual_start_time: str, current_time_of_user: str) -> NoReturn:
        """
        Close the Task for: Service_Downtime_Window_Task(3) ,
        If CR Task Status is already closed then will go back to
        the task page.
        """
        try:
            if self.is_visible(TaskSectionLocators.SERVICE_DOWNTIME_WINDOW_TASK_SPAN):
                self.double_click(TaskSectionLocators.SERVICE_DOWNTIME_WINDOW_TASK_SPAN)
            else:
                try:
                    time.sleep(2)
                    self.double_click(TaskSectionLocators.SERVICE_DOWNTIME_WINDOW_TASK_SPAN)
                except TimeoutException:
                    self.double_click(TaskSectionLocators.SERVICE_DOWNTIME_WINDOW_TASK_SPAN)
        except (StaleElementReferenceException, NoSuchElementException):
            element = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(TaskSectionLocators.SERVICE_DOWNTIME_WINDOW_TASK_SPAN))
            self.double_click(element)

        if not self.__is_task_closed_already():
            self.click(CommonTaskDateLocators.DATE_SECTOR_IN_TASK)
            self.write(CloseChangeLocators.CLOSE_START_DATE, actual_start_time)
            self.write(CloseChangeLocators.CLOSE_END_DATE, current_time_of_user)
            self.click(CloseChangeLocators.CLOSE_MENU_SELECT)
            self.hover_over(CloseChangeLocators.SELECT_CLOSE_FROM_LST)
            self.click(CloseChangeLocators.SELECT_CLOSE_FROM_LST)
            self.click(CommonTaskDateLocators.SAVE_TASK_BTN)
            self.__back_to_change_task_page()
            time.sleep(2)
        else:
            print("WARN: Service Downtime Window Task is closed already !")
            self.__back_to_change_task_page()
            time.sleep(2)

    def close_system_downtime_duration_task(self, actual_start_time: str, actual_end_time: str) -> NoReturn:
        """
            Close the Task for: System_Downtime_Task(4) ,
            If CR Task Status is already closed then will go back to
            the task page.
        """
        try:
            if self.is_visible(TaskSectionLocators.SYSTEM_DOWNTIME_TASK):
                self.double_click(TaskSectionLocators.SYSTEM_DOWNTIME_TASK)
            else:
                try:
                    time.sleep(2)
                    self.double_click(TaskSectionLocators.SYSTEM_DOWNTIME_TASK)
                except TimeoutException:
                    time.sleep(5)
                    self.double_click(TaskSectionLocators.SYSTEM_DOWNTIME_TASK)
        except (StaleElementReferenceException, NoSuchElementException):
            element = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(TaskSectionLocators.SYSTEM_DOWNTIME_TASK))
            self.double_click(element)

        if not self.__is_task_closed_already():
            self.click(CommonTaskDateLocators.DATE_SECTOR_IN_TASK)
            self.__common_closing_activity(actual_start_time, actual_end_time)
        else:
            print("WARN: System Downtime Duration Task is closed already !")
            self.__back_to_change_task_page()
            time.sleep(2)

    def __common_closing_activity(self, start_time: str, end_time: str) -> NoReturn:
        """ Perform the common closing activity in the 3 task """
        self.write(CloseChangeLocators.CLOSE_START_DATE, start_time)
        if self.get_change_type():
            self.write(CloseChangeLocators.CLOSE_END_DATE, end_time)
        else:
            self.write(CloseChangeLocators.CLOSE_END_DATE, start_time)
        self.click(CloseChangeLocators.CLOSE_MENU_SELECT)
        self.hover_over(CloseChangeLocators.SELECT_CLOSE_FROM_LST)
        self.click(CloseChangeLocators.SELECT_CLOSE_FROM_LST)
        time.sleep(1)
        self.click(CommonTaskDateLocators.SAVE_TASK_BTN)
        try:
            self.__back_to_change_task_page()
            time.sleep(2)
        except ElementClickInterceptedException:
            self.check_for_expected_frame(FrameBoxLocators.FRAME_OF_CONFIRMATION, FrameBoxLocators.FRAME_OK_BUTTON)
            self.__back_to_change_task_page()
            time.sleep(2)

    def goto_next_stage(self) -> NoReturn:
        """ Take the Change Request to Next Stage after closing all 3 tasks """
        if not self.is_change_status_closed():
            self.click(CloseChangeLocators.NEXT_STAGE_BUTTON)
            self.check_for_expected_frame(FrameBoxLocators.FRAME_OF_CONFIRMATION, FrameBoxLocators.FRAME_OK_BUTTON)
        else:
            print("WARN: Change Status  Was Closed already!")

    def goto_task_page(self) -> NoReturn:
        """ Goto the task section on the close change page """
        self.click(TaskSectionLocators.TASK_PAGE)

    def is_status_scheduled_for_approval(self):
        """ Check if the current status for CR is Scheduled for approval """
        status = self.get_value_of_element(CloseChangeLocators.CURRENT_CR_STATUS)
        if status == "Scheduled For Approval":
            return True
        else:
            return False
