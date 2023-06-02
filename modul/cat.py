import json
import requests
from aiogram import types


async def process_cat_command(message: types.Message):
    url = "https://catfact.ninja/fact"
    response = requests.request("GET", url)
    a = json.loads(response.text)
    temp = (a.get('fact'))
    await message.answer(f'{temp}')
