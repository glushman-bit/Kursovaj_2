from abc import ABC
from abc import abstractmethod


class AbstractAdapter(ABC):
    """Абстрактный класс для класса получения API запросов APIAdapter."""

    @abstractmethod
    def get_coordinates(self, country: str) -> dict:
        pass

    @abstractmethod
    def get_aeroplanes(self, country: str) -> None:
        pass
