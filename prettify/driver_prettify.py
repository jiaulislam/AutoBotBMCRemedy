from rich.table import Table
from rich.layout import Layout
from rich import box, print
from rich.prompt import Prompt
from rich.panel import Panel
from .prettify_ldma import Header, make_sponsor_message

class MenuLayout:

    def __init__(self):
        self._layout = Layout()
        self._table = Table(title="AUTOBOT MENU", expand=True, 
                            show_lines=True, box=box.SQUARE_DOUBLE_HEAD,
                            title_style="#0000ff italic")

    def __rich__(self):
        self._layout.split(
            Layout(name="head", size=3),
            Layout(name="body", ratio=1),
        )

        self._layout["body"].split_column(
            Layout(name="mid_section", ratio=2),
            Layout(name="table", ratio=3)
        )

        # Tables
        self._table.add_column("Action Button", justify="center", header_style="#3be13b", no_wrap=True, style="#3be13b")
        self._table.add_column("Action Description", justify="center", header_style="bold cyan", no_wrap=True, style="cyan")

        self._table.add_row("1", "CREATE NCR 🧩")
        self._table.add_row("2", "CLOSE NCR  🎯")
        self._table.add_row("3", "CANCEL NCR  🧨")
        self._table.add_row("4", "LDMA PARSER  📆")
        self._table.add_row("0", "EXIT AUTOBOT  ⚔")

        self._layout["head"].update(Header("WELCOME TO AUTOBOT"))
        self._layout["mid_section"].update(make_sponsor_message())
        self._layout["table"].update(self._table)
        return self._layout

def get_menu_choice() -> int:
    choice = Prompt.ask("Enter choice", choices=["1","2","3","4","0"])
    return int(choice)
