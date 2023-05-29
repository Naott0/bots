from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def process_cam_command(message: types.Message):
    await message.answer(text='Это инлайн-кнопки с параметром "url"',
                         reply_markup=keyboard4)


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
# Создаем объект инлайн-клавиатуры
keyboard4: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1], [url_button_2], [url_button_3], [url_button_4]])
