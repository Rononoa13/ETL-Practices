import csv
import database


# database.create_customer_table()
# Open the CSV file and iterate over their rows
with open('customer_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        # Extract the data from the row
        print(row)
