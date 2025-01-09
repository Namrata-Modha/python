"""
Date: 24-10-2024
Author: Namrata Modha
Purpose: Demonstrate the use of Exceptions in python
"""

"""
#while True:
try:
    # Attempt to execute the following block of code
    number = int(input("Enter an integer: "))
    # If successful, print the valid integer
    print(f"You entered a valid integer of {number}.")
    print(type(number))
    #return number
except ValueError:
    # If a ValueError occurs execute this block
    print("You entered an invalid integer. Please try again.")

print("Thanks!")

"""
import sys
filename = input("Enter filename: ")
movies = []
try:
    with open(filename) as file:
        raise OSError("OSError")
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
except FileNotFoundError as e:
    print("FileNotFoundError:", e)
    sys.exit()
except OSError as e:
    print("OSError:", e)
    sys.exit()
except Exception as e:
    print(type(e), e)
    sys.exit()

