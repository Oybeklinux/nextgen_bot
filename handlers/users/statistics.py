from datetime import date

from aiogram import types
from aiogram.dispatcher.filters import Command

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
