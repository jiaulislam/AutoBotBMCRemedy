"""
All the locator's of the LDMA page
developer : jiaul_islam
"""
from typing import Tuple

from selenium.webdriver.common.by import By


class LDMALoginLocators(object):
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SIGNIN_BTN = (By.XPATH, "//input[@name='submit']")


class LDMALogoutLocators(object):
    LOGOUT_BTN = (By.XPATH, "//a[contains(text(), 'Logout')]")


class LinkBudgetActivityLocator(object):
    GOTO_LINK_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Link')]")
    GOTO_LINKS_DROPDOWN = (
        By.XPATH, "//a[@href='http://ldma.robi.com.bd/view/link/linksearch.php']")
    INSERT_LINKCODE_TEXTBOX = (By.XPATH, "//input[@id='search']")
    CLICK_ID_STATUSTYPE_DROPDOWN = (By.XPATH, "//select[@id='statusType']")
    SELECT_ALL_DROPDOWN = (By.XPATH, "//select[@id='statusType']//option[contains(text(),'Select All')]")
    SEARCH_BTN = (By.XPATH, "//input[@name='submit']")
    INSERT_SITE_CODE_1 = (By.XPATH, "//input[@id='siteCode']")
    INSERT_SITE_CODE_2 = (By.XPATH, "//input[@id='siteCode2']")

    @staticmethod
    def select_found_linkid(linkid: str) -> Tuple[By, str]:
        """ Return the Custom dynamic XPATH with Link ID """
        XPATH_FOR_LINKID = f"//div[@class='table-responsive']//td//a[contains(text(), '{linkid}')]"
        return By.XPATH, XPATH_FOR_LINKID

    @staticmethod
    def is_available_lb(site_code: str) -> Tuple[By, str]:
        return By.XPATH, f"//a[contains(text(), '{site_code}')]"

    BLOCK_INFORMATION = (By.XPATH, "//*[@id='linkadd']")
    SITE_ID_1 = (By.XPATH, "//input[@id='siteID1']")
    SITE_ID_2 = (By.XPATH, "//input[@id='siteID2']")

    SEARCH_RESULT = (By.XPATH, "//*[@id='search_result']/div/table/tbody/tr[3]/td[1]")
    SEARCH_2 = (By.XPATH, "//*[@id='search_result']/div/table/tbody/tr[3]/td[8]")
    SEARCH_1 = (By.XPATH, "//*[@id='search_result']/div/table/tbody/tr[3]/td[6]")
