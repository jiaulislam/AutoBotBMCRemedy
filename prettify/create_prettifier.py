from time import sleep
from typing import Tuple

from rich.align import Align
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
from rich import box
from prettify.prettify_ldma import Header


def get_table() -> Table:
    table = Table(title="Status", box=box.ROUNDED, show_lines=True, expand=True)

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
            vertical="top"
        ), title="Task Details", border_style="yellow", padding=(1, 0), expand=True
    )
    return table_panel


# sl: str, coordinator_name: str, cr_number: str, status: str

def add_row_table(table: Table, *data: Tuple[str, ...]) -> None:
    table.add_row(*data)


def get_layout() -> Layout:
    layout = Layout()
    layout.split(
        Layout(name="header", size=3),
        Layout(name="body", size=2),
    )

    layout["header"].update(Header("NCR Creation Status"))
    return layout


def get_job_progress():
    job_progress = Progress(
        "{task.description}",
        SpinnerColumn(),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    )
    jobs = job_progress.add_task("[cyan]Creating", total=200)

    total = sum(task.total for task in job_progress.tasks)
    overall_progress = Progress()
    overall_task = overall_progress.add_task("All Jobs", total=int(total))

    progress_table = Table.grid()
    progress_table.add_row(
        Panel.fit(
            overall_progress, title="Overall Progress", border_style="green", padding=(2, 2)
        ),
        Panel.fit(job_progress, title="[b]Jobs", border_style="red", padding=(1, 2)),
    )

    panel = Panel(Align.center(progress_table, vertical="middle"), title="Task", border_style="magenta")
