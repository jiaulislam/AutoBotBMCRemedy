"""
All the locator's of the LDMA page
developer : jiaul_islam
"""
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

    @staticmethod
    def select_found_linkid(linkid: str) -> tuple:
        """ Return the Custom dynamic XPATH with Link ID """
        XPATH_FOR_LINKID = f"//div[@class='table-responsive']//td//a[contains(text(), '{linkid}')]"
        return By.XPATH, XPATH_FOR_LINKID

    BLOCK_INFORMATION = (By.XPATH, "//*[@id='linkadd']")
    SITE_ID_1 = (By.XPATH, "//input[@id='siteID1']")
    SITE_ID_2 = (By.XPATH, "//input[@id='siteID2']")


class LinkAttributesLocator(object):

    # Site Name
    SITE1_NAME = (By.XPATH, "//input[@id = 'site1Name']")
    SITE2_NAME = (By.XPATH, "//input[@id='siteID2']")

    # Site ID 
    SITE1_NEID = (By.XPATH, "//input[@id='site1NeId']")
    SITE2_NEID = (By.XPATH, "//input[@id='site2NeId']")

    # Hop Nodal Base 
    HOP_NODAL_BASE = (By.XPATH, "//input[@id='PDH_SDH_Nodal']")

    # Extra Field Site // TDMA
    TDMA_STATUS = (By.XPATH, "//input[@id='extrafieldSite2']")

    # AMM Status 
    AMM_SITE1 = (By.XPATH, "//input[@id='ammTypeSite1']")
    AMM_SITE2 = (By.XPATH, "//input[@id='ammTypeSite2']")

    # IDU/ Magazine
    AMMTYPE_SITE1 = (By.XPATH, "//input[@id='nodalefield1']")
    AMMTYPE_SITE2 = (By.XPATH, "//input[@id='nodalefield2']")
