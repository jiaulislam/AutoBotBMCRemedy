from alive_progress import alive_bar
from selenium.common.exceptions import TimeoutException

from Pages.ldma import ParseLinkBudget
from Pages.base import BasePage
from Utilites.terminal_colors import bcolors


class LDMA_Parser(BasePage):
    """ LinkBudget Parser """
    def __init__(self, driver):
        super().__init__(driver)

    def parse_link_budget(self, link_ids: list, site_ids: list):
        """ Parse the Link Budget """
        if link_ids is not None:
            parse_info = ParseLinkBudget(driver=self.driver, timeout=3)
            parse_info.login_ldma()
            parse_info.make_dir()
            with alive_bar(len(link_ids)) as bar:
                try:
                    for ID in link_ids:
                        parse_info.goto_links()
                        parse_info.insert_link_code(ID)
                        parse_info.select_all_dropdown()
                        parse_info.click_search()
                        try:
                            parse_info.select_found_link_code(ID)
                            bar()
                        except TimeoutException:
                            print(f"{bcolors.WARNING}Invalid Link ID --> {ID}{bcolors.WARNING}")
                            bar()
                            continue
                        # parse_info.export_pdf_file(id) # Export As PDF
                        parse_info.export_file(ID)  # Export As HTML
                        # parse_info.export_word_file(id) # Export As DOC
                        # parse_info.delete_html_file(id) # Delete the Exported HTML file
                    parse_info.logout_ldma()
                    self.driver.quit()
                except Exception as e:
                    print(e)
        else:
            parse_info = ParseLinkBudget(driver=self.driver, timeout=3)
            parse_info.login_ldma()
            parse_info.make_dir()

            with alive_bar(len(site_ids)) as bar:
                for site in site_ids:
                    parse_info.goto_links()
                    parse_info.select_all_dropdown()
                    parse_info.insert_site_code_1(site)
                    parse_info.click_search()
                    if parse_info.is_available_site_1():
                        LINK_ID = parse_info.get_link_id()
                        parse_info.search_lb_with_sitecode(site)
                        parse_info.export_file(LINK_ID)
                        bar()
                        continue
                    parse_info.clear_site_code_1()
                    parse_info.insert_site_code_2(site)
                    parse_info.click_search()
                    if parse_info.is_available_site_2():
                        LINK_ID = parse_info.get_link_id()
                        parse_info.search_lb_with_sitecode(site)
                        parse_info.export_file(LINK_ID)
                        bar()
                        continue
                    else:
                        print(f"{bcolors.FAIL}{site} : Link Budget not closed.{bcolors.ENDC}")
                        bar()
                parse_info.logout_ldma()
                self.driver.quit()
