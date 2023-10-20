migrations = {
    0: [
        """CREATE TABLE IF NOT EXISTS open_lessons(            
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            course varchar(30),
            date datetime,        
            format varchar(20),  
            language varchar(3))""",
        """CREATE TABLE IF NOT EXISTS courses(
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
            image varchar(300))""",
        """CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            phone varchar(20))""",
        """CREATE TABLE IF NOT EXISTS open_lesson_users(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            user_id int,
            open_lesson_id int,     
            course_name varchar(30),  
            language varchar(3),                 
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(open_lesson_id) REFERENCES open_lessons(id))""",
        """CREATE TABLE IF NOT EXISTS migrations(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            version int UNIQUE,
            migrated TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""
    ],
    1: [
        "ALTER TABLE courses ADD COLUMN official_name varchar(50)"
    ],
    2: [
        "ALTER TABLE open_lesson_users ADD COLUMN course_id varchar(50)"
    ],

}