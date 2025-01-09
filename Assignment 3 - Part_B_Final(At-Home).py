"""
Author: Namrata Modha
Purpose: Payroll system using inheritance in OOP.
The program includes classes for different types of employees (Part-Time, Full-Time, Intern).
Each employee type has specific salary calculation rules.
Date: 14-11-2024
"""

# File path for storing employee data
EMPLOYEE_FILE = "employee_inherit.txt"

class Employee:
    def __init__(self, fName, lName, age, emp_id, dept):
        # Encapsulated attributes (private) for employee details
        self.__fName = fName
        self.__lName = lName
        self.__age = age      
        self.__emp_id = emp_id 
        self.__dept = dept    

    # Getters and Setters for encapsulated attributes
    def get_fName(self): return self.__fName
    def set_fName(self, fName): self.__fName = fName
    def get_lName(self): return self.__lName
    def set_lName(self, lName): self.__lName = lName
    def get_age(self): return self.__age
    def set_age(self, age): 
        # Validate age to ensure it is between 18 and 100
        if 18 <= age <= 100:
            self.__age = age
        else:
            print("Invalid age. Please enter an age between 18 and 100.")
    def get_emp_id(self): return self.__emp_id
    def set_emp_id(self, emp_id): self.__emp_id = emp_id
    def get_dept(self): return self.__dept
    def set_dept(self, dept): self.__dept = dept

    # Abstract method for salary calculation
    def calc_salary(self):
        # This method should be overridden in subclasses
        raise NotImplementedError("This method should be overridden in subclasses.")

    # Method to get employee type
    def get_employee_type(self):
        return "Employee"  # Default employee type

    # Display employee details
    def emp_details(self):
        print("\nEmployee Details:")
        print(f"First Name: {self.get_fName()}")
        print(f"Last Name: {self.get_lName()}")
        print(f"Age: {self.get_age()}")
        print(f"Employee ID: {self.get_emp_id()}")
        print(f"Department: {self.get_dept()}")
        print(f"Employee Type: {self.get_employee_type()}")

class FullTimeEmployee(Employee):
    def __init__(self, fName, lName, age, emp_id, dept, rate_of_pay, benefits, vacationDays):
        # Initialize attributes specific to Full-Time employees
        super().__init__(fName, lName, age, emp_id, dept)  # Call the parent constructor
        self.__rate_of_pay = rate_of_pay  # Hourly rate of pay
        self.__benefits = benefits          # Benefits provided to the employee
        self.__vacationDays = vacationDays  # Number of vacation days

    def calc_salary(self):
        # Calculate monthly salary for full-time employees
        return self.__rate_of_pay * 40  # Assuming 40 hours per week

    def get_employee_type(self):
        return "Full-Time Employee"  # Override to specify employee type

    def emp_details(self):
        # Display full-time employee details including salary calculation
        super().emp_details()  # Call the parent method to display common details
        print(f"Rate of Pay: ${self.__rate_of_pay}")
        print(f"Benefits: {self.__benefits}")
        print(f"Vacation Days: {self.__vacationDays}")
        print(f"Calculated Salary: ${self.calc_salary()}")

class PartTimeEmployee(Employee):
    def __init__(self, fName, lName, age, emp_id, dept, hours_worked, rate_of_pay):
        # Initialize attributes specific to Part-Time employees
        super().__init__(fName, lName, age, emp_id, dept)  # Call the parent constructor
        self.__hours_worked = hours_worked  # Total hours worked in a pay period
        self.__rate_of_pay = rate_of_pay      # Hourly rate of pay

    def calc_salary(self):
        # Calculate salary based on hours worked for part-time employees
        return self.__hours_worked * self.__rate_of_pay  # Total pay for hours worked

    def get_employee_type(self):
        return "Part-Time Employee"  # Override to specify employee type

    def emp_details(self):
        # Display part-time employee details including salary calculation
        super().emp_details()  # Call the parent method to display common details
        print(f"Hours Worked: {self.__hours_worked}")
        print(f"Rate of Pay: ${self.__rate_of_pay}")
        print(f"Calculated Salary: ${self.calc_salary()}")

class Intern(Employee):
    def __init__(self, fName, lName, age, emp_id, dept, stipend=200):
        # Initialize attributes specific to Interns
        super().__init__(fName, lName, age, emp_id, dept)  # Call the parent constructor
        self.__stipend = stipend  # Default stipend for interns

    def calc_salary(self):
        # Interns receive a fixed stipend
        return self.__stipend  # Return the stipend amount

    def get_employee_type(self):
        return "Intern"  # Override to specify employee type

    def emp_details(self):
        # Display intern details including salary calculation
        super().emp_details()  # Call the parent method to display common details
        print(f"Stipend: ${self.__stipend}")
        print(f"Calculated Salary: ${self.calc_salary()}")

# Validation functions to ensure correct input
def validate_age(age):
    # Check if age is a digit and within the valid range
    return age.isdigit() and 18 <= int(age) <= 100

def validate_hours(hours):
    # Check if hours is a digit and greater than zero
    return hours.isdigit() and int(hours) > 0

