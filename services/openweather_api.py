import requests
from datetime import datetime
from config import Config
from tools import convert_to_celsius, ms_to_kmh

def fetch_weather():
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={Config.QUERY}&appid={Config.API_KEY}'
        res = requests.get(url)
        data = res.json()
        #print(data)

        weather = { "temp":convert_to_celsius( data["main"]["temp"]),
            "tempodczuw": convert_to_celsius(data["main"]["feels_like"]),
            "cisnienie": data["main"]["pressure"],
            "wilgotnosc": data["main"]["humidity"],
            "opis": data["weather"][0]["description"],
            "miejsce": data["name"],
            "wiatr": ms_to_kmh( data["wind"]["speed"]),
            "zachmurzenie": data["clouds"]["all"],
            "data":datetime.now().strftime("%H:%M:%S %Y-%m-%d")
        }
        return (weather)


    except Exception as e:
        print(e)





