from abc import ABC
from abc import abstractmethod
from src.Planes import Planes
from typing import Any, List, Dict
class AbstractWorkerFile(ABC):
    """Абстрактный класс для класса работы с файлом."""

    @abstractmethod
    def add_info_plane_in_file(self, object_plane: Planes) -> None:
        ...

    @abstractmethod
    def read_info_plane_from_file(self) -> List[Dict[str, Any]]:
        ...

    @abstractmethod
    def delete_info_plane_from_file(self) -> None:
        ...
