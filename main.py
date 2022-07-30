import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

from save_and_load import load_json, save_json

load_dotenv()
TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    data = load_json()
    user_id = str(message.from_user.id)
    if user_id not in data:
        data[user_id] = 0
        save_json(data)
    await message.reply("Стартанули!!!")


@dp.message_handler()
async def counter(msg: types.Message):
    try:
        number = float(msg.text)
        data = load_json()
        user_id = str(msg.from_user.id)
        try:
            data[user_id] = round(number+data[user_id],2)
        except KeyError:
            data[user_id] = number
        save_json(data)
        await bot.send_message(msg.from_user.id, f'{data[user_id]:g}')
    except ValueError:
        await bot.send_message(msg.from_user.id, 'WTF? Число давай')


if __name__ == '__main__':
    executor.start_polling(dp)
