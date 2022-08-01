from aiogram import types
from aiogram.dispatcher import filters

from main import dp, bot
from save_and_load import load_json, save_json


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    data = load_json()
    user_id = str(message.from_user.id)
    if user_id not in data:
        data[user_id] = 0
        save_json(data)
    await message.reply("Стартанули!!!\n"
                        "Кстати /reset всё сбросит")


@dp.message_handler(commands=['reset'])
async def reset(message: types.Message):
    data = load_json()
    user_id = str(message.from_user.id)
    data[user_id] = 0
    save_json(data)
    await message.reply(str(data[user_id]))


@dp.message_handler(filters.Text(endswith='₽'))
async def counter(msg: types.Message):
    try:
        number = float(msg.text.rstrip('₽'))
        data = load_json()
        user_id = str(msg.from_user.id)
        try:
            data[user_id] = round(number + data[user_id], 2)
        except KeyError:
            data[user_id] = number
        save_json(data)
        await bot.send_message(msg.from_user.id,
                               f"Сумма: *{str(data[user_id]).rstrip('0').rstrip('.')}*",
                               parse_mode="MarkdownV2")
    except ValueError:
        await not_recognised()


@dp.message_handler()
async def not_recognised(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Принимаю только рубли.')