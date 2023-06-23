import json

import requests
from aiogram import types


async def process_dog_command(message: types.Message):
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    ui = json.loads(response.text)
    gav = (ui.get('message'))
    await message.answer_photo(gav)
