
from loader import db

open_lesson_dates = {
    "python": {"date": "14.10.2023", "time": "17:00"},
    "flutter": {"date": "Уже прошло", "time": ""},
    "php": {"date": "Не определено", "time": ""}
}

from aiogram.types import User



class Texts:
    strings = {
        "uz": {
            "courses":(
                "*Bizning kurslarimiz:*\n\n"
                 "#courses\n\n"
                 "To'g'ri kursni tanlashga yordam berish uchun biz bepul ochiq darslarni o'tkazamiz, unda siz o'quv reja bilan tanishishingiz, o'qituvchi bilan tanishishingiz va ro'yxatdan o'tishingiz mumkin.😉\n\n"
                 "Bizning asosiy menyuda siz o'zingizni qiziqtirgan bo'limni tanlashingiz mumkin ⬇️:"
            ),
            "course": (
                "<b>#course_name</b>\n\n"
                "ℹ️<b> Kurs haqida umumiy ma’lumot</b>\n\n"
                "#about"
                "💼 <b>Karyera istiqboli</b>\n\n"
                "#career"
                "🎯 <b>Mo’ljallangan auditoriya</b>\n\n"
                "#for_whom"
                "📝 <b>Talablar</b>\n\n"
                "#requirements"
            ),

            "about_us": (
                "🔝*NextGen Academy* – Bangladeshdagi Amerika xalqaro universiteti (AIUB), AIUB qoshidagi Uzluksiz ta’lim instituti (ICE) va O‘zbekiston IT-parki bilan hamkorlik doirasida 2022-yilda ochilgan O‘zbekistondagi birinchi xalqaro IT akademiyasidir.\n\n"
                "🤝NextGen Academy *Python instituti*, *Javascript instituti*, *Cisco Networking Academy*, *Fortinet* kabi xalqaro ishlab chiqaruvchilarning hamkori hisoblanadi. Ushbu hamkorlik talabalarga xalqaro dasturlarda sifatli ta'lim olish imkonini beradi, shuningdek, xalqaro sertifikat olish imkoniyatini beradi.\n\n"
                "🖊Bizning akademiyamiz jadal rivojlanayotgan IT-sanoatda muvaffaqiyatli martaba uchun zarur bo'lgan bilim, ko'nikma va amaliy va xalqaro tajribani berishga bag'ishlangan.\n\n"
                "📉Biz *O‘zbekistonda va jahon bozorida* malakali IT mutaxassislariga ortib borayotgan talablarga javob beradigan keng qamrovli dasturlarni taqdim etish orqali soha talablari va mavjud kadrlar o‘rtasidagi bo'liqni bartaraf etishga intilamiz."
            ),
            "contact": (
                "🏙 *Bizning manzil:*\n"
                 "Toshkent sh., Moʻminova ko'chasi bino 4\\1, 100041. \nAloqabank binosi, 16-qavat. \nOrientir: INHA universiteti\n\n\n"
                 "☎ *Kontaktlar:*\n"
                 "Telegram: [nextgen_admin](https://t.me/kamilaa3)\n"
                 "Tel: +998 55-515-99-00\n"
                 "Elektron pochta: nextgenacademyuzb@gmail.com\n\n"
                 "📍 *Joylashuv:* \n"
                 "[Yandex](https://yandex.com/maps/-/CDUpMN~f) | [Google Maps](https://maps.app.goo.gl/QxA81NH4D5UDnGMTA)\n\n"
                 "*Ijtimoiy tarmoqlarimiz:*\n"
                 "[Veb-sayt](https://nextgen.uz/) | [Telegram](https://t.me/nextgenacademyuz) | [Facebook](https://www.facebook.com/profile.php?id=100090080721603) | [Instagram](https://www.instagram.com/ngen.uz/)\n"
            ),
            "open_lesson": (
                    "Quyida *#course* kursi bo'yicha ochiq dars haqida ma'lumot keltirilgan. "
                    "\nOchiq darsga yozilish uchun *#button* tugmasini bosing\n\n"
                    
                    "📆 *Sanasi*: #date\n"
                    "🕰 *Vaqti*: #time\n"
                    "🇺🇿 *Tili*: #language\n"
                    "❗ *Format*: oflayn"
                ),
            "open_lesson_confirm": (
                "Menejerimiz tez orada siz bilan bog'lanib, barcha savollaringizga javob berishini kuting.😊"
            ),
            "send_phone": (
                "*📱 Raqamni yuborish* tugmasini bosib telefon raqamingizni yuboring"
            ),
            "bsend_phone" : ("📱 Raqamni yuborish"),
            "tinput_name": ("Iltimos, ismingizni kiriting"),
            "tsignup_info": ("Siz muvaffaqiyatli ro'yxatdan o'tdingiz!"),
            "tmain_menu": "Asosiy menyu",
            "bcourses": "🔍 Kurslar",
            "bsettings": "⚙ Sozlamalar",
            "bedit_lang": "🇺🇿 Tilni o'zgartirish",
            "bedit_name": "🖊 Ismni o'zgartirish",
            "bto_main": "⬅ Orqaga",
            "iopen_lesson": "📅 Ochiq dars",
            "iopen_lesson_vip": "📅 Ochiq darsga yozilish",
            "iget_in_touch": "🗣 Bog'lanish",
            "iabout_us": "Biz haqimizda ❓",
            "icantact": "Aloqa 📱",
            "commands": ["*Buyruqlar ro'yxati*\n",
                         "/start - ishga tushirish",
                         "/help - ma'lumotnoma",
                         "/courses - kurs haqida",
                         "/settings - sozlamalar"],
            "warn_phone_len": "Telefon raqami 9 yoki 12 ta raqamdan iborat bo'lishi kerak. Iltimos, qayta kiriting",
            "phone_edit_ok": "Sizning raqamingiz muvaffaqiyatli o'zgartirildi!",
            "icourse_content": "📖 Kursning mundarijasi",
            "icourse_objective": "🎯 Kursning maqsadi",
            "icancel": "❌ Bekor qilish",
            "iconfirm": "✅ Tasdiqlash",
            'ru': "Rus tili",
            'uz': "O'zbek tili",
            'en': "Ingliz tili",
            'excuse_open_lesson': "Kechirasiz *#course* bo'yicha ochiq dars soat #time #date sanada bo'lib o'tdi",
            "lang_changed": "Til muvaffaqiyatli yangilandi",
            "name_changed": "Ismingiz muvaffaqiyatli o'zgartirildi!",
            'lstart': 'Botni ishga tushirish',
            'lhelp': 'Yordam',
            'lcourses': 'Kurs haqida',
            'lsettings': 'Sozlamalar'

        },
        "ru": {
            "courses": (
                "*Наши курсы:*\n\n"
                "#courses\n\n"
                "Чтобы помочь вам выбрать подходящий курс, мы проводим бесплатные открытые уроки, где вы узнаете о программе обучения, познакомитесь с преподавателем и сможете записаться.😉\n\n"
                "В нашем главном меню вы можете выбрать интересующий вас раздел ⬇️ :"
            ),
            "course":(
                "<b>#course_name</b>\n\n"
                "ℹ️<b>Обзор курса</b>\n\n"
                "#about"
                "💼 <b>Карьерный путь</b>\n\n"
                "#career"
                "🎯 <b>Целевая аудитория</b>\n\n"
                "#for_whom"
                "📝 <b>Предварительные Требования</b>\n\n"
                "#requirements"
            ),

            "about_us": (
                "🔝*NextGen Academy* - первая международная IT академия в Узбекистане, открытая в рамках сотрудничества с Американским Международным Университетом в Бангладеш (AIUB), Институтом Непрерывного Образования (ICE) при AIUB и IT Парком Узбекистана в 2022 году.\n\n" 
                "🤝NextGen Academy  является партнером международных вендоров как *Python institute*, *JS institute*, *Cisco Networking Academy*, *Fortinet*. Это партнерство позволяет студентам получить качественное обучение по международным программам, а также дает возможность для получения сертификатa международного образца.\n\n"
                "🖊Наша академия посвящена передаче знаний, навыков и практического и международного опыта, необходимых для успешной карьеры в быстро развивающейся IT - индустрии.\n\n" 
                "📉Мы стремимся сократить разрыв между требованиями промышленности и доступными кадрами, предоставляя  всеобъемлющие программы, отвечающие растущему спросу на квалифицированных IT - специалистов *в Узбекистане и мировом рынке*\n\n"
            ),
            "contact": (
                "🏙 *Наш адрес:*\n"
                "г. Ташкент, Муминова, 4\1, 100041. Здания Aloqabank , 16-этаж. Ориентир: Университет INHA\n\n\n"                       
                "☎ *Контакты:*\n"
                "Telegram: [nextgen_admin](https://t.me/kamilaa3)\n"
                "Тел: +998 55-515-99-00\n"
                "Email: nextgenacademyuzb@gmail.com\n\n"        
                "📍 *Локация:* \n"
                "[Yandex](https://yandex.com/maps/-/CDUpMN~f) | [Google Maps](https://maps.app.goo.gl/QxA81NH4D5UDnGMTA)\n\n"            
                "*Наши социальные сети:*\n"
                "[Website](https://nextgen.uz/) | [Telegram](https://t.me/nextgenacademyuz) | [Facebook](https://www.facebook.com/profile.php?id=100090080721603) | [Instagram](https://www.instagram.com/ngen.uz/)\n"
            ),
            "open_lesson": (
                     "Ниже представлена информация об открытом занятии по курсу *#course*"
                     "\nНажмите кнопку *#button*, чтобы записаться на открытое занятие\n\n"
                    
                     "📆 *Дата*: #date\n"
                     "🕰 *Время*: #time\n"
                     "🇺🇿 *Язык*: #language\n"
                     "❗ *Формат*: офлайн"
                ),
            "open_lesson_confirm": (
                "Ожидайте, наш менеджер свяжется с вами в ближайшее время и ответит на все ваши вопросы.😊"
            ),
            "send_phone": (
                "Отправьте свой номер телефона, нажав кнопку *📱 Отправить контакт*."
            ),
            "bsend_phone": ("📱 Отправить контакт"),
            "tinput_name": ("Пожалуйста, введите Ваше имя"),
            "tsignup_info": ("Вы успешно зарегистрированы!"),
            "tmain_menu": "Главное меню",
            "bcourses": "🔍 Курсы",
            "bsettings": "⚙ Настройки",
            "bedit_lang": "🇺🇿 Изменить язык",
            "bedit_name": "🖊 Изменить имя",
            "bto_main": "⬅ Назад",
            "iopen_lesson": "📅 Открытый урок",
            "iopen_lesson_vip": "📅 Записаться на открытые уроки",
            "iget_in_touch": "Связаться",
            "iabout_us": "О нас ❓",
            "icantact": "Контакты 📱",
            "commands": ["*Список команд*\n",
                         "/start - начать диалог",
                         "/help - получить справку",
                         "/courses - получить информацию о курсах",
                         "/settings - настройки"],
            "warn_phone_len": 'Номер телефона должен состоять из 9 или 12 цифр. Введите заново',
            "phone_edit_ok": 'Ваш номер успешно изменен!',
            "icourse_content": "📖 Учебная Программа Курса",
            "icourse_objective": "🎯 Цели Курса",
            "icancel": "❌ Отмена",
            "iconfirm": "✅ Подтвердить",
            'ru': "Русский язык",
            'uz': "Узбекский язык",
            'en': "Английкий язык",
            'excuse_open_lesson': "Извините, открытый урок по *#course* состоялся #date в #time",
            "lang_changed": "Язык успешно обновлен",
            "name_changed": "Ваш имя успешно изменен!",
            'lstart': 'Запустить бота',
            'lhelp': 'Помощь',
            'lcourses':'Информация о курсах',
            'lsettings': 'Настройки'


        },
        "en": {

            "courses": (
                "*Our courses:*\n\n"
                 "#courses\n\n"
                 "To help you choose the right course, we hold free open lessons where you can learn about the curriculum, meet the teacher and be able to enroll.😉\n\n"
                 "In our main menu you can select the section you are interested in ⬇️:"
            ),
            "course":(
                "<b>#course_name</b>\n\n"
                "ℹ️<b>Course Overview</b>\n\n"
                "#about"
                "💼 <b>Career Pathways</b>\n\n"
                "#career"
                "🎯 <b>Target Audience</b>\n\n"
                "#for_whom"
                "📝 <b>Prerequisites</b>\n\n"
                "#requirements"
            ),
            "about_us": (
                """
🔝*NextGen Academy* is the first international IT academy in Uzbekistan, opened as part of cooperation with the American International University in Bangladesh (AIUB), the Institute of Continuing Education (ICE) at AIUB and the IT Park of Uzbekistan in 2022.

🤝NextGen Academy is a partner of international vendors such as *Python institute*, *JS institute*, *Cisco Networking Academy*, *Fortinet*. This partnership allows students to receive quality training in international programs, and also provides the opportunity to obtain an international certificate.

🖊Our academy is dedicated to imparting the knowledge, skills and practical and international experience necessary for a successful career in the rapidly developing IT industry.

📉We strive to bridge the gap between industry requirements and available talent by providing comprehensive programs that meet the growing demand for qualified IT professionals *in Uzbekistan and the global market*"""
            ),
            "contact": (
                "🏙 *Our address:*\n"
                "Tashkent, Muminova, 4\1, 100041. Aloqabank building, 16th floor. Landmark: INHA University\n\n\n"
                "☎ *Contacts:*\n"
                "Telegram: [nextgen_admin](https://t.me/kamilaa3)\n"
                "Tel: +998 55-515-99-00\n"
                "Email: nextgenacademyuzb@gmail.com\n\n"
                "📍 *Location:* \n"
                "[Yandex](https://yandex.com/maps/-/CDUpMN~f) | [Google Maps](https://maps.app.goo.gl/QxA81NH4D5UDnGMTA)\n\n"
                "*Our social networks:*\n"
                "[Website](https://nextgen.uz/) | [Telegram](https://t.me/nextgenacademyuz) | [Facebook](https://www.facebook.com/profile.php?id= 100090080721603) | [Instagram](https://www.instagram.com/ngen.uz/)\n"),
            "open_lesson": (
                    "The following is information about an open class for the *#course* course."
                     "\nPress the *#button* button to sign up for an open class\n\n"
                    
                     "📆 *Date*: #date\n"
                     "🕰 *Time*: #time\n"
                     "🇺🇿 *Language*: #language\n"
                     "❗ *Format*: offline"
                ),
            "open_lesson_confirm": (
                "enОжидайте, наш менеджер свяжется с вами в ближайшее время и ответит на все ваши вопросы.😊"
            ),
            "send_phone": (
                "Send your phone number by pressing the *📱 Send contact* button"
            ),
            "bsend_phone": ("📱 Send contact"),
            "tinput_name": ("Please enter your name"),
            "tsignup_info": ("You have successfully registered!"),
            "tmain_menu": "Main menu",
            "bcourses": "🔍 Courses",
            "bsettings": "⚙ Settings",
            "bedit_lang": "🇺🇿 Edit language",
            "bedit_name": "🖊 Edit name",
            "bto_main": "⬅ Back",
            "iopen_lesson": "📅 Open lesson",
            "iopen_lesson_vip": "📅 Sign up for an open lesson",
            "iget_in_touch": "Contact us",
            "iabout_us": "About us ❓",
            "icantact": "Contacts 📱",
            "commands": ["*Command list*\n",
                         "/start - start the bot",
                         "/help - get information",
                         "/courses - get info about courses",
                         "/settings - settings"],
            "warn_phone_len": 'The phone number must consist of 9 or 12 digits. Please re-enter',
            "phone_edit_ok": 'Your number has been successfully updated!',
            "icourse_content": "📖 Course Curriculum",
            "icourse_objective": "🎯Course Objectives",
            "icancel": "❌ Cancel",
            "iconfirm": "✅ Confirm",
            'ru': "Russian",
            'uz': "Uzbek",
            'en': "English",
            'excuse_open_lesson': "Sorry open class on *#course* was held at #time on #date",
            "lang_changed": "Language updated successfully",
            "name_changed": "Your name has been successfully changed!",
            'lstart': 'Run the bot',
            'lhelp': 'Help',
            'lcourses': 'Course information',
            'lsettings': 'Settings'
        }
    }

    language_code = None

    @classmethod
    def get(cls, key: str) -> str:
        try:
            user_id = User.get_current().id
            language = db.select_user_language(user_id)
        except:
            language = 'uz'
        return cls.strings[language][key]

    @classmethod
    def get_list(cls, key: str) -> list:
        return [cls.strings['uz'][key], cls.strings['ru'][key], cls.strings['en'][key]]


