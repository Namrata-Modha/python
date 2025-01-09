import sqlite3
from tkinter import *
from tkinter import messagebox

# Database connection
conn = sqlite3.connect('payroll_system.db')

# Class Definitions
class Payroll:
    def __init__(self):
        self.employees = []
        self.compensations = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_compensation(self, compensation):
        self.compensations.append(compensation)

    def get_all_employees(self):
        return self.employees

    def get_all_compensations(self):
        return self.compensations

class Employee:
    def __init__(self, name, employee_type):
        self.name = name
        self.type = employee_type
        self.employee_id = None

    def save(self):
        try:
            with conn:
                cursor = conn.execute("INSERT INTO Employee (name, type) VALUES (?, ?)", (self.name, self.type))
                self.employee_id = cursor.lastrowid  # This captures the employee_id of the newly inserted row
                return self.employee_id
        except sqlite3.Error as e:
            raise ValueError(f"Error saving employee to database: {e}")

    @staticmethod
    def get_all():
        try:
            with conn:
                return conn.execute("SELECT * FROM Employee").fetchall()
        except sqlite3.Error as e:
            raise ValueError(f"Error retrieving employees: {e}")

class FullTime(Employee):
    def __init__(self, name, hourly_rate):
        super().__init__(name, "Full-Time")
        self.hourly_rate = hourly_rate
        self.hours_worked = 40 * 4  # Full-time: 40 hours/week * 4 weeks

    def calculate_salary(self):
        salary = self.hourly_rate * self.hours_worked
        return salary

class PartTime(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, "Part-Time")
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        salary = self.hourly_rate * self.hours_worked
        return salary

class Vehicle:
    def __init__(self, employee_id, make, model, year):
        self.employee_id = employee_id
        self.make = make
        self.model = model
        self.year = year

    def save(self):
        try:
            with conn:
                conn.execute("INSERT INTO Vehicle (employee_id, make, model, year) VALUES (?, ?, ?, ?)",
                             (self.employee_id, self.make, self.model, self.year))
        except sqlite3.Error as e:
            raise ValueError(f"Error saving vehicle to database: {e}")

    @staticmethod
    def get_by_employee(employee_id):
        try:
            with conn:
                return conn.execute("SELECT * FROM Vehicle WHERE employee_id = ?", (employee_id,)).fetchall()
        except sqlite3.Error as e:
            raise ValueError(f"Error retrieving vehicle information: {e}")

class Compensation:
    def __init__(self, employee_id, hourly_rate, hours_worked, benefits, vacation_days, employee_type):
        self.employee_id = employee_id
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.benefits = benefits
        self.vacation_days = vacation_days
        self.employee_type = employee_type
        self.tax_rate, self.tax_rate_percentage = self.set_tax_rate(employee_type)
        self.monthly_salary = self.calculate_salary(employee_type)

    def set_tax_rate(self, employee_type):
        if employee_type == 'Part-Time':
            return 0.15, "15%"  # 15% tax for part-time employees
        elif employee_type == 'Full-Time':
            return 0.18, "18%"  # 18% tax for full-time employees
        elif employee_type == 'Intern':
            return 0, "0%"  # 0% tax for interns
        else:
            raise ValueError("Invalid employee type")

    def calculate_salary(self, employee_type):
        try:
            if employee_type == 'Part-Time':
                salary = self.hourly_rate * self.hours_worked
            elif employee_type == 'Full-Time':
                salary = self.hourly_rate * 40 * 4  # 40 hours per week, 4 weeks in a month
            elif employee_type == 'Intern':
                salary = 200  # Fixed salary for interns
            else:
                raise ValueError("Invalid employee type")
            
            salary_after_tax = salary - (salary * self.tax_rate)
            return salary_after_tax, salary * self.tax_rate
        except Exception as e:
            raise ValueError(f"Error calculating salary: {e}")

    def save(self):
        try:
            with conn:
                conn.execute("INSERT INTO Compensation (employee_id, hourly_rate, hours_worked, benefits, vacation_days, monthly_salary, tax_rate) VALUES (?, ?, ?, ?, ?, ?, ?)",
                             (self.employee_id, self.hourly_rate, self.hours_worked, self.benefits, self.vacation_days, self.monthly_salary[0], self.tax_rate_percentage))
        except sqlite3.Error as e:
            raise ValueError(f"Error saving compensation to database: {e}")


# GUI Setup
root = Tk()
root.title("Payroll System")
root.geometry("600x600")

