from unittest.mock import mock_open
from unittest.mock import patch

import pytest

from tests.conftest import COUNTRY_DATA
from utils.country_name import get_country_name


@pytest.mark.parametrize("input_name, json_data, expected", COUNTRY_DATA)
@patch("utils.country_name.json.load")
@patch("builtins.open", new_callable=mock_open)
def test_get_country_name(_mock_file, mock_json, input_name, json_data, expected):
    """Тест функции get_country_name через параметрайз"""
    mock_json.return_value = json_data
    result = get_country_name(input_name)

    assert result == expected
