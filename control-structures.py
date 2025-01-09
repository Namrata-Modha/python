"""
Date:12-09-2024
Author:Namrata Sharad Modha
Purpose: Demonstrate Control Structures
"""

print("Welcome to my Payroll System")

# Static Program Start

print("---Static Code---")
# Hard code/Initialize values to 2 variables
firstNum = 10
secondNum = 20

#Perform Sum of the above mentioned variables and save it in a new variable
total = firstNum + secondNum
print(total) #Printing the total as it is without formating

#Perform Average on the total
average = total / 2
print(f"Average of {firstNum} and {secondNum} is {average}") #Print the Average of total with 'f' string to format the output

#Static Program End

#Dynamic Program Start

print("---Dynamic Code---")
#Prompt the user to enter first and second number and type cast the variables as input by default returns as string
num1 = int(input("Please enter your First Number: "))
num2 = int(input("Please enter your Second Number: "))

#Perform Sum of the above mentioned variables and save it in a new variable
sumOfTotal = num1 + num2
print(sumOfTotal) #Printing the sum as it is without formating

#Perform Average on the sumOfTotal
avg = sumOfTotal / 2
print(f"Average of {num1} and {num2} is {avg}") #Print the Average of sumOfTotal with 'f' string to format the output

#Dynamic Program End

