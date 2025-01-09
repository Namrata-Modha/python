"""
Date: 17-09-2024
Author: Namrata Sharad Modha
Purpose: Demonstrate payroll system with user input and formatting
"""

# Prompting user for employee details
firstName = input("Please enter the employee's First Name: ")  # Asking for first name
lastName = input("Please enter the employee's Last Name: ")    # Asking for last name
empId = input("Please enter the employee's ID Number (numbers only): ")  # Asking for employee ID number

# Checking if the input is numeric, and displaying an error if it's not
if empId.isdigit():  # Checking if the input is numeric
    # Concatenating first and last name
    fullName = firstName + " " + lastName  # Combining first and last names with a space in between

    #Displaying the concatenated string
    print(f"\nMy name is {fullName}. My employee ID is {empId}.")
    
    # Displaying formatted employee details with tabs using tabs (\t) to space out the columns neatly
    print("\nFirst Name\tLast Name\tID")  # Header with column names
    print(f"{firstName}\t\t{lastName}\t\t{empId}")  # Displaying employee details in a tabular format
else:
    print("Error: Employee ID must be numeric.")  # Error message for non-numeric input
    

