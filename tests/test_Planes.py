from datetime import datetime

import pytest

from src.Planes import Planes


def test_planes_initialization(plane_data):
    """Тест на инициализацию"""
    plane = Planes(**plane_data)

    assert plane.time_position == plane_data["time_position"]
    assert plane.country == plane_data["country"]
    assert plane.callsign == plane_data["callsign"]
    assert plane.velocity == plane_data["velocity"]
    assert plane.geo_altitude == plane_data["geo_altitude"]
    assert plane.on_ground == plane_data["on_ground"]


def test_planes_airborne_and_status(plane_data, plane_grounded):
    """Тест проверки статуса самолета"""
    fly = Planes(**plane_data)
    ground = Planes(**plane_grounded)

    # Проверка состояния
    assert fly.is_airborne is True
    assert ground.is_airborne is False

    # Проверка статуса
    assert fly.status_aeroplane == "В полете"
    # assert ground.status_aeroplane == "На земле"
    #
    # # Проверка bool
    assert bool(fly) is True
    assert bool(ground) is False


def test_planes_comparison() -> None:
    """Тест на сравнение самолетов"""
    plane1 = Planes(1766166618, "A", "CS1", 200, 3000, False)
    plane2 = Planes(1766166618, "B", "CS2", 150, 4000, False)

    # Сравнение скорости
    assert (plane1 >= plane2) is True
    assert (plane2 >= plane1) is False

    # Сравнение высоты
    assert (plane1 <= plane2) is True
    assert (plane2 <= plane1) is False


@pytest.mark.parametrize(
    "attr, value, expected",
    [
        ("time_position", "not_a_number", ValueError),
        ("country", 123, "Страна не передана"),
        ("callsign", 456, "Позывной не передан"),
        ("velocity", "fast", 0.0),
        ("geo_altitude", "high", 0.0),
    ],
)
def test_planes_validation(attr, value, expected, plane_data) -> None:
    """Тест валидации параметров"""
    data = plane_data.copy()
    data[attr] = value

    if expected == ValueError:
        with pytest.raises(ValueError):
            Planes(**data)
    else:
        plane = Planes(**data)
        assert getattr(plane, attr) == expected


def test_planes_time_from_timestamp(plane_data):
    """Тест на корректность времени"""
    plane = Planes(**plane_data)
    time_str = plane.get_time_from_time_position

    # Проверка, что строка в ISO формате
    dt = datetime.fromisoformat(time_str)
    assert isinstance(dt, datetime)


def test_planes_with_other_class() -> None:
    """Тест сравнения с параметром другого класса"""
    plane = Planes(1766166618, "A", "CS1", 200, 3000, False)

    class TestPlanes:
        pass

    assert plane.__ge__(TestPlanes) is NotImplemented
    assert plane.__le__(TestPlanes) is NotImplemented
