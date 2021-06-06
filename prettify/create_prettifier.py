from typing import Tuple

from rich import box
from rich.align import Align
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table

from prettify.prettify_ldma import Header


def get_table() -> Table:
    table = Table(title="NCR Creation Status", box=box.ROUNDED, show_lines=True, expand=True)

    table.add_column("SL", justify="center")
    table.add_column("Zone", justify="center")
    table.add_column("Service Type", justify="center")
    table.add_column("Coordinator", justify="center")
    table.add_column("CR Number", justify="center", style="cyan")
    table.add_column("Status", justify="center")
    return table


def get_table_panel(table: Table) -> Panel:
    table_panel = Panel(
        Align.center(
            table,
            vertical="middle"
        ), title="Task Details", border_style="yellow", padding=(1, 0), expand=True
    )
    return table_panel


def add_row_table(table: Table, *data: Tuple[str, ...]) -> None:
    table.add_row(*data)


def get_layout() -> Layout:
    layout = Layout()
    layout.split(
        Layout(name="header", size=3)
        # Layout(name="body", size=2),
    )

    layout["header"].update(Header("Create NCR"))
    return layout
