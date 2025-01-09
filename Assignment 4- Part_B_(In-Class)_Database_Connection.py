"""
Author: Namrata Modha
Purpose: Demonstrate Database connection in Python
Date: 21-11-2024
"""
import sqlite3

# Establishing a connection to the SQLite database.

conn = sqlite3.connect('movies.sqlite')  # Creates or connects to a database file.

c = conn.cursor()  # Creating a cursor object to execute SQL commands.

# retrieve and display all records from the table.
# query = '''SELECT * FROM Movie'''
# c.execute(query)

# SQL INSERT statement to add a new record into the 'Movie' table.
# This query inserts values into the columns 'categoryID', 'name', 'year', and 'minutes'.
insertQuery = '''INSERT INTO Movie (categoryID, name, year, minutes) VALUES (2, 'Iron Man', '2000', 100)'''

# Executing the INSERT query using the cursor object.
c.execute(insertQuery)

# Committing the changes to the database.
# This ensures that the new record is saved and persists in the database file.
conn.commit()

# Checking if the connection to the database exists, and if so, closing it to release resources.
if conn:
    conn.close()
