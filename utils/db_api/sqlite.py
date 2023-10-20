import sqlite3

from utils.db_api.migrations.sql import migrations


class Database:

    def __init__(self, path_to_db="data/main.db"):
        self.db = path_to_db
        self.migrate()

    def migrate(self):
        # create initial tables
        for sql in migrations[0]:
            self.execute(sql, commit=True)
        # migration
        self.insert_migrations(0)
        last_version = self.last_migrate_version()
        for version, sqls in migrations.items():
            if version == 0 or version <= last_version:
                continue

            for sql in sqls:
                self.execute(sql, commit=True)
            self.insert_migrations(version)

    def last_migrate_version(self):
        sql = "SELECT max(version) from migrations"
        return self.execute(sql, fetchone=True)[0]

    def insert_migrations(self, version):
        sql = "insert or replace into migrations (version) values(?)"
        self.execute(sql, parameters=(version,), commit=True)



    @property
    def connection(self):
        return sqlite3.connect(self.db)

    def execute(self, sql:str, parameters: tuple = tuple(), fetchone=False,
                fetchall=False, commit=False):

        connection = self.connection
        connection.set_trace_callback(self.logger)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)

        data = None
        if commit:
            connection.commit()

        if fetchone:
            data = cursor.fetchone()

        if fetchall:
            data = cursor.fetchall()

        connection.close()
        return data

    def logger(self, statement):
        print(f'''
_______________________________________
{statement}
_______________________________________
''')


    # EXTRA FUNCTIONS
    def format_args(self, parameters: dict):
        sql =" AND ".join(
            [f"{param} = ?" for param in parameters]
        )
        parameters = list(parameters.values())
        return sql, parameters

    # USERS
    def add_user(self, id:int, name:str, email:str = None):
        sql = """INSERT INTO users(id, name, email) VALUES(?,?,?)"""

        parameters = (id, name, email)
        self.execute(sql, parameters, commit=True)

    def is_user_registered(self, id):
        sql = "SELECT count(*) FROM users WHERE id=? and phone is not NULL"
        row = self.execute(sql,(id,), fetchone=True)
        return row[0] > 0

    def select_all_users(self):
        sql = """SELECT * FROM users"""
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql, parameters = self.format_args(kwargs)
        sql = f"""SELECT * FROM users WHERE {sql}"""
        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_user_language(self, id):
        sql = f"""SELECT language FROM users WHERE id=?"""
        row = self.execute(sql, (id, ), fetchone=True)
        if not row:
            return None
        return row[0]


    def select_count(self):
        return self.execute("""SELECT count(*) FROM users""", fetchone=True)

    def update_user(self, **kwargs):
        id = kwargs['id']
        kwargs.pop('id')
        sql, parameters = self.format_args(kwargs)
        parameters.append(id)
        sql = sql.replace('AND', ',')
        sql = f"""UPDATE users SET {sql} WHERE id=?"""
        try:
            self.execute(sql, parameters, commit=True)
        except Exception as e:
            print(e)

    def delete_user(self, id):
        sql = """DELETE users WHERE id=?"""
        self.execute(sql, parameters=(id,), commit=True)

    def delete_all(self):
        sql = """DELETE FROM users"""
        self.execute(sql, commit=True)

    # COURSES
    def select_course_by_name(self, user_id, name):
        sql = """
            SELECT id, name, description, about,career, for_whom,requirements,image, official_name 
            FROM courses 
            WHERE lower(name)=lower(?) and language=(select language from users where id=?)"""
        return self.execute(sql, parameters=(name,user_id), fetchone=True)

    def select_course_objective(self, user_id, course):
        sql = """
            SELECT objective 
            FROM courses 
            WHERE language=(select language from users where id=?) and lower(name)=lower(?)"""
        return self.execute(sql, parameters=(user_id, course), fetchone=True)

    def select_course_curriculum(self, user_id, course):
        sql = """
            SELECT content 
            FROM courses 
            WHERE language=(select language from users where id=?) and lower(name)=lower(?)"""
        return self.execute(sql, parameters=(user_id,course), fetchone=True)

    def select_courses(self, user_id, only_name=False, only_desc=False,
                       only_about=False,
                       inline_mode=False):

        if only_name:
            sql = "SELECT name FROM courses WHERE language=(select language from users where id=?)"
            return self.execute(sql, parameters=(user_id,), fetchall=True)
        if only_desc:
            sql = "SELECT name, description, official_name FROM courses WHERE language=(select language from users where id=?)"
            return self.execute(sql, parameters=(user_id,), fetchall=True)
        if only_about:
            sql = "SELECT about FROM courses WHERE language=(select language from users where id=?)"
            return self.execute(sql, parameters=(user_id,), fetchall=True)
        if inline_mode:

            sql = "SELECT id,name,image, description, official_name FROM courses WHERE language=(select language from users where id=?)"
            return self.execute(sql, parameters=(user_id,), fetchall=True)

    # OPEN LESSONS
    def select_open_lesson(self, course):

        sql = f"""SELECT strftime('%d.%m.%Y',o.date) as date, strftime('%H:%M',o.date) as time, o.language, c.official_name
                FROM open_lessons o
                LEFT JOIN courses c ON lower(c.name) = lower(o.course) and c.language = o.language
                WHERE lower(course) = lower(?)
                ORDER by date DESC
                LIMIT 1"""

        sql = sql.replace('#condition', 'course_id=(select id from courses where name=?)')
        return self.execute(sql, parameters=(course,), fetchone=True)

    # OPEN LESSON USERS
    def insert_open_lesson_users(self, user_id, open_lesson_id=None, course_name=None):
        if not open_lesson_id and not course_name:
            raise Exception("at least two arguments should be provided")
        if open_lesson_id:
            sql = "INSERT INTO open_lesson_users(user_id,open_lesson_id) VALUES(?,?)"
            self.execute(sql, parameters=(user_id, open_lesson_id), commit=True)
        else:
            sql = """INSERT INTO open_lesson_users(user_id, course_id)
            VALUES(?,(select id from courses where lower(?)=lower(name)))"""
            self.execute(sql, parameters=(user_id, course_name), commit=True)

if __name__ == "__main__":
    db = Database()
