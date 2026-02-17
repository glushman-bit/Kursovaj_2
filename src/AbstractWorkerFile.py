from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Dict
from typing import List

from src.Planes import Planes


class AbstractWorkerFile(ABC):
    """Абстрактный класс для класса работы с файлом."""

    @abstractmethod
    def add_info_plane_in_file(self, object_plane: Planes) -> None: ...

    @abstractmethod
    def read_info_plane_from_file(self) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def delete_info_plane_from_file(self) -> None: ...
