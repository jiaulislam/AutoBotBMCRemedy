"""
This module is to help with parsing the required information for a Link Budget
developer : jiaul_islam
"""
import os
import shutil
from typing import Union

import pdfkit
import win32com.client as win32
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
    TimeoutException
)
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base import BasePage
from utilites.ldmalocators import (
    LDMALoginLocators,
    LDMALogoutLocators,
    LinkBudgetActivityLocator
)
from utilites.static_data import LDMAData


class ParseLinkBudget(BasePage):
    """ Login to the LDMA """

    def __init__(self, driver: WebDriver, timeout: int) -> None:
        super().__init__(driver=driver, timeout=timeout)
        self.username = LDMAData.LDMA_USERNAME
        self.password = LDMAData.LDMA_PASSWORD
        self.SITE_A = None
        self.SITE_B = None

    def login_ldma(self) -> None:
        """ Log in to the LDMA """
        self.write(LDMALoginLocators.USERNAME_INPUT, self.username)
        self.write(LDMALoginLocators.PASSWORD_INPUT, self.password)
        self.click(LDMALoginLocators.SIGNIN_BTN)

    def logout_ldma(self) -> None:
        """ Logout from LDMA """
        self.click(LDMALogoutLocators.LOGOUT_BTN)

    def goto_links(self) -> None:
        """ Goto action Link -> Links """
        self.click(LinkBudgetActivityLocator.GOTO_LINK_DROPDOWN)
        self.click(LinkBudgetActivityLocator.GOTO_LINKS_DROPDOWN)

    def insert_link_code(self, LINK_ID: str) -> None:
        """ Insert the Link Code in Text Box """
        self.write(LinkBudgetActivityLocator.INSERT_LINKCODE_TEXTBOX, LINK_ID)

    def click_search(self) -> None:
        """ Click The search button """
        self.click(LinkBudgetActivityLocator.SEARCH_BTN)

    def select_all_dropdown(self) -> None:
        """ 'Select All' from dropdown """
        self.click(LinkBudgetActivityLocator.CLICK_ID_STATUSTYPE_DROPDOWN)
        self.click(LinkBudgetActivityLocator.SELECT_ALL_DROPDOWN)

    def select_found_link_code(self, LINK_ID: str) -> None:
        """ Select the Found Link ID from table """
        element = LinkBudgetActivityLocator.select_found_linkid(LINK_ID)
        self.click(element)

    def __parse_element_innerHTML(self) -> str:
        """ Select all the block of required HTML in LB information """
        element = self.find_element(*LinkBudgetActivityLocator.BLOCK_INFORMATION)

        return element.get_attribute("innerHTML")

    # TODO : Need to fix the bug 
    @staticmethod
    def make_dir() -> None:
        """ Make a directory for LB Output """
        if os.path.exists(os.getcwd() + '/LinkBudgetDumps'):
            shutil.rmtree('LinkBudgetDumps')
            os.mkdir('LinkBudgetDumps')
            os.chdir(os.getcwd() + "/LinkBudgetDumps")
        else:
            os.mkdir('LinkBudgetDumps')
            os.chdir(os.getcwd() + "/LinkBudgetDumps")

    def __set_site_A(self) -> None:
        """ Set the Site-A Code """
        try:
            SITE_A = self.find_element(*LinkBudgetActivityLocator.SITE_ID_1)
            self.SITE_A = SITE_A.get_attribute("value")
        except AttributeError:
            pass

    def __set_site_B(self) -> None:
        """ Set the Site-B Code """
        try:
            SITE_B = self.find_element(*LinkBudgetActivityLocator.SITE_ID_2)
            self.SITE_B = SITE_B.get_attribute("value")
        except AttributeError:
            pass

    def set_filename(self, LINK_ID: str) -> str:
        """ Set the File Name Formatting """
        self.__set_site_A()
        self.__set_site_B()

        return f"{LINK_ID}__{self.SITE_A}-{self.SITE_B}"

    def export_file(self, LINK_ID: str) -> None:
        """ Export the File as .HTML file """
        get_file = f"{self.set_filename(LINK_ID)}.html"
        with open(get_file, 'w+', encoding='utf-8') as writer:
            writer.write(self.__parse_element_innerHTML())

    def export_pdf_file(self, LINK_ID: str) -> None:
        """ Export the LB as PDF File """
        source_code = self.__parse_element_innerHTML()
        PDF_FILE = f"{self.set_filename(LINK_ID)}.pdf"
        pdfkit.from_string(source_code, PDF_FILE)

    def export_word_file(self, LINK_ID: str) -> None:
        """ Export the LB as Word File """
        word = win32.Dispatch('Word.Application')
        file_path = f"{os.getcwd()}/{self.set_filename(LINK_ID)}.html"
        doc = word.Documents.Add(file_path)
        output_fileName = f"{os.getcwd()}/{self.set_filename(LINK_ID)}.doc"
        doc.SaveAs(output_fileName, FileFormat=0)
        doc.Close()
        word.Quit()

    def delete_html_file(self, LINK_ID: str) -> None:
        """ Delete the HTML file """
        PATH_TO_DELETE = f"{os.getcwd()}/{self.set_filename(LINK_ID)}.html"
        os.remove(PATH_TO_DELETE)

    def search_lb_with_sitecode(self, SITE_ID: str) -> None:
        """ Search LB With Site ID """

        try:
            self.click(LinkBudgetActivityLocator.is_available_lb(SITE_ID))
        except NoSuchElementException as e:
            print(f"Error Found ! Error details: {e}")
            pass
        except ElementClickInterceptedException as e:
            print(f"Error Found ! Error details: {e}")
            pass
        except TimeoutException:
            pass

    def insert_site_code_1(self, SITE_ID: str) -> None:
        try:
            self.write(LinkBudgetActivityLocator.INSERT_SITE_CODE_1, SITE_ID)
        except ElementClickInterceptedException as e:
            print(f"Error Found ! Error details: {e}")
        except NoSuchElementException as e:
            print(f"Error Found ! Error details: {e}")
        except Exception as e:
            print(f"Error Found ! Error details: {e}")

    def insert_site_code_2(self, SITE_ID: str) -> None:
        try:
            self.write(LinkBudgetActivityLocator.INSERT_SITE_CODE_2, SITE_ID)
        except ElementClickInterceptedException as e:
            print(f"Error Found ! Error details: {e}")
        except NoSuchElementException as e:
            print(f"Error Found ! Error details: {e}")
        except Exception as e:
            print(f"Error Found ! Error details: {e}")

    def clear_site_code_1(self) -> None:

        try:
            element = self.find_element(*LinkBudgetActivityLocator.INSERT_SITE_CODE_1)
            element.clear()
        except NoSuchElementException as e:
            print(f"Error Found ! Error details: {e}")
        except ElementClickInterceptedException as e:
            print(f"Error Found ! Error details: {e}")

    def clear_site_code_2(self) -> None:

        try:
            element = self.find_element(*LinkBudgetActivityLocator.INSERT_SITE_CODE_2)
            element.clear()
        except NoSuchElementException as e:
            print(f"Error Found ! Error details: {e}")
        except ElementClickInterceptedException as e:
            print(f"Error Found ! Error details: {e}")

    def get_link_id(self) -> Union[str, None]:

        try:
            elements = self.find_elements(*LinkBudgetActivityLocator.SEARCH_RESULT)
            if elements is not None:
                return elements[-1].text
            return None
        except NoSuchElementException:
            pass

    def is_available_site_1(self) -> bool:

        try:
            return self.is_visible(LinkBudgetActivityLocator.SEARCH_1)
        except NoSuchElementException as e:
            print(f"Not Found in Site 1:  {e}")
        except TimeoutException as e:
            print(f"Error Found in Site 1: {e}")
            pass

    def is_available_site_2(self) -> bool:

        try:
            return self.is_visible(LinkBudgetActivityLocator.SEARCH_2)
        except NoSuchElementException as e:
            print(f"Not Found in Site 2:  {e}")
        except TimeoutException as e:
            print(f"Error Found in Site 2: {e}")
            pass
