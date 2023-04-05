import sqlite3

# Open a connection to the database
connection = sqlite3.connect('example.db')

CREATE_TABLE_USER = """
    CREATE TABLE users (
     id INTEGER PRIMARY KEY,
     name TEXT, 
     email TEXT
    )
"""

INSERT_INTO_USERS = """
    INSERT INTO users (name, email) 
    VALUES (?, ?)
"""


def create_table_user():
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_TABLE_USER)

def add_value_to_user_table(name, email):
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_INTO_USERS, (name, email, ))
        new_id = cursor.lastrowid
        return new_id
# create_table_user()