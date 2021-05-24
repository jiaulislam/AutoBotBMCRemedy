import logging
from rich.console import Console
from functools import wraps
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchFrameException


logging.basicConfig(filename='autobot.log',
                    level=logging.ERROR, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
console = Console(color_system='truecolor')


def add_logging(fn):
    """ trace the exceptions """
    @wraps(fn)
    def wrapper(*args):
        try:
            fn(*args)
        except TimeoutException:
            logging.error(f'TimeoutException at {fn.__qualname__}')
            console.log(
                f"⚠️ TimeoutException: [red]Element not visible.[/red]. Source: [cyan italic]{fn.__qualname__}[/]"
            )
        except AttributeError:
            logging.error(f'AttributeError at {fn.__qualname__}')
            console.log(
                f"⚠️ 'Nonetype' object found. Source: [cyan italic]{fn.__qualname__}[/]"
            )
        except NoSuchElementException:
            logging.error(f'NoSuchElementException at {fn.__qualname__}')
            console.log(
                f"⚠️ NoSuchElementException: [red]Element not found.[/red]. Source: [cyan italic]{fn.__qualname__}[/]"
            )
        except NoSuchFrameException:
            logging.error(f'NoSuchFrameException at {fn.__qualname__}')
            console.log(
                f"⚠️ NoSuchFrameException: [red]Frame not found.[/red]. Source: [cyan italic]{fn.__qualname__}[/]"
            )

    return wrapper