def toggle_fields(*args):
    employee_type = employee_type_var.get()

    # Hide or show fields based on the employee type
    if employee_type == 'Part-Time':
        hourly_rate_label.grid(row=3, column=0, padx=10, pady=10)
        hourly_rate_entry.grid(row=3, column=1)
        hours_worked_label.grid(row=4, column=0, padx=10, pady=10)
        hours_worked_entry.grid(row=4, column=1)
        vacation_days_label.grid_remove()
        vacation_days_entry.grid_remove()
        benefits_label.grid_remove()
        benefits_entry.grid_remove()
    elif employee_type == 'Full-Time':
        hourly_rate_label.grid(row=3, column=0, padx=10, pady=10)
        hourly_rate_entry.grid(row=3, column=1)
        hours_worked_label.grid_remove()
        hours_worked_entry.grid_remove()
        vacation_days_label.grid(row=6, column=0, padx=10, pady=10)
        vacation_days_entry.grid(row=6, column=1)
        benefits_label.grid(row=5, column=0, padx=10, pady=10)
        benefits_entry.grid(row=5, column=1)
    elif employee_type == 'Intern':
        hourly_rate_label.grid_remove()
        hourly_rate_entry.grid_remove()
        hours_worked_label.grid_remove()
        hours_worked_entry.grid_remove()
        vacation_days_label.grid_remove()
        vacation_days_entry.grid_remove()
        benefits_label.grid_remove()
        benefits_entry.grid_remove()

# Fetch Employees and Update Table
def update_employee_table():
        for widget in employee_table_frame.winfo_children():
            widget.destroy()

        # Define the headers including the extra fields from the joins
        headers = ["ID", "Name", "Type", "Hourly Rate", "Hours Worked", "Benefits", "Vacation Days", "Monthly Salary", "Tax Rate", "Vehicle Make", "Vehicle Model", "Vehicle Year"]
        
        # Create header labels
        for col, header in enumerate(headers):
            Label(employee_table_frame, text=header, borderwidth=1, relief="solid", width=15).grid(row=0, column=col)

        try:
            with conn:
                # Modified SQL query with JOINs Employee, Compensation, and Vehicle tables
                query = """
                SELECT e.employee_id, e.name, e.type, 
                   c.hourly_rate, c.hours_worked, c.benefits, c.vacation_days, c.monthly_salary, c.tax_rate,
                   v.make AS vehicle_make, v.model AS vehicle_model, v.year AS vehicle_year
                FROM Employee e
                LEFT JOIN Compensation c ON e.employee_id = c.employee_id
                LEFT JOIN Vehicle v ON e.employee_id = v.employee_id
                """
                employees = conn.execute(query).fetchall()
                
                # Populate the table with data
                for row_num, employee in enumerate(employees, start=1):
                    for col_num, value in enumerate(employee):
                        Label(employee_table_frame, text=value, borderwidth=1, relief="solid", width=15).grid(row=row_num, column=col_num)
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error retrieving employee list: {e}")


def calculate_salary():
    try:
        # Get employee type from dropdown
        employee_type = employee_type_var.get()
        name = name_entry.get().strip()
        if not name:
            raise ValueError("Employee name is required.")
        
        # Validate and get vehicle details
        vehicle_make = vehicle_make_entry.get().strip()
        vehicle_model = vehicle_model_entry.get().strip()
        try:
            vehicle_year = int(vehicle_year_entry.get().strip()) if vehicle_year_entry.get() else None
        except ValueError:
            raise ValueError("Vehicle year must be a valid number.")

        # For Interns, use the fixed salary and skip validations for hourly_rate, hours_worked, and vacation_days
        if employee_type == 'Intern':
            hourly_rate = 0  # Interns don't have an hourly rate
            hours_worked = 0  # Interns don't need to provide hours worked
            vacation_days = 0  # Interns don't need to provide vacation days
            benefits = 'None'  # Default benefits for Interns
        else:
            # Read and validate hourly_rate (for Part-Time and Full-Time)
            try:
                hourly_rate = float(hourly_rate_entry.get())
            except ValueError:
                raise ValueError("Hourly Rate must be a number.")
            
            # For Full-Time, set hours_worked to 160 hours per month (40 hours per week * 4 weeks)
            if employee_type == 'Full-Time':
                hours_worked = 40 * 4
            else:
                try:
                    # Read and validate hours_worked (only for Part-Time)
                    hours_worked = float(hours_worked_entry.get())
                except ValueError:
                    raise ValueError("Hours Worked must be a number.")
            
            # Read and validate vacation_days (for all employee types)
            try:
                vacation_days = int(vacation_days_entry.get()) if vacation_days_entry.get() else 0
            except ValueError:
                raise ValueError("Vacation Days must be an integer.")
            
            benefits = benefits_entry.get() if benefits_entry.get() else 'None'  # Default benefits if not provided

        # Create Employee instance
        employee = None
        if employee_type == "Full-Time":
            employee = FullTime(name, hourly_rate)
        elif employee_type == "Part-Time":
            employee = PartTime(name, hourly_rate, hours_worked)
        else:
            employee = Employee(name, employee_type)

        # Save employee and get employee_id
        employee_id = employee.save()  # Save and retrieve the employee_id

        # Create a Compensation instance and calculate salary
        compensation = Compensation(employee_id, hourly_rate, hours_worked, benefits, vacation_days, employee_type)
        
        # Get salary and tax
        monthly_salary_after_tax, tax_amount = compensation.calculate_salary(employee_type)
        
        # Display salary after tax, tax amount, and tax rate
        monthly_salary_label_val.config(text=f"{monthly_salary_after_tax:.2f}")
        tax_label_val.config(text=f"{tax_amount:.2f}")
        tax_rate_label_val.config(text=f"{compensation.tax_rate_percentage}")

        # Save to database
        compensation.save()

        # Save Vehicle if details are provided
        if vehicle_make and vehicle_model and vehicle_year:
            vehicle = Vehicle(employee_id, vehicle_make, vehicle_model, vehicle_year)
            vehicle.save()

        messagebox.showinfo("Success", f"Salary calculated: ${monthly_salary_after_tax:.2f}")
        # Table Update
        update_employee_table()
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
        
