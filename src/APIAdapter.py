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

    def __init__(self):
        self.openstreetmap_url = \
            'https://nominatim.openstreetmap.org/search'
        self.opensky_url = \
            'https://opensky-network.org/api/states/all?'
        self.aeroplanes = None


    def get_coordinates(self, country):
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

        params = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3],
        }

        response = requests.get(url=self.opensky_url, params=params)

        self.aeroplanes = response.json()


class Planes:

    def __init__(self, country, callsign, velocity, geo_altitude):
        self.country = country
        self.callsign = callsign
        self.velocity = velocity
        self.geo_altitude = geo_altitude





test = APIAdapter()
coordinates = test.get_coordinates('Russia')
test.get_aeroplanes(coordinates)
print(test.aeroplanes)