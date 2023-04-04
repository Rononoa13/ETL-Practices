import csv
import database

# database.create_customer_table()
with open('customer_data.csv', 'r') as file1, open('orders.csv', 'r') as file2:
    reader1 = csv.DictReader(file1)
    reader2 = csv.DictReader(file2)
    # using the zip() function to match corresponding rows from each file.
    for row1, row2 in zip(reader1, reader2):
 
        # Extract the data from the rows
        customer_id = row1['customer_id']
        name = row1['name']
        email = row1['email']
        age_str = row1['age']
        country = row1['country']

        # from row 2
        product_name = row2['product_name']

        # Transform the data
        age = int(age_str)
        new_name = name + product_name
        # database.insert_into_customer_table(customer_id, new_name, email, age, country)