import datetime
import logging
from ctypes import Union
from random import random, randint, choice
from typing import Union

import asyncpg
from aiogram.types import User
from asyncpg import Pool, Connection

from data import config
from utils.db_api.migrations.postgresql import migrations


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetchall: bool = False,
                      fetchone: bool = False,
                      fetchval: bool = False,
                      execute: bool = False
                      ):
        result = None
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetchone:
                    result = await connection.fetchrow(command, *args)
                if fetchall:
                    result = await connection.fetch(command, *args)
                if fetchval:
                    result = await connection.fetchval(command, *args)
                if execute:
                    result = await connection.execute(command, *args)

            return result

    async def migrate(self):
        # create initial tables
        for sql in migrations[0]:
            await self.execute(sql, execute=True)

        last_version = await self.last_migrate_version() or 0
        for version, sqls in migrations.items():
            if version <= last_version:
                continue

            for sql in sqls:
                print(f'============{sql}==============')
                await self.execute(sql, execute=True)

            await self.insert_migrations(version)

    async def last_migrate_version(self):
        sql = "SELECT max(version) from migrations"
        return await self.execute(sql, fetchval=True)

    async def if_exist_migrations(self, version):
        sql = 'select * from migrations where version=$1'
        return True if await self.execute(sql, version, fetchone=True) else False

    async def insert_migrations(self, version):
        if not await self.if_exist_migrations(version):
            sql = "insert into migrations (version) values($1)"
            await self.execute(sql, version, execute=True)

    # EXTRA FUNCTIONS
    @staticmethod
    def format_args(parameters: dict):
        sql = " AND ".join(
            [f"{param} = ${number}" for number, param in enumerate(parameters.keys(), 1)]
        )
        return sql, list(parameters.values())

    # USERS
    async def add_user(self, id: int, name: str, email: str = None):
        sql = """INSERT INTO users(id, name, email) VALUES($1,$2,$3)"""
        result = await self.execute(sql, id, name, email, execute=True)
        print(result)
        return result

    async def is_user_registered(self, id):
        sql = "SELECT count(*) FROM users WHERE id=$1 and phone is not NULL"
        val = await self.execute(sql, id, fetchval=True)
        return val > 0

    async def select_all_users(self):
        sql = """SELECT * FROM users"""
        return await self.execute(sql, fetchall=True)

    async def select_user(self, **kwargs):
        sql, parameters = self.format_args(kwargs)
        sql = f"""SELECT * FROM users {sql}"""
        return await self.execute(sql, *parameters, fetchone=True)

    async def select_user_language(self, id):
        sql = f"""SELECT language FROM users WHERE id=$1"""
        row = await self.execute(sql, id, fetchone=True)
        if not row:
            return 'uz'
        return row[0]

    async def select_count(self):
        return await self.execute("""SELECT count(*) FROM users""", fetchval=True)

    async def update_user(self, **kwargs):
        id = kwargs['id']
        kwargs.pop('id')
        sql, parameters = self.format_args(kwargs)
        parameters.append(id)
        sql = sql.replace('AND', ',')
        sql = f"""UPDATE users SET {sql} WHERE id=${len(parameters)}"""
        # print(sql)
        # print(parameters)
        try:
            await self.execute(sql, *parameters, execute=True)
        except Exception as e:
            print(e)

    async def delete_user(self, id):
        sql = """DELETE FROM users WHERE id=$1"""
        return await self.execute(sql, id, execute=True)

    async def delete_all(self):
        sql = """DELETE FROM users"""
        await self.execute(sql, execute=True)

    # COURSES
    async def select_course_by_name(self, user_id, name):
        sql = """
            SELECT id, name, description, about,career, for_whom,requirements,image, official_name 
            FROM courses 
            WHERE lower(name)=lower($1) and language=(select coalesce(language,'uz') from users where id=$2)"""
        return await self.execute(sql, name, user_id, fetchone=True)

    async def select_course_objective(self, user_id, course):
        sql = """
            SELECT objective 
            FROM courses 
            WHERE language=(select COALESCE(language,'uz') from users where id=$1) and lower(name)=lower($2)"""
        return await self.execute(sql, user_id, course, fetchone=True)

    async def select_course_curriculum(self, user_id, course):
        sql = """
            SELECT content 
            FROM courses 
            WHERE language=(select COALESCE(language,'uz') from users where id=$1) and lower(name)=lower($2)"""
        return await self.execute(sql, user_id, course, fetchone=True)

    async def select_courses(self, only_name=False, only_desc=False,
                             only_about=False,
                             inline_mode=False):
        user_id = User.get_current().id
        if only_name:
            sql = "SELECT name FROM courses WHERE language=(select COALESCE(language,'uz') from users where id=$1)"
            return await self.execute(sql, user_id, fetchall=True)
        if only_desc:
            sql = "SELECT name, description, official_name FROM courses WHERE language=(select COALESCE(language,'uz') from users where id=$1)"
            return await self.execute(sql, user_id, fetchall=True)
        if only_about:
            sql = "SELECT about FROM courses WHERE language=(select COALESCE(language,'uz') from users where id=$1)"
            return await self.execute(sql, user_id, fetchall=True)
        if inline_mode:
            sql = "SELECT id,name,image, description, official_name FROM courses WHERE language=(select COALESCE(language,'uz') from users where id=$1)"
            return await self.execute(sql, user_id, fetchall=True)

    # OPEN LESSONS
    async def insert_open_lesson(self, course, date, language, format):
        sql = """INSERT INTO open_lessons(course, date, language, format)
        VALUES($1,$2,$3,$4) RETURNING id"""
        return await self.execute(sql, course,date,language,format, fetchone=True)

    async def select_open_lesson(self, course):

        sql = f"""SELECT to_char(o.date,'DD.MM.YY') as date, to_char(o.date,'HH24:MI') as time, o.language, c.official_name
                FROM open_lessons o
                LEFT JOIN courses c ON lower(c.name) = lower(o.course) and c.language = o.language
                WHERE lower(course) = lower($1)
                ORDER by date DESC
                LIMIT 1"""

        return await self.execute(sql, course, fetchone=True)

    # OPEN LESSON USERS
    async def insert_open_lesson_users(self, user_id, open_lesson_id=None, course_name=None):

        if not open_lesson_id and not course_name:
            raise Exception("at least two arguments should be provided")
        if not course_name:
            sql = "INSERT INTO open_lesson_users(user_id,open_lesson_id) VALUES($1,$2)"
            result = await self.execute(sql, user_id, open_lesson_id, execute=True)
        elif not open_lesson_id:
            sql = """INSERT INTO open_lesson_users(user_id, course_name)
            VALUES($1,$2)"""
            result = await self.execute(sql, user_id, course_name, execute=True)
        else:
            sql = """INSERT INTO open_lesson_users(user_id,open_lesson_id, course_name)
            VALUES($1,$2,$3)"""
            result = await self.execute(sql, user_id, open_lesson_id, course_name, execute=True)
        print("result: ", result)

    async def get_open_lesson_users(self, course=None):
        if not course:
            sql = """SELECT o.course_name, u.name,u.phone, u.id, to_char(s.date,'DD.MM.YY') as date, to_char(s.date,'HH24:MI') as time
                FROM open_lesson_users o
                LEFT JOIN users u ON u.id=o.user_id
                LEFT JOIN open_lessons s ON s.id=o.open_lesson_id"""
            return await self.execute(sql, fetchall=True)
        else:
            sql = """SELECT o.course_name, u.name,u.phone, u.id, to_char(s.date,'DD.MM.YY') as date, to_char(s.date,'HH24:MI') as time
                FROM open_lesson_users o
                LEFT JOIN users u ON u.id=o.user_id
                LEFT JOIN open_lessons s ON s.id=o.open_lesson_id
                WHERE o.course_name = $1"""
            return await self.execute(sql, course, fetchall=True)

    #     SELECTION TABLE
    async def is_contest_started(self):
        sql = "SELECT status FROM selection"
        row = await self.execute(sql, fetchone=True)
        return row['status']

    async def start_contest(self):
        sql = "UPDATE  selection SET status=True"
        await self.execute(sql, execute=True)
        sql = "UPDATE  users SET is_participant = False"
        await self.execute(sql, execute=True)

    async def stop_contest(self):
        sql = "UPDATE  selection SET status=False"
        await self.execute(sql, execute=True)

    async def start_user_contest(self):
        user_id = User.get_current().id
        sql = "UPDATE  users SET is_participant = True WHERE id=$1"
        await self.execute(sql, user_id, execute=True)

    async def is_contest_winner(self):
        user_id = User.get_current().id
        sql = "SELECT count(*) FROM users WHERE id=$1 and is_winner=True"
        val = await self.execute(sql, user_id, fetchval=True)
        return val > 0

    async def select_random_user(self):
        sql = "SELECT id,name,phone FROM users WHERE is_participant = True and is_winner = False"
        rows = await self.execute(sql, fetchall=True)
        if not rows:
            return None
        selected_row = choice(rows)
        sql = "UPDATE  users SET is_winner=True WHERE id=$1"
        await self.execute(sql, selected_row['id'],execute=True)
        return selected_row

    async def contest_participants(self):
        sql = "SELECT id,name,phone,is_winner FROM users WHERE is_participant = True"
        return await self.execute(sql, fetchall=True)

    async def select_users_by_group(self, group):
        sql = "SELECT id,name,phone,is_winner FROM users WHERE group_name =$1"
        return await self.execute(sql, group, fetchall=True)

    async def select_users_by_date(self, date):
        sql = "SELECT id,name,phone,is_winner FROM users WHERE date(created_at) =$1"
        return await self.execute(sql, date, fetchall=True)

    async def number_of_users(self, **kwargs):
        sql, parameters = self.format_args(kwargs)
        sql = "WHERE " + sql if sql else ''
        sql = f"""SELECT count(*) FROM users {sql}"""
        return await self.execute(sql, *parameters, fetchval=True)


