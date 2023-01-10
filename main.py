import json
import dotenv
import os
import requests
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

dotenv.load_dotenv()
TOK = os.getenv("API_TOKEN")
# полученный у @BotFather
API_TOKEN: str = TOK
# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)




# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard2: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton('Москва')
button_2: KeyboardButton = KeyboardButton('Махачкала')
button_3: KeyboardButton = KeyboardButton('Ростов-на-Дону ')
button_5: KeyboardButton = KeyboardButton('Aктуальная погода сейчас')
button_6: KeyboardButton = KeyboardButton('Курс валют')
button_7: KeyboardButton = KeyboardButton('Факты о кошках [EN]')
button_8: KeyboardButton = KeyboardButton('Узнать IP адрес')
button_9: KeyboardButton = KeyboardButton('Новости Nasa [EN]')
button_10: KeyboardButton = KeyboardButton('Random dog')
button_11: KeyboardButton = KeyboardButton('Сочи')
button_12: KeyboardButton = KeyboardButton('Генератор оскорблений 18+')
button_13: KeyboardButton = KeyboardButton('Веб камеры Ростов-на-Дону')
# Добавляем кнопки в клавиатуру методом add
keyboard.add(button_1, button_2, button_11, button_3)
keyboard2.add(button_5, button_6, button_7, button_9, button_10, button_12,button_13)




# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: types.Message):
    await message.answer(
        'Привет! нажми на кнопку !!!👇', reply_markup=keyboard2)


async def process_dog_command(message: types.Message):
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    ui = json.loads(response.text)
    gav = (ui.get('message'))
    await message.answer(f'{gav}')


async def process_nassa_command(message: types.Message):
    url = "https://api.nasa.gov/planetary/apod?api_key=i7Zw44df1S9mgDvGc7ybK2OZMQGti2MniO4SnIM3"
    response = requests.request("GET", url)
    nassa = json.loads(response.text)
    text1 = (nassa.get('explanation'))
    url2 = (nassa.get('url'))
    await message.answer(f'{text1} {url2} ')


async def process_ip_command(message: types.Message):
    url = "http://ipwho.is/"
    response = requests.request("GET", url)
    a = json.loads(response.text)
    country = (a.get('country'))
    countryCode = (a.get('country_code'))
    regionName = (a.get('region'))
    city = (a.get('city'))
    zip = (a.get('postal'))
    lat = (a.get('latitude'))
    lon = (a.get('longitude'))
    ip = (a.get('ip'))
    con = "Страна:"
    reg = "Регион:"
    cit = "Город:"
    zi = "Почтовый индекс:"
    la = "Широта:"
    ln = "Долгота: "
    en = "Язык: "
    ip2 = "Ваш ip адрес:"
    await message.answer(
        f' {ip2}  {ip} \n {con} {country} \n {en} {countryCode} \n {reg} {regionName} \n {cit} {city} \n {zi} {zip} \n {la} {lat} \n {ln}{lon} \n ')


async def process_pogoda_command(message: types.Message):
    await message.answer('Выберите город! ', reply_markup=keyboard)


async def process_cat_command(message: types.Message):
    url = "https://catfact.ninja/fact"
    response = requests.request("GET", url)
    a = json.loads(response.text)
    temp = (a.get('fact'))
    await message.answer(f'{temp}')

# Создаем объект инлайн-клавиатуры
keyboard5: InlineKeyboardMarkup = InlineKeyboardMarkup()

# Создаем объекты инлайн-кнопок
url_button_1: InlineKeyboardButton = InlineKeyboardButton(
                                        text='Cтадион, левый берег"',
                                        url='https://webcams.windy.com/webcams/stream/1481608492?lookr.com:98556ab992b25aa05817ba65ce8c7bce:1673268752')
url_button_2: InlineKeyboardButton = InlineKeyboardButton(
                                        text='Соборный',
                                        url='https://webcams.windy.com/webcams/stream/1638727136')
url_button_3: InlineKeyboardButton = InlineKeyboardButton(
                                        text='Ворошиловский проспект',
                                        url='https://webcams.windy.com/webcams/stream/1658941999')
