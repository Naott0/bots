import os
from aiogram import types
from aiogram.bot import bot

AUDIO_URL = 'http://muzmo.ru/get/music/20140507/muzmo_ru_Metallica_-_Metalica_Fuel_12710830.mp3?sid=3ip4uccps4mp3ljt2viipsqcep'
AUDIO_URL2 = 'https://mp3muza.com/music/metallica/#'
AUDIO_V_ROCK = os.path.expanduser('/home/support/TelegramBot/bots/audio/GTA_Vice_City_Radio_-_V-ROCK.mp3')
AUDIO_FLASH = os.path.expanduser('Flash_FM.mp3')
JPG = open('/home/support/TelegramBot/bots/audio/1.jpeg', 'rb')
FUEL = open('/home/support/TelegramBot/bots/audio/fuel.jpg', 'rb')

async def process_gta_v_rock_command(message: types.Message):
    audio = types.InputFile(AUDIO_V_ROCK)
    await message.answer_photo(JPG)
    await message.answer_audio(audio, performer='GTA vice city', title='V-Rock Redio')

async def process_flash_fm_command(message: types.Message):
    audio = types.InputFile(AUDIO_FLASH)
    # await message.answer_photo(JPG)
    await message.answer_audio(audio, performer='GTA vice city', title='Flash-FM')
async def process_metallica_command(message: types.Message):
    await message.answer_photo(FUEL)
    await message.answer_audio(AUDIO_URL, performer='Foo', title='Bar')
