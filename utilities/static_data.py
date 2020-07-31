import os

'''
This page is all about static data that won't be changed through the Tests. 
All the time this data should be static as-is like here
'''


class StaticData(object):
    BASE_URL = 'http://itsm-web.robi.com.bd:8080/arsys/shared/login.jsp?/arsys/home'
    USERNAME = os.environ.get("BMC_USER")  # Get the username
    PASSWORD = os.environ.get("BMC_PASS")  # Get the password
    IT_HOME = 'IT Home'
    READ_EXCEL_FILE = 'E:/AutoBotBMCRemedy/data_driver/Change_Requirement.xlsx'
    WRITE_EXCEL_FILE = 'E:/AutoBotBMCRemedy/data_driver/Change_Request_List.xlsx'
    CANCEL_CHANGE_TXT_FILE_PATH = 'E:/AutoBotBMCRemedy/data_driver/cancel.txt'
    CLOSE_CHANGE_TXT_FILE_PATH = 'E:/AutoBotBMCRemedy/data_driver/change.txt'
