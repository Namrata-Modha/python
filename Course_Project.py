import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Database Functions
def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect("payroll_system.db")

def fetch_departments():
    """Fetch all departments from the Departments table."""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT department_id, department_name FROM Departments")
        departments = cursor.fetchall()
        conn.close()
        return departments
    except Exception as e:
        print(f"An error occurred while fetching departments: {e}")
        return []

def fetch_employees():
    """Fetch all employees with details from the database."""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = '''
            SELECT eb.employee_id, eb.first_name || ' ' || eb.last_name AS Name, eb.age, d.department_name, 
                   ed.employee_type, ed.salary, GROUP_CONCAT(ebs.benefit_description, ', ') AS benefits, ed.rate_of_pay, ed.hours_worked, ed.vacation_days
            FROM EmployeeBasicInfo eb
            JOIN Departments d ON eb.department_id = d.department_id
            LEFT JOIN EmployeeDetails ed ON eb.employee_id = ed.employee_id
            LEFT JOIN EmployeeBenefits ebs ON eb.employee_id = ebs.employee_id
            GROUP BY eb.employee_id
        '''
        cursor.execute(query)
        employees = cursor.fetchall()
        conn.close()
        return employees
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Unable to fetch employees: {e}")
        return []

def calculate_salary(employee_type, rate_of_pay, hours_worked):
    """Calculate salary based on employee type."""
    try:
        rate_of_pay = float(rate_of_pay) if rate_of_pay is not None else 0.0
        hours_worked = float(hours_worked) if hours_worked is not None else 0.0

        if employee_type == "Part-Time":
            return rate_of_pay * hours_worked
        elif employee_type == "Full-Time":
            return rate_of_pay * 40  # Assume 40-hour workweek for full-time
        else:
            return 200  # Interns have a salary/stipend of fix 200
    except ValueError:
        raise ValueError("Invalid input for salary calculation.")


def update_employee_in_db(employee_id, basic_info, details_info):
    """Update employee data in the database."""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        # Update salary based on employee type
        employee_type = details_info[0]
        rate_of_pay = details_info[1]
        hours_worked = details_info[2] if employee_type == "Part-Time" else 0
        
        salary = calculate_salary(employee_type, rate_of_pay, hours_worked)

        cursor.execute('''UPDATE EmployeeBasicInfo 
                          SET first_name = ?, last_name = ?, age = ?, department_id = ?
                          WHERE employee_id = ?''', (*basic_info, employee_id))
        cursor.execute('''UPDATE EmployeeDetails 
                          SET employee_type = ?, rate_of_pay = ?, hours_worked = ?, vacation_days = ?, salary = ?
                          WHERE employee_id = ?''', (*details_info, salary, employee_id))
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        conn.close()

def delete_employee_from_db(employee_id):
    """Delete employee data from the database."""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM EmployeeDetails WHERE employee_id = ?', (employee_id,))
        cursor.execute('DELETE FROM EmployeeBasicInfo WHERE employee_id = ?', (employee_id,))
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        conn.close()

def save_benefits(employee_id, benefits):
    """Save benefits for a full-time employee."""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        for benefit in benefits:
            cursor.execute('''INSERT INTO EmployeeBenefits (employee_id, benefit_description)
                              VALUES (?, ?)''', (employee_id, benefit))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred while saving benefits: {e}")

