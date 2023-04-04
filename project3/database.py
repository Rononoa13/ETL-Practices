import sqlite3

# Open a connection to the database
connection = sqlite3.connect('customers.db')

# Define the SQL query to create a new table
CREATE_TABLE_CUSTOMER_QUERY = """
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    age INTEGER,
    country TEXT
);
"""
# Define the SQL query to insert data into table
INSERT_INTO_CUSTOMER_TABLE = """
INSERT INTO customers (customer_id, name, email, age, country)
VALUES (?, ?, ?, ?, ?);
"""

# -------- CREATE TABLE FUNCTION
def create_customer_table():
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_TABLE_CUSTOMER_QUERY)
        return cursor
    

def insert_into_customer_table(customer_id, name, email, age, country):
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_INTO_CUSTOMER_TABLE, (customer_id, name, email, age, country, ))
# insert_into_customer_table('1','John Doe','johndoe@example.com','35','USA')
# -------- Function call to create a customer table  
# create_customer_table()