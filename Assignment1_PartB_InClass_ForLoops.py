"""
Date: 19-09-2024
Author: Namrata Modha
Purpose: Practice For loop
"""

"""
for i in range(2,17,2):
    print(i)
"""

"""
WAP that prompts the user to enter two numbers, display sum and average of the two numbers. Execute using for loop.
"""

# Initialising the variables so that we dont get not declared error
total = 0
avg = 0
# Looping through to get 2 inputs from the user
for i in range(1,3):
    num = int(input(f"Enter num {i} " +": "))
    # Performing the sum of two numbers and storing it in total
    total = total + num

# Performing Average on the total of 2 numbers
avg = total / i

# Printing the total and average
print(f"Total is: {total}") 
print(f"Average is {avg}")

    
