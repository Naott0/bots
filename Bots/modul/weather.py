import datetime
import json
import requests
from aiogram import types

from Project.Bots.modul import keyboards


async def process_pogoda_command(message: types.Message):
    await message.answer('Выберите город! ', reply_markup=keyboards.keyboard)

async def process_pnd_command(message: types.Message):
    url = "https://api.weather.yandex.ru/v2/fact?lat=47.222078&lon=39.720349&extra=true"
    headers = {'X-Yandex-API-Key': "097bf658-bf6b-445c-b0a3-6214d61b54d0"}
    response = requests.request("GET", url, headers=headers)
    a = json.loads(response.text)
    temp = (a.get('temp'))
    z = "Температура (°C):"
    current_datetime = datetime.now()
    rt = "Cейчас в Ростове-на-Дону !"
    feels_like = (a.get('feels_like'))
    b = "Ощущаемая температура (°C):"
    condition = (a.get('condition'))
    c = "Hебо:"
    ii = {'clear': '☀️', 'partly-cloudy': '🌤️', 'cloudy': '🌥️', 'overcast': '☁️', 'drizzle': '💧', ' light-rain': '☔️',
          'rain': '🌧️', 'moderate-rain': '🌧️🌧', ' heavy-rain ': '💧💧💧', 'showers': '💦',
          'continuous-heavy-rain': '🌧️🌬', 'wet-snow': '🌧️❄️', 'light-snow': '🌨️', 'snow': '❄️',
          'snow-showers': '❄️❄️️❄️', 'hail': '🧊',
          'thunderstorm': '⚡️', 'thunderstorm-with-rain': '⛈️', 'thunderstorm-with-hail': '⚡️🧊'}
    condition = (ii.get(condition))
    wind_speed = (a.get('wind_speed'))
    v = "Скорость ветра (в м/с):"
    pressure_mm = (a.get('pressure_mm'))
    d = "Давление (в мм рт. ст.).:"
    humidity = (a.get('humidity'))
    h = "Влажность воздуха %:"
    vet = "Направление ветра:"
    wind_dir = (a.get('wind_dir'))

    vet2 = {'nw': 'северо-западное', 'n': 'северное', 'ne': ' северо-восточное', 'e': 'восточное',
            'se': ' юго-восточное', 's': 'южное', 'sw': ' юго-западное', 'w': 'западное', 'c': 'штиль'}
    wind_dir3 = (vet2.get(wind_dir))

    await message.answer(
        f'{rt} \n {current_datetime} \n {z} {temp} \n {b} {feels_like} \n {c} {condition} \n {vet} {wind_dir3} \n {v} {wind_speed} \n {d} {pressure_mm} \n {h} {humidity}')


async def process_moscow_command(message: types.Message):
    url = "https://api.weather.yandex.ru/v2/fact?lat=55.81579208&lon=37.38003159&extra=true"
    headers = {'X-Yandex-API-Key': "097bf658-bf6b-445c-b0a3-6214d61b54d0"}
    response = requests.request("GET", url, headers=headers)
    a = json.loads(response.text)
    temp = (a.get('temp'))
    z = "Температура (°C):"
    current_datetime = datetime.now()
    rt = "Cейчас в Москве  !"
    feels_like = (a.get('feels_like'))
    b = "Ощущаемая температура (°C):"
    condition = (a.get('condition'))
    c = "Hебо:"
    ii = {'clear': '☀️', 'partly-cloudy': '🌤️', 'cloudy': '🌥️', 'overcast': '☁️', 'drizzle': '💧', ' light-rain': '☔️',
          'rain': '🌧️', 'moderate-rain': '🌧️🌧', ' heavy-rain ': '💧💧💧', 'showers': '💦',
          'continuous-heavy-rain': '🌧️🌬', 'wet-snow': '🌧️❄️', 'light-snow': '🌨️', 'snow': '❄️',
          'snow-showers': '❄️❄️️❄️', 'hail': '🧊',
          'thunderstorm': '⚡️', 'thunderstorm-with-rain': '⛈️', 'thunderstorm-with-hail': '⚡️🧊'}
    condition = (ii.get(condition))
    wind_speed = (a.get('wind_speed'))
    v = "Скорость ветра (в м/с):"
    pressure_mm = (a.get('pressure_mm'))
    d = "Давление (в мм рт. ст.).:"
    humidity = (a.get('humidity'))
    h = "Влажность воздуха %:"
    vet = "Направление ветра:"
    wind_dir = (a.get('wind_dir'))

    vet2 = {'nw': 'северо-западное', 'n': 'северное', 'ne': ' северо-восточное', 'e': 'восточное',
            'se': ' юго-восточное', 's': 'южное', 'sw': ' юго-западное', 'w': 'западное', 'c': 'штиль'}
    wind_dir3 = (vet2.get(wind_dir))

    await message.answer(
        f'{rt} \n {current_datetime} \n {z} {temp} \n {b} {feels_like} \n {c} {condition} \n {vet} {wind_dir3} \n {v} {wind_speed} \n {d} {pressure_mm} \n {h} {humidity}')


