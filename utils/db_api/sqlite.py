import sqlite3


class Database:

    def __init__(self, path_to_db="data/main.db"):
        self.db = path_to_db
        self.create_table_users()
        self.create_table_courses()
        self.create_table_open_lessons()
        self.create_table_open_lesson_users()


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

    # CREATE TABLE
    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name varchar(255) NOT NULL,
        email varchar(255),
        language varchar(3),
        phone varchar(20)
        )"""
        # 1-uzbek, 2-russian, 3-english
        
        self.execute(sql, commit=True)

    def create_table_open_lessons(self):
        sql = """
        CREATE TABLE IF NOT EXISTS open_lessons(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        course int,
        date datetime,        
        format varchar(20),  
        language varchar(3)
        )"""

        self.execute(sql, commit=True)

    def create_table_courses(self):
        sql = """
        CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
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
        image varchar(300)
        )"""
        self.execute(sql, commit=True)

    def create_table_open_lesson_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS open_lesson_users(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        user_id int,
        open_lesson_id int,     
        course_name_id INTEGER,  
        language varchar(3),                 
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(open_lesson_id) REFERENCES open_lessons(id)
        )"""

        self.execute(sql, commit=True)

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
            SELECT id, name, description, about,career, for_whom,requirements,image 
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
            sql = "SELECT name, description FROM courses WHERE language=(select language from users where id=?)"
            return self.execute(sql, parameters=(user_id,), fetchall=True)
        if only_about:
            sql = "SELECT about FROM courses WHERE language=(select language from users where id=?)"
            return self.execute(sql, parameters=(user_id,), fetchall=True)
        if inline_mode:

            sql = "SELECT id,name,image, description FROM courses WHERE language=(select language from users where id=?)"
            return self.execute(sql, parameters=(user_id,), fetchall=True)

    # OPEN LESSONS
    def select_open_lesson(self, course):

        sql = f"""  SELECT strftime('%d-%m-%Y',date) as date, strftime('%H:%M',date) as time, language
                    FROM open_lessons
                    WHERE lower(course) = lower(?)
                    ORDER by date DESC
                    LIMIT 1"""

        sql = sql.replace('#condition', 'course_id=(select id from courses where name=?)')
        return self.execute(sql, parameters=(course,), fetchone=True)



if __name__ == "__main__":
    db = Database()
