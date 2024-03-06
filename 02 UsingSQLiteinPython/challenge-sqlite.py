import sqlite3

connection = sqlite3.connect("users-sqlite.db")

cursor = connection.cursor()

cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS Users 
               (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
               first_name TEXT, last_name TEXT,
               email_address TEXT)''')

users_to_interact = [
    ('Sarah', 'Perry', 'sarah.perry@gmail.com'),
    ('Kat', 'Martin', 'kat.m@gmail.com'),
    ('Jay', 'Pat', 'j.pat@gmail.com'),
    ('Jessica', 'Jones', 'jess.j@hotmail.com'),
    ('Percy', 'Perry', 'percy.perry@gmail.com'),
]

cursor.executemany(''' 
    INSERT INTO Users(first_name, last_name, email_address)
                   VALUES (?,?,?)''', users_to_interact)

cursor.execute("SELECT * FROM Users")

print(cursor.fetchall())

connection.commit()
connection.close()



