import os
from aiogram import types


AUDIO_URL = 'http://muzmo.ru/get/music/20140507/muzmo_ru_Metallica_-_Metalica_Fuel_12710830.mp3?sid=3ip4uccps4mp3ljt2viipsqcep'
AUDIO_URL2 = 'https://mp3muza.com/music/metallica/#'
AUDIO_V_ROCK = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/GTA_Vice_City/V_ROCK/GTA_Vice_City_Radio_-_V-ROCK.mp3')
AUDIO_FLASH1 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/GTA_Vice_City/FLASH_FM/Flash FM part_1.mp3')
AUDIO_FLASH2 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/GTA_Vice_City/FLASH_FM/Flash FM part_2.mp3')
AUDIO_FLASH3= os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/GTA_Vice_City/FLASH_FM/Flash FM part_3.mp3')
AUDIO_WAVE1= os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/GTA_Vice_City/Wave 103/GTA Vice City Wave 103 part_1.mp3')
AUDIO_WAVE2= os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/GTA_Vice_City/Wave 103/GTA Vice City Wave 103 part_2.mp3')
AUDIO_WAVE3= os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/GTA_Vice_City/Wave 103/GTA Vice City Wave 103 part_3.mp3')
AUDIO_WAVE4= os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/GTA_Vice_City/Wave 103/GTA Vice City Wave 103 part_4.mp3')
METALLICA1 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/Metallica/Metallica - 72 Seasons/01 - Metallica - 72 Seasons.mp3')
METALLICA2 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/Metallica/Metallica - 72 Seasons/02 - Metallica - Shadows Follow.mp3')
METALLICA3 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/Metallica/Metallica - 72 Seasons/03 - Metallica - Screaming Suicide.mp3')
METALLICA4 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/Metallica/Metallica - 72 Seasons/04 - Metallica - Sleepwalk My Life Away.mp3')
METALLICA5 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/Metallica/Metallica - 72 Seasons/05 - Metallica - You Must Burn!.mp3')
METALLICA6 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/Metallica/Metallica - 72 Seasons/06 - Metallica - Lux Æterna.mp3')
METALLICA7 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/Metallica/Metallica - 72 Seasons/07 - Metallica - Crown of Barbed Wire.mp3')
METALLICA8 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/Metallica/Metallica - 72 Seasons/08 - Metallica - Chasing Light.mp3')
METALLICA9 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/Metallica/Metallica - 72 Seasons/09 - Metallica - If Darkness Had a Son.mp3')
METALLICA10 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/Metallica/Metallica - 72 Seasons/10 - Metallica - Too Far Gone-.mp3')
METALLICA11 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/Metallica/Metallica - 72 Seasons/11 - Metallica - Room of Mirrors.mp3')
METALLICA12 = os.path.expanduser(
    '/home/support/TelegramBot/Project/Bots/audio/Metallica/Metallica - 72 Seasons/12 - Metallica - Inamorata.mp3')

#
# FUEL = open('/Project/audio/fuel.jpg', 'rb')




async def process_gta_v_rock_command(message: types.Message):
    audio = types.InputFile(AUDIO_V_ROCK)
    VROCK = open('/home/support/TelegramBot/Project/Bots/audio/GTA_Vice_City/V_ROCK/1.jpeg', 'rb')
    await message.answer_photo(VROCK)
    await message.answer_audio(audio, performer='GTA vice city', title='V-Rock Redio')



async def process_flash_fm_command(message: types.Message):
    audio1 = types.InputFile(AUDIO_FLASH1)
    audio2 = types.InputFile(AUDIO_FLASH2)
    audio3 = types.InputFile(AUDIO_FLASH3)
    FLASH = open('/home/support/TelegramBot/Project/Bots/audio/GTA_Vice_City/FLASH_FM/1.jpg', 'rb')
    await message.answer_photo(FLASH)
    await message.answer_audio(audio3, performer='GTA vice city part 1', title='Flash-FM')
    await message.answer_audio(audio2, performer='GTA vice city part 2', title='Flash-FM')
    await message.answer_audio(audio1, performer='GTA vice city part 3', title='Flash-FM')

async def process_wave_command(message: types.Message):
    audio1 = types.InputFile(AUDIO_WAVE1)
    audio2 = types.InputFile(AUDIO_WAVE2)
    audio3 = types.InputFile(AUDIO_WAVE3)
    audio4 = types.InputFile(AUDIO_WAVE4)
    WAVE = open('/home/support/TelegramBot/Project/Bots/audio/GTA_Vice_City/Wave 103/1_.jpg', 'rb')
    await message.answer_photo(WAVE)
    await message.answer_audio(audio1, performer='GTA vice city part 1', title='Wave-103-FM')
    await message.answer_audio(audio2, performer='GTA vice city part 2', title='Wave-103-FM')
    await message.answer_audio(audio3, performer='GTA vice city part 3', title='Wave-103-FM')
    await message.answer_audio(audio4, performer='GTA vice city part 4', title='Wave-103-FM')

async def process_metallica_command(message: types.Message):
    audio = types.InputFile(METALLICA1)
    M72 = open('/home/support/TelegramBot/Project/Bots/audio/Metallica/Metallica - 72 Seasons/cover.jpg', 'rb')
    await message.answer_photo(M72)
    await message.answer_audio(audio)
    audio1 = types.InputFile(METALLICA2)
    await message.answer_audio(audio1)
    audio3 = types.InputFile(METALLICA3)
    await message.answer_audio(audio3)
    audio4 = types.InputFile(METALLICA4)
    await message.answer_audio(audio4)
    audio5 = types.InputFile(METALLICA5)
    await message.answer_audio(audio5)
    audio6 = types.InputFile(METALLICA6)
    await message.answer_audio(audio6)
    audio7 = types.InputFile(METALLICA7)
    await message.answer_audio(audio7)
    audio8 = types.InputFile(METALLICA8)
    await message.answer_audio(audio8)
    audio9 = types.InputFile(METALLICA9)
    await message.answer_audio(audio9)
    audio10 = types.InputFile(METALLICA10)
    await message.answer_audio(audio10)
    audio11 = types.InputFile(METALLICA11)
    await message.answer_audio(audio11)
    audio12 = types.InputFile(METALLICA12)
    await message.answer_audio(audio12)
