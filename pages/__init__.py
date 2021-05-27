from abc import ABC, abstractmethod
from drivers import Driver

class Page(ABC):
    """ Abstraction of Page """
    @abstractmethod
    def driver(self) -> Driver:
        pass

    @abstractmethod
    def open(self, url) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
