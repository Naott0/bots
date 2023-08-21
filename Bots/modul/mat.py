import json
import requests
from aiogram import types


async def process_mat_command(message: types.Message):
    url = "https://evilinsult.com/generate_insult.php?lang=ru&type=json"
    response = requests.get(url)
    a = json.loads(response.text)
    mat = (a.get('insult'))
    await message.answer(f'{mat}')
