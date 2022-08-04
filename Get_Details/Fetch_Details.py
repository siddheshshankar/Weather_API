import requests
from dataclasses import dataclass


class GetData:

    def __init__(self, url):
        self.url = url

    def get_response(self):
        """
        This method send and get response from the web server
        :return: weather details in JSON format
        """
        return requests.get(self.url).json()

    def get_celsius(self):
        return round(self.get_response().get('main').get('temp') - 273.15, 2)

    def get_humidity(self):
        return float(self.get_response().get('main').get('humidity'))

    def get_forecast(self):
        return self.get_response().get('weather')[0].get('main')


@dataclass
class StoreData:
    temperature: float
    humidity: float
    forecast: str
