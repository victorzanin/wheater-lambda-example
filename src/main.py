from services.api_client import WeatherAPIClient  
from services.db_handler import DynamoDBHandler  

def lambda_handler(event, context):  
    # 1. Collect data  
    api_client = WeatherAPIClient()  
    weather_data = api_client.get_weather("Sao_Paulo")  

    # 2. Save in DynamoDB  
    db_handler = DynamoDBHandler()  
    db_handler.save(weather_data)  

    return {"status": "success"}  