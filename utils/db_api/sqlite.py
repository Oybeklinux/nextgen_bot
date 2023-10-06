import sqlite3

class Database:

    def __init__(self, path_to_db = "main.db"):
        self.db = path_to_db

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
        email varchar(255)
        )"""
        
        self.execute(sql, commit=True)

    def add_user(self, id:int, name:str, email:str = None):
        sql = """INSERT INTO users(id, name, email) VALUES(?,?,?)"""

        parameters = (id, name, email)
        self.execute(sql, parameters, commit=True)

    def select_all_users(self):
        sql = """SELECT * FROM users"""
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql, parameters = self.format_args(kwargs)
        sql = f"""SELECT * FROM users WHERE {sql}"""
        return self.execute(sql, parameters=parameters, fetchone=True)


    def format_args(self, parameters: dict):
        sql =" AND ".join(
            [f"{param} = ?" for param in parameters]
        )
        parameters = tuple(parameters.values())
        return sql, parameters

    def select_count(self):
        return self.execute("""SELECT count(*) FROM users""", fetchone=True)

    def update_email(self, email, id):
        sql = """UPDATE users SET email=? WHERE id=?"""
        self.execute(sql, paramameters=(email, id), commit=True)

    def delete_user(self, id):
        sql = """DELETE users WHERE id=?"""
        self.execute(sql, parameters=(id,), commit=True)

    def delete_all(self):
        sql = """DELETE FROM users"""
        self.execute(sql, commit=True)

if __name__ == "__main__":
    db = Database()
