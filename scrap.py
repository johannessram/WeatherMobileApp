import requests
import statistics
from typing import Callable
from key import OPENWEATHER_API_KEY

class Day:
    def __init__(self, date, temp=None, min_temp=None, max_temp=None, humidity_percentage=None):
        self.date = date
        self.temp = temp
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.humidity_percentage = humidity_percentage

        print(self.date, self.temp, self.min_temp, self.max_temp, self.humidity_percentage)

def dump_api_response_body():
    city = "Fianarantsoa"

    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric'.format(city, OPENWEATHER_API_KEY)

    res = requests.get(url)
    data = res.json()
    all_date_information = {}
    all_temp = []
    all_min_temp = []
    all_max_temp = []
    all_humidity_percentage = []
    last_date = None
    current_date = None
    for i in range(len(data['list'])):
        day = data['list'][i]
        date = day['dt_txt'].split()[0]
        if not last_date and not current_date:
            last_date = date
            current_date = date

        if current_date != date:
            information = Day(date=last_date,
                temp=int(statistics.mean(all_temp)),
                min_temp=int(min(all_min_temp)),
                max_temp=int(max(all_max_temp)),
                humidity_percentage=int(statistics.mean(all_humidity_percentage)))
            all_date_information[last_date] = information
            all_temp = []
            min_temp = []
            max_temp = []
            all_humidity_percentage = []
            last_date = current_date
            current_date = date

        all_temp.append(day['main']['temp'])
        all_humidity_percentage.append(day['main']['humidity'])
        all_min_temp.append(day['main']['temp_min'])
        all_max_temp.append(day['main']['temp_max'])

    information = Day(date=last_date,
        temp=int(statistics.mean(all_temp)),
        min_temp=int(min(all_min_temp)),
        max_temp=int(max(all_max_temp)),
        humidity_percentage=int(statistics.mean(all_humidity_percentage)))
    all_date_information[last_date] = information

    return all_date_information


