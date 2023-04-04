import csv
import os
import database


# Set the path to the CSV file
csv_file_path = os.path.join('data', 'dim_country.csv')
# 
def insert_into_dim_country_table():
    with open(csv_file_path, 'r') as csv_file:
        dim_country_reader = csv.DictReader(csv_file)
        for row in dim_country_reader:
            database.add_entry_to_dim_country_table(row['country_id'], row['country_code'], row['country_name'])

def insert_pre_data_into_dim_stores_table():
    database.add_pre_data_to_dim_stores_table()

store_id = {}
for row in database.get_store_id_from_dim_stores_table(): # Loop over row in database
    # print(f'row - {row[0]}')
    key = f"store_id" #Create a key
    value = row[0] # Create a value
    store_id[key] = value # Add key value pair in the dictionary

    print(store_id)


# insert_into_dim_country_table()
# insert_pre_data_into_dim_stores_table()
# print(get_country_code('india'))