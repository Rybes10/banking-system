# This script handles logging a user into the banking system
import mysql.connector

def login():
    print("Welcome to my very own Banking System! ")
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rpemon2008@#", # for god's ske, how many times do I have to see this password
        database="banking_system"
    )

    cursor = connection.cursor() # Connect to the database

    # Verify the account number and PIN
    query = "SELECT * FROM accounts WHERE account_number = %s AND pin = %s"
    cursor.execute(query, (account_number, pin))

    account = cursor.fetchone() # Fetch the account details

    if account:
        print(f"\u2705 Welcome, {account[1]}!")
        return account_number
    else:
        print("\u274C Invalid account number or PIN.")
        return None

    cursor.close()
    connection.close()

# Login function can be called from other scripts
if __name__ == "__main__":
    login()