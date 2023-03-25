import pandas as pd

# Load data from CSV
orders = pd.read_csv('orders.csv')

# Group the orders by customer and sum the order amounts
customer_orders = orders.groupby('customer_id').agg({'product_price': 'sum'})
print(customer_orders)

# Rename the column to total_spent
customer_orders = customer_orders.rename(columns={'product_price': 'total_spent'})
print(customer_orders)

# Print the transformed data
