"""
Date: 31-10-2024
Author: Namrata Modha
Purpose: To demonstrate the concept of OOP
"""

class Car:
    # first parameter is a pointer and can be anything in terms of name
    def __init__(self, make, color, model, year):
        self.make = make
        self.color = color
        self.model = model
        self.year = year

    def display(self):
        print(f" Make: {self.make}\n Color: {self.color}\n Model: {self.model}\n Year: {self.year}\n")

carObj1 = Car('tesla', 'grey', 'T', 2025)
carObj2 = Car('BMW', 'grey', 'X', 2025)

carObj1.display()
carObj2.display()

print(f"Make of the car for object 1 is {carObj1.make}")
print(f"Make of the car for object 2 is {carObj2.make}")


    
        



        
