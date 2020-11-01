"""
This module is to help with parsing the required information for a Link Budget
developer : jiaul_islam
"""
from utilities.static_data import LDMAData
from utilities.ldmalocators import LDMALoginLocators, LDMALogoutLocators, LinkBudgetActivityLocator
from pages.base import BasePage

class ParseLinkBudget(BasePage):
    """ Login to the LDMA """

    def __init__(self, driver):
        super().__init__(driver)
        self.username = LDMAData.LDMA_USERNAME
        self.password = LDMAData.LDMA_PASSWORD

    def login_ldma(self):
        """ Log in to the LDMA """
        self.write(LDMALoginLocators.USERNAME_INPUT, self.username)
        self.write(LDMALoginLocators.PASSWORD_INPUT, self.password)
        self.click(LDMALoginLocators.SIGNIN_BTN)

    def logout_ldma(self):
        """ Logout from LDMA """
        self.click(LDMALogoutLocators.LOGOUT_BTN)

    def goto_links(self):

        self.click(LinkBudgetActivityLocator.GOTO_LINK_DROPDOWN)
        self.click(LinkBudgetActivityLocator.GOTO_LINKS_DROPDOWN)
        
    def insert_link_code(self, link_code):

        self.write(LinkBudgetActivityLocator.INSERT_LINKCODE_TEXTBOX, link_code)

    def click_search(self):

        self.click(LinkBudgetActivityLocator.SEARCH_BTN)

    def select_all_dropdown(self):

        self.click(LinkBudgetActivityLocator.CLICK_ID_STATUSTYPE_DROPDOWN)
        self.click(LinkBudgetActivityLocator.SELECT_ALL_DROPDOWN)

    def select_found_link_code(self, link_id):

        element = LinkBudgetActivityLocator.select_found_linkid(link_id)
        self.click(element)

