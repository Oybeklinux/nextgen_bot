from datetime import date

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode

from filters import IsAdmin
from loader import dp, db


@dp.message_handler(Command('today'), IsAdmin())
async def send_sms_command(message: types.Message):
    users = await db.select_users_by_date(date.today())

    text = f"Bugun ro'yxatdan o'tganlar ({len(users)}):"
    text += f"\n{'ID'.center(12)} | {'name'.center(14)} | 🏆 "
    for user in users:
        if user['name'] and user['phone']:
            is_winner = '🏆' if user['is_winner'] else ''
            text += f"\n{str(user['id']).center(12)} | {user['name'][:12].center(14)} | {is_winner} "
    await message.answer(text=f'<code>{text}</code>')


@dp.message_handler(Command('all'), IsAdmin())
async def send_sms_command(message: types.Message):
    users_number = await db.number_of_users()
    text = f"Hamma ro'yxatdan o'tganlar {users_number} ta:"
    print(text)
    await message.answer(text=text)


@dp.message_handler(Command('stat'), IsAdmin())
async def send_sms_command(message: types.Message):
    all_users_count = await db.number_of_users()
    participants_count = await db.number_of_users()
    users_without_phone = await db.number_of_users(phone=None)
    users_without_name = await db.number_of_users(name=None)
    text = f"Hamma ro'yxatdan o'tganlar <b>{all_users_count}</b> ta. Shulardan:\n"
    text += f" - tanlovda qatnashganlar <b>{participants_count}</b>\n"
    text += f" - telefon raqam jo'natmaganlar <b>{users_without_phone}</b>\n"
    text += f" - ismini yozmaganlar <b>{users_without_name}</b>"
    await message.answer(text=text, parse_mode=ParseMode.HTML)
