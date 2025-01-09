"""
Date: 22-10-2024
Author: Namrata Modha
Purpose: Write a program that incorporates functions and arrays along with file I/O operations to achieve your initial payroll system.
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
    for i, staff in enumerate(staff_list, start=1):  # loop over a list(or any iterable) & keep track of index and value of each item
        print(f"{i}. {staff['ID']} - {staff['first_name']} {staff['last_name']}, {staff['type']}, Age: {staff['age']}, Salary: {staff['salary']}")
    print()

# Function to generate a new ID
def generate_id(staff_list):
    if not staff_list:  # Check if the staff list is empty
        return "001"  # Start with ID "001" if the list is empty
    else:
        last_id = int(staff_list[-1]['ID'])  # Get the last ID in the list and convert it to an integer
        new_id = last_id + 1  # Increment the last ID by 1
        return f"{new_id:03d}"  # Format the new ID as a three-digit number with leading zeros

# Function to add a new staff member with salary and age validation
def add_staff(staff_list):
    staff = {} # Create an empty dictionary to store staff details
    staff['type'] = input("Type of staff: ")
    staff['first_name'] = input("First name: ")
    staff['last_name'] = input("Last name: ")
    
    # Automatically generate a new ID
    staff['ID'] = generate_id(staff_list)
    
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
            # Check if the age is between 16 and 100
            if staff['age'] < 16 or staff['age'] > 100:
                raise ValueError("Age must be between 16 and 100.")
            # Break out of the loop if the input is valid
            break
        except ValueError as e:
            # Handle the error by printing an error message
            print(f"Invalid input for age: {e}. Please enter a valid age (16 to 100).")
    
    staff_list.append(staff)  # Add the staff dictionary to the list
    print(f"{staff['first_name']} {staff['last_name']} was added with ID {staff['ID']}.\n")
    save_staff_to_file(staff_list)  # Save the updated staff list to the file

# Function to delete a staff member by their number in the list
def delete_staff(staff_list):
    while True:
        number = input("Number: ")
        if not number.isdigit():  # Check if the input is a valid number
            print("Invalid input. Please enter a valid number.")
        else:
            number = int(number) - 1  # Convert to 0-based index
            if 0 <= number < len(staff_list):  # Check if the number is within the valid range
                staff = staff_list.pop(number)  # Remove the staff member from the list
                print(f"{staff['first_name']} {staff['last_name']} was deleted.\n")
                save_staff_to_file(staff_list)  # Save the updated staff list to the file
                break
            else:
                print(f"Invalid staff number. Please enter a number between 1 and {len(staff_list)}.")

# Function to save staff details to a text file
def save_staff_to_file(staff_list):
    with open("staff_data.txt", "w") as file:  # Open the file in write mode
        for staff in staff_list:
            # Write each staff member's details to the file, separated by commas
            file.write(f"{staff['ID']},{staff['type']},{staff['first_name']},{staff['last_name']},{staff['salary']},{staff['age']}\n")

# Function to load staff details from a text file
def load_staff_from_file():
    staff_list = []
    try:
        with open("staff_data.txt", "r") as file:  # Open the file in read mode
            for line in file:
                # Split each line by commas to extract staff details
                ID, type, first_name, last_name, salary, age = line.strip().split(',')
                # Add the staff member to the list
                staff_list.append({
                    "ID": ID,
                    "type": type,
                    "first_name": first_name,
                    "last_name": last_name,
                    "salary": float(salary),
                    "age": int(age)
                })
    except FileNotFoundError:
        pass  # If the file does not exist, return an empty list
    return staff_list

# Main function to drive the program
def main():
    # Load staff members from file
    staff_list = load_staff_from_file()
    
    display_menu()  # Display the command menu
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_staff(staff_list)  # List all staff members
        elif command.lower() == "add":
            add_staff(staff_list)  # Add a new staff member
        elif command.lower() == "del":
            delete_staff(staff_list)  # Delete a staff member
        elif command.lower() == "exit":
            break  # Exit the program
        else:
            print("Not a valid command. Please try again.\n")
    print("Thanks for accessing the Payroll system!")

if __name__ == "__main__":
    main()
