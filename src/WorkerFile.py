import json
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List

from src.AbstractWorkerFile import AbstractWorkerFile
from src.Planes import Planes


class WorkerFile(AbstractWorkerFile):
    """Класс для работы сохранения и добавления данных в файл."""

    def __init__(self, filename: str | None = None) -> None:
        if filename is None:
            base_dir = Path(__file__).resolve().parent.parent
            self.filename = base_dir / "data" / "InfoPlane.json"
        else:
            self.filename = Path(filename)

    def add_info_plane_in_file(self, object_plane: Planes) -> None:
        """Добавление информации о самолете в файл"""
        try:
            with open(self.filename, "w+", encoding="UTF-8") as file:
                file.seek(0)
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []

                object_dict = {
                    "Время": object_plane.get_time_from_time_position,
                    "Страна": object_plane.country,
                    "Позывной": object_plane.callsign,
                    "Скорость": f"{object_plane.velocity} м/с.",
                    "высота": f"{object_plane.geo_altitude} м.",
                    "Статус": object_plane.status_aeroplane,
                }
                if object_dict not in data:
                    data.append(object_dict)

                file.seek(0)
                file.truncate()
                json.dump(data, file, ensure_ascii=False, indent=4)

        except FileNotFoundError:
            return

    def read_info_plane_from_file(self) -> List[Dict[str, Any]]:
        """Функция чтения данных из файла"""
        try:
            with open(self.filename, "r", encoding="UTF-8") as file:
                try:
                    return json.load(file)  # type: ignore
                except json.JSONDecodeError:
                    return []

        except FileNotFoundError:
            return []

    def delete_info_plane_from_file(self) -> None:
        """Функция удаления файлов из файла (очищает файл)"""
        try:
            with open(self.filename, "w", encoding="UTF-8") as file:
                json.dump([], file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            ...
