import datetime
import sys

import openpyxl
from .terminal_colors import bcolors

"""
This class is for exporting the all the important information
that is required to keep track of the change request for who 
the change request is belong to.

written by: jiaul_islam
"""


class Data_Export:
    def __init__(self, file_path):
        try:
            self.is_used(file_path)
            self._change_list_excel = openpyxl.load_workbook(filename=file_path)
            self._sheet = self._change_list_excel.active
        except FileNotFoundError as error:
            print(error)
            sys.exit()

    def change_sheet(self, sheet_name):
        try:
            self._sheet = self._change_list_excel.get_sheet_by_name(sheet_name)
        except Exception as error:
            print(error)

    def insert_date(self, index: int, date: str):
        """ insert the date of the Change requesting """
        date_to_insert = datetime.datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S')
        my_date = str(date_to_insert.strftime("%d-%b-%y"))
        self._sheet['B' + str(index)] = my_date

    def insert_project_coordinator(self, index: int, name: str):
        """ insert the project coordinator name in the excel """
        self._sheet['C' + str(index)] = name

    def insert_project_name(self, index: int, project_name: str):
        """ insert the project name in the excel """
        self._sheet['D' + str(index)] = project_name

    def insert_change_activity(self, index: int, activity: str):
        """ insert the change activity in the excel """
        self._sheet['E' + str(index)] = activity

    def insert_impact_site_list(self, index: int, impact_site_list: str):
        """ insert the impact site list in the excel """
        ctr = 0
        sites = impact_site_list.split(',')
        site_list = ""
        for site in sites:
            site.strip()
            site_list += site
            if ctr != len(sites) - 1:
                site_list += ','
                ctr += 1
        self._sheet['F' + str(index)] = site_list

    def insert_service_type(self, index: int, service_type: str):
        """ insert the service type of the change request in the excel file"""
        self._sheet['G' + str(index)] = service_type

    def insert_downtime_duration(self, index: int, duration: str):
        """ insert the downtime duration limit in the excel file """
        self._sheet['H' + str(index)] = duration

    def insert_commercial_zone(self, index: int, commercial_zone: str):
        """ insert the commercial zone in the excel file """
        self._sheet['I' + str(index)] = commercial_zone

    def insert_change_number(self, index: int, change_number: str):
        """ insert the change number in the excel file for respective Change request """
        self._sheet['J' + str(index)] = change_number

    def insert_change_manager(self, index: int, change_manager: str):
        """ insert the change manager in the excel file """
        self._sheet['K' + str(index)] = change_manager

    def save_workbook(self, file_path):
        """ Save the workbook """
        self._change_list_excel.save(file_path)

    def close_workbook(self):
        """ Close the workbook """
        self._change_list_excel.close()

    @staticmethod
    def is_used(my_file: str):
        """ Checks if the user is already kept opened the excel file trying to write """
        while True:
            try:
                my_file = open(my_file, 'a+')
                my_file.close()
                break
            except IOError:
                input(f"{bcolors.FAIL}File Already in used ! "
                      f"Please close the file. Press Enter to retry...{bcolors.ENDC}")
