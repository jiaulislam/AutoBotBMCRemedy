"""
This module is to help with parsing the required information for a Link Budget
developer : jiaul_islam
"""
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
    TimeoutException
)

from Utilites.ldmalocators import (
    LDMALoginLocators,
    LDMALogoutLocators,
    LinkBudgetActivityLocator
)
from Utilites.terminal_colors import bcolors
from Utilites.static_data import LDMAData
from Pages.base import BasePage
import win32com.client
import shutil
import pdfkit
import os


class ParseLinkBudget(BasePage):
    """ Login to the LDMA """
    def __init__(self, driver):
        super().__init__(driver)
        self.username = LDMAData.LDMA_USERNAME
        self.password = LDMAData.LDMA_PASSWORD
        self.SITE_A = None
        self.SITE_B = None

    def login_ldma(self):
        """ Log in to the LDMA """
        self.write(LDMALoginLocators.USERNAME_INPUT, self.username)
        self.write(LDMALoginLocators.PASSWORD_INPUT, self.password)
        self.click(LDMALoginLocators.SIGNIN_BTN)

    def logout_ldma(self):
        """ Logout from LDMA """
        self.click(LDMALogoutLocators.LOGOUT_BTN)

    def goto_links(self):
        """ Goto action Link -> Links """
        self.click(LinkBudgetActivityLocator.GOTO_LINK_DROPDOWN)
        self.click(LinkBudgetActivityLocator.GOTO_LINKS_DROPDOWN)

    def insert_link_code(self, LINK_ID):
        """ Insert the Link Code in Text Box """
        self.write(LinkBudgetActivityLocator.INSERT_LINKCODE_TEXTBOX, LINK_ID)

    def click_search(self):
        """ Click The search button """
        self.click(LinkBudgetActivityLocator.SEARCH_BTN)

    def select_all_dropdown(self):
        """ 'Select All' from dropdown """
        self.click(LinkBudgetActivityLocator.CLICK_ID_STATUSTYPE_DROPDOWN)
        self.click(LinkBudgetActivityLocator.SELECT_ALL_DROPDOWN)

    def select_found_link_code(self, LINK_ID):
        """ Select the Found Link ID from table """
        element = LinkBudgetActivityLocator.select_found_linkid(LINK_ID)
        self.click(element)

    def __parse_element_innerHTML(self):
        """ Select all the block of required HTML in LB information """
        element = self.find_element(*LinkBudgetActivityLocator.BLOCK_INFORMATION)

        return element.get_attribute("innerHTML")

    @staticmethod
    def make_dir():
        """ Make a directory for LB Output """
        if os.path.exists(os.getcwd() + '/LinkBudget'):
            shutil.rmtree('LinkBudget')
            os.mkdir('LinkBudget')
            os.chdir(os.getcwd()+"/LinkBudget")
        else:
            os.mkdir('LinkBudget')
            os.chdir(os.getcwd()+"/LinkBudget")

    def __set_site_A(self):
        """ Set the Site-A Code """
        SITE_A = self.find_element(*LinkBudgetActivityLocator.SITE_ID_1)
        self.SITE_A = SITE_A.get_attribute("value")

    def __set_site_B(self):
        """ Set the Site-B Code """
        SITE_B = self.find_element(*LinkBudgetActivityLocator.SITE_ID_2)
        self.SITE_B = SITE_B.get_attribute("value")

    def set_filename(self, LINK_ID):
        """ Set the File Name Formatting """
        self.__set_site_A()
        self.__set_site_B()

        return f"{LINK_ID}__{self.SITE_A}-{self.SITE_B}"

    def export_file(self, LINK_ID):
        """ Export the File as .HTML file """
        get_file = f"{self.set_filename(LINK_ID)}.html"
        with open(get_file, 'w+', encoding='utf-8') as writer:
            writer.write(self.__parse_element_innerHTML())

    def export_pdf_file(self, LINK_ID):
        """ Export the LB as PDF File """
        source_code = self.__parse_element_innerHTML()
        PDF_FILE = f"{self.set_filename(LINK_ID)}.pdf"
        print(f"{bcolors.OKCYAN}Working --> {PDF_FILE}.{bcolors.ENDC}")
        pdfkit.from_string(source_code, PDF_FILE)

    def export_word_file(self, LINK_ID):
        """ Export the LB as Word File """
        word = win32com.client.Dispatch('Word.Application')
        file_path = f"{os.getcwd()}/{self.set_filename(LINK_ID)}.html"
        doc = word.Documents.Add(file_path)
        output_fileName = f"{os.getcwd()}/{self.set_filename(LINK_ID)}.doc"
        doc.SaveAs(output_fileName, FileFormat=0)
        doc.Close()
        print(f"{bcolors.OKGREEN}File Created: {self.set_filename(LINK_ID)}.doc{bcolors.ENDC}")
        word.Quit()

    def delete_html_file(self, LINK_ID):
        """ Delete the HTML file """
        PATH_TO_DELETE = f"{os.getcwd()}/{self.set_filename(LINK_ID)}.html"
        os.remove(PATH_TO_DELETE)

    def search_lb_with_sitecode(self, SITE_ID):
        """ Search LB With Site ID """

        try:
            self.click(LinkBudgetActivityLocator.is_available_lb(SITE_ID))
        except NoSuchElementException as e:
            print(f"Error Found ! Error details: {e}")
            pass
        except ElementClickInterceptedException as e:
            print(f"Error Found ! Error details: {e}")
            pass

    def insert_site_code_1(self, SITE_ID):
        try:
            self.write(LinkBudgetActivityLocator.INSERT_SITE_CODE_1, SITE_ID)
        except ElementClickInterceptedException as e:
            print(f"Error Found ! Error details: {e}")
        except NoSuchElementException as e:
            print(f"Error Found ! Error details: {e}")
        except Exception as e:
            print(f"Error Found ! Error details: {e}")

    def insert_site_code_2(self, SITE_ID):
        try:
            self.write(LinkBudgetActivityLocator.INSERT_SITE_CODE_2, SITE_ID)
        except ElementClickInterceptedException as e:
            print(f"Error Found ! Error details: {e}")
        except NoSuchElementException as e:
            print(f"Error Found ! Error details: {e}")
        except Exception as e:
            print(f"Error Found ! Error details: {e}")

    def clear_site_code_1(self):

        try:
            element = self.find_element(*LinkBudgetActivityLocator.INSERT_SITE_CODE_1)
            element.clear()
        except NoSuchElementException as e:
            print(f"Error Found ! Error details: {e}")
        except ElementClickInterceptedException as e:
            print(f"Error Found ! Error details: {e}")

    def clear_site_code_2(self):

        try:
            element = self.find_element(*LinkBudgetActivityLocator.INSERT_SITE_CODE_2)
            element.clear()
        except NoSuchElementException as e:
            print(f"Error Found ! Error details: {e}")
        except ElementClickInterceptedException as e:
            print(f"Error Found ! Error details: {e}")

    def get_link_id(self):

        try:
            elements = self.find_elements(*LinkBudgetActivityLocator.SEARCH_RESULT)
            return elements[-1].text
        except NoSuchElementException:
            pass

    def is_lb_found(self):

        try:
            return self.is_visible(LinkBudgetActivityLocator.SEARCH_RESULT)
        except NoSuchElementException as e:
            print(f"Not Found in Site 1:  {e}")
        except TimeoutException as e:
            print(f"Error Found in Site 1: {e}")
            pass
