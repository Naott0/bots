import json

import requests
from aiogram import types
async def process_nassa_command(message: types.Message):
    url = "https://api.nasa.gov/planetary/apod?api_key=i7Zw44df1S9mgDvGc7ybK2OZMQGti2MniO4SnIM3"
    response = requests.request("GET", url)
    nassa = json.loads(response.text)
    text1 = (nassa.get('explanation'))
    url2 = (nassa.get('url'))
    await message.answer(f'{text1} {url2} ')