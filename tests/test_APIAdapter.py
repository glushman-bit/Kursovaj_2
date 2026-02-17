from unittest.mock import Mock
from unittest.mock import patch

import pytest

from src.APIAdapter import APIAdapter


@patch("src.APIAdapter.requests.get")
def test_get_coordinates_correct(mock_get):
    """Проверка корректности работы функции"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"boundingbox": ["41.6765597", "83.3362128", "-141.0027500", "-52.3237664"]}]
    mock_get.return_value = mock_response

    adapter = APIAdapter()
    adapter.openstreetmap_url = "https://url.test"

    result = adapter.get_coordinates("Canada")
    assert result == ["41.6765597", "83.3362128", "-141.0027500", "-52.3237664"]
    mock_get.assert_called_once()


@patch("src.APIAdapter.requests.get")
def test_get_coordinates_http_error(mock_get):
    """Проверка на ошибки запроса"""
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    adapter = APIAdapter()

    with pytest.raises(Exception, match="Ошибка запроса: 500"):
        adapter.get_coordinates("Canada")


@patch("src.APIAdapter.requests.get")
def test_get_coordinates_invalid_json(mock_get):
    """Проверка при неверного ответа"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError
    mock_get.return_value = mock_response

    adapter = APIAdapter()

    with pytest.raises(ValueError, match="Ответ не JSON"):
        adapter.get_coordinates("Canada")


@patch("src.APIAdapter.requests.get")
def test_get_coordinates_empty_json(mock_get):
    """Проверка на возврат пустого списка"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = []
    mock_get.return_value = mock_response

    adapter = APIAdapter()

    with pytest.raises(ValueError, match="Пустой ответ API"):
        adapter.get_coordinates("Canada")


@patch("src.APIAdapter.requests.get")
def test_get_aeroplanes_correct(mock_get):
    """Проверка корректности работы функции"""
    mock_data = {"time": 1766142246, "states": [["4b1812", "SWR438A ", "Switzerland"]]}

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_data
    mock_get.return_value = mock_response

    adapter = APIAdapter()
    adapter.opensky_url = "https://opensky.test"

    coordinates = ["41.6765597", "83.3362128", "-141.0027500", "-52.3237664"]

    adapter.get_aeroplanes(coordinates)

    assert adapter.aeroplanes == mock_data
    mock_get.assert_called_once()


@patch("src.APIAdapter.requests.get")
def test_get_aeroplanes_http_error(mock_get):
    """Проверка на ошибки запроса"""
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    adapter = APIAdapter()

    with pytest.raises(Exception, match="Ошибка запроса: 500"):
        adapter.get_aeroplanes(["41.6765597", "83.3362128", "-141.0027500", "-52.3237664"])


@patch("src.APIAdapter.requests.get")
def test_get_aeroplanes_invalid_json(mock_get):
    """Проверка при неверном ответе с сервера"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError
    mock_get.return_value = mock_response

    adapter = APIAdapter()

    with pytest.raises(ValueError, match="Ответ не JSON"):
        adapter.get_aeroplanes([1, 2, 3, 4])