def validate_rate(rate):
    # Check if rate is a valid number greater than zero
    return rate.replace('.', '', 1).isdigit() and float(rate) > 0

# Helper function to load employees from file
def load_employees():
    employees = []  # Initialize an empty list to store employees
    try:
        with open(EMPLOYEE_FILE, "r") as file:
            for line in file:
                data = line.strip().split("|")  # Split line into components
                # Create employee objects based on the type specified in the data
                if data[6] == "full-time":
                    employees.append(FullTimeEmployee(data[0], data[1], int(data[2]), data[3], data[4], float(data[5]), data[7], int(data[8])))
                elif data[6] == "part-time":
                    employees.append(PartTimeEmployee(data[0], data[1], int(data[2]), data[3], data[4], float(data[5]), float(data[6])))
                elif data[6] == "intern":
                    employees.append(Intern(data[0], data[1], int(data[2]), data[3], data[4]))
                else:
                    print(f"Unknown employee type for line: {line}")  # Handle unknown types
    except FileNotFoundError:
        print("Employee file not found. Starting with an empty list.")  # Handle file not found
    return employees  # Return the list of employees

# Helper function to save employees to file
def save_employees(employees):
    with open(EMPLOYEE_FILE, "w") as file:
        for emp in employees:
            # Write employee details to file based on their type
            if isinstance(emp, FullTimeEmployee):
                line = f"{emp.get_fName()}|{emp.get_lName()}|{emp.get_age()}|{emp.get_emp_id()}|{emp.get_dept()}|{emp._FullTimeEmployee__rate_of_pay}|full-time|{emp._FullTimeEmployee__benefits}|{emp._FullTimeEmployee__vacationDays}\n"
            elif isinstance(emp, PartTimeEmployee):
                line = f"{emp.get_fName()}|{emp.get_lName()}|{emp.get_age()}|{emp.get_emp_id()}|{emp.get_dept()}|{emp._PartTimeEmployee__hours_worked}|{emp._PartTimeEmployee__rate_of_pay}|part-time|\n"
            else:
                line = f"{emp.get_fName()}|{emp.get_lName()}|{emp.get_age()}|{emp.get_emp_id()}|{emp.get_dept()}|intern|\n"
            file.write(line)  # Write the line to the file

# CRUD functions for managing employees
def add_employee(employees):
    # Gather employee details from user input
    fName = input("Enter first name: ")
    lName = input("Enter last name: ")
    age = input("Enter age: ")
    while not validate_age(age):
        print("Invalid age. Please enter an age between 18 and 100.")
        age = input("Enter age: ")
    emp_id = input("Enter employee ID: ")
    dept = input("Enter department: ")
    emp_type = input("Is this a Full-Time employee, Part-Time employee, or Intern? (full-time/part-time/intern): ").lower()

    # Create a new employee object based on the type specified
    if emp_type == 'full-time':
        rate_of_pay = input("Enter rate of pay: ")
        while not validate_rate(rate_of_pay):
            print("Rate of pay must be greater than 0.")
            rate_of_pay = input("Enter rate of pay: ")
        benefits = input("Enter benefits (comma-separated): ")
        vacationDays = int(input("Enter number of vacation days: "))
        new_employee = FullTimeEmployee(fName, lName, int(age), emp_id, dept, float(rate_of_pay), benefits, vacationDays)
    elif emp_type == 'part-time':
        hours_worked = input("Enter hours worked: ")
        while not validate_hours(hours_worked):
            print("Hours worked must be greater than 0.")
            hours_worked = input("Enter hours worked: ")
        rate_of_pay = input("Enter rate of pay: ")
        while not validate_rate(rate_of_pay):
            print("Rate of pay must be greater than 0.")
            rate_of_pay = input("Enter rate of pay: ")
        new_employee = PartTimeEmployee(fName, lName, int(age), emp_id, dept, int(hours_worked), float(rate_of_pay))
    elif emp_type == 'intern':
        new_employee = Intern(fName, lName, int(age), emp_id, dept)
    else:
        print("Invalid employee type. Please try again.")
        return

    employees.append(new_employee)  # Add the new employee to the list
    save_employees(employees)  # Save the updated list to the file
    print("Employee added successfully!")  # Confirmation message

def list_employees(employees):
    # Display the list of employees
    if employees:
        for emp in employees:
            emp.emp_details()  # Call the method to display each employee's details
    else:
        print("No employees found.")  # Message if no employees exist

