import time
from typing import Union

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    TimeoutException
)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base import BasePage
from utilites.make_data import make_downtime_from_open_time_2
from utilites.locators import (
    CloseChangeLocators as Close_Locators,
    CancelRequestLocators as Cancel_Locators,
    TaskSectionLocators as Task_Locators,
    DateSectionSelector as Date_Locators,
    CommonTaskDateLocators as Common_Locators,
    FrameBoxLocators as Frame_Locators
)

"""
This class will help us to close the Change Request as per user requirement.
it will inherit the base page class for the basic functionality.

written by: jiaul_islam
"""


class CloseRequests(BasePage):
    """ Close the Change Request in BMC Remedy """

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, timeout=10)
        self.__change_type: bool = False
        self.__change_number: str = ""
        self.__invalid_change_numbers: list = []

    def __set_change_number(self, change_number: str) -> None:
        """ Set the value of Change Number """
        self.__change_number = change_number

    def get_change_number(self) -> str:
        """ Get the Value of Change Number """
        return self.__change_number

    def __set_change_type(self) -> None:
        """ Set the Value of Change Type """
        self.__change_type = self.__is_service_effective()

    def get_change_type(self) -> bool:
        """ Get the Change Request type """
        return self.__change_type

    def get_actual_start_date(self) -> Union[str, None]:
        """ Get the Closing Change Request Date & Time """
        self.click(Date_Locators.DATE_PAGE)
        if self.get_text(Close_Locators.ACTUAL_OPEN_DATE) != "":
            return self.get_text(Close_Locators.ACTUAL_OPEN_DATE)
        else:
            return None

    @staticmethod
    def get_index_for_change_number(change_number: str, list_of_change_number: list) -> Union[int, None]:
        """ returns the correct position of the change number from the list """
        try:
            return list_of_change_number.index(change_number) + 2
        except ValueError:
            return None

    def add_change_to_invalid_list(self, change_number: str) -> None:
        """ append the invalid change_number found the the invalid list """
        self.__invalid_change_numbers.append(change_number)

    def find_the_change_request(self, change_number: str, index: int) -> None:
        """ Find the Change Request with respect to user shared number"""

        final_xpath = "//table[@id='T301444200']//tr[" + str(index) + "]//td[1]/nobr[1]/span"

        dynamicXPATH = Close_Locators.get_changeable_xpath(final_xpath)  # get the tuple

        try:
            self.double_click(dynamicXPATH)
            self.__set_change_number(change_number)  # set the change number for future use
        except NoSuchElementException as error:
            print(error)

    def get_invalid_change_numbers(self) -> None:
        """ Fetch all the invalid change numbers from the list """
        if len(self.__invalid_change_numbers):
            print("Below change request number not found:", end=" ")
            print(",".join(self.__invalid_change_numbers))

    def __is_task_closed_already(self) -> bool:
        """ Check if the task is already closed or not """
        time.sleep(1)
        if self.get_text(Close_Locators.TASK_INIT_STATUS) == "Closed":
            return True
        return False

    def is_change_status_closed(self) -> bool:
        """
        Check if the Change status is already closed or completed
        """
        status = self.get_text(Cancel_Locators.STATUS_AREA)

        if status == 'Closed' or status == 'Completed':
            return True
        return False

    def __is_service_effective(self) -> bool:
        """Check if the current working Change is service effective or not.
            :rtype: bool
        """
        try:
            if self.is_visible(Close_Locators.TASK_PLAN_START_DATE):
                if self.get_text(Close_Locators.TASK_PLAN_START_DATE) != self.get_text(
                        Close_Locators.TASK_PLAN_END_DATE):
                    return True
        except NoSuchElementException as error:
            print(error)

    def __back_to_change_task_page(self) -> None:
        """ Go back to the Change request control page """
        makeXPATH = f"//a[@class='btn'][contains(text(),'{self.__change_number}')]"
        dynamicXPATH = Close_Locators.get_changeable_xpath(makeXPATH)
        try:
            self.back_to_home_page(dynamicXPATH)
        except ElementClickInterceptedException:
            time.sleep(2)
            self.back_to_home_page(dynamicXPATH)
        time.sleep(2)

    def __common_closing_activity(self, start_time: str) -> None:
        """ Perform the common closing activity in the 3 task """
        self.write(Close_Locators.TASK_ACTUAL_START_DATE, start_time)
        if self.get_change_type():
            _start_date: str = self.get_text(Close_Locators.TASK_PLAN_START_DATE)
            _end_date: str = self.get_text(Close_Locators.TASK_PLAN_END_DATE)
            _actual_end_date: str = make_downtime_from_open_time_2(start_time, _start_date, _end_date)
            self.write(Close_Locators.TASK_ACTUAL_END_DATE, _actual_end_date)
        else:
            self.write(Close_Locators.TASK_ACTUAL_END_DATE, start_time)
        self.click(Close_Locators.CLOSE_MENU_SELECT)
        self.hover_over(Close_Locators.SELECT_CLOSE)
        self.click(Close_Locators.SELECT_CLOSE)
        time.sleep(1)
        self.click(Common_Locators.SAVE_TASK_BTN)
        try:
            self.__back_to_change_task_page()
            time.sleep(2)
        except ElementClickInterceptedException:
            self.handle_frame_alert(Frame_Locators.FRAME_OF_CONFIRMATION, Frame_Locators.FRAME_OK_BUTTON)
            self.__back_to_change_task_page()

    def close_service_downtime_duration_task(self, actual_start_time: str) -> None:
        """
        Close the Task for: Service_Downtime_Duration_Task(2) ,
        If CR Task Status is already closed then will go back to
        the task page.
        """
        self.double_click(Task_Locators.SERVICE_DOWNTIME_DURATION_TASK_SPAN)

        if not self.__is_task_closed_already():
            self.click(Common_Locators.DATE_SECTOR_IN_TASK)
            self.__set_change_type()
            self.__common_closing_activity(actual_start_time)
        else:
            self.__back_to_change_task_page()

    def close_service_downtime_window_task(self, actual_start_time: str, current_time_of_user: str) -> None:
        """
        Close the Task for: Service_Downtime_Window_Task(3) ,
        If CR Task Status is already closed then will go back to
        the task page.
        """
        try:
            if self.is_visible(Task_Locators.SERVICE_DOWNTIME_WINDOW_TASK_SPAN):
                self.double_click(Task_Locators.SERVICE_DOWNTIME_WINDOW_TASK_SPAN)
            else:
                try:
                    time.sleep(2)
                    self.double_click(Task_Locators.SERVICE_DOWNTIME_WINDOW_TASK_SPAN)
                except TimeoutException:
                    self.double_click(Task_Locators.SERVICE_DOWNTIME_WINDOW_TASK_SPAN)
        except (StaleElementReferenceException, NoSuchElementException):
            element = WebDriverWait(self._driver, self.timeout).until(
                ec.visibility_of_element_located(Task_Locators.SERVICE_DOWNTIME_WINDOW_TASK_SPAN))
            self.double_click(element)

        if not self.__is_task_closed_already():
            self.click(Common_Locators.DATE_SECTOR_IN_TASK)
            self.write(Close_Locators.TASK_ACTUAL_START_DATE, actual_start_time)
            self.write(Close_Locators.TASK_ACTUAL_END_DATE, current_time_of_user)
            self.click(Close_Locators.CLOSE_MENU_SELECT)
            self.hover_over(Close_Locators.SELECT_CLOSE)
            self.click(Close_Locators.SELECT_CLOSE)
            time.sleep(1)
            self.click(Common_Locators.SAVE_TASK_BTN)
            self.__back_to_change_task_page()
        else:
            self.__back_to_change_task_page()

    def close_system_downtime_duration_task(self, actual_start_time: str) -> None:
        """
            Close the Task for: System_Downtime_Task(4) ,
            If CR Task Status is already closed then will go back to
            the task page.
        """
        try:
            if self.is_visible(Task_Locators.SYSTEM_DOWNTIME_TASK):
                self.double_click(Task_Locators.SYSTEM_DOWNTIME_TASK)
            else:
                try:
                    time.sleep(2)
                    self.double_click(Task_Locators.SYSTEM_DOWNTIME_TASK)
                except TimeoutException:
                    time.sleep(2)
                    self.double_click(Task_Locators.SYSTEM_DOWNTIME_TASK)
        except (StaleElementReferenceException, NoSuchElementException):
            element = WebDriverWait(self._driver, self.timeout).until(
                ec.visibility_of_element_located(Task_Locators.SYSTEM_DOWNTIME_TASK))
            self.double_click(element)

        if not self.__is_task_closed_already():
            self.click(Common_Locators.DATE_SECTOR_IN_TASK)
            self.__common_closing_activity(actual_start_time)
        else:
            self.__back_to_change_task_page()

    def goto_next_stage(self) -> None:
        """ Take the Change Request to Next Stage after closing all 3 tasks """
        if not self.is_change_status_closed():
            self.click(Close_Locators.NEXT_STAGE_BUTTON)
            self.handle_frame_alert(Frame_Locators.FRAME_OF_CONFIRMATION, Frame_Locators.FRAME_OK_BUTTON)
        else:
            print("WARN: Change Status  Was Closed already!")

    def goto_task_page(self) -> None:
        """ Goto the task section on the close change page """
        self.click(Task_Locators.TASK_PAGE)

    def is_status_scheduled_for_approval(self):
        """ Check if the current status for CR is Scheduled for approval """
        status = self.get_text(Close_Locators.CURRENT_CR_STATUS)
        if status == "Scheduled For Approval":
            return True
        return False