db = Database()


async def test_users():

    # USER
    user_id = randint(1, 1000_000)
    name = choice(['otabek', 'oybek', "ulug'bek"])
    print(f'Adding user without phone: {user_id}', 'Result: ', end=' ')
    await db.add_user(user_id,name )
    print(f'Checking user is not registered')
    assert (await db.is_user_registered(user_id)) is False
    print('Adding user phone')
    await db.update_user(id=user_id, phone='1234567')
    print(f'Checking user is registered')
    assert (await db.is_user_registered(user_id)) is True
    print('Adding user language')
    lang = choice(['uz','ru','en'])
    await db.update_user(id=user_id, language=lang)
    print('Getting language')
    await db.select_user_language(user_id) == lang
    print(f'Check if user name is {name}')
    assert (await db.select_user(id=user_id))['name'] == name
    print(f'Delete user: {user_id}')
    await db.delete_user(user_id)
    print('Check if user is deleted')
    assert (await db.select_user(id=user_id)) is None

    # print('Deleting all users')
    # await db.delete_all()
    # assert (await db.select_count()) == 0


async def test_courses():
    user_id = randint(1,1000_000)

    name = choice(['Anvar','Otabke','Jasur'])
    language = choice(['ru','uz', 'en'])
    print(f'Adding user\nid:{user_id}, name:{name}, language: {language}')
    await db.add_user(user_id, name)
    await db.update_user(id=user_id,language=language)

    print('Only courses name')
    names = await db.select_courses(only_name=True)
    for name in names:
        print(name)
    print('Only courses description')
    names = await db.select_courses(only_desc=True)
    for name in names:
        print(name)
    print('Only courses about')
    names = await db.select_courses(only_about=True)
    for name in names:
        print(name)
    print('Courses inline mode')
    names = await db.select_courses(inline_mode=True)
    for name in names:
        print(name)

    course = await db.select_course_by_name(user_id, 'python')
    print('Get python course\n', course)

    objective = await db.select_course_objective(user_id, 'python')
    print('Python objective\n', objective)
    curriculum = await db.select_course_curriculum(user_id, 'python')
    print('curriculum\n', curriculum)
    await db.delete_user(user_id)


async def test_open_class():
    course = choice(['python', 'php', 'flutter'])
    language = choice(['ru', 'en', 'uz'])
    format = choice(['online', 'offline'])
    row = await db.insert_open_lesson(course, datetime.datetime.now(), language,format)
    open_lesson_id = row['id']
    print(f'Inserting open lesson {course}, {language}, {format} id:{open_lesson_id}')
    print('Chechking inserted courses')
    rows = await db.select_open_lesson(course)
    print('Open lesson list:\n', rows)
    user_id = randint(1,1000_000)
    name = choice(['Otabek', 'Oybek', 'Anvar', 'Bekzod'])
    await db.add_user(user_id, name)
    await db.update_user(id=user_id, language=language)

    await db.insert_open_lesson_users(user_id,open_lesson_id,course_name=course)
    print('User who are registered to open lessons')
    rows = await db.get_open_lesson_users()
    for row in rows:
        print(rows)


if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(db.connect())
    loop.run_until_complete(db.migrate())
    loop.run_until_complete(test_open_class())
