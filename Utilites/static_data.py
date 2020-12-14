import os

'''
This page is all about static data that won't be changed through the Tests. 
All the time this data should be static as-is like here

written by: jiaul_islam
'''


class StaticData(object):
    BMC_URL = 'http://itsm-web.robi.com.bd:8080/arsys/shared/login.jsp?/arsys/home'
    USERNAME = os.environ.get("BMC_USER")  # Get the username
    PASSWORD = os.environ.get("BMC_PASS")  # Get the password
    IT_HOME = 'IT Home'
    READ_EXCEL_FILE = 'E:/Python Projects/AutoBotBMCRemedy/data_driver/Request_CR.xlsx'
    WRITE_EXCEL_FILE = 'E:/Python Projects/AutoBotBMCRemedy/data_driver/Output_CR.xlsx'
    CANCEL_CHANGE_TXT_FILE_PATH = 'E:/Python Projects/AutoBotBMCRemedy/data_driver/cancel.txt'
    CLOSE_CHANGE_TXT_FILE_PATH = 'E:/Python Projects/AutoBotBMCRemedy/data_driver/change.txt'
    VIEW_ATTACHMENT_DEFAULT_STATE = 'View Attachment Disabled'


class LDMAData(object):
    LDMA_URL = 'http://ldma.robi.com.bd/view/common/login.php'
    LDMA_USERNAME = os.environ.get("LDMA_USER")
    LDMA_PASSWORD = os.environ.get("LDMA_PASS")


class ROCData(object):
    ROC_URL = 'https://roc.robi.com.bd/ROC/ROCPages/Pages/ROBIROC_Login.aspx'
    ROC_USERNAME = os.environ.get("ROC_USER")
    ROC_PASSWORD = os.environ.get("ROC_PASS")