# GUI Application
class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("900x700")
        self.root.configure(bg="#f5f5f5")

        # Title
        tk.Label(root, text="Employee Management System", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

        # Form Frame
        form_frame = tk.Frame(root, bg="#f5f5f5")
        form_frame.pack(pady=10)

        # Form Fields
        self.create_form_row(form_frame, "First Name:", "first_name_entry")
        self.create_form_row(form_frame, "Last Name:", "last_name_entry")
        self.create_form_row(form_frame, "Age:", "age_entry")

        # Department Dropdown
        tk.Label(form_frame, text="Department:", bg="#f5f5f5").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.dept_var = tk.StringVar()
        self.dept_var.set("Select Departments")  # Default value
        self.departments = fetch_departments()
        if not self.departments:
            messagebox.showerror("Error", "No departments found in the database. Please add departments first.")
        else:
            self.dept_dropdown = ttk.Combobox(form_frame, textvariable=self.dept_var, state="readonly")
            self.dept_dropdown['values'] = [f"{dept[1]} (ID: {dept[0]})" for dept in self.departments]
            self.dept_dropdown.grid(row=3, column=1, padx=10, pady=5)

        # Employee Type Dropdown
        tk.Label(form_frame, text="Employee Type:", bg="#f5f5f5").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.type_var = tk.StringVar()
        self.type_var.set("Select Employee Type")  # Default value
        tk.OptionMenu(form_frame, self.type_var, "Full-Time", "Part-Time", "Intern").grid(row=4, column=1, padx=10, pady=5)
        self.type_var.trace_add("write", self.update_dynamic_fields)

        # Dynamic Fields
        self.dynamic_frame = tk.Frame(root, bg="#f5f5f5")
        self.dynamic_frame.pack(pady=10)
        self.update_dynamic_fields()

        # Buttons
        button_frame = tk.Frame(root, bg="#f5f5f5")
        button_frame.pack(pady=20)
        tk.Button(button_frame, text="Add Employee", command=self.add_employee, bg="#4CAF50", fg="white", width=15).pack(side="left", padx=10)
        tk.Button(button_frame, text="Update Employee", command=self.update_employee, bg="#2196F3", fg="white", width=15).pack(side="left", padx=10)
        tk.Button(button_frame, text="Delete Employee", command=self.delete_employee, bg="#F44336", fg="white", width=15).pack(side="left", padx=10)

        # Employee Table
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Age", "Department", "Type", "Salary", "Benefits", "Pay", "Hours", "Vacation"), show="headings", height=10)
        self.tree.pack(pady=10, fill=tk.X)

        for col in ("ID", "Name", "Age", "Department", "Type", "Salary", "Benefits", "Pay", "Hours", "Vacation"):
            self.tree.heading(col, text=col)
        
        # Add event to handle row selection in treeview
        self.tree.bind("<ButtonRelease-1>", self.on_employee_select)

        self.update_employee_table()

    def create_form_row(self, parent, label_text, entry_attr):
        """Create a row for input fields."""
        row = len(parent.grid_slaves()) // 2
        tk.Label(parent, text=label_text, bg="#f5f5f5").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        setattr(self, entry_attr, tk.Entry(parent))
        getattr(self, entry_attr).grid(row=row, column=1, padx=10, pady=5)

    def update_dynamic_fields(self, *args):
        """Update dynamic fields based on employee type."""
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()

        emp_type = self.type_var.get()

        if emp_type == "Full-Time":
            self.create_form_row(self.dynamic_frame, "Rate of Pay:", "rate_of_pay_entry")
            self.create_form_row(self.dynamic_frame, "Vacation Days:", "vacation_days_entry")
            tk.Label(self.dynamic_frame, text="Benefits (comma separated):", bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=5, sticky="w")
            self.benefits_entry = tk.Entry(self.dynamic_frame)
            self.benefits_entry.grid(row=2, column=1, padx=10, pady=5)

        elif emp_type == "Part-Time":
            self.create_form_row(self.dynamic_frame, "Rate of Pay:", "rate_of_pay_entry")
            self.create_form_row(self.dynamic_frame, "Hours Worked:", "hours_worked_entry")

        elif emp_type == "Intern":
            # Intern has no pay, hours, or benefits fields
            pass

    def add_employee(self):
        """Add a new employee to the database."""
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = self.age_entry.get()
        department_name = self.dept_var.get()
        department_id = int(department_name.split(" (ID: ")[1].split(")")[0])
        employee_type = self.type_var.get()

        rate_of_pay = self.rate_of_pay_entry.get() if hasattr(self, "rate_of_pay_entry") else None
        hours_worked = self.hours_worked_entry.get() if hasattr(self, "hours_worked_entry") else None
        vacation_days = self.vacation_days_entry.get() if hasattr(self, "vacation_days_entry") else None
        benefits = self.benefits_entry.get().split(",") if hasattr(self, "benefits_entry") else []

        if not all([first_name, last_name, age]):
            messagebox.showerror("Error", "Please fill all required fields.")
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO EmployeeBasicInfo (first_name, last_name, age, department_id)
                              VALUES (?, ?, ?, ?)''', (first_name, last_name, age, department_id))
            employee_id = cursor.lastrowid

            cursor.execute('''INSERT INTO EmployeeDetails (employee_id, employee_type, rate_of_pay, hours_worked, vacation_days)
                              VALUES (?, ?, ?, ?, ?)''', (employee_id, employee_type, rate_of_pay, hours_worked, vacation_days))
            conn.commit()

            if benefits:
                save_benefits(employee_id, benefits)
            conn.close()
            messagebox.showinfo("Success", "Employee added successfully.")
            self.update_employee_table()
            self.clear_form()  # Clear the form after success
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def update_employee(self):
        """Update the selected employee's details."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an employee to update.")
            return

        # Retrieve values from existing widgets if they exist
        rate_of_pay = None
        hours_worked = None
        vacation_days = None
        benefits = []
        
        try:
            rate_of_pay = float(self.rate_of_pay_entry.get()) if hasattr(self, "rate_of_pay_entry") and self.rate_of_pay_entry.winfo_exists() else None
        except ValueError:
            rate_of_pay = None

        try:
            hours_worked = float(self.hours_worked_entry.get()) if hasattr(self, "hours_worked_entry") and self.hours_worked_entry.winfo_exists() else None
        except ValueError:
            hours_worked = None

        try:
            vacation_days = float(self.vacation_days_entry.get()) if hasattr(self, "vacation_days_entry") and self.vacation_days_entry.winfo_exists() else None
        except ValueError:
            vacation_days = None

        if hasattr(self, "benefits_entry") and self.benefits_entry.winfo_exists():
            benefits = self.benefits_entry.get().split(",")

        # Retrieve basic information
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = self.age_entry.get()
        department_name = self.dept_var.get()
        department_id = int(department_name.split(" (ID: ")[1].split(")")[0])
        employee_type = self.type_var.get()

        if not all([first_name, last_name, age, department_id]):
            messagebox.showerror("Error", "Please fill all required fields.")
            return

        # Get selected employee ID
        item = self.tree.item(selected_item)
        employee_id = item["values"][0]

        try:
            # Update employee in database
            update_employee_in_db(employee_id, (first_name, last_name, age, department_id),
                                  (employee_type, rate_of_pay, hours_worked, vacation_days))

            # Save benefits only for Full-Time employees
            if benefits and employee_type == "Full-Time":
                save_benefits(employee_id, benefits)

            messagebox.showinfo("Success", "Employee updated successfully.")
            self.update_employee_table()
            self.clear_form()  # Clear the form after success
            
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")


    def delete_employee(self):
        """Delete the selected employee from the database."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an employee to delete.")
            return

        item = self.tree.item(selected_item)
        employee_id = item["values"][0]

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete employee {employee_id}?")
        if confirm:
            delete_employee_from_db(employee_id)
            messagebox.showinfo("Success", "Employee deleted successfully.")
            self.update_employee_table()
            self.clear_form()  # Clear the form after success

    def on_employee_select(self, event):
        """Handle row selection in the employee table."""
        selected_item = self.tree.selection()
        if not selected_item:
            return

        item = self.tree.item(selected_item)
        values = item["values"]

        self.first_name_entry.delete(0, tk.END)
        self.first_name_entry.insert(0, values[1].split(" ")[0])
        self.last_name_entry.delete(0, tk.END)
        self.last_name_entry.insert(0, values[1].split(" ")[1])
        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, values[2])

        department_name = values[3]
        for dept in self.departments:
            if dept[1] == department_name:
                self.dept_var.set(f"{dept[1]} (ID: {dept[0]})")
                break
        
        self.type_var.set(values[4])
        self.update_dynamic_fields()

        if values[4] == "Full-Time":
            self.rate_of_pay_entry.delete(0, tk.END)
            self.rate_of_pay_entry.insert(0, values[7])
            self.vacation_days_entry.delete(0, tk.END)
            self.vacation_days_entry.insert(0, values[9])
            self.benefits_entry.delete(0, tk.END)
            self.benefits_entry.insert(0, values[6])
        elif values[4] == "Part-Time":
            self.rate_of_pay_entry.delete(0, tk.END)
            self.rate_of_pay_entry.insert(0, values[7])
            self.hours_worked_entry.delete(0, tk.END)
            self.hours_worked_entry.insert(0, values[8])

    def update_employee_table(self):
        """Update the employee table after any operation."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        employees = fetch_employees()
        for employee in employees:
            self.tree.insert("", "end", values=employee)
    
    def clear_form(self):
        """Clear all input fields in the form."""
        # Clear text entry fields
        self.first_name_entry.delete(0, 'end')
        self.last_name_entry.delete(0, 'end')
        self.age_entry.delete(0, 'end')
        
        if hasattr(self, "rate_of_pay_entry") and self.rate_of_pay_entry.winfo_exists():
            self.rate_of_pay_entry.delete(0, 'end')

        if hasattr(self, "hours_worked_entry") and self.hours_worked_entry.winfo_exists():
            self.hours_worked_entry.delete(0, 'end')

        if hasattr(self, "vacation_days_entry") and self.vacation_days_entry.winfo_exists():
            self.vacation_days_entry.delete(0, 'end')
    
        # Reset dropdowns
        self.type_var.set("Select Employee Type")
        self.dept_var.set("Select Departments")


if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()
