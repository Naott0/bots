import dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
from bots import cam, dog, cat, nassa, currency, mat, audio, music
from bots.keyboards import keyboard2

dotenv.load_dotenv()
TOK = os.getenv("API_TOKEN")
# полученный у @BotFather
API_TOKEN: str = TOK
# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: types.Message):
    await message.answer(
        'Привет! нажми на кнопку !!!👇', reply_markup=keyboard2)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения, кроме команд "/start" и "/help"
async def send_echo(message: types.Message):
    await message.reply("Bы ввели неверную команду, воспользуйтесь меню \nили отправьте пожалуйста /start")


# https://www.youtube.com/watch?v=ORMED692Ma8
# https://hits.gybka.com/artist/6573287-Gta_Vice_City_Radio/

# Регистрируем хэндлеры
dp.register_message_handler(process_start_command, commands='start')
# dp.register_message_handler(process_pogoda_command, text='Aктуальная погода сейчас')
# dp.register_message_handler(process_pnd_command, text='Ростов-на-Дону')
# dp.register_message_handler(process_sochi_command, text='Сочи')
# dp.register_message_handler(process_moscow_command, text='Москва')
# dp.register_message_handler(process_makala_command, text='Махачкала')
dp.register_message_handler(currency.process_rub_command, text='Курс валют')
dp.register_message_handler(cat.process_cat_command, text='Факты о кошках [EN]')
dp.register_message_handler(nassa.process_nassa_command, text='Новости Nasa [EN]')
dp.register_message_handler(dog.process_dog_command, text='Random dog')
dp.register_message_handler(mat.process_mat_command, text='Генератор оскорблений 18+')
dp.register_message_handler(cam.process_cam_command, text='Веб камеры Ростов-на-Дону')
dp.register_message_handler(audio.process_audio_command, text='Audio')
dp.register_message_handler(music.process_metallica_command, text='Metallica')
dp.register_message_handler(audio.process_gta_command, text='GTA Vice City Radio')
dp.register_message_handler(music.process_gta_v_rock_command, text='V-ROCK')
dp.register_message_handler(music.process_flash_fm_command, text='Flash-FM')
dp.register_message_handler(send_echo)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
