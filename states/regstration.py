from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterStates(StatesGroup):
    start = State()
    language = State()
    phone = State()
    name = State()