def edit_employee():
    def proceed_with_edit():
        try:
            employee_id = int(id_entry.get().strip())
            employee = conn.execute("SELECT * FROM Employee WHERE employee_id = ?", (employee_id,)).fetchone()
            if not employee:
                raise ValueError("Employee ID not found.")
            
            # Close the ID entry window
            id_window.destroy()

            # Fetch Compensation and Vehicle data
            compensation = conn.execute("SELECT * FROM Compensation WHERE employee_id = ?", (employee_id,)).fetchone()
            vehicle = conn.execute("SELECT * FROM Vehicle WHERE employee_id = ?", (employee_id,)).fetchone()

            # Popup window for editing
            edit_window = Toplevel(root)
            edit_window.title("Edit Employee")
            
            # Employee Details
            name_label = Label(edit_window, text="Employee Name")
            name_label.grid(row=0, column=0, padx=10, pady=10)
            name_entry = Entry(edit_window)
            name_entry.insert(0, employee[1])  # Populate existing name
            name_entry.grid(row=0, column=1, padx=10, pady=10)

            type_label = Label(edit_window, text="Employee Type")
            type_label.grid(row=1, column=0, padx=10, pady=10)
            type_entry = Entry(edit_window)
            type_entry.insert(0, employee[2])  # Populate existing type
            type_entry.grid(row=1, column=1, padx=10, pady=10)

            # Compensation Details
            hourly_rate_label = Label(edit_window, text="Hourly Rate")
            hourly_rate_label.grid(row=2, column=0, padx=10, pady=10)
            hourly_rate_entry = Entry(edit_window)
            hourly_rate_entry.insert(0, compensation[1] if compensation else "")
            hourly_rate_entry.grid(row=2, column=1, padx=10, pady=10)

            hours_worked_label = Label(edit_window, text="Hours Worked")
            hours_worked_label.grid(row=3, column=0, padx=10, pady=10)
            hours_worked_entry = Entry(edit_window)
            hours_worked_entry.insert(0, compensation[2] if compensation else "")
            hours_worked_entry.grid(row=3, column=1, padx=10, pady=10)

            benefits_label = Label(edit_window, text="Benefits")
            benefits_label.grid(row=4, column=0, padx=10, pady=10)
            benefits_entry = Entry(edit_window)
            benefits_entry.insert(0, compensation[3] if compensation else "")
            benefits_entry.grid(row=4, column=1, padx=10, pady=10)

            vacation_days_label = Label(edit_window, text="Vacation Days")
            vacation_days_label.grid(row=5, column=0, padx=10, pady=10)
            vacation_days_entry = Entry(edit_window)
            vacation_days_entry.insert(0, compensation[4] if compensation else "")
            vacation_days_entry.grid(row=5, column=1, padx=10, pady=10)

            # Vehicle Details
            vehicle_make_label = Label(edit_window, text="Vehicle Make")
            vehicle_make_label.grid(row=6, column=0, padx=10, pady=10)
            vehicle_make_entry = Entry(edit_window)
            vehicle_make_entry.insert(0, vehicle[2] if vehicle else "")
            vehicle_make_entry.grid(row=6, column=1, padx=10, pady=10)

            vehicle_model_label = Label(edit_window, text="Vehicle Model")
            vehicle_model_label.grid(row=7, column=0, padx=10, pady=10)
            vehicle_model_entry = Entry(edit_window)
            vehicle_model_entry.insert(0, vehicle[3] if vehicle else "")
            vehicle_model_entry.grid(row=7, column=1, padx=10, pady=10)

            vehicle_year_label = Label(edit_window, text="Vehicle Year")
            vehicle_year_label.grid(row=8, column=0, padx=10, pady=10)
            vehicle_year_entry = Entry(edit_window)
            vehicle_year_entry.insert(0, vehicle[4] if vehicle else "")
            vehicle_year_entry.grid(row=8, column=1, padx=10, pady=10)

            def save_edit():
                try:
                    # Gather updated fields
                    new_name = name_entry.get().strip()
                    new_type = type_entry.get().strip()
                    new_hourly_rate = float(hourly_rate_entry.get().strip() or 0)
                    new_hours_worked = float(hours_worked_entry.get().strip() or 0)
                    new_benefits = benefits_entry.get().strip() or "None"
                    new_vacation_days = int(vacation_days_entry.get().strip() or 0)
                    new_vehicle_make = vehicle_make_entry.get().strip()
                    new_vehicle_model = vehicle_model_entry.get().strip()
                    new_vehicle_year = int(vehicle_year_entry.get().strip() or 0)

                    if not new_name or not new_type:
                        raise ValueError("Name and Type cannot be empty.")

                    # Update Employee
                    with conn:
                        conn.execute("UPDATE Employee SET name = ?, type = ? WHERE employee_id = ?", 
                                     (new_name, new_type, employee_id))

                    # Update Compensation
                    if compensation:
                        conn.execute("UPDATE Compensation SET hourly_rate = ?, hours_worked = ?, benefits = ?, vacation_days = ? WHERE employee_id = ?", 
                                     (new_hourly_rate, new_hours_worked, new_benefits, new_vacation_days, employee_id))
                    else:
                        conn.execute("INSERT INTO Compensation (employee_id, hourly_rate, hours_worked, benefits, vacation_days) VALUES (?, ?, ?, ?, ?)", 
                                     (employee_id, new_hourly_rate, new_hours_worked, new_benefits, new_vacation_days))

                    # Update Vehicle
                    if vehicle:
                        conn.execute("UPDATE Vehicle SET make = ?, model = ?, year = ? WHERE employee_id = ?", 
                                     (new_vehicle_make, new_vehicle_model, new_vehicle_year, employee_id))
                    elif new_vehicle_make and new_vehicle_model:
                        conn.execute("INSERT INTO Vehicle (employee_id, make, model, year) VALUES (?, ?, ?, ?)", 
                                     (employee_id, new_vehicle_make, new_vehicle_model, new_vehicle_year))

                    messagebox.showinfo("Success", "Employee updated successfully!")
                    edit_window.destroy()
                    update_employee_table()

                except ValueError as ve:
                    messagebox.showerror("Error", str(ve))
                except sqlite3.Error as e:
                    messagebox.showerror("Error", f"Database error: {e}")

            save_button = Button(edit_window, text="Save Changes", command=save_edit)
            save_button.grid(row=9, column=0, columnspan=2, pady=10)

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")

    # Entry window to get Employee ID
    id_window = Toplevel(root)
    id_window.title("Enter Employee ID")
    Label(id_window, text="Enter Employee ID:").grid(row=0, column=0, padx=10, pady=10)
    id_entry = Entry(id_window)
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    proceed_button = Button(id_window, text="Proceed", command=proceed_with_edit)
    proceed_button.grid(row=1, column=0, columnspan=2, pady=10)



