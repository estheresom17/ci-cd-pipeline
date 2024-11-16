from src.app import get_weather
import pytest
from unittest.mock import patch

@patch("src.app.requests.get")
def test_get_weather_success(mock_get):
    # Mock API response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "main": {"temp": 25},
        "weather": [{"description": "clear sky"}]
    }

    result = get_weather("Helsinki")
    assert result == "The current temperature in Helsinki is 25°C with clear sky."

@patch("src.app.requests.get")
def test_get_weather_error(mock_get):
    # Simulate API error
    mock_get.side_effect = Exception("API error")

    result = get_weather("InvalidCity")
    assert "Error fetching weather data" in result
