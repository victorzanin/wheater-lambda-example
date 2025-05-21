import boto3  
from datetime import datetime  

class DynamoDBHandler:  
    def __init__(self):  
        self.table = boto3.resource("dynamodb").Table("WeatherData")  

    def save(self, data: dict) -> None:  
        item = {  
            "timestamp": datetime.now().isoformat(),  
            "city": data["name"],  
            "temperature": data["main"]["temp"] - 273.15,  
            "humidity": data["main"]["humidity"],  
        }  
        self.table.put_item(Item=item)