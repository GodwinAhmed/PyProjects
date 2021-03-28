from typing import DefaultDict
import requests
from pprint import pprint

API_Key = '6d8e3e6fadb620abab0e48103d171589' # API key generated from openweather.org 

city = input("Enter a city: ")
base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
weather_data = requests.get(base_url).json()
pprint(weather_data)