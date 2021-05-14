from rich.table import Table
from rich.layout import Layout
from rich import box, print
from prettify_ldma import Header

class MenuLayout:

    def __init__(self):
        self.layout = Layout()
        self.table = Table(title="ACTIONS", expand=True, show_lines=True, box=box.DOUBLE_EDGE)

    def __rich__(self):
        self.layout.split(
            Layout(name="head", size=3),
            Layout(name="body", ratio=1),
            Layout(name="footer", size=2)
        )

        self.layout["body"].split_column(
            Layout(name="Box 1", ratio=2),
            Layout(name="Box 2", ratio=3)
        )

        # Tables
        self.table.add_column("Action Button", justify="center")
        self.table.add_column("Action Description", justify="center")

        self.table.add_row("1", "🎟️  CREATE NCR")
        self.table.add_row("2", "📗  CLOSE NCR")
        self.table.add_row("3", "✂️  CANCEL NCR")
        self.table.add_row("4", "🗃️  LDMA PARSER")
        self.table.add_row("0", "❌ EXIT AUTOBOT")

        self.layout["head"].update(Header("WELCOME TO AUTOBOT"))
        self.layout["Box 2"].update(self.table)
        return self.layout

print(MenuLayout())