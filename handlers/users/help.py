from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import ParseMode

from data.config import admins
from data.texts import _
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = await _('commands')
    if message.from_user and message.from_user.id in admins:
        text.append("/today - bugun ro'yxatdan o'tganlar")
        text.append("/sendsms - hammaga habar jo'natish")

    await message.answer('\n'.join(text), parse_mode=ParseMode.MARKDOWN)


