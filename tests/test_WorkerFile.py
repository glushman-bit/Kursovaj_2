import json
from unittest.mock import patch

from src.WorkerFile import WorkerFile


def test_add_info_plane_in_file(tmp_path, example_plane):
    """Тест на добавление данных о самолете в файл"""
    file_path = tmp_path / "planes.json"
    worker = WorkerFile(file_path)

    # Добавляем самолет
    worker.add_info_plane_in_file(example_plane)

    # Проверяем, что файл реально создан
    assert file_path.exists()

    # Проверяем содержимое
    with open(file_path, "r", encoding="UTF-8") as f:
        data = json.load(f)

    assert isinstance(data, list)
    plane_data = data[0]
    assert plane_data["Страна"] == example_plane.country
    assert plane_data["Позывной"] == example_plane.callsign
    assert plane_data["Скорость"] == f"{example_plane.velocity} м/с."
    assert plane_data["высота"] == f"{example_plane.geo_altitude} м."
    assert plane_data["Статус"] == example_plane.status_aeroplane


def test_read_info_plane_from_file(tmp_path):
    """Тест чтения данных из файла"""
    file_path = tmp_path / "planes.json"
    worker = WorkerFile(file_path)

    # Записываем данные
    test_data = [{"Страна": "Switzerland", "Позывной": "SWR438A"}]
    with open(file_path, "w", encoding="UTF-8") as f:
        json.dump(test_data, f, ensure_ascii=False, indent=4)

    # Читаем через WorkerFile
    result = worker.read_info_plane_from_file()
    assert result == test_data


def test_read_invalid_json(tmp_path):
    """Тест на пустой и невалидный json-файл"""
    file_path = tmp_path / "planes.json"
    worker = WorkerFile(file_path)

    file_path.write_text("")
    result = worker.read_info_plane_from_file()
    assert result == []

    file_path.write_text("invalid json")
    result = worker.read_info_plane_from_file()
    assert result == []


def test_delete_info_plane_from_file(tmp_path):
    """Тест удаления данных из файла"""
    file_path = tmp_path / "planes.json"
    worker = WorkerFile(file_path)

    # Записываем тестовые данные
    with open(file_path, "w", encoding="UTF-8") as f:
        json.dump([{"Страна": "Switzerland"}], f)

    # Очищаем файл
    worker.delete_info_plane_from_file()

    # Проверяем, что файл пустой
    with open(file_path, "r", encoding="UTF-8") as f:
        data = json.load(f)
    assert data == []


def test_file_not_found_add_read_delete(example_plane):
    """Тест проверки исключений в методах:
    add_info_plane_in_file, read_info_plane_from_file, delete_info_plane_from_file
    """
    worker = WorkerFile("nonexistent.json")

    with patch("builtins.open", side_effect=FileNotFoundError):
        assert worker.add_info_plane_in_file(example_plane) is None

    with patch("builtins.open", side_effect=FileNotFoundError):
        assert worker.read_info_plane_from_file() == []

    with patch("builtins.open", side_effect=FileNotFoundError):
        assert worker.delete_info_plane_from_file() is None
