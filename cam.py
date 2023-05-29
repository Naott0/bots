from aiogram import types
from bots import keyboards


# async def process_cam_command(message: types.Message):
#     await message.answer(
#         text='Веб камеры online ',
#         reply_markup=keyboards.keyboard4)
async def process_cam_command(message: types.Message):
    await message.answer(text='Это инлайн-кнопки с параметром "url"',
                         reply_markup=keyboards.keyboard4)