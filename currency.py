
import requests
from aiogram import types


async def process_rub_command(message: types.Message):
    url = "https://api.apilayer.com/fixer/latest?symbols=RUB&base=USD"

    payload = {}
    headers = {
        "apikey": "aR3ra49CC7kwxyJXU3tQRJglPqL8eRLO"
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    rub = (response.text[127:139])
    t = "USD"
    iu = "Курс валют на данный момент:"

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
    info = "Fixer.io - Данные об обменных курсах 170 мировых валют в режиме реального времени, обновляются каждые 60 " \
           "секунд.  Данные о валютах, представляемых Fixer, поступают от поставщиков финансовых данных и банков, " \
           "включая Европейский центральный банк."
    await message.answer(f'{iu}\n  {t}: {rub}{eur1}: {eur}{CNY1}: {CNY}\n{info}')
