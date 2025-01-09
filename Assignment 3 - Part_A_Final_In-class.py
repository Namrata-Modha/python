"""
Date: 31-10-2024
Author: Namrata Modha
Purpose: WAP that uses OOP to create a class for an employee object.
Your program should display employee details inclusive of name, age, id, number, employee_type(Fulltime, Partime), hours_worked, rate_of_pay
If partime salary = hours worked * rate
your class should include a function called calc_salary() to compute the salary of the staff.
It should also include a method to display the details.
"""

class Employee:
    def __init__(self, name, age, emp_id, number, employee_type, hours_worked, rate_of_pay):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.number = number
        self.employee_type = employee_type  # Fulltime or Parttime
        self.hours_worked = hours_worked
        self.rate_of_pay = rate_of_pay

    # Calculate salary based on employee type
    def calc_salary(self):
        if (self.employee_type.lower() == "parttime"):
            return (self.hours_worked * self.rate_of_pay)
        else:
            return self.rate_of_pay # Assuming full-time employees have a fixed salary

     # Display employee details
    def emp_details(self):
        print(f"Employee Details:\n")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Number: {self.number}")
        print(f"Employee Type: {self.employee_type}")
        print(f"Hours Worked: {self.hours_worked}")
        print(f"Rate of Pay: ${self.rate_of_pay}")
        print(f"Calculated Salary: ${self.calc_salary()}")
        
emp1 = Employee("Nam", 25, "E123", "555-0123", "Parttime", 16, 17.50)
emp2 = Employee("Alice", 28, "E124", "555-0456", "Fulltime", 40, 3000)

emp1.emp_details()
print("\n")
emp2.emp_details()
