migrations = {
    0: [
        """CREATE TABLE IF NOT EXISTS open_lessons(            
            id SERIAL PRIMARY KEY, 
            course varchar(30),
            date TIMESTAMP,        
            format varchar(20),  
            language varchar(3))""",
        """CREATE TABLE IF NOT EXISTS courses(
            id SERIAL PRIMARY KEY, 
            name varchar(100) NOT NULL,
            description varchar(300),
            language varchar(3),
            about text,
            career text,
            for_whom text,
            requirements text,
            content text,
            objective text,
            price integer,
            image varchar(300))""",
        """CREATE TABLE IF NOT EXISTS users(
            id BIGINT PRIMARY KEY, 
            name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            phone varchar(20))""",
        """CREATE TABLE IF NOT EXISTS open_lesson_users(
            id SERIAL PRIMARY KEY, 
            user_id BIGINT,
            open_lesson_id INTEGER,                             
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(open_lesson_id) REFERENCES open_lessons(id))""",
        """CREATE TABLE IF NOT EXISTS migrations(
            id SERIAL PRIMARY KEY, 
            version INTEGER UNIQUE,
            migrated TIMESTAMP DEFAULT now())"""
    ],
    1: [
        "ALTER TABLE courses ADD COLUMN official_name varchar(300)"
    ],
    2: [
        ("ALTER TABLE open_lesson_users ADD COLUMN course_name varchar(30)")
    ],
    # inserting courses
    3: [
        """
        BEGIN TRANSACTION;

INSERT INTO "courses" ("id","name","description","language","about","career","for_whom","requirements","content","objective","price","image","official_name") VALUES (2,'Python','Dasturlash asoslari. OOP. GUI ilovalari. Veb-ilovalarni yaratish','uz','Python Asoslari va Django Freymvorki kursi keng qamrovli kurs bo''lib, u Python tilida dasturlashning asosiy tushunchalari va dasturlash texnikasi bilan tanishish hamda mashhur Django veb freymvorkini batafsil o''rganishni o’z ichiga olgan.\n\n

Ushbu kurs o’rganuvchilarning veb ilovalarni ishlab chiqish va Python sintaksisi, ma''lumotlar tuzilmalari, boshqaruv oqimi va obyektga yo''naltirilgan dasturlash asoslari haqida to''liq tushunchaga ega bo''lishlari uchun asosiy dasturlash ko''nikmalari va bilimlaridan iborat.\n\n 

Bundan tashqari, kursda modellar, viewlar, shablonlar, formalar va ma''lumotlar bazasi integratsiyasi kabi mavzularni o''z ichiga olgan mustahkam va kengaytiriladigan veb ilovalarni yaratish uchun Djangoning muhim xususiyatlarini o''rgatiladi. Kurs oxirida o’rganuvchilar Python dasturlash bo‘yicha mustahkam fundamentga ega bo‘ladilar hamda dinamik va interaktiv veb ilovalarni yaratish uchun Django freymvorkidan foydalanish imkoniyatiga ega bo‘ladilar.','Python dasturlash tili va Django freymvorkida olingan bilim bilan o’rganuvchilar Python dasturchisi, Django dasturchisi, Full-stack dasturchisi, veb saytlar dasturchisi, ma’lumotlar tahlilchisi kabi ish o’rinlarini egallashi yoki mustaqil ravishda shug’ullanishlari mumkin.','Ushbu kurs boshlang''ich va o''rta darajadagi Python dasturchilari uchun mo''ljallangan.','Ushbu o''quv dasturi yuqori o''rta maktablar, texnik maktablar va kollejlar yoki universitetlar uchun mo''ljallangan. Dasturlash bo''yicha oldindan bilim talab etilmaydi.','📚 *Python asoslari 1-qism*                

	- Python va kompyuter dasturlashiga kirish

	- Ma''lumotlar turlari, o''zgaruvchilar, asosiy kiritish-chiqarish amallari, asosiy operatorlar

	- Mantiqiy qiymatlar, shartli bajarilishlar, sikllar, ro‘yxatlar va ro‘yxatlarni qayta ishlash, mantiqiy va bit bo’yicha operatsiyalar

	- Funksiyalar, tupllar, lug''atlar va ma''lumotlarni qayta ishlash



📚 *Python asoslari 2-qism*

	- Modullar, paketlar va PIP

	- Istisnolar, string lar, String va List metodlari

	- Obyektga yo''naltirilgan dasturlash

	- Generatorlar, iteratorlar va yopishlar

	- Fayl tizimi, katalog daraxtlari va fayllar bilan ishlash

	- Tanlangan Python Standard Library modullari



📚 *GUI dasturlash*

	- GUI dasturlash yasash

	- JSON bilan ishlash

	- Klass yordamida o’yinlar yasash

	- CSV bilan ishlash

	- API bilan ishlash



📚 *SQL va uni Pythonda qo''lash*

	- Select, Update, Insert, Delete amallari

	- SQLni dasturlarda qo’llash



📚 *HTML va CSS*

	- HTML teglari bilan ishlash

	- table tegi bilan ishlash

	- form tegi bilan ishlash

	- CSS bilan ishash



📚 *Django freymvorki*

	- Django freymvorki va uning xususiyatlariga kirish

	- Django loyihasini sozlash

	- Django modellari va ma''lumotlar bazasining integratsiyasi

	- Dinamik veb sahifalar uchun Django shablonlari

	- Djangoda formalar va foydalanuvchi ma''lumotlarini qayta ishlash

	- Autentifikatsiya va foydalanuvchini boshqarish

	- URL yo’naltirish va HTTP so''rovlarini qayta ishlash



📚 *Django Rest freymvorki*

	- Django bilan RESTful API ishlab chiqish

	- Serializer

	- CRUD amallari

	- Autentifikatsiya va foydalanuvchini boshqarish

	- Token bilan ishlash

	- Postman yordamida test qilish','✅ *Python asoslari 1-qismi* nomzodning Python tilida dasturlashning muhim jihatlari bilan bog''liq kodlash vazifalarini bajarish qobiliyatini o''lchaydigan professional ishonchnomasi bo’lgan PCEP – Sertifikatlangan boshlang’ich darajadagi Python dasturchisi sertifikati (imtihon PCEP-30-0x) bilan moslash;\n\n 



✅ *Python asoslari 2-qismi* nomzodning Python tilida oʻrta darajadagi kodlash vazifalarini bajarish qobiliyatini oʻlchaydigan professional, yuqori stavkali ishonchnomasi boʻlgan PCAP – Python dasturlash boʻyicha Certified Associate sertifikati (Exam PCAP-31-0x) bilan moslash;\n\n



✅ *GUI dasturlash*da turli o''yinlar yaratish orqali ob''ektga yo''naltirilgan dasturlashni amaliy qo''llash;



✅ *Pythonda SQL* yordamida CRUD operatsiyalarini bajarishga o''rgatish;



✅ Veb-dasturlashning old tomoni uchun zarur bo''lgan CSS va HTML teglarini o''rgatish;



✅ Python veb dasturlash ikki qismga bo''lingan: *Django Framework* va *Django Rest Framework*. Bu bo''lim talabalarga ma''lumotlar bazasiga ega veb-ilovalar va API-larni yaratish, himoyalash va boshqarishni o''rgatish uchun mo''ljallangan.',1800000,'https://telegra.ph/file/1ed2732d276af0a239ca1.png','Python Asoslari va Django Freymvorki'),
 (3,'Python','Основы программирования. ООП. GUI приложений. Создание веб-приложений','ru','Основы Python и фреймворк Django это полноценный курс, который обеспечивает введение в фундаментальные концепции и методы программирования с использованием языка Python, наряду с углубленным изучением популярного веб-фреймворка Django.



Этот курс дает учащимся необходимые навыки программирования и знания для разработки веб-приложений и дает глубокое понимание синтаксиса Python, структур данных, потока управления и принципов объектно-ориентированного программирования. 



Кроме того, он раскрывает сильные возможности Django для создания надежных и масштабируемых веб-приложений, охватывая такие темы, как модели, представления, шаблоны, формы и интеграция баз данных. К концу курса участники получат прочные знания основ в области программировании на Python и смогут использовать фреймворк Django для создания динамичных и интерактивных веб-приложений.

','Благодаря навыкам, полученным в программировании на Python и платформе Django, учащиеся могут работать в качестве Python разработчиков, Django разработчиков, Full-stack разработчиков, разработчиков веб-приложений, аналитиков данных или даже работать над проектами во фрилансе.','Этот курс предназначен для начинающих разработчиков на Python и разработчиков среднего уровня.','Учебная программа предназначена для учеников старших классов средних школ, студентов техникумов, колледжей или университетов. Никаких предварительных знаний в области программирования не требуется.','📚 *Основы Python Часть 1*

    - Введение в Python и компьютерное программирование

    - Типы данных, переменные, основные операции ввода-вывода, базовые операторы

    - Логические значения, условное выполнение, циклы, списки и их обработка, логика и побитовые операции

    - Функции, кортежи, словари и обработка данных



📚 *Основы Python Часть 2*

    - Модули, пакеты и PIP

    - Исключения, String, методы String и List

    - Объектно-ориентированное программирование

    - Генераторы, итераторы и замыкания

    - Работа с файловой системой, деревьями каталогов и файлами

    - Выбранные модули стандартной библиотеки Python



📚 *Программирование с графическим интерфейсом*

    - Работа с JSON

    - Создание игр с использованием класса

    - Работа с CSV

    - Работа с API



📚 *SQL и его реализация на Python*

    - создание, чтение, модификация, удаление

    - применение SQL в программах



📚 *HTML и CSS*

    - работа с HTML-тегами.

    - работать с тегом таблицы

    - работа с тегом формы

    - работа с CSS



📚 *Веб-разработка на Python с использованием Django*

    - Введение в фреймворк Django и его возможности.

    - Индивидуальный проект Джанго

    - Модели Django и интеграция с базами данных

    - Шаблоны Django для динамических сайтов.

    - Формы и обработка пользовательского входа в Django

    - Аутентификация и управление пользователями

    - Маршрутизация URL-адреса и обработка HTTP-запроса



📚 *API в Django Rest Framework*

    - Разработка RESTful API с помощью Django

    - Сериализатор

    - CRUD-операции

    - Аутентификация и управление пользователями

    - Работа с токенами

    - Тестирование с помощью Postman','✅ *Основы Python часть 1* соответствует сертификату PCEP – Certified Entry-Level Python Programmer certification (Exam PCEP-30-0x), который представляет собой профессиональное удостоверение, оценивающее способность кандидата выполнять задачи по программированию, связанные с основами программирования на языке Python.



✅ *Основы Python часть 2*, соответствует сертификату PCAP – Certified Associate in Python Programming certification (Exam PCAP-31-0x), который представляет собой профессиональный сертификат с высокими ставками, который измеряет способность кандидата выполнять задачи программирования среднего уровня на языке Python.



✅Практическое применение объектно-ориентированного программирования путем создания различных игр в *графическом программировании*;



✅Обучение выполнению CRUD-операций с использованием *SQL на Python*;



✅Обучение тегам *CSS и HTML*, необходимым для веб-программирования;



✅Веб-разработка на Python разделена на две части: *Django Framework* и *Django Rest Framework*, которые предназначены для обучения студентов тому, как создавать, защищать и администрировать динамические веб-приложения и API.',1800000,'https://telegra.ph/file/1ed2732d276af0a239ca1.png','Основы Python и фреймворк Django'),
 (4,'Python','Basics of programming. OOP. GUI applications. Developing web apps','en','Python Essentials and Django Framework is a comprehensive course that provides an introduction to the fundamental concepts and techniques of programming using the Python language, along with an in-depth exploration of the popular Django web framework.



This course equips learners with essential programming skills and knowledge to develop web applications and gain a solid understanding of Python''s syntax, data structures, control flow, and object-oriented programming principles. 



Furthermore, it delves into Django''s powerful features for building robust and scalable web applications, covering topics such as models, views, templates, forms, and database integration. By the end of the course, participants will have a strong foundation in Python programming and be able to leverage the Django framework to create dynamic and interactive web applications.

','With the skills gained in Python programming and Django framework, learners can pursue roles as Python Developers, Django Developers, Full-stack Developers, Web Application Developers, Data Analyst, or even work on freelance projects.','This course is designed for Beginner and Intermediate level Python developers.','The curriculum is designed for upper secondary schools, technical schools, and colleges or universities. No prior knowledge of programming is required.','📚 *Python Essentials Part 1*

	- Introduction to Python and Computer Programming

	- Data Types, Variables, Basic Input Output Operations, Basic Operators

	- Boolean Values, Conditional Execution, Loops, Lists and List Processing, Logic, and Bitwise Operations

	- Functions, Tuples, Dictionaries, and Data Processing



📚 *Python Essentials Part 2*

	- Modules, Packages, and PIP

	- Exceptions, Strings, String and List Methods



📚 *Object Oriented Programming*

	- Generators, iterators, and closures

	- Working with filesystem, directory trees and files

	- Selected Python Standard Library modules



📚 *GUI programming*

	- Making GUI programming

	- Working with JSON

	- Class help making games

	- Working with CSV

	- Working with the API



📚 *SQL in Python*

	- CRUD operations

	- Application of SQL in programs



📚 *HTML and CSS*

	- Working with HTML tags

	- Work with the table tag

	- Work with form tag

	- Working with CSS



📚 *Django framework*

	- An introduction to the Django framework and its implications

	- Setting up a Django project

	- Django models and database integration

	- Django templates for dynamic web pages

	- Forms and data processing in Django

	- Authentication and user management

	- URL routing and handling HTTP requests



📚 *Django Rest framework*

	- RESTful API with Django

	- Serializer

	- CRUD operations

	- Authentication and user management

	- Working with tokens

	- Testing using Postman','✅ *Python Essentials Part 1* is aligned with PCEP – Certified Entry-Level Python Programmer certification (Exam PCEP-30-0x) which is a professional credential that measures the candidate''s ability to accomplish coding tasks related to the essentials of programming in the Python language.



✅ *Python Essentials Part 2* is aligned with PCAP – Certified Associate in Python Programming certification (Exam PCAP-31-0x) which is a professional, high-stakes credential that measures the candidate''s ability to perform intermediate-level coding tasks in the Python language.



✅ Practical application of object-oriented programming by creating various games in *GUI programming*;



✅ Teaching CRUD operations using *SQL in Python*;



✅ Teaching *CSS and HTML* tags which is necessary for front-end of web programming;



✅ Python Web Development is divided into two parts: *Django Framework* and *Django Rest Framework* which are designed to teach students how to build, secure, and administer dynamic, database-backed web applications and APIs.',1800000,'https://telegra.ph/file/1ed2732d276af0a239ca1.png','Python Essentials and Django Framework'),
 (5,'Php','PHP tilida veb-ilovalarni ishlab chiqish','uz','PHP va Laravel bilan veb ilovalarni yaratish kursi o’rganuvchilarni PHP va Laravel yordamida dinamik veb ilovalarni yaratish uchun zarur bo''lgan ko''nikmalar bilan ta’minlash uchun mo''ljallangan interaktiv va keng qamrovli dastur hisoblanadi.

Bazaviy va mukammal darajalarni o''z ichiga olgan kurs veb dasturlashning mashhur skript tili bo''lgan PHP va murakkab kodlash vazifalarini soddalashtiradigan mustahkam PHP freymvorki Laravelga kirish bilan boshlanadi. O’rganuvchilarning bilimi o''sib borishi bilan ular Laravelning MVC arxitekturasi, ma''lumotlar bazasi migratsiyasi, Eloquent ORM va o''rta dastur kabi murakkabroq mavzularni o''rganadilar. 

Qo''shimcha modullar marshrutlash, bleyd shablonlari, forma so''rovlari va Laravelning xavfsizlik xususiyatlarini chuqur o''rganishni ta''minlaydi. Kurs oxirida ishtirokchilar kengaytiriladigan va samarali veb dasturlash uchun PHP va Laravelning kuchidan foydalangan holda to''liq ishlaydigan veb ilovani ishlab chiqish, sinab ko''rish va joylashtirish imkoniyatiga ega bo''lishadi.

','Ushbu kurs PHP va Laravelga alohida e''tibor qaratgan holda veb dasturlash bilimlariga asos yaratadi, bu esa o’rganuvchilarga Full Stack Web Developers bo''lish imkonini beradi. Olingan ko''nikmalar va bilimlar senior veb dasturchi, dasturiy ta''minot injeneri yoki startaplar uchun texnik direktor kabi ilg''or rollar uchun qadam bo''lib xizmat qilishi mumkin.','Ushbu kursning mo’ljallangan auditoriyasi veb dasturlashga qiziqqan yangi boshlovchilar, PHP va Laravelni o''z ichiga olgan holda o''z bilim va ko''nikmalarini kengaytirmoqchi bo''lgan mavjud dasturchilar va keng qo''llaniladigan dasturlash tili va freymvorklarida amaliy ko''nikmalarga ega bo''lishni istagan kompyuter fanlari talabalarini o''z ichiga oladi.

','PHP yoki Laravel bilan oldindan tajribaga ega bo''lish shart emas, chunki kurs o''quvchilarni bazadan toki murakkab mavzularga yo''naltirish uchun mo''ljallangan. Biroq, ba''zi tajribaga ega bo''lganlar uchun ham o''z malakalarini oshirish va kengaytirishda foydali bo''lishi mumkin.','📚 *Part 1: PHP va MySQL*

	- PHP va veb dasturlashga kirish

	- Funksiyalar

	- Ma''lumotlar formati va tiplari

	- Veb funksiya imkoniyatlari

	- Obyektga yo''naltirilgan dasturlash

	- Xavfsizlik

	- I/O

	- Satrlar va patternlar

	- Massivlar

	- PHP and MySQL

	- Xatoliklar bilan ishlash



📚 *Part 2: Laravel Freymvorki*

	- Laravel haqida tushuncha

	- Marshrutlash

	- Kontrollerlar

	- Ma''lumotlar bazasi

	- Aqlli ORM

	- Hodisalar

	- Fayllarni saqlash

	- Foydalanuvchi interfeysi

	- Log jurnaliga yozish

	- Mail

	- Bildirishnomalar

	- Xavfsizlik

	- Sessiyalar

	- Vazifalarni rejalashtirish

	- Veb soketlar

	- Nosozliklarni tuzatish va xatoliklarni qayta ishlash



📚 *Part 3: Haqiqiy loyihalar*

	- Bloglar platformasini yaratish

	- Elektron tijorat saytini yaratish

	- Joylashtirish va yakuniy fikrlar','✅ Veb dasturlash uchun PHP va Laravel asoslari haqida keng qamrovli tushunchaga ega bo''lish



✅ Laravel migratsiyalari va Eloquent ORM yordamida ma''lumotlar bazalarini yaratish va boshqarishni o''rganish



✅ Laravelning MVC arxitekturasini va samarali marshrutlash sxemalarini qanday yaratishni tushunish



✅ Samarali UI ishlab chiqish uchun Master Laravel''s Blade shablonlash mexanizmi



✅ Laravelning ichki o‘rnatilgan funksiyalaridan foydalangan holda forma so‘rovlari va tekshirishni boshqarishni o‘rganish



✅ Veb-ilovalarni himoya qilish uchun Laravelning xavfsizlik xususiyatlarini qanday qo''llashni tushunish



✅ PHP va Laravel yordamida to''liq veb-ilovani ishlab chiqish, sinab ko''rish va joylashtirish



✅ Veb dasturlashda muammolarni hal qilish va kodlash samaradorligini oshirish

',1800000,'https://telegra.ph/file/0e21628945a0fe4bd0417.png','PHP va Laravel bilan veb ilovalarni yaratish'),
 (6,'Php','Разработка веб-приложений на языке php','ru','Курс «Создание веб-приложений с помощью PHP и Laravel» представляет собой интерактивную комплексную программу, предназначенную для того, чтобы дать учащимся навыки, необходимые для создания динамических веб-приложений с использованием PHP и Laravel.



Охватывая как основы, так и продвинутые аспекты, курс начинается с введения в PHP язык программирования, подходящий для веб-разработки, и Laravel, которая упрощает сложные задачи кодирования. По мере обучения студенты углубляются в более сложные темы, такие как архитектура MVC Laravel, миграция баз данных, Eloquent ORM и посредники (Middleware). 



Дополнительные модули обеспечивают углубленное изучение маршрутизации, шаблонов Blade, запросов форм и функций безопасности Laravel. К концу курса участники должны уметь разрабатывать, тестировать и развертывать полнофункциональное веб-приложение с использованием PHP и Laravel, используя возможности этих инструментов для масштабируемой и эффективной веб-разработки.

','Этот курс закладывает основу для карьеры в веб-разработке с особым акцентом на PHP и Laravel, что позволяет учащимся стать полнофункциональными веб-разработчиками. Приобретенные навыки и знания также могут послужить трамплином для более продвинутых должностей, таких как старший веб-разработчик, инженер-программист или даже технический директор стартапов.

','Целевая аудитория этого курса включает новичков, интересующихся веб-разработкой, существующих разработчиков, желающих расширить свой набор навыков, включив в него PHP и Laravel, а также студентов, изучающих информатику, желающих приобрести практические навыки в широко используемом языке программирования и среде программирования.

','Никакого предварительного опыта работы с PHP или Laravel не требуется, поскольку курс предназначен для того, чтобы помочь учащимся перейти от основ к более сложным темам. Однако те, у кого есть некоторый опыт, также могут найти это полезным для совершенствования и расширения своих навыков.

','📚 *Часть 1: PHP и MySQL*

	- Введение в PHP и веб-разработку

	- Функции

	- Формат и типы данных

	- Веб-функции

	- Объектно-ориентированного программирования

	- Безопасность

	- Ввод/Вывод

	- Строки и Шаблоны

	- Массивы

	- PHP и MySQL

	- Обработка ошибок



📚 *Часть 2: Фреймворк Laravel*

	- Введение в Laravel 

	- Маршрутизация

	- Контроллеры

	- База данных

	- Eloquent ORM

	- События

	- Хранилище файлов

	- Фронтенд

	- Логирование

	- Почта

	- Уведомления

	- Безопасность

	- Сессии

	- Планирование задач

	- Веб-сокеты

	- Отладка и Обработка Ошибок



📚 *Часть 3:Реальные проекты*

	- Создание платформы для блогов

	- Создание интернет-магазина

	- Развертывание и заключительные мысли','✅ Получить полное понимание PHP и фреймворка Laravel для веб-разработки



✅ Узнать, как создавать и управлять базами данных с использованием миграций и Eloquent ORM в Laravel



✅ Понимать архитектуру MVC в Laravel и способы создания эффективных маршрутов



✅ Освоить шаблонизатор Blade в Laravel для эффективной разработки пользовательского интерфейса



✅ Узнать, как обрабатывать запросы и проводить валидацию форм с помощью встроенных функций Laravel



✅ Изучить, как применять средства безопасности Laravel для защиты веб-приложений



✅ Разрабатывать, тестировать и развертывать полноценное веб-приложение с использованием PHP и Laravel



✅ Улучшить навыки решения проблем и эффективности кодирования в веб-разработке.

',1800000,'https://telegra.ph/file/0e21628945a0fe4bd0417.png','Создание веб-приложений с помощью PHP и Laravel'),
 (7,'Php','Development of web applications in PHP language','en','The Building Web Applications with PHP and Laravel course is an interactive and comprehensive program designed to equip learners with the skills needed to create dynamic web applications using PHP and Laravel.



Covering both the basics and advanced aspects, the course begins with an introduction to PHP, a popular scripting language suitable for web development, and Laravel, a robust PHP framework that simplifies complex coding tasks. As students progress, they delve into more complex topics such as Laravel''s MVC architecture, database migrations, Eloquent ORM, and middleware. 



Additional modules provide in-depth exploration of routing, blade templating, form requests, and Laravel''s security features. By the end of the course, participants should be able to develop, test, and deploy a fully functional web application using PHP and Laravel, harnessing the power of these tools for scalable and efficient web development.

','This course sets the foundation for a career in web development, with specific emphasis on PHP and Laravel, enabling learners to become Full Stack Web Developers. The acquired skills and knowledge can also serve as a stepping stone for advanced roles such as Senior Web Developer, Software Engineer, or even CTO for startups.

','The target audience for this course includes beginners interested in web development, existing developers looking to expand their skill set to include PHP and Laravel, and computer science students wanting to acquire practical skills in a widely-used programming language and framework.

','No prior experience with PHP or Laravel is required, as the course is designed to guide learners from the basics to more advanced topics. However, those with some experience may also find it useful for refining and expanding their skills.','📚 *Part 1: PHP and MySQL*

	- Introduction to PHP and Web Development

	- VFunctions

	- Data Format & Types

	- Web Features

	- Object Oriented Programming

	- Security

	- I/O

	- Strings & Patterns

	- Arrays

	- PHP and MySQL

	- Error Handling



📚 *Part 2: Laravel Framework*

	- Introduction to Laravel

	- Routing

	- Controllers

	- Database

	- Eloquent ORM

	- Events

	- File Storage

	- Frontend

	- Logging

	- Mail

	- Notifications

	- Security

	- Sessions

	- Task Scheduling

	- Websockets

	- Debugging and Error Handling



📚 *Part 3: Real-world Projects*

	- Building a Blogging Platform

	- Building an E-commerce Site

	- Deployment and Final Thoughts','✅ Gain a comprehensive understanding of PHP and Laravel framework for web development



✅ Learn to create and manage databases using Laravel''s migrations and Eloquent ORM



✅ Understand Laravel''s MVC architecture and how to create effective routing schemes



✅ Master Laravel''s Blade templating engine for efficient UI development



✅ Learn to handle form requests and validation using Laravel''s built-in features



✅ Understand how to apply Laravel''s security features to protect web applications



✅ Develop, test, and deploy a complete web application using PHP and Laravel



✅ Enhance problem-solving skills and coding efficiency in web development

',1800000,'https://telegra.ph/file/0e21628945a0fe4bd0417.png','Building Web Applications with PHP and Laravel'),
 (8,'Flutter','Turli xil operatsion tizimlar uchun ilovalarni ishlab chiqish','uz','Flutter va Dart yordamida ilovalarni ishlab chiqish kursi mashhur Flutter SDK va Dart dasturlash tilini chuqur va har tomonlama tushunish imkonini beradi. Ushbu kurs o’rganuvchilarga oddiy kod bazasidan foydalangan holda Android va iOS platformalari uchun chiroyli, samarali va funksional mobil ilovalarni yaratish jarayoni bo''yicha yo''l-yo''riq beradi.



Dart tiliga kirish, Flutter vidjetlarini tushunish, holat boshqaruvi, tashqi API bilan ishlash, kamera va joylashuv kabi qurilma xususiyatlarini joriy etish, testdan o‘tkazish va ilovalarni tayyor qilib chiqarishni o‘z ichiga oladi. Kurs oxirida o’rganuvchilar Flutter va Dartdan foydalangan holda sifatli, haqiqiy hayotdagi ilovalar va tayyor mahsulot holatiga kelgan mobil ilovalarni yaratish uchun malakali va yaxshi ko’nikmaga ega bo''ladilar.','Ushbu keng qamrovli kursni yakunlash Flutter dasturchilari, mobil ilovalar dasturchisi yoki platformalararo dasturchi sifatida texnologik startaplarda, tashkil etilgan dasturiy ta''minot kompaniyalarida yoki frilanser sifatida ishlash imkoniyatiga ega bo''lish uchun yo''l ochadi.','Ushbu kurs boshlang''ich va o''rta darajadagi mobil ilovalarni ishlab chiquvchilar uchun mo''ljallangan.','O’rganuvchilar dasturlash konseptsiyalari haqida asosiy tushunchaga ega bo''lishlari va mobil dasturlashga ishtiyoqi bo''lishi kutiladi; Dart bo''yicha oldindan bilimlar foydali bo’ladi, lekin majburiy emas, chunki kurs uni boshlang’ich bilimlar bilan o’rgatadi.','📚 *1-qism. Dartga kirish*

	- Dartda obyektga yo''naltirilgan dasturlash

	- Dartda asinxron dasturlash

	- Dart kutubxonalari va paketlari



📚 *2-qism. Flutter freymvorki*

	- Flutter freymvorki

	- Flutter asoslari

	- Flutter vidjetlari

	- Flutterda holat boshqaruvi

	- API va Firebase bilan ishlash

	- Flutterda Firebase xizmatlari

	- Ichki xususiyatlarga kirish

	- Flutterda test qilish

	- Onlayn storega joylashtirish



📚 *3-qism. Haqiqiy loyihalar*

	- Loyihani rejalashtirish

	- To''liq dasturni yaratish

	- Ilovani sinab ko''rish

	- Onlayn storega joylashtirish

	- API va Firebase bilan ishlash

	- Joylashtirishdan keyingi tahlil va yangilanishlar','✅  Dart dasturlash tilining asosiy va ilg‘or xususiyatlarini o‘rganish.

 

✅  Flutter SDK va uning vidjetga asoslangan arxitekturasini tushunish.

 

✅  Vizual jihatdan chiroyli, samarali va funksional platformalararo mobil ilovalarni ishlab chiqish.

 

✅  Qurilmaning ichki xususiyatlari va tashqi APIlarni qo’llash.

 

✅  Flutter ilovasida holat boshqaruvi yechimlarini tushunish va qo‘llash

 

✅  Ilova ishonchliligi va unumdorligini ta''minlash uchun test qilish usullarini o''rganish

 Google Play Store va Apple App Storega ilovalarni joylashtirish jarayonini tushunish',1800000,'https://telegra.ph/file/7aa34eeab125b70322d44.png','Flutter va Dart yordamida ilovalarni ishlab chiqish
'),
 (9,'Flutter','Разработка приложений под различные операционные системы','ru','Курс "Разработка Приложений с Помощью Flutter и Dart" обеспечивает глубокое и всестороннее понимание популярного Flutter SDK и языка программирования Dart. Этот курс поможет пройти слушателям через процесс создания красивых, производительных и функциональных мобильных приложений как для платформ Android, так и для iOS с использованием единой кодовой базы.

Темы,  в курсе, включают введение в язык Dart, понимание виджетов Flutter, управление состоянием, работу с внешними API, реализацию функций устройства, таких как камера и местоположение, тестирование и развертывание приложений. К концу курса студенты будут владеть навыками создания качественных, реальных и готовых к производству мобильных приложений с использованием Flutter и Dart.

','Прохождение этого комплексного курса открывает путь к карьере разработчиков Flutter, мобильных приложений или кроссплатформенных приложений с возможностью работы в технологических стартапах, известных компаниях-разработчиках программного обеспечения или в качестве фрилансеров.

','Этот курс предназначен для разработчиков мобильных приложений начального и среднего уровня.

','Ожидается, что учащиеся будут обладать базовым пониманием концепций программирования и энтузиазмом в отношении мобильной разработки; владение предварительными знаниями Dart желательно, но не обязательно, поскольку курс охватывает его с основ.','📚 *Часть 1: Программирование Dart *

	- Введение в Dart

	- Объектно-ориентированное программирование в Dart

	- Асинхронное программирование в Dart

	- Библиотеки и пакеты Dart



📚 *Часть 2: Фреймворк Flutter *

	- Фреймворк Flutter 

	- Основы Flutter 

	- Виджеты Flutter 

	- Управление состоянием во Flutter

	- Работа с API и Firebase

	- Сервисы Firebase в Flutter

	- Доступ к встроенным функциям

	- Тестирование во Flutter

	- Развертывание



📚 *Часть 3: Реальные проекты*

	- Планирование проекта

	- Создание полноценного приложения

	- Тестирование приложения

	- Развертывание

	- Работа с API и Firebase

	- Анализ и обновления после развертывания','✅ Изучите основы и продвинутый возможности языка программирования Dart.



✅ Изучите Flutter SDK и его архитектуру на основе виджетов.



✅ Разрабатывайте визуально привлекательные, производительные и функциональные кроссплатформенные мобильные приложения.



✅ Реализовать собственные функции устройства и внешние API.



✅ Понимать и применять решения по управлению состоянием в приложении Flutter



✅ Изучите методологии тестирования для обеспечения надежности и производительности приложений



✅ Понять процесс развертывания приложений в Google Play Store и Apple App Store.',1800000,'https://telegra.ph/file/7aa34eeab125b70322d44.png','Разработка Приложений с Помощью Flutter и Dart'),
 (10,'Flutter','Development of applications for various operating systems','en','The Apps Development with Flutter and Dart course provides an in-depth and comprehensive understanding of the popular Flutter SDK and the Dart programming language. This course will guide learners through the process of building beautiful, performant, and functional mobile applications for both Android and iOS platforms using a single codebase.



Topics covered in the course include an introduction to Dart language, understanding Flutter widgets, state management, working with external APIs, implementing device features like camera and location, testing, and deploying the apps. By the end of the course, students will be proficient and well-equipped with the skills to create quality, real-world, and production-ready mobile applications using Flutter and Dart.

','Completion of this comprehensive course paves the way for careers as Flutter developers, mobile app developers, or cross-platform app developers, with opportunities to work in tech startups, established software companies, or as freelancers.

','This course is designed for Beginner and Intermediate level mobile apps developers.','Learners are expected to have basic understanding of programming concepts and enthusiasm for mobile development; prior knowledge of Dart is beneficial but not necessary as the course covers it from the basics.','📚 *Part 1: Dart Programming*

	- Introduction to Dart

	- Object-Oriented Programming in Dart

	- Asynchronous Programming in Dart

	- Dart Libraries and Packages



📚 *Part 2: Flutter Framework*

	- Flutter Framework

	- Flutter Basics

	- Flutter Widgets

	- State Management in Flutter

	- Working with APIs and Firebase

	- Firebase Services in Flutter

	- Accessing Native Features

	- Testing in Flutter

	- Deployment



📚 *Part 3: Real-world Projects*

	- Project Planning

	- Building a Complete App

	- Testing the App

	- Deployment

	- Working with APIs and Firebase

	- Post-deployment Analysis and Updates','✅ Learn the basics and advanced features of the Dart programming language;



✅ Understand the Flutter SDK and its widget-based architecture;



✅ Develop visually appealing, performant, and functional cross-platform mobile applications;



✅ Implement native device features and external APIs;



✅ Understand and apply state management solutions in a Flutter app;



✅ Learn testing methodologies to ensure app reliability and performance;



✅ Understand the process of deploying apps to the Google Play Store and Apple App Store.

',1800000,'https://telegra.ph/file/7aa34eeab125b70322d44.png','Apps Development with Flutter and Dart
');
COMMIT;
"""
    ],
    4: [
        """ALTER TABLE open_lesson_users ADD COLUMN date TIMESTAMP default now()"""
    ]
}