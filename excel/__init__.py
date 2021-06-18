from abc import ABC, abstractmethod
from typing import Dict


class Excel(ABC):

    @abstractmethod
    def get_row(self, row_num: int) -> Dict[str, str]:
        pass

    @abstractmethod
    def insert(self, row_num: int, data: str) -> None:
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def close(self):
        pass
