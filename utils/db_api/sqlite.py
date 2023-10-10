import sqlite3


class Database:

    def __init__(self, path_to_db="data/main.db"):
        self.db = path_to_db
        self.create_table_users()

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

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users(
        id int PRIMARY KEY, 
        name varchar(255) NOT NULL,
        email varchar(255),
        language varchar(3),
        phone varchar(20)
        )"""
        # 1-uzbek, 2-russian, 3-english
        
        self.execute(sql, commit=True)

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


    def format_args(self, parameters: dict):
        sql =" AND ".join(
            [f"{param} = ?" for param in parameters]
        )
        parameters = list(parameters.values())
        return sql, parameters

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

if __name__ == "__main__":
    db = Database()
