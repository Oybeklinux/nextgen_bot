from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandSettings
from aiogram.types import ParseMode

from data.texts import Texts
from filters.is_in import IsIn
from keyboards import language_ikb, language_cb, get_phone_kb, get_main_kb
from keyboards.default.settings import get_settings_kb
from loader import dp, db
from utils.set_bot_commands import set_default_commands


@dp.message_handler(CommandSettings())
@dp.message_handler(IsIn('bsettings'))
async def show_settings(message: types.Message):
    await message.answer('Выберите пункт', reply_markup=get_settings_kb())


@dp.message_handler(IsIn('bedit_name'))
async def edit_name(message: types.Message, state:FSMContext):
    await message.answer(text=Texts().get('tinput_name'), reply_markup=get_settings_kb())
    await state.set_state('edit_name')


@dp.message_handler(IsIn('bedit_lang'))
async def edit_language(message: types.Message, state: FSMContext):
    text = "Выберите язык"
    await message.answer(f'{text}', reply_markup=language_ikb)
    await state.set_state('edit_languge')



@dp.message_handler(IsIn('bsend_phone'))
async def edit_phone(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(Texts.get('bsend_phone'),
                         reply_markup=get_phone_kb(), parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(state='edit_name')
async def name_to_settings(message: types.Message, state: FSMContext):
    name = message.text
    db.update_user(id=message.from_user.id, name=name)
    text = Texts.get('name_changed')
    await message.answer(text=text, reply_markup=get_settings_kb())
    await state.finish()


@dp.callback_query_handler(language_cb.filter(), state='edit_languge')
async def lang_to_settings(callback: types.CallbackQuery, state: FSMContext) -> None:
    language = language_cb.parse(callback.data)['language']
    db.update_user(id=callback.from_user.id, language=language)

    text = Texts.get('lang_changed')
    await set_default_commands(dp)
    await callback.message.answer(text=text, reply_markup=get_settings_kb())
    await state.finish()


@dp.message_handler(IsIn('bto_main'))
async def back_to_main(message: types.Message):
    await message.answer(text=Texts.get('tmain_menu'), reply_markup=get_main_kb())

