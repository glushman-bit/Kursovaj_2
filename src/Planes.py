from src.APIAdapter import APIAdapter
import json

class Planes:
    """Класс объекта самолет"""

    def __init__(self, country, callsign, velocity, geo_altitude):
        self.country = self.__validate_country(country)
        self.callsign = self.__validate_callsign(callsign)
        self.velocity = self.__validate_velocity(velocity)
        self.geo_altitude = self.__validate_geo_altitude(geo_altitude)

    def __ge__(self, other):
        """Сравнение скорости"""
        if not isinstance(other, Planes):
            return NotImplemented

        return self.velocity > other.velocity


    def __le__(self, other):
        """Сравнение высоты"""
        if not isinstance(other, Planes):
            return NotImplemented

        return self.geo_altitude > other.geo_altitude



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
            velocity = 0
        else:
            velocity = velocity
        return velocity

    @staticmethod
    def __validate_geo_altitude(geo_altitude):
        """Валидация объекта - высота"""
        if not isinstance(geo_altitude, float | int):
            geo_altitude = 0
        else:
            geo_altitude = geo_altitude
        return geo_altitude



test = APIAdapter()
coordinates = test.get_coordinates('Russia')
test.get_aeroplanes(coordinates)
print(json.dumps(test.aeroplanes, indent=4))