import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data import start_text
from handlers.users.course import send_main_menu
from keyboards import language_ikb, main_kb
from loader import dp, db
from states.regstration import RegisterStates


@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    try:
        db.add_user(id=user_id, name=message.from_user.full_name)
    except sqlite3.IntegrityError:
        pass
    if not db.is_user_registered(user_id):
        await message.answer(f'{start_text.replace("full_name", message.from_user.full_name)}',
                         reply_markup=language_ikb)
    else:
        await message.answer('Вы успешно зарегистрированы', reply_markup=main_kb)

