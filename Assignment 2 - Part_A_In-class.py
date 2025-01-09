"""
Date: 26-09-2024
Author: Namrata Modha
Purpose: To demonstrate the use of functions

WAP that utilizes a function that should accept birthyear of the user. Your function should calculate and return the age of the user
Your program should then determine based on age if the user is eligeble for a drivers license. The required age is 16.
"""
from datetime import datetime # Import the datetime module to work with dates

def calculateAge(year):
    # Calculate the current age by subtracting the birth year from the current year
    age = datetime.now().year - birth_year
    print(age)
    return age # Return the calculated age

def eligibility(birth_year):
    # Call the calculateAge function to get the age
    age = calculateAge(birth_year)
    # Check if the age is 16 or older
    if age >= 16:
        return f"You are {age} years old. You are eligible for a driver's license."
    else:
        return f"You are {age} years old. You are not eligible for a driver's license."

# Prompt the user to enter their birth year
birth_year = int(input("Enter your birth year: "))
# Call the eligibility function and store the result
result = eligibility(birth_year)
print(result)
