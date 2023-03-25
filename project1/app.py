import csv


def get_store_code():
    # Open a CSV file
    with open('dim_country.csv') as file:

        # Create a reader object to read from input file
        reader = csv.DictReader(file)

        # Open the output csv file
        with open('dim_country_transform.csv', 'w', newline='') as output_file:
            # Create a writer object to write to the output file
            fieldname = ['country_id', 'country_code',
                         'country_name', 'store_code']
            writer = csv.DictWriter(output_file, fieldnames=fieldname)

            writer.writeheader()
            # Loop through each row in the input file and write it to the output file
            for row in reader:
                store_code = row['country_code'] + row['country_id']
                row['store_code'] = store_code
                writer.writerow(row)


get_store_code()
