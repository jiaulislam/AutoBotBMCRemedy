import re
import sys
from typing import List
from datetime import datetime

from openpyxl import load_workbook
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from rich import print
from rich.prompt import Confirm

"""
This class is for exporting the all the important information
that is required to keep track of the change request for who 
the change request is belong to.

written by: jiaul_islam
"""


class Data_Export:
    def __init__(self, file_path: str) -> None:
        try:
            self._is_used(file_path)
            self._change_list_excel: Workbook = load_workbook(filename=file_path)
            self._sheet: Worksheet = self._change_list_excel.active
        except FileNotFoundError as error:
            print(error)
            sys.exit()

    def change_sheet(self, sheet_name: str) -> None:
        try:
            self._sheet = self._change_list_excel[sheet_name]
        except Exception as error:
            raise error

    def insert_date(self, index: int, date: str) -> None:
        """ insert the date of the Change requesting """
        date_to_insert = datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S')
        my_date = str(date_to_insert.strftime("%d-%b-%y"))
        self._sheet['B' + str(index)] = my_date

    def insert_project_coordinator(self, index: int, name: str) -> None:
        """ insert the project coordinator name in the excel """
        self._sheet['C' + str(index)] = name

    def insert_project_name(self, index: int, project_name: str) -> None:
        """ insert the project name in the excel """
        self._sheet['D' + str(index)] = project_name

    def insert_change_activity(self, index: int, activity: str) -> None:
        """ insert the change activity in the excel """
        self._sheet['E' + str(index)] = activity

    def insert_impact_site_list(self, index: int, impact_site_list: str) -> None:
        """ insert the impact site list in the excel """
        _PATTERN = r'([A-Z]{5}(?:(?:[A-Z0-9][0-9])|(?:[0-9][A-Z0-9])))'
        sites: List[str] = re.findall(_PATTERN, impact_site_list)

        self._sheet['F' + str(index)] = ",".join(sites)

    def insert_service_type(self, index: int, service_type: str) -> None:
        """ insert the service type of the change request in the excel file"""
        self._sheet['G' + str(index)] = service_type

    def insert_downtime_duration(self, index: int, duration: str) -> None:
        """ insert the downtime duration limit in the excel file """
        self._sheet['H' + str(index)] = duration

    def insert_commercial_zone(self, index: int, commercial_zone: str) -> None:
        """ insert the commercial zone in the excel file """
        self._sheet['I' + str(index)] = commercial_zone

    def insert_change_number(self, index: int, change_number: str) -> None:
        """ insert the change number in the excel file for respective Change request """
        self._sheet['J' + str(index)] = change_number

    def insert_change_manager(self, index: int, change_manager: str) -> None:
        """ insert the change manager in the excel file """
        self._sheet['K' + str(index)] = change_manager

    def save_workbook(self, file_path: str) -> None:
        """ Save the workbook """
        self._change_list_excel.save(file_path)

    def close_workbook(self) -> None:
        """ Close the workbook """
        self._change_list_excel.close()

    @staticmethod
    def _is_used(my_file: str) -> None:
        """ Checks if the user is already kept opened the excel file trying to write """
        while True:
            try:
                with open(my_file, "a+"):
                    break
            except IOError:
                if Confirm.ask("File Closed ?", default="(y)", show_default=True):
                    pass
