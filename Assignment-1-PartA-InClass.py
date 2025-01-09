"""
Date:12-09-2024
Author:Namrata Sharad Modha
Purpose: Demonstrate Control Structures
"""

print("Welcome to my Payroll System")

"""
wap that prompts the user to enter the first name, last name, gender, age.
if the user is a male or over the age of 16 then he is eligible for boarding school.
"""

#Prompt the user user to enter first name, last name, gender and age.

firstName = input("Please enter your First Name: ")
lastName = input("Please enter your Last Name: ")
gender = input("Please enter your Gender M/F: ")
age = int(input("Please enter your Age: "))

#Check if the user is male based on gender or the age is over 16
if (gender.upper() == 'M' or age > 16):
    print(f"Congratulations {firstName}, You're eligible for boarding school")
else:
    print(f"Unfortunatly {firstName}, You're not yet eligible for boarding school")
