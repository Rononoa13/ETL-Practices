import csv
import database


# database.create_customer_table()
# Open the CSV file and iterate over their rows
with open('customer_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    # next(reader)
    for row in reader:
        # Extract the data from the row
        customer_id = row['customer_id']
        name = row['name']
        email = row['email']
        age_str = row['age']
        country = row['country']

        # Transform the data
        age = int(age_str)

        # Load the data into the database
        # database.insert_into_customer_table(customer_id, name, email, age, country)
        
