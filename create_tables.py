# This file basically connects to MySQL and creates the 'accounts' table
import mysql.connector

# Establish connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rpemon2008@#",  # oh no, I hope you don't have to use this password 
    database="banking_system"
)

cursor = connection.cursor()

# Create table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_number INT PRIMARY KEY,
    name VARCHAR(100),
    pin VARCHAR(10),
    balance DECIMAL(10, 2)
)
""")

connection.commit()  # Save the changes
print("\u2705 Table 'accounts' created successfully!")

cursor.close()
connection.close()

