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
# Define the SQL query to create a new table
CREATE_TABLE_ORDERS_QUERY = """
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    total_amount DECIMAL(10, 2)
);
"""

# Define the SQL query to insert data into table
INSERT_INTO_CUSTOMER_TABLE = """
INSERT INTO customers (customer_id, name, email, age, country)
VALUES (?, ?, ?, ?, ?);
"""

# Define the SQL query to insert data into table
INSERT_INTO_ORDERS_TABLE = """
INSERT INTO orders (order_id,customer_id,order_date,total_amount)
VALUES (?, ?, ?, ?);
"""

# -------- CREATE TABLE FUNCTION
def create_customer_table():
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_TABLE_CUSTOMER_QUERY)
        return cursor
    

def create_orders_table():
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_TABLE_ORDERS_QUERY)
        return cursor


# -------- CREATE TABLE FUNCTION


def insert_into_customer_table(customer_id, name, email, age, country):
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_INTO_CUSTOMER_TABLE, (customer_id, name, email, age, country, ))


def insert_into_orders_table(order_id,customer_id,order_date,total_amount):
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_INTO_ORDERS_TABLE, (order_id,customer_id,order_date,total_amount, ))



# -------- Function call to create a customer table  
# create_customer_table()
# create_orders_table()