def delete_employee():
    def proceed_with_delete():
        try:
            employee_id = int(id_entry.get().strip())
            
            with conn:
                # Delete related records in Vehicle (if not using ON DELETE CASCADE)
                conn.execute("DELETE FROM Vehicle WHERE employee_id = ?", (employee_id,))
                
                # Delete related records in Compensation (if not using ON DELETE CASCADE)
                conn.execute("DELETE FROM Compensation WHERE employee_id = ?", (employee_id,))
                
                # Delete the employee from Employee table
                result = conn.execute("DELETE FROM Employee WHERE employee_id = ?", (employee_id,))
                if result.rowcount == 0:
                    raise ValueError("Employee ID not found.")
            
            messagebox.showinfo("Success", "Employee deleted successfully!")
            id_window.destroy()  # Close the ID entry window
            update_employee_table()
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error deleting employee: {e}")

    # Create the ID entry window
    id_window = Toplevel(root)
    id_window.title("Enter Employee ID")
    Label(id_window, text="Enter Employee ID:").grid(row=0, column=0, padx=10, pady=10)
    id_entry = Entry(id_window)
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    proceed_button = Button(id_window, text="Proceed", command=proceed_with_delete)
    proceed_button.grid(row=1, column=0, columnspan=2, pady=10)

def list_employees():
    try:
        employees = Employee.get_all()
        if not employees:
            messagebox.showinfo("No Employees", "No employees found in the system.")
            return
        list_window = Toplevel(root)
        list_window.title("List of Employees")
        listbox = Listbox(list_window, width=50, height=20)
        listbox.pack(padx=10, pady=10)
        for emp in employees:
            listbox.insert(END, f"ID: {emp[0]}, Name: {emp[1]}, Type: {emp[2]}")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error retrieving employee list: {e}")

