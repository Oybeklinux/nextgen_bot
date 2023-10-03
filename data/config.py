import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [
    57018741
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

main_text = f"""👋 Привет #full_name! Я бот NextGen Academy. Я здесь, чтобы помочь тебе с твоим обучением. 🤓
В данном боте вы можете получить всю подробную информацию о наших курсах, ознакомиться с каждым направлением по отдельности и узнать об анонсах ближайших бесплатных мероприятий. 🌟

Наш бот позволяет связаться с менеджерами для получения бесплатной онлайн-консультации по выбору направления. 

Наши курсы:
💻 ВЕБ ПРОГРАММИРОВАНИЕ. Создание сайтов и веб-приложений.
 🐍 PYTHON. Создание Telegram ботов, онлайн-магазинов и веб-приложений.
📱 ANDROID & IOS РАЗРАБОТКА. Разработка приложений под различные операционные системы.

Чтобы помочь вам выбрать подходящий курс, мы проводим бесплатные открытые уроки, где вы узнаете о программе обучения, познакомитесь с преподавателем и сможете записаться.😉

В нашем главном меню вы можете выбрать интересующий вас раздел ⬇️ :"""