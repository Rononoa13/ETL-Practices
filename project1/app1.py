import csv

'''
Get country code when country name is provided.
'''


def get_store_code():

    # Return a capitalized version of the string.
    user_country = input('Enter a country name: ').capitalize()

    # Open a CSV file
    with open('dim_country.csv') as file:

        # Create a reader object to read from input file
        reader = csv.DictReader(file)
        for row in reader:
            if user_country == row['country_name']:
                return row['country_code']

        return f"Country Not Found"


print(get_store_code())
