from aiogram import types

from bots import keyboards


async def process_audio_command(message: types.Message):
    await message.answer(
        text='Подкасты, музыка и многое другое',
        reply_markup=keyboards.keyboard3)