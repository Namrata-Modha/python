"""
Date: 15-10-2024
Author: Namrata Modha
Purpose: Write a program that incorporates functions and arrays to achieve your initial payroll system.
Your program should utilize a main function which is the driver function. The following requirements are to be adhered to: 

Add a staff
Delete a staff
List or view staff details 
Display menu items that prompt the user to choose which option they want to partake in.
"""

# Function to display the menu options to the user
def display_menu():
    print("------Welcome to the Payroll System------")
    print("COMMAND MENU")
    print("list - List all staff")
    print("add - Add a staff")
    print("del - Delete a staff")
    print("exit - Exit program")
    print()

# Function to list all staff details
def list_staff(staff_list):
    for i, staff in enumerate(staff_list, start=1): # loop over a list (or any iterable) and keep track of both the index and the value of each item
        print(f"{i}. {staff['ID']} - {staff['first_name']} {staff['last_name']}, {staff['type']}, Age: {staff['age']}, Salary: {staff['salary']}")
    print()

# Function to add a new staff member with salary and age validation
def add_staff(staff_list):
    staff = {}
    staff['type'] = input("Type of staff: ")
    staff['first_name'] = input("First name: ")
    staff['last_name'] = input("Last name: ")
    staff['ID'] = input("ID: ")
    
    # Validate salary input
    while True:
        try:
            # Attempt to convert the input to a float
            staff['salary'] = float(input("Salary: "))
            # Check if the salary is a positive number
            if staff['salary'] <= 0:
                # Raise an error if the salary is not positive
                raise ValueError("Salary must be a positive number.")
            # Break out of the loop if the input is valid
            break
        except ValueError as e:
            # Handle the error by printing an error message
            print(f"Invalid input for salary: {e}. Please enter a positive number.")
    
    # Validate age input
    while True:
        try:
            # Attempt to convert the input to an integer
            staff['age'] = int(input("Age: "))
            # Check if the age is at least 16
            if staff['age'] < 16 or staff['age'] > 100:
                raise ValueError("Age must be between 16 and 100.")
            # Break out of the loop if the input is valid
            break
        except ValueError as e:
            # Handle the error by printing an error message
            print(f"Invalid input for age: {e}. Please enter a valid age (16 to 100).")
    
    staff_list.append(staff)
    print(f"{staff['first_name']} {staff['last_name']} was added.\n")

# Function to delete a staff member by their number in the list
def delete_staff(staff_list):
    while True:
        number = input("Number: ")
        if not number.isdigit():
            print("Invalid input. Please enter a valid number.")
        else:
            number = int(number) - 1  # Convert to 0-based index
            if 0 <= number < len(staff_list):
                staff = staff_list.pop(number)
                print(f"{staff['first_name']} {staff['last_name']} was deleted.\n")
                break
            else:
                print(f"Invalid staff number. Please enter a number between 1 and {len(staff_list)}.")

# Main function to drive the program
def main():
    staff_list = [
        {"type": "Manager", "first_name": "John", "last_name": "Doe", "ID": "001", "salary": 75000, "age": 45},
        {"type": "Developer", "first_name": "Jane", "last_name": "Smith", "ID": "002", "salary": 65000, "age": 30},
        {"type": "Designer", "first_name": "Emily", "last_name": "Jones", "ID": "003", "salary": 60000, "age": 28}
    ]
    display_menu()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_staff(staff_list)
        elif command.lower() == "add":
            add_staff(staff_list)
        elif command.lower() == "del":
            delete_staff(staff_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Thanks for accessing the Payroll system!")

if __name__ == "__main__":
    main()


