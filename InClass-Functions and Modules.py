from datetime import datetime
# Define and intitiate a function

def getGreetings():
    print("Hello World")

print("This function will demonstrate the use of user defined functions")
getGreetings() # Calling a function


# defining a function that accepts a parameter

def getGreetingsWithPara(name):
    print(f"Hello {name}, Greetings from function")

print("This function will demonstrate the use of user defined functions with parameters")
"""
name = input("Please enter your name:") #prompting the user to enter their name for the function

getGreetingsWithPara(name) # Calling a function
"""
"""
WAF that accepts 2 numbers. it should display the product of the 2 numbers as well as the name of the user
"""

#defining the function that accepts 3 param
def calculateProduct(num1, num2, name):
    print(f"Hello {name}, Greetings from function")
    product = float(num1) * float(num2)# Perfoming the logic for product
    print(f"Product of number 1 and number 2 is: {product}")
    
#name = input("Please enter your name:") #prompting the user to enter their name for the function
#number1 = input("Please enter number 1:")#prompting the user to enter number 1 for the function
#number2 = input("Please enter number 2:")#prompting the user to enter number 2 for the function

#calculateProduct(number1, number2, name) # Calling a function



# defining a function that returns a parameter

def greeting(name):
    print(f"Hello {name}")
    age = 15
    return age

#name = input("Please enter your name:") #prompting the user to enter their name for the function
#getAge = greeting(name)

#print(f"Age is: {getAge}")

#print(greeting(name))



"""
WAP that utilizes a function that should accept birthyear of the user. Your function should calculate and return the age of the user
Your program should then determine based on age if the user is eligeble for a drivers license. The required age is 16.
"""


def calculateAge(year):
    age = datetime.now().year - birth_year
    print(age)
    return age

def eligibility(birth_year):
    age = calculateAge(birth_year)
    if age >= 16:
        return f"You are {age} years old. You are eligible for a driver's license."
    else:
        return f"You are {age} years old. You are not eligible for a driver's license."

birth_year = int(input("Enter your birth year: "))
result = eligibility(birth_year)
print(result)

