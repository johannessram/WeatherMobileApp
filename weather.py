from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image, AsyncImage
from kivy.properties import StringProperty
from kivy.config import Config

import scrap

Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')

class MainApp(StackLayout):
    pass

class Wallpaper(Image):
    pass

class WelcomeLabel(Label):
    pass

class DateLabel(Label):
    pass

class MinTempLabel(Label):
    pass

class MaxTempLabel(Label):
    pass

class HumidityLabel(Label):
    pass

class GlobalLayout(GridLayout):
    pass

class WeatherIcon(Image):
    pass

class Container(BoxLayout):
    date = StringProperty()
    min_temp = StringProperty()
    max_temp = StringProperty()
    humidity_percentage = StringProperty()

    def __init__(self, date, min_temp, max_temp, humidity_percentage, **kwargs):
        super().__init__(**kwargs)
        self.date = date
        self.min_temp = str(min_temp) + '°C'
        self.max_temp = str(max_temp) + '°C'
        self.humidity_percentage = str(humidity_percentage) + '%'

    pass

class TodayDateLabel(Label):
    pass

class LocationFloatLayout(FloatLayout):
    location = StringProperty()
    temperature = StringProperty()

    def __init__(self, location, temperature, **kwargs):
        super().__init__(**kwargs)
        self.location = location
        self.temperature = str(temperature) + ('°C')
        # self.add_widget(TodayDateLabel(text=self.location + ' ' + temperature))

class WeatherApp(App):
    def build(self):
        scroll_view = ScrollView()
        global_layout = GlobalLayout()
        daily_forecast = scrap.dump_api_response_body()
        print(daily_forecast)
        today = list(daily_forecast.values())[0]

        self.root = MainApp()
        self.root.add_widget(WelcomeLabel())
        self.root.add_widget(LocationFloatLayout('Fianarantsoa', today.temp))
        for _, day in daily_forecast.items():
            global_layout.add_widget(Container(
                date=day.date,
                min_temp=day.min_temp,
                max_temp=day.max_temp,
                humidity_percentage=day.humidity_percentage
            ))

        


        # [global_layout.add_widget(Container(date='05/07/2024', min_temp='13°c', max_temp='30°c', humidity_percentage='40%')) for _ in range(2)]
        scroll_view.add_widget(global_layout)
        self.root.add_widget(scroll_view)
        return self.root

if __name__ == "__main__":
    WeatherApp().run()
