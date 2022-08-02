import re

from aiogram import types

from main import dp
from save_and_load import load_json, save_json, make_sum


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
async def reset(msg: types.Message):
    data = load_json()
    data[str(msg.chat.id)] = 0
    save_json(data)
    await msg.reply('Сброс')


@dp.message_handler(regexp=re.compile(r'(^|\s)\d+\u20BD', re.IGNORECASE))
async def counter(msg: types.Message, regexp: re.match):
    number = int(regexp[0][:-1])
    chat_sum = make_sum(msg.chat.id, number)
    await msg.answer(f"Сумма: *{chat_sum}*", parse_mode="MarkdownV2")