class Text:
    strings = {
        "en": {
            "start": (
                "<b>Hi {}!</b>\n\n"
                "This bot will help you upload your files to "
                "telegraph and get links to them.\n\n"
                "<b>Upload your file:</b>\n"
                "<i>Only .jpg, .jpeg, .png, .gif and .mp4 files "
                "with a maximum size of 5 MB are allowed.</i>"
            ),
            "source": (
                "https://github.com/nessshon/telegraph-uploader-bot"
            ),
            "file_to_big_error": (
                "<b>File too big:{}</b>\n"
                "<i>The file size must not exceed 5 MB.</i>"
            ),
            "retry_after_error": (
                "<b>Flood control exceeded!</b>\n"
                "<i>Retry in {} seconds.</i>"
            ),
            "file_type_error": (
                "<b>Unsupported type!</b>\n"
                "<i>Allowed only .jpg, .jpeg, .png, .gif and .mp4 files.</i>"
            ),
            "another_error": (
                "<b>Unknown error!</b>\n"
                "<i>Try again later.</i>"
            ),
        },
        "ru": {
            "start": (
                "<b>Привет {}!</b>\n\n"
                "Этот бот поможет загрузить файлы в "
                "telegraph и получить на них ссылки.\n\n"
                "<b>Отправьте файл:</b>\n"
                "<i>Допускаются файлы .jpg, .jpeg, .png, .gif и .mp4 "
                "с максимальным размером 5 МБ.</i>"
            ),
            "source": (
                "https://github.com/nessshon/telegraph-uploader-bot"
            ),
            "file_to_big_error": (
                "<b>Файл слишком большой:{}</b>\n"
                "<i>Размер файла не должен превышать 5MB.</i>"
            ),
            "retry_after_error": (
                "<b>Превышено кол-во запросов!</b>\n"
                "<i>Повторите попытку через {} секунд.</i>"
            ),
            "file_type_error": (
                "<b>Неподдерживаемый тип!</b>\n"
                "<i>Разрешены только файлы .jpg, .jpeg, .png, .gif и .mp4.</i>"
            ),
            "another_error": (
                "<b>Неизвестная ошибка!</b>\n"
                "<i>Попробуйте повторить позже.</i>"
            )
        }
    }

    def __init__(self):
        # language_code = User.get_current().language_code
        user_id = User.get_current().id
        language_code = db.select_user_language(id=user_id)
        self.language_code = language_code if language_code == "ru" else "en"

    def get(self, key: str) -> str:

        return self.strings[self.language_code][key]