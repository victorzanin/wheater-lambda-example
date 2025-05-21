import requests  

class WeatherAPIClient:  
    def __init__(self):  
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"  
        self.api_key = "SUA_CHAVE"  # Use Environment Variables 

    def get_weather(self, city: str) -> dict:  
        params = {"q": city, "appid": self.api_key}  
        response = requests.get(self.base_url, params=params)  
        response.raise_for_status()  # Error when HTTP != 200  
        return response.json()  