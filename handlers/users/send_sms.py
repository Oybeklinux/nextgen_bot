import json

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

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
    await message.answer(text='SMS matnini yozing. Shablonda #name deb yozsangiz ism bilan almashtiriladi')
    await state.set_state('write_sms')


@dp.message_handler(state='write_sms')
async def send_sms_(message: types.Message, state: FSMContext):
    text = message.text
    rows = await db.select_all_users()
    await state.finish()
#     text = """Assalomu alaykum, #name
# Bugungi tadbirimizga kelganingizdan hursand bo'ldik 😊. O'ylaymanki Pythonda 🐍 qanday qilib SMS ✉️ yuborishni bilib oldingiz.
#
# Kelgusi haftada "Pythonda yuzni tan olish (Face recognition)" mavzusi haqida bo'lib o'tadi. Biz bilan aloqada 🧑‍💻bo'ling va qiziqqanlarga ham yetkazishni unutmang
#
# NextGen Academy xalqaro o'quv markazi (https://t.me/NextGenAcademy_bo)"""
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


@dp.message_handler(Command('send_sms'))
async def send_sms_command(message: types.Message, state: FSMContext):
    await message.answer(text='Tanishingizni telefon raqamini kiriting')
    await state.set_state('write_sms_to_friend')


@dp.message_handler(state='write_sms_to_friend')
async def send_sms_(message: types.Message, state: FSMContext):
    if type(message) is types.Contact:
        phone = message.contact.phone_number
    else:
        phone = message.text.replace('+', '').replace(' ','').replace('-','')
        if len(phone) == 9:
            phone += '998'
        elif len(phone) != 12:
            await message.answer(text="Telefon raqami formati 998xxxxxxxxx bo'lishi kerak")

    await state.finish()
    text = """Assalomu alaykum. 
Sizni tanishingiz #name kelgusi haftada "Pythonda yuzni tan olish (Face recognition)" mavzusi haqida bo'lib o'tadigan tadbirga taklif qiladi. 

Tadbir NextGen Academy xalqaro o'quv markazida bo'ladi. To'liqroq ma'lumotni botimizdan olsangiz bo'ladi (https://t.me/NextGenAcademy_bot)"""
    text = text.replace('#name', message.from_user.full_name)
    data = [{"phone": phone, "text": text}]
    data = json.dumps(data)
    result = await send_sms(data)
    if result.status_code == 403:
        await message.answer(text='Kechirasiz xatolik yuz berdi')
    else:
        await message.answer(text=f"Xabar yuborildi. Rahmat")