from rich.align import Align
from rich.layout import Layout
from rich.console import Console, RenderGroup
from rich import box
from rich.prompt import Prompt
from rich.table import Table
from datetime import datetime
from rich.panel import Panel
from rich.text import Text

console = Console()


class Header:
    """Display header with clock."""
    def __init__(self, header_text: str) -> None:
        self.header_text = header_text

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(f"\t\t\t{self.header_text}",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white")


def make_sponsor_message() -> Panel:
    """Some example content."""
    sponsor_message = Table.grid(padding=1)
    sponsor_message.add_column(style="green", justify="right")
    sponsor_message.add_column(no_wrap=True)
    sponsor_message.add_row(
        "✔ GitHub 🤓 ",
        "[u blue link=https://github.com/jiaulislam]https://github.com/jiaulislam",
    )

    intro_message = Text.from_markup(
        """Consider supporting my work via Github 🤘 🤘 🤘. - Jiaul Islam"""
    )

    message = Table.grid(padding=1)
    message.add_column()
    message.add_column(no_wrap=True)
    message.add_row(intro_message, sponsor_message)

    message_panel = Panel(
        Align.center(
            RenderGroup(intro_message, "\n", Align.center(sponsor_message)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b red]Thanks for using my application!",
        border_style="bright_blue",
    )
    return message_panel


def get_choice() -> int:
    choice = Prompt.ask("Enter your choice", choices=['1', '2', '0'])
    return int(choice)


class MainMenuLayout:
    """ Return the main menu layout """

    def __init__(self) -> None:
        self.layout = Layout()
        self.table = Table(title="LDMA PARSER ACTIONS", expand=True)

    def __rich__(self) -> Layout:
        self.layout.split(
            Layout(name="head", size=3),
            Layout(name="body"),
        )

        self.layout["body"].split_column(
            Layout(name='should_be_unused', visible=False),
            Layout(name='table2'),
            Layout(name='action_table'),
        )
        self.table.add_column("Action Button", justify="center", style="cyan", no_wrap=True)
        self.table.add_column("Actions", style="magenta", justify="center")

        self.table.add_row("1", "TO SEARCH WITH LINK CODE")
        self.table.add_row("2", "TO SEARCH WITH SITE ID")
        self.table.add_row("0", "BACK TO MAIN MENU")

        self.layout["head"].update(Header("LDMA-PARSER"))
        self.layout["action_table"].update(self.table)
        self.layout["table2"].update(make_sponsor_message())

        return self.layout
