"""
Author: Namrata Modha
Purpose: Demonstrate Database connection in Python with Xampp
Date: 21-11-2024
"""
# Import the mysql.connector library to connect to the MySQL database
import mysql.connector

# Establish a connection to the MySQL database
# Specify the host, user credentials, and the name of the database
conn = mysql.connector.connect(
    host="localhost",   # Server host (local machine in this case)
    user="root",        # MySQL username
    password="",        # MySQL password (empty if no password is set)
    database="test"     # Name of the database to connect to
)

# Create a cursor object to execute SQL queries
mycursor = conn.cursor()

# Define an SQL query to insert data into the 'tester' table
query = "INSERT INTO tester(id, name) VALUES (1, 'Namrata')" 

# Execute the SQL query using the cursor object
mycursor.execute(query)

# Commit the transaction to save the changes in the database
conn.commit()

# Print the number of rows inserted as confirmation
print(mycursor.rowcount, "record inserted")



