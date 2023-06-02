from aiogram import types
from bots.modul import keyboards


async def process_audio_command(message: types.Message):
    await message.answer(
        text='Подкасты, музыка и многое другое\n(beta version)',
        reply_markup=keyboards.keyboard3)
async def process_gta_command(message: types.Message):
    await message.answer(
        text='Выбери радио !',
        reply_markup=keyboards.keyboard5)