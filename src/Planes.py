from datetime import datetime, UTC
from src.APIAdapter import APIAdapter

class Planes:
    """Класс объекта самолет"""

    def __init__(self, time_position: datetime, country: str, callsign: str, velocity: float | int, geo_altitude: float | int, on_ground: bool):
        self.time_position = self.__validate_time_position(time_position)
        self.country = self.__validate_country(country)
        self.callsign = self.__validate_callsign(callsign)
        self.velocity = self.__validate_velocity(velocity)
        self.geo_altitude = self.__validate_geo_altitude(geo_altitude)
        self.on_ground = self.__validate_on_ground(on_ground)

    def __str__(self):
        return f'{self.country} {self.callsign} {self.velocity} {self.geo_altitude} {str(self.on_ground)}'

    def __ge__(self, other: 'Planes'):
        """Сравнение скорости"""
        if not isinstance(other, Planes):
            return NotImplemented

        print(self.velocity, " >= ", other.velocity)
        return self.velocity >= other.velocity


    def __le__(self, other: 'Planes'):
        """Сравнение высоты"""
        if not isinstance(other, Planes):
            return NotImplemented

        print(self.geo_altitude, " <= ", other.geo_altitude)
        return self.geo_altitude <= other.geo_altitude

    @property
    def is_airborne(self) -> bool:
        """Сравнение состояния самолета: в полете или на земле"""
        return self.on_ground is False

    def __bool__(self):
        return self.is_airborne

    @staticmethod
    def __validate_time_position(time_position):
        if not isinstance(time_position, float | int):
            raise ValueError("time_position должен быть timestamp (int или float)")

        return time_position

    @staticmethod
    def __validate_country(country):
        """Валидация объекта - страна"""
        if not isinstance(country, str):
            country = "Страна не передана"
        else:
            country = country
        return country

    @staticmethod
    def __validate_callsign(callsign):
        """Валидация объекта - позывной"""
        if not isinstance(callsign, str):
            callsign = "Позывной не передан"
        else:
            callsign = callsign
        return callsign

    @staticmethod
    def __validate_velocity(velocity):
        """Валидация объекта - скорость"""
        if not isinstance(velocity, float | int):
            velocity = 0.0
        else:
            velocity = velocity
        return velocity

    @staticmethod
    def __validate_geo_altitude(geo_altitude):
        """Валидация объекта - высота"""
        if not isinstance(geo_altitude, float | int):
            geo_altitude = 0.0
        else:
            geo_altitude = geo_altitude
        return geo_altitude

    def __validate_on_ground(self, on_ground):
        if isinstance(on_ground, bool):
            return on_ground

        return self.geo_altitude <= 0

    @property
    def status_aeroplane(self):
        return "В полете" if self.geo_altitude > 0 else "На земле"

    @property
    def get_time_from_time_position(self):
        if self.time_position is None:
            return None

        time_utc = datetime.fromtimestamp(self.time_position, UTC)
        local_time = time_utc.astimezone().isoformat(sep=" ")
        return local_time
