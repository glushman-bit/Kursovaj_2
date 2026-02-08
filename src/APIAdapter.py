from abc import ABC, abstractmethod

import requests


class AbstractAdapter(ABC):

    @abstractmethod
    def get_coordinates(self, country: str) -> dict:
        pass

    @abstractmethod
    def get_aeroplanes(self, country: str) -> None:
        pass


class APIAdapter(AbstractAdapter):
    """Класс обращения к API ресурсам"""

    def __init__(self):
        self.openstreetmap_url = \
            'https://nominatim.openstreetmap.org/search'
        self.opensky_url = \
            'https://opensky-network.org/api/states/all?'
        self.aeroplanes = None


    def get_coordinates(self, country):
        """Получения координат воздушного пространства страны"""
        headers_nominatim = {
            'User-Agent': 'test-app/1.0'
        }
        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': 1
        }
        response = requests.get(
            url=self.openstreetmap_url,
            params=params_nominatim,
            headers=headers_nominatim
        )

        data = response.json()

        geo_coordinates = data[0].get("boundingbox")

        return geo_coordinates

    def get_aeroplanes(self, geo_coordinates: list) -> None:
        """Получения самолетов в координатах воздушного пространства страны"""
        params = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3],
        }

        response = requests.get(url=self.opensky_url, params=params)

        self.aeroplanes = response.json()

