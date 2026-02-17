from typing import Any, List, cast, Dict

import requests

from src.AbstractAdapter import AbstractAdapter


class APIAdapter(AbstractAdapter):
    """Класс обращения к API ресурсам, для получения координат страны и
    получения списка самолетов."""

    def __init__(self) -> None:
        self.openstreetmap_url: str = "https://nominatim.openstreetmap.org/search"
        self.opensky_url: str = "https://opensky-network.org/api/states/all?"
        self.aeroplanes: list | dict | None = None

    def get_coordinates(self, country: str) -> list[str]:
        """Получения координат воздушного пространства страны"""
        headers_nominatim = {"User-Agent": "test-app/1.0"}
        params_nominatim = {"country": country, "format": "json", "limit": 1}
        params_nominatim_str: dict[str, str] = {k: str(v) for k, v in params_nominatim.items()}

        response = requests.get(url=self.openstreetmap_url, params=params_nominatim_str, headers=headers_nominatim)

        if response.status_code != 200:
            raise Exception(f"Ошибка запроса: {response.status_code}, {self.openstreetmap_url}.")
        try:
            data: list[dict[str, Any]] = response.json()
        except ValueError:
            raise ValueError("Ответ не JSON")

        if not data:
            raise ValueError("Пустой ответ API")

        geo_coordinates = cast(List[str], data[0].get("boundingbox"))

        return geo_coordinates  # List[str]

    def get_aeroplanes(self, geo_coordinates: list[str]) -> Dict:
        """Получения списка самолетов в координатах воздушного пространства страны"""
        params = {
            "lamin": geo_coordinates[0],
            "lamax": geo_coordinates[1],
            "lomin": geo_coordinates[2],
            "lomax": geo_coordinates[3],
        }

        response = requests.get(url=self.opensky_url, params=params)

        if response.status_code != 200:
            raise Exception(f"Ошибка запроса: {response.status_code}, {self.opensky_url}.")

        try:
            data = response.json()
        except ValueError:
            raise ValueError("Ответ не JSON")

        self.aeroplanes = data
