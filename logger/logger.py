import logging
from logging import Logger
from datetime import date


def get_logger() -> Logger:
    # main logger
    logger = logging.getLogger("main")
    logger.setLevel(logging.WARNING)

    # file handler
    file_handler = logging.FileHandler(f"logs/{date.today()}.log")
    file_handler.setLevel(logging.WARNING)

    # formatter
    formatter = logging.Formatter(
        '[%(asctime)s] - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
