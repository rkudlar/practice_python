import requests
import json

API_KEY = "b6ad656cc94a39c3a2929c1e17ff42da"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}"

    response = requests.get(url)
    data = json.loads(response.text)

    if response.status_code == 200:
        temperature = round(data["main"]["temp"] - 273.15)
        weather_description = data["weather"][0]["description"]
        print(f"Погода в {city}")
        print(f"Температура: {temperature}°C")
        print(f"Опис: {weather_description}")
    else:
        print("Під час отримання даних про погоду сталася помилка.")
        print(data)

city = input("Введіть місто: ")

get_weather(city)
