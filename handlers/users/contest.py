import logging

from aiogram import types
from aiogram.types import ParseMode
from aiogram.utils.exceptions import Unauthorized

from data.texts import _
from filters.is_in import IsIn
from keyboards import get_main_kb
from loader import dp, db, bot


@dp.message_handler(IsIn('bсontest'))
async def participate_in_contest(message: types.Message):
    if not await db.is_contest_started():
        await message.answer(text=await _("wait_contest"), reply_markup=await get_main_kb(),
                             parse_mode=ParseMode.MARKDOWN)
        return

    if await db.is_contest_winner():
        await message.answer(text=await _("participating_not_allowed"), reply_markup=await get_main_kb())
        return

    num = message.from_user.id
    await db.start_user_contest()
    text = await _("mcontenst_number")
    text = text.replace('#number', str(num))
    await message.answer(text=text, reply_markup=await get_main_kb())


@dp.message_handler(IsIn('random_choice'))
async def random_choice(message: types.Message):
    row = await db.select_random_user()
    if not row:
        await message.answer(text=await _("no_participants"))
        return
    text = await _("show_winner")
    text = text.replace("#id", str(row['id'])).replace("#name", row['name'])

    await send_all_users(text, message)
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(IsIn('bсontest_users'))
async def contest_users(message: types.Message):
    rows = await db.contest_participants()

    if not rows:
        await message.answer(text=await _("no_participants"))
        return

    text = f'Tanlovda qatnashuvchilar {len(rows)}:'

    for user in rows:
        if user['name'] and user['phone']:
            is_winner = '🏆' if user['is_winner'] else ''
            text += f"\n{str(user['id']).center(12)} | {user['name'][:12].center(14)} | {is_winner}"
    await message.answer(text=f'<code>{text}</code>')


async def send_all_users(text, message:types.Message):
    users = await db.contest_participants()
    logging.info(f"BEGIN: Sending message to all: {text}")
    for user in users:

        try:
            await bot.send_message(chat_id=user['id'], text=text,
                               parse_mode=ParseMode.MARKDOWN)
            logging.info(f"{user['id']} {user['name']}")
        except Unauthorized:
            await message.answer(text=f"{user['id']} {user['name']} blocked the bot")
            logging.info(f"{user['id']} {user['name']} blocked the bot")

    users = await db.select_users_by_group('worker')
    for user in users:

        try:
            await bot.send_message(chat_id=user['id'], text=text,
                               parse_mode=ParseMode.MARKDOWN)
            logging.info(f"{user['id']} {user['name']}")
        except Unauthorized:
            await message.answer(text=f"{user['id']} {user['name']} blocked the bot")
            logging.info(f"{user['id']} {user['name']} blocked the bot")

    logging.info(f"END: Sending message to all: {text}")


@dp.message_handler(IsIn('bstart'))
async def start_contest(message: types.Message):

    await db.start_contest()
    text = await _("contest_started")
    await message.reply(text=text)


@dp.message_handler(IsIn('bstop'))
async def stop_contest(message: types.Message):
    await db.stop_contest()
    text = await _("contest_stopped")
    await send_all_users(text, message)
    await message.reply(text=text)