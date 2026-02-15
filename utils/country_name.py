import json
from pathlib import Path


def get_country_name(found_country: str) -> str | None:
    """Функция получения названия страны на английском языке,
    чтение данных из файла Countries.json.
    Возвращает None если страна не найдена."""

    base_dir = Path(__file__).resolve().parent.parent
    filename = base_dir / 'data' / 'Countries.json'

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    found_country_lower = found_country.lower().strip()

    for country in data:
        if country['ru'].lower() == found_country_lower:
            return country['en'].capitalize()

    return None

