from functools import wraps
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchFrameException
import logging
from datetime import date

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '[%(asctime)s] - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
handler = logging.FileHandler(f'logs/{date.today()}.log')
handler.setFormatter(formatter)
handler.setLevel(logging.WARNING)
logger.addHandler(handler)


def add_logger(fn):
    """ trace the exceptions """
    @wraps(fn)
    def wrapper(*args):
        try:
            fn(*args)
        except TimeoutException:
            logger.error(
                f"TimeoutException: Request Couldn't finished due to timeout.")
        except AttributeError:
            logger.error(
                f"'Nonetype' object found.")
        except NoSuchElementException:
            logger.error(
                f"NoSuchElementException: ElementNotFound in the DOM.")
        except NoSuchFrameException:
            logger.error(
                f"NoSuchFrameException: FrameNotFound in the DOM.")
        except TypeError:
            logger.error(
                f"TypeError: Element Type mismatch")

    return wrapper
