from rich import box
from rich.align import Align
from rich.console import Console, RenderableType
from rich.layout import Layout
from rich.panel import Panel
from rich.prompt import IntPrompt
from rich.table import Table

console: Console = Console()


def make_layout() -> Layout:
    layout: Layout = Layout(name='root')
    layout["root"].split_column(
        Layout(name="body", ratio=10),
        Layout(name="footer", size=4)
    )
    return layout


def _menu_choice_table() -> Table:
    table: Table = Table(padding=(0, 13), box=box.ASCII)

    table.add_column("PRESS KEY", justify="center",
                     header_style="#16C60C",
                     no_wrap=True, style="#16C60C")
    table.add_column("METHOD", justify="center",
                     header_style="#F9F1A5 bold",
                     no_wrap=True, style="#F9F1A5")

    table.add_row("1", "With LINK-ID", )
    table.add_row("2", "With SITE-NAME")
    table.add_row("3", "EXIT MENU")

    return table


def body_panel(item: RenderableType) -> Panel:
    display_panel: Panel = Panel(
        Align.center(
            item,
            vertical="middle"
        ),
        box=box.ROUNDED,
        title='LDMA PARSER',
        border_style="bright_green",
    )
    return display_panel


def footer_panel() -> Panel:
    display_footer: Panel = Panel(
        Align.center(
            ":heart::heart::heart: Made with love :heart::heart::heart:\n\t@jibon",
            vertical='middle'
        ),
        border_style="#DC143C"
    )
    return display_footer


def take_choice_input() -> int:
    choice: int = IntPrompt.ask("Select", choices=['1', '2', '3'])
    return choice


def menu() -> int:
    layout: Layout = make_layout()
    layout["body"].size = 10
    layout["body"].update(body_panel(_menu_choice_table()))
    layout["footer"].update(footer_panel())

    console.print(layout)

    return take_choice_input()
