from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from asyncpg import UniqueViolationError

from data.texts import _
from keyboards import language_ikb, get_main_kb
from loader import dp, db


@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message):
    user_id = message.from_user.id

    try:
        await db.add_user(id=user_id, name=message.from_user.full_name)
    except UniqueViolationError:
        pass
    user = await db.select_user(id=user_id)
    name = user[1]
    text = (
        "🇺🇿 Assalomu alaykum #full_name 👋! Men NextGen Academy botiman.\n"
        "Ro'yxatdan o'tish uchun tilingizni tanlang\n\n"
        "🇷🇺 Привет, #full_name 👋! Я бот Академии NextGen.\n"
        "Выберите язык для регистрации\n\n"
        "🇬🇧 Hello #full_name 👋! I'm a NextGen Academy bot.\n"
        "Select your language to sign up\n\n"
    ).replace("#full_name", name)

    if not await db.is_user_registered(user_id):
        # text += "Для регистрации выберите пожалуйста свой язык"
        await message.answer(f'{text}', reply_markup=language_ikb)
    else:
        # text = Texts().get("start").replace("full_name", message.from_user.full_name)
        await message.answer(await _('tmain_menu'), reply_markup=await get_main_kb())

