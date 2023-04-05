import csv
import database

# database.create_customer_table()
with open('customer_data.csv', 'r') as customer_file, open('orders_data.csv', 'r') as orders_file:
    customer_reader = csv.DictReader(customer_file)
    order_reader = csv.DictReader(orders_file)
    
    for c_row in customer_reader:
        # Extract the data from the rows
        customer_id = c_row['customer_id']
        name = c_row['name']
        email = c_row['email']
        age_str = c_row['age']
        country = c_row['country']
        print(customer_id)

    for o_row in order_reader:
        print(customer_id)
        order_id = o_row['order_id']
        order_date_str = o_row['order_date']
        total_amount_str = o_row['total_amount']

        # change date format to 'MM-DD-YYYY'
        order_date = order_date_str.split('-')
        order_date = '-'.join([order_date[2], order_date[1], order_date[0]])

        total_amount = float(total_amount_str)
        
    # Load into database
        # database.insert_into_orders_table(order_id,customer_id,order_date,total_amount)

# print(order_date)
# print(order_date_str)
# print(total_amount_str)
# print(total_amount)