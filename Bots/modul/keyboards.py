from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard2: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
keyboard3: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard5: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# Создаем объекты кнопок
button_6: KeyboardButton = KeyboardButton('Курс валют')
button_7: KeyboardButton = KeyboardButton('Факты о кошках [EN]')
button_8: KeyboardButton = KeyboardButton('Узнать IP адрес')
button_9: KeyboardButton = KeyboardButton('Новости Nasa [EN]')
button_10: KeyboardButton = KeyboardButton('Random dog')
button_12: KeyboardButton = KeyboardButton('Генератор оскорблений 18+')
button_13: KeyboardButton = KeyboardButton('Веб камеры Ростов-на-Дону')
button_14: KeyboardButton = KeyboardButton('Audio')
button_15: KeyboardButton = KeyboardButton('Metallica')
button_16: KeyboardButton = KeyboardButton('GTA Vice City Radio')
button_17: KeyboardButton = KeyboardButton('Flash-FM')
button_18: KeyboardButton = KeyboardButton('V-ROCK')

# Добавляем кнопки в клавиатуру методом add
keyboard2.add(button_6, button_7, button_9, button_10, button_12, button_13, button_14)
keyboard3.add(button_15, button_16)
keyboard5.add(button_17, button_18)


# button_1: KeyboardButton = KeyboardButton('Москва')
# button_2: KeyboardButton = KeyboardButton('Махачкала')
# button_3: KeyboardButton = KeyboardButton('Ростов-на-Дону ')
# button_5: KeyboardButton = KeyboardButton('Aктуальная погода сейчас')
# button_11: KeyboardButton = KeyboardButton('Сочи')
# keyboard.add(button_1, button_2, button_11, button_3)