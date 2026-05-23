"""
what is a cursor ? 

A cursor is an object used to send commands to the database and fetch the resulting rows. Think of it as a pointer or a control structure that acts as a middleware between your Python code and the database instance. 

The Mechanism: You use it to execute SQL queries using methods like .execute().
Memory Management: Instead of loading a massive dataset entirely into Python's memory at once, 

A cursor allows you to iterate through the data row-by-row or in smaller batches via methods like .fetchone() or .fetchall().

all operation in SQLite are made by cursors, and not by connection object itself.
that is so that we can have one single connection, but potentially multiple cursors either reading data or atmost one writing data. 



what is commit ? 

A commit is a method called on the connection object (connection.commit()) that permanently saves changes to the database. 

The Mechanism: When you run data modification queries (INSERT, UPDATE, DELETE), the database doesn't write them directly to the physical storage immediately. Instead, it safely holds them inside a temporary "staged" state called a transaction.

Data Integrity: Calling .commit() signals that the transaction is complete and successful. If you don't call .commit() and the Python script closes or encounters an error, all your changes will be discarded (known as a rollback). 

"""


import sqlite3

# 1. Establish the main connection to the database
conn = sqlite3.connect("company.db")

# 2. Create the cursor to execute commands
cursor = conn.cursor()

# 3. Use the cursor to run an operation (Changes are staged in memory)
cursor.execute('CREATE TABLE employees (name VARCHAR(50), role VARCHAR(50));')
cursor.execute("INSERT INTO employees (name, role) VALUES ('Alice', 'Developer')")

# 4. COMMIT the changes (Saves Alice permanently to the database file)
conn.commit()

# 5. Use the cursor to fetch data (Read-only queries do not need a commit)
cursor.execute("SELECT * FROM employees")
all_employees = cursor.fetchall()
print(all_employees)

# 6. Clean up resources
conn.close()
