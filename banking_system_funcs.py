# The holy grail file to run the banking app and handle user actions
import mysql.connector

from login_stuff import login

# Display menu options
def show_menu():
    print("-------- Main Menu ---------")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    return input("Select an option: ")

# Show current balance for the logged-in user
def check_balance(account_number):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rpemon2008@#", # for the love of all that is holy, please change this password
        database="banking_system"
    )

    cursor = connection.cursor() # Fetch the balance for the account number
    query = "SELECT balance FROM accounts WHERE account_number = %s" # SQL query to get the balance
    cursor.execute(query, (account_number,)) # Execute the query with the account number as a parameter 
    balance = cursor.fetchone()[0] # Fetch the first result (the balance)

    print(f"\u2705 Your balance is ${balance:.2f}")

    cursor.close() # Close the cursor to free up resources
    connection.close() # Close the connection to the database

# Deposit money into the account
def deposit(account_number):
    amount = float(input("Enter the amount to deposit: "))

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rpemon2008@#", # i will crash out if I see this password one more time
        database="banking_system"
    )

    cursor = connection.cursor()
    query = "UPDATE accounts SET balance = balance + %s WHERE account_number = %s"
    cursor.execute(query, (amount, account_number))

    connection.commit()
    print(f"\u2705 ${amount:.2f} deposited successfully.")

    cursor.close() 
    connection.close() 

# Withdraw money from the account
def withdraw(account_number):
    amount = float(input("Enter the amount to withdraw: "))

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rpemon2008@#", # sooooo, my laptop is on fire now
        database="banking_system"
    )

    cursor = connection.cursor()
    query = "SELECT balance FROM accounts WHERE account_number = %s"
    cursor.execute(query, (account_number,))
    balance = cursor.fetchone()[0]

    # Ensure there is enough funds
    if balance >= amount:
        query = "UPDATE accounts SET balance = balance - %s WHERE account_number = %s"
        cursor.execute(query, (amount, account_number))
        connection.commit()
        print(f"\u2705 ${amount:.2f} withdrawn successfully.")
    else:
        print("\u274C Insufficient funds.")

    cursor.close() 
    connection.close() 

# Main program loop
def main():
    account_number = login()
    if account_number:
        while True:
            choice = show_menu()
            if choice == '1': # Check balance
                check_balance(account_number)
            elif choice == '2': # Deposit money
                deposit(account_number)
            elif choice == '3': # Withdraw money
                withdraw(account_number)
            elif choice == '4': # Exit the program
                print("Thank you for using my banking system!")
                break
            else: # Invalid option
                print("\u274C Invalid option, please try again.")

# Start the program
if __name__ == "__main__":
    main()

