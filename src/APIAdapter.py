from src.AbstractAdapter import AbstractAdapter
import requests


class APIAdapter(AbstractAdapter):
    """Класс обращения к API ресурсам, для получения координат страны и
        получения списка самолетов."""

    def __init__(self):
        self.openstreetmap_url = \
            'https://nominatim.openstreetmap.org/search'
        self.opensky_url = \
            'https://opensky-network.org/api/states/all?'
        self.aeroplanes = None


    def get_coordinates(self, country: str) -> list:
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

        if response.status_code != 200:
            raise Exception(f'Ошибка запроса: {response.status_code}, {self.openstreetmap_url}.')
        try:
            data = response.json()
        except ValueError:
            return "Ответ не JSON"

        if not data:
            return None

        geo_coordinates = data[0].get("boundingbox")

        return geo_coordinates

    def get_aeroplanes(self, geo_coordinates: list) -> None:
        """Получения списка самолетов в координатах воздушного пространства страны"""
        params = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3],
        }

        response = requests.get(url=self.opensky_url, params=params)

        if response.status_code != 200:
            raise Exception(f"Ошибка запроса: {response.status_code}, {self.opensky_url}.")

        try:
            data = response.json()
        except ValueError:
            return "Ответ не JSON"

        self.aeroplanes = data
        return data

# coordinates = APIAdapter().get_coordinates('poland')
# print(coordinates)
#
# result = APIAdapter().get_aeroplanes(coordinates)
#
# print(result)

