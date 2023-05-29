from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard2: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
keyboard3: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# Создаем объекты кнопок
# button_1: KeyboardButton = KeyboardButton('Москва')
# button_2: KeyboardButton = KeyboardButton('Махачкала')
# button_3: KeyboardButton = KeyboardButton('Ростов-на-Дону ')
# button_5: KeyboardButton = KeyboardButton('Aктуальная погода сейчас')
button_6: KeyboardButton = KeyboardButton('Курс валют')
button_7: KeyboardButton = KeyboardButton('Факты о кошках [EN]')
button_8: KeyboardButton = KeyboardButton('Узнать IP адрес')
button_9: KeyboardButton = KeyboardButton('Новости Nasa [EN]')
button_10: KeyboardButton = KeyboardButton('Random dog')
# button_11: KeyboardButton = KeyboardButton('Сочи')
button_12: KeyboardButton = KeyboardButton('Генератор оскорблений 18+')
button_13: KeyboardButton = KeyboardButton('Веб камеры Ростов-на-Дону')
button_14: KeyboardButton = KeyboardButton('Audio')
button_15: KeyboardButton = KeyboardButton('Metallica')
button_16: KeyboardButton = KeyboardButton('GTA Vice City Radio')

# Создаем объекты инлайн-кнопок
url_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Cтадион, левый берег',
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
# keyboard.add(button_1, button_2, button_11, button_3)
keyboard2.add(button_6, button_7, button_9, button_10, button_12, button_13, button_14)
keyboard3.add(button_15, button_16)

# Создаем объект инлайн-клавиатуры
keyboard4: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],
                     [url_button_2], [url_button_3], [url_button_4]])


