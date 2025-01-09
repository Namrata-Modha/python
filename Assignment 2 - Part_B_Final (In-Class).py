"""
Date: 17-10-2024
Author: Namrata Modha
Purpose: Demonstrate the use of File or File handling using python
"""


# a file named "test", will be created if not exists with the writing mode.
#f = open('employee.txt', 'w')

# whenever we work with write 'w' it always replace the file content

# while using the with function/method we dont need to close the file it will close it auto. its a neater way work with file
with open('employee.txt', 'w') as f:
    # file will be added with the below content with writ function
    f.write("Payroll System\n")
    f.write("-------------Employee Listing-----------\n")
    f.write("EmployeeName \t Employee Dept\n")
    f.write("John Doe \t Designer\n")
    f.write("Anna Cat \t Developer\n")
    f.write("Salena G \t Manager\n")

# this is mandatory to add when we are dealing with file handling operations
#f.close()

with open('employee.txt', 'a') as f:
    f.write("Ariana G\t Manager\n")

# Read the entire file as a single string
# Opens the file "employee.txt" in read mode and stores the content in the 'contents' variable
print("Read the entire file as a single string")
with open("employee.txt") as file:
    contents = file.read()  # Reads the entire file content as a string
    print(contents)  # Prints the entire content of the file

# Read the entire file as a list of lines
# Each line in the file becomes an element in the 'emp' list
print("Read the entire file as a list of lines")
with open("employee.txt") as file:
    emp = file.readlines()  # Reads all lines and stores them as a list of strings
    print(emp[0], end="")  # Prints the first line without adding a new line
    print(emp[1])  # Prints the second line, with a new line at the end

# Read the file line by line
# Reads each line one by one, allowing you to process them individually
print("Read the file line by line")
with open("employee.txt") as file:
    emp1 = file.readline()  # Reads the first line from the file
    print(emp1, end="")  # Prints the first line without adding a new line
    emp2 = file.readline()  # Reads the second line from the file
    print(emp2)  # Prints the second line with a new line at the end





# How to Write the Items in a List to a File
members = ["John Cleese", "Eric Idle"]  # A list of names to write into the file

# Open "members.txt" in write mode ("w") which overwrites the file if it exists, or creates a new one
with open("members.txt", "w") as file:
    for m in members:
        file.write(f"{m}\n")  # Writes each member on a new line, using "\n" to add a new line at the end

# How to Read the Lines in a File into a List
members = []  # Initialize an empty list to store the file's content

# Open "members.txt" in read mode (default mode) to read its content line by line
with open("members.txt") as file:
    for line in file:
        line = line.replace("\n", "")  # Removes the newline character at the end of each line
        members.append(line)  # Adds the cleaned line (name) to the 'members' list
        print(members)  # Prints the list after each addition to show the current state

