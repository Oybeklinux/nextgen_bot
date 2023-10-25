from aiogram import types

from keyboards import get_main_kb
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(message.text, reply_markup=await get_main_kb())
