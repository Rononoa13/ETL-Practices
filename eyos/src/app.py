import csv
import os
from models.database import get_country_code_from_dim_country, get_store_id_from_dim_stores_table, add_csv_data_to_dim_stores_table

#  Set the path to the CSV file
dim_country_csv_file_path = os.path.join('data', 'dim_country.csv')
sample_csv_file_path = os.path.join('data', 'sample_csv.csv')

'''
lookup function that returns a value from a dictionary based on a key:
Get country code when country name is provided.
'''

def get_store_code():

    # Return a capitalized version of the string.

    # Open a CSV file
    with open(dim_country_csv_file_path) as file, open(sample_csv_file_path) as sample_file:
        # Create a reader object to read from input file
        dim_country_reader = csv.DictReader(file)
        sample_csv_reader = csv.DictReader(sample_file)

        store_id = {}
        for row in get_store_id_from_dim_stores_table(): # Loop over row in database
            # print(f'row - {row[0]}')
            key = f"store_id" #Create a key
            value = row[0] # Create a value
            store_id[key] = value # Add key value pair in the dictionary


        for row in sample_csv_reader:
            country_code = get_country_code_from_dim_country(row['country_name'])
            print(country_code)
            # country_code_list.append(country_code)
            # country_code = iter(country_code_list)
            # store_id = get_store_id_from_dim_stores_table()
            # store_id = country_code + store_id[row]

            # Insert the data into the dim_stores table
            add_csv_data_to_dim_stores_table(country_code + str(store_id['store_id']), row['store_name'], country_code, row['street_name'], row['pin_code'], row['lvl1_geog'], row['lvl2_goeg'], row['lvl3_geog']  )
        
            # print(row)
        # print(country_code_list)

        # store_id_list = []
        # for row in range(len(get_store_id_from_dim_stores_table())):
        #     store_id = get_store_id_from_dim_stores_table()
        #     print(store_id)
            # store_id = country_code_list[row] + str(store_id)
            # print(store_id)
            # store_id_list.append(store_id)
            # store_id = iter(store_id_list)

        # print(store_id_list)
        print("Code block reaches here")

print(get_store_code())
