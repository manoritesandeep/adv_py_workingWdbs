import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///users-sqlalchemy.db', echo=True)

users_to_insert = [
    {'first_name': 'Dave', 'last_name': 'Devon', 'email_address' : 'dd@gmail.com'},
    {'first_name': 'Jerry', 'last_name': 'Sharma', 'email_address' : 'js@gmail.com'},
    {'first_name': 'Perry', 'last_name': 'Perks', 'email_address' : 'pp@hotmail.com'},
    {'first_name': 'Deli', 'last_name': 'Daily', 'email_address' : 'ddaily@outlook.com'},
    {'first_name': 'Kathryn', 'last_name': 'Hodge', 'email_address' : 'kh@sample.com'},
]

with engine.connect() as conn:
    conn.execute(sqlalchemy.text(''' CREATE TABLE IF NOT EXISTS Users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    email_address TEXT)'''))
    
    conn.execute(sqlalchemy.text(
        ''' INSERT INTO Users (
        first_name, last_name, email_address)
        VALUES (:first_name, :last_name, :email_address)'''), users_to_insert)
    
    result = conn.execute(sqlalchemy.text("SELECT * FROM Users"))
    for row in result:
        print(row)

    conn.commit()

