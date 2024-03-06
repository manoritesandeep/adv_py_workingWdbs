import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

# cursor.execute(''' CREATE TABLE IF NOT EXISTS movies
#                (Title TEXT, Director TEXT, Year INT) ''')

# cursor.execute(''' INSERT INTO Movies VALUES('Taxi Driver', 'Martin Scorsese', 1976) ''')

# famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
#                ('Back to the Future', 'Robert Zemeckis', 1985),
#                ('Moonrise Kingdom', 'Wes Anderson', 2012)]
# cursor.executemany('INSERT INTO Movies VALUES (?,?,?)', famousFilms)
# cursor.execute("SELECT * FROM Movies")

release_year = (1985,)

cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)

print(cursor.fetchall())

# Save changes to database
connection.commit()
connection.close()
