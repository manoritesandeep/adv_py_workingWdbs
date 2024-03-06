## Using sqlalchemy expression language
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///users-sqlalchemy-exprnlang.db', echo=True)

users_to_insert = [
    {'first_name': 'Dave', 'last_name': 'Devon', 'email_address' : 'dd@gmail.com'},
    {'first_name': 'Jerry', 'last_name': 'Sharma', 'email_address' : 'js@gmail.com'},
    {'first_name': 'Perry', 'last_name': 'Perks', 'email_address' : 'pp@hotmail.com'},
    {'first_name': 'Deli', 'last_name': 'Daily', 'email_address' : 'ddaily@outlook.com'},
    {'first_name': 'Kathryn', 'last_name': 'Hodge', 'email_address' : 'kh@sample.com'},
]

metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table("Users",
                               metadata,
                               sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
                               sqlalchemy.Column("first_name", sqlalchemy.String),
                               sqlalchemy.Column("last_name", sqlalchemy.String),
                               sqlalchemy.Column("email_address", sqlalchemy.String),
                               )

metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(sqlalchemy.insert(users_table).values(users_to_insert))
    for row in conn.execute(sqlalchemy.select(users_table)):
        print(row)

    conn.commit()

