"""
Author: Namrata Modha
Purpose: Demonstrate the use of Inheritence in python
Date: 07-11-2024
"""
class Employee:
    def __init__(self, fName, lName, age, emp_id, dept, hours_worked, rate_of_pay):
        self.fName = fName
        self.lName = lName
        self.age = age
        self.emp_id = emp_id
        self.dept = dept #Department 
        self.hours_worked = hours_worked
        self.rate_of_pay = rate_of_pay
        
    # Display employee details
    def emp_details(self):
        print(f"Employee Details:\n")
        print(f"First Name: {self.fName}")
        print(f"Last Name: {self.lName}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.dept}")
        print(f"Hours Worked: {self.hours_worked}")
        print(f"Rate of Pay: ${self.rate_of_pay}")
        print(f"Calculated Salary: ${self.calc_salary()}")
        
    # Calculate salary
    def calc_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, fName, lName, age, emp_id, dept, hours_worked, rate_of_pay, benefits, vacationDays):
        super().__init__(fName, lName, age, emp_id, dept, hours_worked, rate_of_pay)
        self.benefits = benefits
        self.vacationDays = vacationDays

    # Override salary calculation for full-time employees
    def calc_salary(self):
        return self.rate_of_pay  # Fixed monthly salary for full-time employees

    # Overriding emp_details to include full-time specific details
    def emp_details(self):
        super().emp_details()
        print(f"Benefits: {self.benefits}")
        print(f"Vacation Days: {self.vacationDays}")

#Displaying Values
emp = Employee("Nam", "Modha", 25, "E123", "HR", 16, 17.50)
emp.emp_details()

ftEmp = FullTimeEmployee("Alice", "Johnson", 28, "E124", "IT", 40, 3000, "Health, Dental", 20)
ftEmp.emp_details()
