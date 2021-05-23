from rich.console import Console
from selenium.common.exceptions import TimeoutException

console = Console()

def add_logging(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TimeoutException:
            console.log(
                f"TimeoutException: [red]Element not visible.[/red]. Source: [cyan italic]{func.__qualname__}[/]")
        except AttributeError:
            console.log(
                f"'Nonetype' object found. Source: [cyan italic]{func.__qualname__}[/]")
    return wrapper
