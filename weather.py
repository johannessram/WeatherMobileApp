from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image, AsyncImage

from kivy.config import Config
Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')

class shit(Image):
    pass

class MainApp(StackLayout):
    pass

class Wallpaper(Image):
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
    pass

class WeatherApp(App):
    def build(self):
        self.root = MainApp()
        return self.root

if __name__ == "__main__":
    WeatherApp().run()
