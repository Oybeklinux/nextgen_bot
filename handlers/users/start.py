from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from handlers.users.course import send_main_menu
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')
    await send_main_menu(message)

