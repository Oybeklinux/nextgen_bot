import json

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from cleantext import clean

from data.config import TG_URL, TG_LOGIN, TG_PASSWORD
from filters import IsAdmin
from loader import dp, db


async def send_sms(data):

    data = {
        "login": TG_LOGIN,
        "password": TG_PASSWORD,
        "data": data
    }
    try:
        result = requests.post(url=TG_URL, json=data)
        return result
    except Exception as error:
        return f'{error.args}'


@dp.message_handler(Command('send_sms'), IsAdmin())
async def send_sms_command(message: types.Message, state: FSMContext):
    await message.answer(text='SMS matnini yozing. Diqqat!!!\n Smayliklar, havolalar jo\'natish mumkin emas.\n\n'
                              'Shablonda #name deb yozsangiz ism bilan almashtiriladi')
    await state.set_state('write_sms')


@dp.message_handler(state='write_sms')
async def send_sms_(message: types.Message, state: FSMContext):
    text = message.text
    text = clean(text, no_line_breaks=True, no_urls=True, no_emoji=True)

    rows = await db.select_all_users()
    await state.finish()

    user_datas = []
    for row in rows:
        if row['group_name'] != 'worker' and row['phone'] and row['name']:
            mes = text.replace('#name', row['name'])
            user_datas.append({"phone": row['phone'].replace("+",''), "text": mes})

    data = json.dumps(user_datas)
    result = await send_sms(data)
    if result.status_code == 403:
        await message.answer(text="Sizning IP manzilingizdan SMS yuborishga ruhsat yo'q")
    else:
        receivers = json.loads(result.text)
        receivers_res = []
        for receiver in receivers:
            error_mes = receiver['error_text'] if 'error_text' in receiver else '✅'
            receivers_res.append(f"{receiver['recipient']}: {error_mes}")
        mes = '\n'.join(receivers_res)
        await message.answer(text=f"{mes}\nOdamlar soni: {len(user_datas)}")