async def process_sochi_command(message: types.Message):
    url = "https://api.weather.yandex.ru/v2/fact?lat=43.58547592&lon=39.72309494&extra=true"
    headers = {'X-Yandex-API-Key': "097bf658-bf6b-445c-b0a3-6214d61b54d0"}
    response = requests.request("GET", url, headers=headers)
    a = json.loads(response.text)
    temp = (a.get('temp'))
    z = "Температура (°C):"
    current_datetime = datetime.now()
    rt = "Cейчас в Сочи  !"
    feels_like = (a.get('feels_like'))
    b = "Ощущаемая температура (°C):"
    condition = (a.get('condition'))
    c = "Hебо:"
    ii = {'clear': '☀️', 'partly-cloudy': '🌤️', 'cloudy': '🌥️', 'overcast': '☁️', 'drizzle': '💧', ' light-rain': '☔️',
          'rain': '🌧️', 'moderate-rain': '🌧️🌧', ' heavy-rain ': '💧💧💧', 'showers': '💦',
          'continuous-heavy-rain': '🌧️🌬', 'wet-snow': '🌧️❄️', 'light-snow': '🌨️', 'snow': '❄️',
          'snow-showers': '❄️❄️️❄️', 'hail': '🧊',
          'thunderstorm': '⚡️', 'thunderstorm-with-rain': '⛈️', 'thunderstorm-with-hail': '⚡️🧊'}
    condition = (ii.get(condition))
    wind_speed = (a.get('wind_speed'))
    v = "Скорость ветра (в м/с):"
    pressure_mm = (a.get('pressure_mm'))
    d = "Давление (в мм рт. ст.).:"
    humidity = (a.get('humidity'))
    h = "Влажность воздуха %:"
    vet = "Направление ветра:"
    wind_dir = (a.get('wind_dir'))

    vet2 = {'nw': 'северо-западное', 'n': 'северное', 'ne': ' северо-восточное', 'e': 'восточное',
            'se': ' юго-восточное', 's': 'южное', 'sw': ' юго-западное', 'w': 'западное', 'c': 'штиль'}
    wind_dir3 = (vet2.get(wind_dir))

    await message.answer(
        f'{rt} \n {current_datetime} \n {z} {temp} \n {b} {feels_like} \n {c} {condition} \n {vet} {wind_dir3} \n {v} {wind_speed} \n {d} {pressure_mm} \n {h} {humidity}')


async def process_makala_command(message: types.Message):
    url = "https://api.weather.yandex.ru/v2/forecast?lat=42.98310089&lon=47.5047493&extra=true"
    headers = {'X-Yandex-API-Key': "7f5c2cf9-0976-4e02-9c80-b99c47390c44"}
    response = requests.request("GET", url, headers=headers)
    a = json.loads(response.text)
    temp = (a.get('temp'))
    z = "Температура (°C):"
    current_datetime = datetime.now()
    rt = "Cейчас в Махачкале  !"
    feels_like = (a.get('feels_like'))
    b = "Ощущаемая температура (°C):"
    condition = (a.get('condition'))
    c = "Hебо:"
    ii = {'clear': '☀️', 'partly-cloudy': '🌤️', 'cloudy': '🌥️', 'overcast': '☁️', 'drizzle': '💧', ' light-rain': '☔️',
          'rain': '🌧️', 'moderate-rain': '🌧️🌧', ' heavy-rain ': '💧💧💧', 'showers': '💦',
          'continuous-heavy-rain': '🌧️🌬', 'wet-snow': '🌧️❄️', 'light-snow': '🌨️', 'snow': '❄️',
          'snow-showers': '❄️❄️️❄️', 'hail': '🧊',
          'thunderstorm': '⚡️', 'thunderstorm-with-rain': '⛈️', 'thunderstorm-with-hail': '⚡️🧊'}
    condition = (ii.get(condition))
    wind_speed = (a.get('wind_speed'))
    v = "Скорость ветра (в м/с):"
    pressure_mm = (a.get('pressure_mm'))
    d = "Давление (в мм рт. ст.).:"
    humidity = (a.get('humidity'))
    h = "Влажность воздуха %:"
    vet = "Направление ветра:"
    wind_dir = (a.get('wind_dir'))

    vet2 = {'nw': 'северо-западное', 'n': 'северное', 'ne': ' северо-восточное', 'e': 'восточное',
            'se': ' юго-восточное', 's': 'южное', 'sw': ' юго-западное', 'w': 'западное', 'c': 'штиль'}
    wind_dir3 = (vet2.get(wind_dir))

    await message.answer(
        f'{rt} \n {current_datetime} \n {z} {temp} \n {b} {feels_like} \n {c} {condition} \n {vet} {wind_dir3} \n {v} {wind_speed} \n {d} {pressure_mm} \n {h} {humidity}')
