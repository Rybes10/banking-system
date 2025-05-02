# Import the MySQL connector module to interact with MySQL from Python
import mysql.connector

try:
    # Attempt to connect to the MySQL database with the given credentials
    connection = mysql.connector.connect(
        host="localhost",            # Host where MySQL is running (usually localhost)
        user="root",                 # Your MySQL username
        password="Rpemon2008@#",     # Your MySQL password — replace this with your own if needed
        database="banking_system"    # The database you're connecting to
    )

    # If the connection is successful, print a success message
    if connection.is_connected():
        print("✅ Successfully connected to MySQL database!") # By the way I got the checkmark emoji from https://emojipedia.org/ and the cross mark from https://emojipedia.org/cross-mark/.

# Catch any errors that occur during the connection attempt
except mysql.connector.Error as err:
    print(f"❌ Error: {err}") # Same for the cross mark emoji, I got it from https://emojipedia.org/cross-mark/.

# Always close the connection at the end, if it was successfully created
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()  # Closes the database connection to avoid any resource leaks
