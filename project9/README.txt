we execute an INSERT query to add a new record to the users table. The query uses parameterized values to prevent SQL injection attacks.

After executing the query, we retrieve the ID of the new record using the **lastrowid** attribute of the cursor object.