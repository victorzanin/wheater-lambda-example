from services.api_client import WeatherAPIClient  
from unittest.mock import patch  

@patch("requests.get")  
def test_get_weather(mock_get):  
    mock_get.return_value.status_code = 200  
    mock_get.return_value.json.return_value = {"main": {"temp": 300}}  
    client = WeatherAPIClient()  
    assert client.get_weather("Sao_Paulo")["main"]["temp"] == 300  