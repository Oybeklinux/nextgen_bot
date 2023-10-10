
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
                 "🔹 *Flutter*. Flutter va Dart yordamida ilovalar ishlab chiqish 📱\n"
                 "🔹 *PYTHON*. Python asoslari va Django freymvorki 🐍\n"
                 "🔹 *PHP*. PHP va Laravel yordamida veb-ilovalar yaratish 💻\n"
                 "🔹 *DevOps*. DevOps va platforma muhandisligi bo'yicha professional bilim ♾\n\n\n"
                 "To'g'ri kursni tanlashga yordam berish uchun biz bepul ochiq darslarni o'tkazamiz, unda siz o'quv reja bilan tanishishingiz, o'qituvchi bilan tanishishingiz va ro'yxatdan o'tishingiz mumkin.😉\n\n"
                 "Bizning asosiy menyuda siz o'zingizni qiziqtirgan bo'limni tanlashingiz mumkin ⬇️:"
            ),
            "python": (
                "<b>Python asoslari va Django Freymvorki </b>\n\n"
                 "Kurs Python tilidan foydalangan holda dasturlashning fundamental tushunchalari va texnikasi bilan tanishishni, shuningdek, mashhur Django veb-freymvorkini chuqur ko‘rib chiqishni o‘z ichiga olgan keng qamrovli kursdir.\n"
                 "Kursda siz zamonaviy veb-ilovalar, desktop ilovalarini yaratish, ma'lumotlar bazalari bilan ishlashni o'rganasiz.🐍\n\n"
                 "7 oylik treningda siz zamonamizning eng talabchan kasblaridan biri uchun kerakli ko'nikmalarini egallaysiz.💪\n\n"
                 "Oyiga: 1 800 000 so‘m\n\n"
                 "PYTHON kursining dasturi:\n\n"
                 "◾️ PYTHON asoslari. Funktsional dasturlash;\n"
                 "◾ OOP - ob'ektga yo'naltirilgan dasturlash;\n"
                 "◾️ Ma'lumotlar bazalari. Strukturaviy so'rovlar tili SQL;\n"
                 "◾️ Ma'lumotlar bazasi va API yordamida dasturlash;\n"
                 "◾️ Django freymvorkidan foydalangan holda veb-ilovalar yaratish;\n"
                 "◾ DRF (Django Rest Framework) asosida API yaratish.\n\n"
                 "Kurs boshlanishidan oldin biz bepul ochiq darslarni o'tkazamiz, unda siz o'quv dasturini ko'rishishingiz, kurs haqida batafsil ma'lumot olishingiz, o'qituvchi bilan tanishishingiz va ro'yxatdan o'tishingiz mumkin.😉"
            ),
            "flutter": (
                "uz*Course Overview*\n"
                "The Apps Development with Flutter and Dart course provides an in-depth and comprehensive understanding of the popular Flutter SDK and the Dart programming language. This course will guide learners through the process of building beautiful, performant, and functional mobile applications for both Android and iOS platforms using a single codebase\n\n"
                "Topics covered in the course include an introduction to Dart language, understanding Flutter widgets, state management, working with external APIs, implementing device features like camera and location, testing, and deploying the apps. By the end of the course, students will be proficient and well-equipped with the skills to create quality, real-world, and production-ready mobile applications using Flutter and Dart.\n\n"
                "*Career Pathways*\n"
                "Completion of this comprehensive course paves the way for careers as Flutter developers, mobile app developers, or cross-platform app developers, with opportunities to work in tech startups, established software companies, or as freelancers.\n\n"
                "*Target Audience*\n"
                "This course is designed for Beginner and Intermediate level mobile apps developers.\n\n"
                "*Prerequisites*\n"
                "Learners are expected to have basic understanding of programming concepts and enthusiasm for mobile development; prior knowledge of Dart is beneficial but not necessary as the course covers it from the basics.\n\n"
                "*Course Objectives*\n"
                " - Learn the basics and advanced features of the Dart programming language;\n"
                " - Understand the Flutter SDK and its widget-based architecture;\n"
                " - Develop visually appealing, performant, and functional cross-platform mobile applications;\n"
                " - Implement native device features and external APIs;\n"
                " - Understand and apply state management solutions in a Flutter app;\n"
                " - Learn testing methodologies to ensure app reliability and performance;\n"
                " - Understand the process of deploying apps to the Google Play Store and Apple App Store;\n"
                "Всего за 7 месяцев вы освоите все необходимые навыки для полноценной профессии.\n\n"
                "Очное обучение за месяц: 1 800 000 сум\n\n"                
                "Перед запуском курса мы проводим бесплатные открытые уроки, где вы узнаете программу обучения, подробности о курсе, познакомитесь с преподавателем и сможете записаться. 😉"
            ),
            "php": (
                "uzНа курсе ВЕБ ПРОГРАММИРОВАНИЕ вы изучите основные языки программирования, научитесь создавать современные сайты, познакомитесь с инструментами, которые используют успешные веб-разработчики. 💻\n\n"
                "Всего за 10 месяцев вы освоите все необходимые навыки для полноценной профессии.\n\n"
                "Очное обучение за месяц: 1 800 000 сум\n\n"
                "Программа курса ВЕБ ПРОГРАММИРОВАНИЕ:\n\n"             
                "◾️ Основы верстки веб-страниц (Visual studio, HTML и CSS);\n"
                "◾️ Изучение графического онлайн-редактора Figma;\n"
                "◾️ Грамотное структурирование кода - БЭМ, надежное хранение проектов и загрузка портфолио на облачные сервисы (GitHub, Heroku и др.) с помощью системы Git;\n"
                "◾️ Полное погружение в самый гибкий язык программирования JavaScript;\n" 
                "◾️ Изучение прогрессивного фреймворка Vue.js;\n"
                "◾️ Vuex -  паттерн управления состоянием + библиотека для приложений на Vue.js;\n"
                "◾️ SASS - препроцессор CSS, продвинутый тип написания CSS;\n"  
                "◾️ Создание одностраничных приложений (SPA) с помощью Vue router;\n"
                "◾️Изучение процесса программирования при создании приложений Api (Application Programming Interface);\n"  
                "◾️Знакомство с облачной базой данных Firebase, которая позволяет пользователям хранить и получать сохраненную информацию, а также имеет удобные средства и методы взаимодействия с ней.\n\n"         
                "Перед запуском курса мы проводим бесплатные открытые уроки, где вы узнаете программу обучения, подробности о курсе, познакомитесь с преподавателем и сможете записаться. 😉"
            ),
            "about_us": (
                "uz🔝<b>NextGen Academy</b> - первая международная IT академия в Узбекистане, открытая в рамках сотрудничества с Американским Международным Университетом в Бангладеш (AIUB), Институтом Непрерывного Образования (ICE) при AIUB и IT Парком Узбекистана в 2022 году.\n\n" 
                "🤝NextGen Academy  является партнером международных вендоров как <b>Python institute</b>, <b>JS institute</b>, <b>Cisco Networking Academy</b>, <b>Fortinet</b>. Это партнерство позволяет студентам получить качественное обучение по международным программам, а также дает возможность для получения сертификатa международного образца.\n\n"
                "🖊Наша академия посвящена передаче знаний, навыков и практического и международного опыта, необходимых для успешной карьеры в быстро развивающейся IT - индустрии.\n\n" 
                "📉Мы стремимся сократить разрыв между требованиями промышленности и доступными кадрами, предоставляя  всеобъемлющие программы, отвечающие растущему спросу на квалифицированных IT - специалистов <b>в Узбекистане и мировом рынке</b>\n\n"
            ),
            "contact": (
                "uz🏙 *Наш адрес:*\n"
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
                "uzВы хотите записаться на открытый урок:\n"
                "Курс: PYTHON\n\n"            
                "📆 Дата: 14.10.2023\n"
                "🕰 Время: 17:00\n"
                "🇺🇿 Язык: Узбекский\n"
                "Формат: оффлайн\n\n"             
                "Нажмите кнопку “Подтвердить” и в скором времени с вами свяжутся наши менджеры."
            ),
            "open_lesson_confirm": (
                "uzОжидайте, наш менеджер свяжется с вами в ближайшее время и ответит на все ваши вопросы.😊"
            ),
            "send_phone": (
                "*📱 Raqamni yuborish* tugmasini bosib telefon raqamingizni yuboring"
            ),
            "bsend_phone" : ("📱 Raqamni yuborish"),
            "tinput_name": ("Пожалуйста, введите Ваше имя"),
            "tsignup_info": ("Siz muvaffaqiyatli ro'yxatdan o'tdingiz!"),
            "tmain_menu": "Asosiy menyu",
            "bcourses": "🔍 Kurslar",
            "bsettings": "⚙ Sozlamalar",
            "bedit_lang": "🇺🇿 Tilni o'zgartirish",
            "bedit_name": "🖊 Ismni o'zgartirish",
            "bto_main": "⬅ Orqaga",
            "iopen_lesson": "Ochiq dars",
            "iget_in_touch": "Bog'lanish",
            "iabout_us": "Biz haqimizda ❓",
            "icantact": "Aloqa 📱",
            "commands": ["Buyruqlar ro'yxati",
                         "Ishga tushirish",
                         "Ma'lumotnoma",
                         "Kurs haqida",
                         "Sozlamalar"]
        },
        "ru": {
            "courses": (
                "*Наши курсы:*\n\n"
                "🔹 *Flutter*. Разработка приложений с использованием Flutter и Dart 📱\n"
                "🔹 *PYTHON*. Основы Python и фреймворк Django 🐍\n"
                "🔹 *PHP*. Создание веб-приложений с использованием PHP и Laravel 💻\n"
                "🔹 *DevOps*. Профессиональное владение DevOps и инженерией платформы ♾\n\n\n"
                "Чтобы помочь вам выбрать подходящий курс, мы проводим бесплатные открытые уроки, где вы узнаете о программе обучения, познакомитесь с преподавателем и сможете записаться.😉\n\n"
                "В нашем главном меню вы можете выбрать интересующий вас раздел ⬇️ :"
            ),
            "python":(
                "<b> Основы Python и фреймворк Django </b>\n\n"
                "Курс представляет собой всесторонний курс, который предоставляет введение в фундаментальные концепции и техники программирования с использованием языка Python, а также подробное изучение популярного веб-фреймворка Django.\n"
                "На курсе вы научитесь создавать современные веб-приложения, desktop-приложений, работа с БД.🐍\n\n"
                "Всего за 7 месяцев обучения вы освоите необходимые навыки для одной из самых востребованных профессий современности.💪\n\n"
                "Очное обучение за месяц: 1 800 000 сум\n\n"
                "Программа курса PYTHON:\n\n"
                "◾️ Основы PYTHON.Изучение функционального программирования;\n"
                "◾  ООП - Объектно-ориентированная программирования;\n"
                "◾️ Базы данных.Изучение основ языка структурированных запросов SQL;\n"
                "◾️ Desktop-приложения с использованием БД и API;\n"
                "◾️ Создание веб-приложений используя фреймворк Django;\n"
                "◾  Создание API на основе DRF (Django Rest Framework).\n\n"
                "Перед запуском курса мы проводим бесплатные открытые уроки, где вы узнаете программу обучения, подробности о курсе, познакомитесь с преподавателем и сможете записаться. 😉"
            ),
            "flutter": (
                "ru*Course Overview*\n"
                "The Apps Development with Flutter and Dart course provides an in-depth and comprehensive understanding of the popular Flutter SDK and the Dart programming language. This course will guide learners through the process of building beautiful, performant, and functional mobile applications for both Android and iOS platforms using a single codebase\n\n"
                "Topics covered in the course include an introduction to Dart language, understanding Flutter widgets, state management, working with external APIs, implementing device features like camera and location, testing, and deploying the apps. By the end of the course, students will be proficient and well-equipped with the skills to create quality, real-world, and production-ready mobile applications using Flutter and Dart.\n\n"
                "*Career Pathways*\n"
                "Completion of this comprehensive course paves the way for careers as Flutter developers, mobile app developers, or cross-platform app developers, with opportunities to work in tech startups, established software companies, or as freelancers.\n\n"
                "*Target Audience*\n"
                "This course is designed for Beginner and Intermediate level mobile apps developers.\n\n"
                "*Prerequisites*\n"
                "Learners are expected to have basic understanding of programming concepts and enthusiasm for mobile development; prior knowledge of Dart is beneficial but not necessary as the course covers it from the basics.\n\n"
                "*Course Objectives*\n"
                " - Learn the basics and advanced features of the Dart programming language;\n"
                " - Understand the Flutter SDK and its widget-based architecture;\n"
                " - Develop visually appealing, performant, and functional cross-platform mobile applications;\n"
                " - Implement native device features and external APIs;\n"
                " - Understand and apply state management solutions in a Flutter app;\n"
                " - Learn testing methodologies to ensure app reliability and performance;\n"
                " - Understand the process of deploying apps to the Google Play Store and Apple App Store;\n"
                "Всего за 7 месяцев вы освоите все необходимые навыки для полноценной профессии.\n\n"
                "Очное обучение за месяц: 1 800 000 сум\n\n"
                "Перед запуском курса мы проводим бесплатные открытые уроки, где вы узнаете программу обучения, подробности о курсе, познакомитесь с преподавателем и сможете записаться. 😉"
            ),
            "php": (
                "ruНа курсе ВЕБ ПРОГРАММИРОВАНИЕ вы изучите основные языки программирования, научитесь создавать современные сайты, познакомитесь с инструментами, которые используют успешные веб-разработчики. 💻\n\n"
                "Всего за 10 месяцев вы освоите все необходимые навыки для полноценной профессии.\n\n"
                "Очное обучение за месяц: 1 800 000 сум\n\n"
                "Программа курса ВЕБ ПРОГРАММИРОВАНИЕ:\n\n"
                "◾️ Основы верстки веб-страниц (Visual studio, HTML и CSS);\n"
                "◾️ Изучение графического онлайн-редактора Figma;\n"
                "◾️ Грамотное структурирование кода - БЭМ, надежное хранение проектов и загрузка портфолио на облачные сервисы (GitHub, Heroku и др.) с помощью системы Git;\n"
                "◾️ Полное погружение в самый гибкий язык программирования JavaScript;\n"
                "◾️ Изучение прогрессивного фреймворка Vue.js;\n"
                "◾️ Vuex -  паттерн управления состоянием + библиотека для приложений на Vue.js;\n"
                "◾️ SASS - препроцессор CSS, продвинутый тип написания CSS;\n"
                "◾️ Создание одностраничных приложений (SPA) с помощью Vue router;\n"
                "◾️Изучение процесса программирования при создании приложений Api (Application Programming Interface);\n"
                "◾️Знакомство с облачной базой данных Firebase, которая позволяет пользователям хранить и получать сохраненную информацию, а также имеет удобные средства и методы взаимодействия с ней.\n\n"
                "Перед запуском курса мы проводим бесплатные открытые уроки, где вы узнаете программу обучения, подробности о курсе, познакомитесь с преподавателем и сможете записаться. 😉"
            ),
            "about_us": (
                "ru🔝<b>NextGen Academy</b> - первая международная IT академия в Узбекистане, открытая в рамках сотрудничества с Американским Международным Университетом в Бангладеш (AIUB), Институтом Непрерывного Образования (ICE) при AIUB и IT Парком Узбекистана в 2022 году.\n\n" 
                "🤝NextGen Academy  является партнером международных вендоров как <b>Python institute</b>, <b>JS institute</b>, <b>Cisco Networking Academy</b>, <b>Fortinet</b>. Это партнерство позволяет студентам получить качественное обучение по международным программам, а также дает возможность для получения сертификатa международного образца.\n\n"
                "🖊Наша академия посвящена передаче знаний, навыков и практического и международного опыта, необходимых для успешной карьеры в быстро развивающейся IT - индустрии.\n\n" 
                "📉Мы стремимся сократить разрыв между требованиями промышленности и доступными кадрами, предоставляя  всеобъемлющие программы, отвечающие растущему спросу на квалифицированных IT - специалистов <b>в Узбекистане и мировом рынке</b>\n\n"
            ),
            "contact": (
                "ru🏙 *Наш адрес:*\n"
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
                "ruВы хотите записаться на открытый урок:\n"
                "Курс: PYTHON\n\n"            
                "📆 Дата: 14.10.2023\n"
                "🕰 Время: 17:00\n"
                "🇺🇿 Язык: Узбекский\n"
                "Формат: оффлайн\n\n"             
                "Нажмите кнопку “Подтвердить” и в скором времени с вами свяжутся наши менджеры."
            ),
            "open_lesson": (
                "ruВы хотите записаться на открытый урок:\n"
                "Курс: PYTHON\n\n"            
                "📆 Дата: 14.10.2023\n"
                "🕰 Время: 17:00\n"
                "🇺🇿 Язык: Узбекский\n"
                "Формат: оффлайн\n\n"             
                "Нажмите кнопку “Подтвердить” и в скором времени с вами свяжутся наши менджеры."
            ),
            "open_lesson_confirm": (
                "ruОжидайте, наш менеджер свяжется с вами в ближайшее время и ответит на все ваши вопросы.😊"
            ),
            "send_phone": (
                "Отправьте свой номер телефона, нажав кнопку *📱 Отправить контакт*."
            ),
            "bsend_phone": ("📱 Отправить контакт"),
            "tinput_name": ("Iltimos, ismingizni kiriting"),
            "tsignup_info": ("Вы успешно зарегистрированы!"),
            "tmain_menu": "Главное меню",
            "bcourses": "🔍 Курсы",
            "bsettings": "⚙ Настройки",
            "bedit_lang": "🇺🇿 Изменить язык",
            "bedit_name": "🖊 Изменить имя",
            "bto_main": "⬅ Назад",
            "iopen_lesson": "Открытый урок",
            "iget_in_touch": "Связаться",
            "iabout_us": "О нас ❓",
            "icantact": "Контакты 📱",
            "commands": ["Список команд",
                         "Начать диалог",
                         "Получить справку",
                         "Получить информацию о курсах",
                         "Настройки"]
        },
        "en": {

            "courses": (
                "*Our courses:*\n\n"
                 "🔹 *Flutter*. Application development using Flutter and Dart 📱\n"
                 "🔹 *PYTHON*. Python basics and Django framework 🐍\n"
                 "🔹 *PHP*. Creating web applications using PHP and Laravel 💻\n"
                 "🔹 *DevOps*. Professional knowledge of DevOps and platform engineering ♾\n\n\n"
                 "To help you choose the right course, we hold free open lessons where you can learn about the curriculum, meet the teacher and be able to enroll.😉\n\n"
                 "In our main menu you can select the section you are interested in ⬇️:"
            ),
            "python": (
                "<b>Python Basics and the Django Framework </b>\n\n"
                 "The course is a comprehensive course that provides an introduction to the fundamental concepts and techniques of programming using the Python language, as well as an in-depth look at the popular web framework Django.\n"
                 "On the course you will learn how to create modern web applications, desktop applications, work with databases.🐍\n\n"
                 "In just 7 months of training, you will master the necessary skills for one of the most in-demand professions of our time.💪\n\n"
                 "Full-time training per month: 1,800,000 sum\n\n"
                 "PYTHON course program:\n\n"
                 "◾️ PYTHON Basics. Learning functional programming;\n"
                 "◾ OOP - Object-Oriented Programming;\n"
                 "◾️ Databases. Learning the basics of the structured query language SQL;\n"
                 "◾️ Desktop applications using a database and API;\n"
                 "◾️ Creating web applications using the Django framework;\n"
                 "◾ Creating an API based on DRF (Django Rest Framework).\n\n"
                 "Before launching the course, we hold free open lessons, where you will get to know the training program, details about the course, meet the teacher and be able to enroll. 😉"
            ),
            "flutter": (
                "<b>PYTHON</b>\n\n"
                "📌 <b>Course Overview</b>\n"
                "The Apps Development with Flutter and Dart course provides an in-depth and comprehensive understanding of the popular Flutter SDK and the Dart programming language. This course will guide learners through the process of building beautiful, performant, and functional mobile applications for both Android and iOS platforms using a single codebase\n\n"
                "Topics covered in the course include an introduction to Dart language, understanding Flutter widgets, state management, working with external APIs, implementing device features like camera and location, testing, and deploying the apps. By the end of the course, students will be proficient and well-equipped with the skills to create quality, real-world, and production-ready mobile applications using Flutter and Dart.\n\n"
                "📌 <b>Career Pathways</b>\n"
                "Completion of this comprehensive course paves the way for careers as Flutter developers, mobile app developers, or cross-platform app developers, with opportunities to work in tech startups, established software companies, or as freelancers.\n\n"
                "📌 <b>Target Audience</b>\n"
                "This course is designed for Beginner and Intermediate level mobile apps developers.\n\n"
                "📌 <b>Prerequisites</b>\n"
                "Learners are expected to have basic understanding of programming concepts and enthusiasm for mobile development; prior knowledge of Dart is beneficial but not necessary as the course covers it from the basics.\n\n"
                "📌 <b>Course Objectives</b>\n"
                " ✅ Learn the basics and advanced features of the Dart programming language;\n"
                " ✅ Understand the Flutter SDK and its widget-based architecture;\n"
                " ✅ Develop visually appealing, performant, and functional cross-platform mobile applications;\n"
                " ✅ Implement native device features and external APIs;\n"
                " ✅ Understand and apply state management solutions in a Flutter app;\n"
                " ✅ Learn testing methodologies to ensure app reliability and performance;\n"
                " ✅ Understand the process of deploying apps to the Google Play Store and Apple App Store;\n\n"
                "<b>Course Curriculum<b>\n"
                "Part 1: Dart Programming"
                " ✅ <b>Introduction to Dart<.b> - Overview of Dart, data types, control flow, and functions"
                " ✅ <b>Object-Oriented Programming in Dart</b> - Classes, objects, inheritance, encapsulation, and polymorphism"
                "Asynchronous Programming in Dart	Understanding Futures, async, await, and Streams"
                "Dart Libraries and Packages	Introduction to important Dart libraries and how to use external packages"
                
                "⏳ <b>Duration</b>: 7 monthes.\n\n"
                "💴 <b>Cost</b>: 1 800 000 сум\n\n"
                "📅 <b>Date of open lesson</b>: 10.10.2014"
            ),
            "php": (
                "enНа курсе ВЕБ ПРОГРАММИРОВАНИЕ вы изучите основные языки программирования, научитесь создавать современные сайты, познакомитесь с инструментами, которые используют успешные веб-разработчики. 💻\n\n"
                "Всего за 10 месяцев вы освоите все необходимые навыки для полноценной профессии.\n\n"
                "Очное обучение за месяц: 1 800 000 сум\n\n"
                "Программа курса ВЕБ ПРОГРАММИРОВАНИЕ:\n\n"
                "◾️ Основы верстки веб-страниц (Visual studio, HTML и CSS);\n"
                "◾️ Изучение графического онлайн-редактора Figma;\n"
                "◾️ Грамотное структурирование кода - БЭМ, надежное хранение проектов и загрузка портфолио на облачные сервисы (GitHub, Heroku и др.) с помощью системы Git;\n"
                "◾️ Полное погружение в самый гибкий язык программирования JavaScript;\n"
                "◾️ Изучение прогрессивного фреймворка Vue.js;\n"
                "◾️ Vuex -  паттерн управления состоянием + библиотека для приложений на Vue.js;\n"
                "◾️ SASS - препроцессор CSS, продвинутый тип написания CSS;\n"
                "◾️ Создание одностраничных приложений (SPA) с помощью Vue router;\n"
                "◾️Изучение процесса программирования при создании приложений Api (Application Programming Interface);\n"
                "◾️Знакомство с облачной базой данных Firebase, которая позволяет пользователям хранить и получать сохраненную информацию, а также имеет удобные средства и методы взаимодействия с ней.\n\n"
                "Перед запуском курса мы проводим бесплатные открытые уроки, где вы узнаете программу обучения, подробности о курсе, познакомитесь с преподавателем и сможете записаться. 😉"
            ),
            "about_us": (
                "en🔝<b>NextGen Academy</b> - первая международная IT академия в Узбекистане, открытая в рамках сотрудничества с Американским Международным Университетом в Бангладеш (AIUB), Институтом Непрерывного Образования (ICE) при AIUB и IT Парком Узбекистана в 2022 году.\n\n" 
                "🤝NextGen Academy  является партнером международных вендоров как <b>Python institute</b>, <b>JS institute</b>, <b>Cisco Networking Academy</b>, <b>Fortinet</b>. Это партнерство позволяет студентам получить качественное обучение по международным программам, а также дает возможность для получения сертификатa международного образца.\n\n"
                "🖊Наша академия посвящена передаче знаний, навыков и практического и международного опыта, необходимых для успешной карьеры в быстро развивающейся IT - индустрии.\n\n" 
                "📉Мы стремимся сократить разрыв между требованиями промышленности и доступными кадрами, предоставляя  всеобъемлющие программы, отвечающие растущему спросу на квалифицированных IT - специалистов <b>в Узбекистане и мировом рынке</b>\n\n"
            ),
            "contact": (
                "en🏙 *Наш адрес:*\n"
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
                "enВы хотите записаться на открытый урок:\n"
                "Курс: #course\n\n"            
                "📆 Дата: #date\n"
                "🕰 Время: #time\n"
                "🇺🇿 Язык: Узбекский\n"
                "Формат: оффлайн\n\n"             
                "Нажмите кнопку “Подтвердить” и в скором времени с вами свяжутся наши менджеры."
            ),
            "open_lesson": (
                "enВы хотите записаться на открытый урок:\n"
                "Курс: PYTHON\n\n"            
                "📆 Дата: 14.10.2023\n"
                "🕰 Время: 17:00\n"
                "🇺🇿 Язык: Узбекский\n"
                "Формат: оффлайн\n\n"             
                "Нажмите кнопку “Подтвердить” и в скором времени с вами свяжутся наши менджеры."
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
            "iopen_lesson": "Open lesson",
            "iget_in_touch": "Contact us",
            "iabout_us": "About us ❓",
            "icantact": "Contacts 📱",
            "commands": ["Command list",
                         "Start the bot",
                         "Get information",
                         "Get info about courses",
                         "Settings"]

        }
    }

    language_code = None

    def __init__(self):
        try:
            user_id = User.get_current().id
            language_code = db.select_user_language(id=user_id)
        except AttributeError:
            language_code = 'uz'
        Texts.language_code = language_code if language_code else "uz"

    @classmethod
    def set_language(cls, language_code):
        cls.language_code = language_code

    @classmethod
    def get(cls, key: str) -> str:
        return cls.strings[Texts.language_code][key]

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