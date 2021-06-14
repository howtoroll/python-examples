import json
import urllib.parse
import urllib.request

from datetime import datetime


# client
class FacadeClient:
    def __init__(self):
        pass

    def ask_forecast(self):
        facade = Facade()
        print(facade.get_forecast('London', 'UK'))


# facade
class Facade:
    def __init__(self):
        pass

    def get_forecast(self, city, country):
        weather_provider = WeatherProvider()
        weather_data = weather_provider.get_weather_data(city, country)

        parser = Parser()
        parsed_data = parser.parse_weather_data(weather_data)

        weather = Weather(parsed_data)
        converter = Converter()
        temperature_celcius = converter.from_kelvin_to_celcius(weather.temperature)

        return temperature_celcius


# subsystems
class Weather:
    def __init__(self, data):
        result = 0

        for r in data:
            result += r

        self.temperature = result / len(data)


class WeatherProvider:
    def __init__(self):
        # unauthorized
        self.api_url = 'http://api.openweathermap.org/data/2.5/forecast?q={},{}'

    def get_weather_data(self, city, country):
        city = urllib.parse.quote(city)
        url = self.api_url.format(city, country)
        return urllib.request.urlopen(url).read()


class Parser:
    def __init__(self):
        pass

    def parse_weather_data(self, weather_data):
        parsed = json.loads(weather_data)
        start_date = None
        result = []

        for data in parsed['list']:
            date = datetime.strptime(data['dt_txt'], '%Y-%m-%d %H:%M:%S')
            start_date = start_date or date
            if start_date.day != date.day:
                return result
            result.append(data['main']['temp'])


class Converter:
    def from_kelvin_to_celcius(self, kelvin):
        return kelvin - 273.15

    def from_celcius_to_kelvin(self, celcius):
        return celcius + 273.15
