import pytest

from src.Planes import Planes

COUNTRY_DATA = [
    (
        "Канада",
        [
            {"ru": "Канада", "en": "canada"},
            {"ru": "Франция", "en": "france"},
        ],
        "Canada",
    ),
    (
        "Испания",
        [
            {"ru": "Германия", "en": "germany"},
        ],
        None,
    ),
    (
        "   кАНАДА ",
        [
            {"ru": "Канада", "en": "canada"},
        ],
        "Canada",
    ),
]
"""parametrize для функции get_country_name"""


@pytest.fixture
def mock_planes_info():
    """Фикстура с примером данных самолетов"""
    return {
        "time": 1766142246,
        "states": [
            [
                "4b1812",  # 0 ICAO24
                "SWR438A",  # 1 callsign
                "Switzerland",  # 2 country
                1766166618,  # 3 time_position
                1766166618,  # 4 last_contact
                -0.0168,  # 5 longitude
                51.0888,  # 6 latitude
                4267.2,  # 7 baro_altitude
                False,  # 8 on_ground
                189.7,  # 9 velocity
                129.39,  # 10 heading
                14.63,  # 11 vertical_rate
                None,  # 12 sensors
                4282.44,  # 13 geo_altitude
                "2061",  # 14 squawk
                False,  # 15 spi
                0,  # 16 position_source
            ]
        ],
    }


@pytest.fixture
def plane_data():
    """Данные самолета"""
    return {
        "time_position": 1766166618,
        "country": "Switzerland",
        "callsign": "SWR438A",
        "velocity": 189.7,
        "geo_altitude": 4282,
        "on_ground": False,
    }


@pytest.fixture
def plane_grounded():
    """Самолет на земле"""
    return {
        "time_position": 1766166618,
        "country": "Switzerland",
        "callsign": "SWR438A",
        "velocity": 189.7,
        "geo_altitude": 4282.44,
        "on_ground": True,
    }


@pytest.fixture
def example_plane():
    """Данные самолета класса Planes"""
    return Planes(
        time_position=1766166618,
        country="Switzerland",
        callsign="SWR438A",
        velocity=428.44,
        geo_altitude=4282.44,
        on_ground=False,
    )
