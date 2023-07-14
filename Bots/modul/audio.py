from aiogram import types
from Project.Bots.modul import keyboards


async def process_audio_command(message: types.Message):
    await message.answer(
        text='Подкасты, музыка и многое другое\n(beta version)',
        reply_markup=keyboards.keyboard3)
async def process_gta_command(message: types.Message):
    await message.answer(
        text='Выбери радиостанцию!',
        reply_markup=keyboards.keyboard5)