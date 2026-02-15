from abc import ABC, abstractmethod


class AbstractWorkerFile(ABC):
    """Абстрактный класс для класса работы с файлом."""

    @abstractmethod
    def add_info_plane_in_file(self, object_plane):
        pass

    @abstractmethod
    def read_info_plane_from_file(self):
        pass

    @abstractmethod
    def delete_info_plane_from_file(self):
        pass