def update_employee(employees):
    emp_id = input("Enter employee ID to update details: ")
    found = False  # Flag to check if employee is found
    for i, emp in enumerate(employees):
        if emp.get_emp_id() == emp_id:
            found = True
            print("\nUpdate Employee Details (press Enter to skip updating any field):")
            
            new_fName = input("Enter new first name: ")
            if new_fName: emp.set_fName(new_fName)  # Update first name if provided

            new_lName = input("Enter new last name: ")
            if new_lName: emp.set_lName(new_lName)  # Update last name if provided

            # Loop until a valid age is entered or the user chooses to skip
            while True:
                new_age = input("Enter new age: ")
                if new_age == "":  # If the user leaves it blank, skip
                    break
                if validate_age(new_age):
                    emp.set_age(int(new_age))  # Update age if valid
                    break  # Exit the loop if valid
                else:
                    print("Invalid age. Please enter a valid age between 18 and 100.")

            new_dept = input("Enter new department: ")
            if new_dept: emp.set_dept(new_dept)  # Update department if provided

            # Initialize variables for rate of pay and hours worked
            new_rate_of_pay = None
            new_hours_worked = None

            if isinstance(emp, PartTimeEmployee):
                # Loop until a valid hours worked is entered or the user chooses to skip
                while True:
                    new_hours_worked = input("Enter new hours worked: ")
                    if new_hours_worked == "":  # If the user leaves it blank, skip
                        break
                    if validate_hours(new_hours_worked):
                        emp._PartTimeEmployee__hours_worked = int(new_hours_worked)  # Update hours worked
                        break  # Exit the loop if valid
                    else:
                        print("Invalid hours worked. Please enter a valid number.")

            elif isinstance(emp, FullTimeEmployee):
                # Loop until a valid rate of pay is entered or the user chooses to skip
                while True:
                    new_rate_of_pay = input("Enter new rate of pay: ")
                    if new_rate_of_pay == "":  # If the user leaves it blank, skip
                        break
                    if validate_rate(new_rate_of_pay):
                        emp._FullTimeEmployee__rate_of_pay = float(new_rate_of_pay # Update rate of pay if valid
                        break  # Exit the loop if valid
                    else:
                        print("Invalid rate of pay. Please enter a valid number.")

            # Update employee type if needed
            new_emp_type = input("Change Employee Type? (full-time/part-time/intern): ").lower()
            
            if new_emp_type == 'full-time' and not isinstance(emp, FullTimeEmployee):
                if new_rate_of_pay is None:  # Ask for rate of pay only if not already provided
                    new_rate_of_pay = input("Enter rate of pay: ")
                    while not validate_rate(new_rate_of_pay):
                        print("Rate of pay must be greater than 0.")
                        new_rate_of_pay = input("Enter rate of pay: ")
                benefits = input("Enter benefits (comma-separated): ")
                vacationDays = int(input("Enter number of vacation days: "))
                # Create a new FullTimeEmployee instance and replace the old one
                employees[i] = FullTimeEmployee(emp.get_fName(), emp.get_lName(), emp.get_age(), emp.get_emp_id(),
                                                emp.get_dept(), float(new_rate_of_pay), benefits, vacationDays)
                print("Employee changed to Full-Time.")
            
            elif new_emp_type == 'part-time' and not isinstance(emp, PartTimeEmployee):
                if new_hours_worked is None:  # Ask for hours worked only if not already provided
                    new_hours_worked = input("Enter hours worked: ")
                    while not validate_hours(new_hours_worked):
                        print("Hours worked must be greater than 0.")
                        new_hours_worked = input("Enter hours worked: ")
                if new_rate_of_pay is None:  # Ask for rate of pay only if not already provided
                    new_rate_of_pay = input("Enter rate of pay: ")
                    while not validate_rate(new_rate_of_pay):
                        print("Rate of pay must be greater than 0.")
                        new_rate_of_pay = input("Enter rate of pay: ")
                # Create a new PartTimeEmployee instance and replace the old one
                employees[i] = PartTimeEmployee(emp.get_fName(), emp.get_lName(), emp.get_age(), emp.get_emp_id(),
                                                  emp.get_dept(), int(new_hours_worked), float(new_rate_of_pay))
                print("Employee changed to Part-Time.")
            
            elif new_emp_type == 'intern' and not isinstance(emp, Intern):
                # Create a new Intern instance and replace the old one
                employees[i] = Intern(emp.get_fName(), emp.get_lName(), emp.get_age(), emp.get_emp_id(), emp.get_dept())
                print("Employee changed to Intern.")

            # Recalculate salary after updates
            print(f"Updated Salary: ${employees[i].calc_salary()}")

            save_employees(employees)  # Save the updated employee list to the file
            break  # Exit the loop after updating

    if not found:
        print("Employee ID not found.")  # Message if employee ID is not found

def delete_employee(employees):
    emp_id = input("Enter employee ID to delete: ")
    for i, emp in enumerate(employees):
        if emp.get_emp_id() == emp_id:
            del employees[i]  # Remove the employee from the list
            print(f"Employee ID {emp_id} deleted successfully.")
            save_employees(employees)  # Save the updated list to the file
            return  # Exit the function after deletion
    print("Employee not found.")  # Message if employee ID is not found

# Main function for Payroll System
def main():
    employees = load_employees()  # Load existing employees from file

    while True:
        # Display the main menu for the payroll system
        print("\nPayroll System Menu:")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")  # Get user choice

        # Call the appropriate function based on user choice
        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            list_employees(employees)
        elif choice == '3':
            update_employee(employees)
        elif choice == '4':
            delete_employee(employees)
        elif choice == '5':
            print("Exiting the Payroll System.")  # Exit message
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")  # Message for invalid choice

if __name__ == "__main__":
    main()  # Start the payroll system
