import os

from aiogram import types

AUDIO_URL = 'http://muzmo.ru/get/music/20140507/muzmo_ru_Metallica_-_Metalica_Fuel_12710830.mp3?sid=3ip4uccps4mp3ljt2viipsqcep'
AUDIO_PATH = os.path.expanduser('GTA_Vice_City_Radio_-_V-ROCK.mp3')


async def process_gta_v_rock_command(message: types.Message):
    audio = types.InputFile(AUDIO_PATH)
    await message.answer_audio(audio, performer='GTA vice city', title='V-Rock Redio')


async def process_metallica_command(message: types.Message):
    await message.answer_audio(AUDIO_URL, performer='Foo', title='Bar')
