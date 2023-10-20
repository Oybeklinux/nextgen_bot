from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import User

from data import config
from utils.db_api.sqlite import Database
from utils.db_api.postgresql import Database as PostgreSQL

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()
# postgresql = PostgreSQL()
