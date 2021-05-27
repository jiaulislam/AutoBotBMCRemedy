from abc import ABC, abstractmethod
from interface.elements import Element

class Driver(ABC):
    """ Abstraction of Driver """
    @abstractmethod
    def get(self, url) -> None:
        pass

    @abstractmethod
    def maximize_window(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def find_element(self, _by: str, value: str) -> Element:
        pass