url_button_4: InlineKeyboardButton = InlineKeyboardButton(
                                        text='Набережная',
                                        url='https://webcams.windy.com/webcams/stream/1614560597')

# Добавляем кнопки в клавиатуру методом add
keyboard5.add(url_button_1).add(url_button_2).add(url_button_3).add(url_button_4)


async def process_cam_command(message: types.Message):
    await message.answer(
        text='Веб камеры online ',
        reply_markup=keyboard5)


async def process_mat_command(message: types.Message):
    url = "https://evilinsult.com/generate_insult.php?lang=ru&type=json"
    response = requests.get(url)
    a = json.loads(response.text)
    mat = (a.get('insult'))
    await message.answer(f'{mat}')


async def process_pnd_command(message: types.Message):
    url = "https://api.weather.yandex.ru/v2/fact?lat=47.222078&lon=39.720349&extra=true"
    headers = {'X-Yandex-API-Key': "c44361a5-54fe-400d-a65d-782c8fc66dcd"}
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
    headers = {'X-Yandex-API-Key': "c44361a5-54fe-400d-a65d-782c8fc66dcd"}
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
    headers = {'X-Yandex-API-Key': "c44361a5-54fe-400d-a65d-782c8fc66dcd"}
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
    url = "https://api.weather.yandex.ru/v2/fact?lat=42.98310089&lon=47.5047493&extra=true"
    headers = {'X-Yandex-API-Key': "c44361a5-54fe-400d-a65d-782c8fc66dcd"}
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


async def process_rub_command(message: types.Message):
    url = "https://api.apilayer.com/fixer/latest?symbols=RUB&base=USD"

    payload = {}
    headers = {
        "apikey": "aR3ra49CC7kwxyJXU3tQRJglPqL8eRLO"
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    rub = (response.text[127:139])
    t = "USD"
    iu = "Курс валют"

    url = "https://api.apilayer.com/fixer/latest?symbols=RUB&base=EUR"

    payload = {}
    headers = {
        "apikey": "aR3ra49CC7kwxyJXU3tQRJglPqL8eRLO"
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    eur = (response.text[127:139])
    eur1 = "EUR"
    url = "https://api.apilayer.com/fixer/latest?symbols=RUB&base=CNY"

    payload = {}
    headers = {
        "apikey": "aR3ra49CC7kwxyJXU3tQRJglPqL8eRLO"
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    CNY = (response.text[127:139])
    CNY1 = "CNY"
    info = "Fixer.io - Данные об обменных курсах 170 мировых валют в режиме реального времени, обновляются каждые 60 секунд.  Данные о валютах, представляемых Fixer, поступают от поставщиков финансовых данных и банков, включая Европейский центральный банк."
    await message.answer(f'{iu}\n  {t}:{rub}{eur1}:{eur}{CNY1}:{CNY}\n{info}')


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения, кроме команд "/start" и "/help"
async def send_echo(message: types.Message):
    await message.reply("Bы ввели неверную команду, воспользуйтесь меню \nили отправьте пожалуйста / start")


# Регистрируем хэндлеры
dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_pogoda_command, text='Aктуальная погода сейчас')
dp.register_message_handler(process_pnd_command, text='Ростов-на-Дону')
dp.register_message_handler(process_sochi_command, text='Сочи')
dp.register_message_handler(process_moscow_command, text='Москва')
dp.register_message_handler(process_makala_command, text='Махачкала')
dp.register_message_handler(process_rub_command, text='Курс валют')
dp.register_message_handler(process_cat_command, text='Факты о кошках [EN]')
dp.register_message_handler(process_ip_command, text='Узнать IP адрес')
dp.register_message_handler(process_nassa_command, text='Новости Nasa [EN]')
dp.register_message_handler(process_dog_command, text='Random dog')
dp.register_message_handler(process_mat_command, text='Генератор оскорблений 18+')
dp.register_message_handler(process_cam_command, text='Веб камеры Ростов-на-Дону')
dp.register_message_handler(send_echo)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
