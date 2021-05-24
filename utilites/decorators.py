from rich.console import Console
from functools import wraps
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchFrameException

console = Console(color_system='truecolor')


def add_logging(fn):
    """ trace the exceptions """
    @wraps(fn)
    def wrapper(*args):
        try:
            fn(*args)
        except TimeoutException:
            console.log(
                f"⚠️ TimeoutException: [red]Element not visible.[/red]. Source: [cyan italic]{fn.__qualname__}[/]"
            )
        except AttributeError:
            console.log(
                f"⚠️ 'Nonetype' object found. Source: [cyan italic]{fn.__qualname__}[/]"
            )
        except NoSuchElementException:
            console.log(
                f"⚠️ NoSuchElementException: [red]Element not found.[/red]. Source: [cyan italic]{fn.__qualname__}[/]"
            )
        except NoSuchFrameException:
            console.log(
                f"⚠️ NoSuchFrameException: [red]Frame not found.[/red]. Source: [cyan italic]{fn.__qualname__}[/]"
            )

    return wrapper
