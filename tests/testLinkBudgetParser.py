from selenium.common.exceptions import TimeoutException

from pages.ldma import ParseLinkBudget
from pages.base import BasePage
from utilites.terminal_colors import Colors
from rich.traceback import install
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.live import Live
from rich import print


# RICH Implementation for providing beautiful CLI visuals
install() #  Traceback install
table = Table(title="Parser Status", show_lines=True)
table.add_column("ROW ID", style="cyan", no_wrap=True, justify="center")
table.add_column("LINK ID/SIDE CODE", style="green", justify="center")
table.add_column("STATUS", justify="center", style="green")

panel = Panel(Align.center(table, vertical="middle"), border_style="none")


class LDMA_Parser(BasePage):
    """ LinkBudget Parser """
    def __init__(self, driver):
        super().__init__(driver)

    def parse_link_budget(self, _link_codes: list[str], _site_codes: list[str]):
        """ Parse the Link Budget """
        if _link_codes is not None:
            parse_info = ParseLinkBudget(driver=self.driver, timeout=3)
            parse_info.login_ldma()
            parse_info.make_dir()
            with Live(panel, refresh_per_second=4):
                try:
                    for _index, _link_code in enumerate(_link_codes):
                        parse_info.goto_links()
                        parse_info.insert_link_code(_link_code)
                        parse_info.select_all_dropdown()
                        parse_info.click_search()
                        try:
                            parse_info.select_found_link_code(_link_code)
                            table.add_row(f"{(_index+1)}", f"{_link_code}", "✅")
                        except TimeoutException:
                            table.add_row(f"{(_index+1)}", f"{_link_code}", "❌")
                            continue
                    # parse_info.export_pdf_file(id) # Export As PDF
                    parse_info.export_file(_link_code)  # Export As HTML
                    # parse_info.export_word_file(id) # Export As DOC
                    # parse_info.delete_html_file(id) # Delete the Exported HTML file
                    parse_info.logout_ldma()
                    self.driver.quit()
                except Exception as error:
                    print(error)
        else:
            parse_info = ParseLinkBudget(driver=self.driver, timeout=3)
            parse_info.login_ldma()
            parse_info.make_dir()

            for _site_code in _site_codes:
                parse_info.goto_links()
                parse_info.select_all_dropdown()
                parse_info.insert_site_code_1(_site_code)
                parse_info.click_search()
                if parse_info.is_available_site_1():
                    LINK_ID = parse_info.get_link_id()
                    parse_info.search_lb_with_sitecode(_site_code)
                    parse_info.export_file(LINK_ID)
                    continue
                parse_info.clear_site_code_1()
                parse_info.insert_site_code_2(_site_code)
                parse_info.click_search()
                if parse_info.is_available_site_2():
                    LINK_ID = parse_info.get_link_id()
                    parse_info.search_lb_with_sitecode(_site_code)
                    parse_info.export_file(LINK_ID)
                    continue
                else:
                    print(f"{Colors.FAIL}{_site_code} : Link Budget not closed.{Colors.ENDC}")
            parse_info.logout_ldma()
            self.driver.quit()
