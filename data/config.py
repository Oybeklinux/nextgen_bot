import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [
    57018741
]

managers = [
    57018741, 1173655735
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
TG_URL = os.getenv("TG_URL")
TG_LOGIN = os.getenv("TG_LOGIN")
TG_PASSWORD = os.getenv("TG_PASSWORD")