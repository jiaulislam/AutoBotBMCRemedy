from typing import Tuple

from rich.align import Align
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.table import Table
from rich.text import Text

from prettify.prettify_ldma import Header
from utilites.sysinfo import get_memory_info, get_platform, get_python_version


class CancelPrettify:
    _layout = Layout()
    _table = Table(title="Cancellation Status", expand=True)

    @staticmethod
    def get_top_layout() -> Panel:
        _memory: Tuple[str] = get_memory_info()
        _platform: str = get_platform()
        _pyversion: str = get_python_version()

        _total_memory: str = _memory[0]
        _available_memory: str = _memory[1]
        _used_percentage: str = _memory[2]
        _used_memory: str = _memory[3]
        _free_memory: str = _memory[4]

        table = Table.grid(expand=True, padding=(1, 1))

        table.add_row(
            "Total Memory: ", Text(
                _total_memory, style="yellow", justify="right")
        )
        table.add_row(
            "Available Memory: ", Text(
                _available_memory, style="green", justify="right")
        )
        table.add_row(
            "Used Memory: ", Text(_used_memory, style="red", justify="right")
        )
        table.add_row(
            "Free Memory: ", Text(_free_memory, style="green", justify="right")
        )
        table.add_row(
            "Used Percentage: ", Text(
                _used_percentage, style="magenta", justify="right")
        )
        table.add_row(
            "OS: ", Text(
                _platform, style="blue", justify="right")
        )
        table.add_row(
            "Python Version: ", Text(
                _pyversion, style="blue", justify="right")
        )
        return Panel(
            table,
            title="System Info",
            border_style="white",
        )

    @classmethod
    def make_layout(cls) -> None:
        cls._layout.split(
            Layout(name="header", size=3),
            Layout(name="body")
        )
        cls._layout["body"].split_row(
            Layout(name="left"),
            Layout(name="tables")
        )
        cls._layout["left"].split_column(
            Layout(name="top", ratio=1),
            Layout(name="progress", size=6)
        )
        cls._layout["header"].update(Header("Cancel Request Status"))
        cls._layout["top"].update(cls.get_top_layout())

    @classmethod
    def get_layout(cls) -> Layout:
        return cls._layout

    @classmethod
    def make_table(cls) -> None:
        cls._table.add_column("SL", justify="center")
        cls._table.add_column("NCR No", justify="center")
        cls._table.add_column("Status", justify="center")

    @classmethod
    def add_row_table(cls, sl: str, ncr_number: str, status: str, style="green") -> None:
        cls._table.add_row(sl, ncr_number, status, style=style)

    @classmethod
    def show_layout(cls) -> Layout:
        return cls._layout

    @classmethod
    def get_table(cls) -> Table:
        return cls._table

    @classmethod
    def merge_layout(cls, progress, table) -> None:
        cls._layout["progress"].update(Panel(
            Align.center(progress, vertical="middle"), border_style="green", title="Overall Status"))
        cls._layout["tables"].update(Panel(
            Align.center(table, vertical="middle"), border_style="cyan", title="Details"))

    @classmethod
    def progress_bar(cls, tasks_range: float) -> Progress:
        job_progress = Progress(
            "{task.description}",
            SpinnerColumn("dots", finished_text="Done", style="cyan"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        )
        progress_table = Table.grid(expand=True, padding=(1, 1))

        job_progress.add_task("[Cancel]:", total=tasks_range)

        progress_table.add_row(
            Panel.fit(job_progress, title="[b]jobs", padding=(2, 2))
        )
        return job_progress