# Compensation fields (part-time/full-time)
employee_type_var = StringVar(value="")
employee_type_label = Label(root, text="Employee Type")
employee_type_label.grid(row=0, column=0, padx=10, pady=10)

employee_type_menu = OptionMenu(root, employee_type_var, "Part-Time", "Full-Time", "Intern")
employee_type_menu.grid(row=0, column=1, padx=10, pady=10)
employee_type_var.trace("w", toggle_fields)

# Input fields
name_label = Label(root, text="Employee Name")
name_label.grid(row=1, column=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=10)

hourly_rate_label = Label(root, text="Hourly Rate")
vacation_days_label = Label(root, text="Vacation Days")
hours_worked_label = Label(root, text="Hours Worked")
benefits_label = Label(root, text="Benefits")

hourly_rate_entry = Entry(root)
hours_worked_entry = Entry(root)
vacation_days_entry = Entry(root)
benefits_entry = Entry(root)


monthly_salary_label = Label(root, text="Monthly Salary After Tax")
monthly_salary_label.grid(row=7, column=0, padx=10, pady=10)
monthly_salary_label_val = Label(root, text="0")
monthly_salary_label_val.grid(row=7, column=1, padx=10, pady=10)

# Tax Amount and Rate Labels
tax_label = Label(root, text="Tax Amount")
tax_label.grid(row=8, column=0, padx=10, pady=10)
tax_label_val = Label(root, text="0")
tax_label_val.grid(row=8, column=1, padx=10, pady=10)

tax_rate_label = Label(root, text="Tax Rate")
tax_rate_label.grid(row=9, column=0, padx=10, pady=10)
tax_rate_label_val = Label(root, text="0%")
tax_rate_label_val.grid(row=9, column=1, padx=10, pady=10)

# Separator/Title for vehicle section
vehicle_section_label = Label(root, text="Vehicle Information (Optional)", font=("Arial", 12, "bold"))
vehicle_section_label.grid(row=10, column=0, columnspan=2, pady=10)

# Vehicle fields
vehicle_make_label = Label(root, text="Vehicle Make")
vehicle_make_label.grid(row=11, column=0, padx=10, pady=10)
vehicle_make_entry = Entry(root)
vehicle_make_entry.grid(row=11, column=1, padx=10, pady=10)

vehicle_model_label = Label(root, text="Vehicle Model")
vehicle_model_label.grid(row=12, column=0, padx=10, pady=10)
vehicle_model_entry = Entry(root)
vehicle_model_entry.grid(row=12, column=1, padx=10, pady=10)

vehicle_year_label = Label(root, text="Vehicle Year")
vehicle_year_label.grid(row=13, column=0, padx=10, pady=10)
vehicle_year_entry = Entry(root)
vehicle_year_entry.grid(row=13, column=1, padx=10, pady=10)

calculate_button = Button(root, text="Add Employee", command=calculate_salary)
calculate_button.grid(row=14, column=1, padx=10, pady=10)

edit_button = Button(root, text="Edit Employee", command=edit_employee)
edit_button.grid(row=14, column=0, padx=10, pady=10)

delete_button = Button(root, text="Delete Employee", command=delete_employee)
delete_button.grid(row=15, column=0, padx=10, pady=10)

# Table Frame
employee_table_frame = Frame(root)
employee_table_frame.grid(row=16, column=0, columnspan=3, padx=10, pady=10)

# Initial Table Update
update_employee_table()

root.mainloop()
