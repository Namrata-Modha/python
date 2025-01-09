"""
Author: Namrata Modha
Purpose: Write a program that simulates the payroll system as we have been working on thus far in class.
Introduce object-oriented programming as a programming paradigm to achieve the objective.
Your program should include a class with attributes and methods pertinent to the payroll system, i.e., an Employee class.
It should include the OOP constructs of encapsulation and abstraction. Use getters and setters to achieve this.
The following requirements are to be adhered to:

- Prompt the user to enter all input values
- Include a main function
- In your program, include functions to add a new staff, list staff details, update staff details, and exit
- Create at least one (1) instance of the Employee class  
- Use the getters and setters methods to update the employee details.

Date: 11-11-2024
"""

# File path for storing employee data
EMPLOYEE_FILE = "employees.txt"

class Employee:
    def __init__(self, fName, lName, age, emp_id, dept, hours_worked, rate_of_pay, emp_type="part-time"):
        # Encapsulated attributes (private)
        self.__fName = fName
        self.__lName = lName
        self.__age = age
        self.__emp_id = emp_id
        self.__dept = dept
        self.__hours_worked = hours_worked
        self.__rate_of_pay = rate_of_pay
        self.__emp_type = emp_type  # This will hold the type of employee, default is part-time

    # Getters and Setters
    def get_fName(self): return self.__fName
    def set_fName(self, fName): self.__fName = fName
    def get_lName(self): return self.__lName
    def set_lName(self, lName): self.__lName = lName
    def get_age(self): return self.__age
    def set_age(self, age): 
        # Age validation
        if 18 <= age <= 100:
            self.__age = age
        else:
            print("Invalid age. Please enter an age between 18 and 100.")
    def get_emp_id(self): return self.__emp_id
    def set_emp_id(self, emp_id): self.__emp_id = emp_id
    def get_dept(self): return self.__dept
    def set_dept(self, dept): self.__dept = dept
    def get_hours_worked(self): return self.__hours_worked
    def set_hours_worked(self, hours_worked): 
        if isinstance(hours_worked, (int, float)):
            self.__hours_worked = hours_worked
        else:
            print("Error: Hours worked must be a number.")
    def get_rate_of_pay(self): return self.__rate_of_pay
    def set_rate_of_pay(self, rate_of_pay):
        if isinstance(rate_of_pay, (int, float)):
            self.__rate_of_pay = rate_of_pay
        else:
            print("Error: Rate of pay must be a number.")

    # Calculate salary
    def calc_salary(self):
        if self.__emp_type == "full-time":
            return self.__rate_of_pay * 40  # Monthly salary for full-time
        else:
            return self.__hours_worked * self.__rate_of_pay  # Hourly rate for part-time

    # Display employee details
    def emp_details(self):
        print("\nEmployee Details:")
        print(f"First Name: {self.get_fName()}")
        print(f"Last Name: {self.get_lName()}")
        print(f"Age: {self.get_age()}")
        print(f"Employee ID: {self.get_emp_id()}")
        print(f"Department: {self.get_dept()}")
        print(f"Hours Worked: {self.get_hours_worked()}")
        print(f"Rate of Pay: ${self.get_rate_of_pay()}")
        print(f"Calculated Salary: ${self.calc_salary()}")
        if isinstance(self, FullTimeEmployee):
            print("Employee Type: Full-Time")
        else:
            print("Employee Type: Part-Time")

    # Format employee data for saving to file
    def to_string(self):
        # self.__class__.__name__ returns the name of the class (either Employee or FullTimeEmployee).And the rest concatenates the private variables, separated by commas
        return f"{self.__class__.__name__},{self.__fName},{self.__lName},{self.__age},{self.__emp_id},{self.__dept},{self.__hours_worked},{self.__rate_of_pay}"

    # Factory method to create Employee from string
    @staticmethod
    def from_string(data):
        parts = data.split(',')
        # returns either an Employee or FullTimeEmployee object based on the first element in the string (parts[0]).
        if parts[0] == "FullTimeEmployee":
            return FullTimeEmployee(parts[1], parts[2], int(parts[3]), parts[4], parts[5],
                                    float(parts[6]), float(parts[7]), parts[8], int(parts[9]))
        else:
            return Employee(parts[1], parts[2], int(parts[3]), parts[4], parts[5],
                            float(parts[6]), float(parts[7]))


class FullTimeEmployee(Employee):
    def __init__(self, fName, lName, age, emp_id, dept, hours_worked, rate_of_pay, benefits, vacationDays):
        super().__init__(fName, lName, age, emp_id, dept, hours_worked, rate_of_pay)
        self.__benefits = benefits
        self.__vacationDays = vacationDays

    # Override salary calculation
    def calc_salary(self):
        return self.get_rate_of_pay() * 40

    # Display full-time employee details
    def emp_details(self):
        super().emp_details()
        print(f"Benefits: {self.__benefits}")
        print(f"Vacation Days: {self.__vacationDays}")

    # Format full-time employee data for saving to file
    def to_string(self):
        return f"{super().to_string()},{self.__benefits},{self.__vacationDays}"


# Helper function to load employees from file
def load_employees():
    employees = []
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")
                # Load data depending on whether the employee is full-time or not
                if data[7] == "full-time":
                    # Benefits remain as comma-separated string within the benefits field
                    employees.append(FullTimeEmployee(data[0], data[1], int(data[2]), data[3], data[4], 
                                                      float(data[5]), float(data[6]), data[8], int(data[9])))
                else:
                    employees.append(Employee(data[0], data[1], int(data[2]), data[3], data[4], 
                                              float(data[5]), float(data[6])))
    except FileNotFoundError:
        print("Employee file not found. Starting with an empty list.")
    return employees


# Helper function to save employees to file
def save_employees(employees):
    with open("employees.txt", "w") as file:
        for emp in employees:
            # Prepare data string based on whether the employee is full-time or not
            if isinstance(emp, FullTimeEmployee):
                line = f"{emp.get_fName()}|{emp.get_lName()}|{emp.get_age()}|{emp.get_emp_id()}|{emp.get_dept()}|{emp.get_hours_worked()}|{emp.get_rate_of_pay()}|full-time|{emp._FullTimeEmployee__benefits}|{emp._FullTimeEmployee__vacationDays}\n"
            else:
                line = f"{emp.get_fName()}|{emp.get_lName()}|{emp.get_age()}|{emp.get_emp_id()}|{emp.get_dept()}|{emp.get_hours_worked()}|{emp.get_rate_of_pay()}|part-time|\n"
            file.write(line)

# Helper function to delete employees from the file
def delete_employee(employees, emp_id):
    # Find employee by ID and remove from list
    for i, emp in enumerate(employees):
        if emp.get_emp_id() == emp_id:
            del employees[i]
            print(f"Employee ID {emp_id} deleted successfully.")
            save_employees(employees)
            return
    print("Employee not found.")

# Main function for Payroll System
def main():
    employees = load_employees()

    while True:
        print("\nPayroll System Menu:")
        print("1. Add New Staff")
        print("2. List Staff Details")
        print("3. Update Staff Details")
        print("4. Delete Staff")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add New Staff
            fName = input("Enter first name: ")
            lName = input("Enter last name: ")
            age = int(input("Enter age: "))
            emp_id = input("Enter employee ID: ")
            dept = input("Enter department: ")
            hours_worked = float(input("Enter hours worked: "))
            rate_of_pay = float(input("Enter rate of pay: "))
            emp_type = input("Is this a Full-Time employee? (yes/no): ").lower()

            if emp_type == 'yes':
                benefits = input("Enter benefits (comma-separated): ")
                vacationDays = int(input("Enter number of vacation days: "))
                new_employee = FullTimeEmployee(fName, lName, age, emp_id, dept, hours_worked, rate_of_pay, benefits, vacationDays)
            else:
                new_employee = Employee(fName, lName, age, emp_id, dept, hours_worked, rate_of_pay)

            employees.append(new_employee)
            save_employees(employees)
            print("Employee added successfully!")

        elif choice == '2':
            # List Staff Details
            if employees:
                for emp in employees:
                    emp.emp_details()
            else:
                print("No employees found.")

        elif choice == '3':
            # Update Staff Details
            emp_id = input("Enter employee ID to update details: ")
            found = False
            for i, emp in enumerate(employees):
                if emp.get_emp_id() == emp_id:
                    found = True
                    print("\nUpdate Employee Details (press Enter to skip updating any field):")
                    
                    new_fName = input("Enter new first name (leave blank to keep current): ")
                    if new_fName: emp.set_fName(new_fName)

                    new_lName = input("Enter new last name (leave blank to keep current): ")
                    if new_lName: emp.set_lName(new_lName)

                    new_age = input("Enter new age (leave blank to keep current): ")
                    if new_age: emp.set_age(int(new_age))

                    new_dept = input("Enter new department (leave blank to keep current): ")
                    if new_dept: emp.set_dept(new_dept)

                    new_hours_worked = input("Enter new hours worked (leave blank to keep current): ")
                    if new_hours_worked: emp.set_hours_worked(float(new_hours_worked))

                    new_rate_of_pay = input("Enter new rate of pay (leave blank to keep current): ")
                    if new_rate_of_pay: emp.set_rate_of_pay(float(new_rate_of_pay))

                    # Update employee type if needed
                    new_emp_type = input("Change to Full-Time? (yes/no/leave blank to keep current): ").lower()
                    if new_emp_type == 'yes' and not isinstance(emp, FullTimeEmployee):
                        benefits = input("Enter benefits (comma-separated): ")
                        vacationDays = int(input("Enter number of vacation days: "))
                        employees[i] = FullTimeEmployee(emp.get_fName(), emp.get_lName(), emp.get_age(), emp.get_emp_id(),
                                                        emp.get_dept(), emp.get_hours_worked(), emp.get_rate_of_pay(),
                                                        benefits, vacationDays)
                        print("Employee changed to Full-Time. Calculated pay updated accordingly.")
                    
                    elif new_emp_type == 'no' and isinstance(emp, FullTimeEmployee):
                        # Convert to a regular Employee
                        employees[i] = Employee(emp.get_fName(), emp.get_lName(), emp.get_age(), emp.get_emp_id(),
                                                emp.get_dept(), emp.get_hours_worked(), emp.get_rate_of_pay())
                        print("Employee changed to Part-Time. Calculated pay updated accordingly.")

                    save_employees(employees)
                    print("Employee details updated successfully!")
                    break
            if not found:
                print("Employee not found with the provided ID.")

        elif choice == '4':
            # Delete Staff
            emp_id = input("Enter employee ID to delete: ")
            delete_employee(employees, emp_id)

        elif choice == '5':
            print("Exiting the Payroll System.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

