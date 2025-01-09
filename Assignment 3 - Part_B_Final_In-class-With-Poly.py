"""
Author: Namrata Modha
Purpose: Demonstrate Polymorphism and Method Overriding in python
Date: 14-11-2024
"""
# Class representing a Car
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def move(self):
        print("Driving...")  # Overridden method in Car class

# Class representing a DonkeyCart
class DonkeyCart:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def move(self):
        print("Riding...")  # Overridden method in DonkeyCart class

# Class representing a Boat
class Boat:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def move(self):
        print("Sailing...")  # Overridden method in Both class

# Class representing a Plane   
class Plane:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def move(self):
        print("Flying...")  # Overridden method in Plane class

# Creating an object of Car and calling its move method
carObj = Car("Tesla", "Y")
# Creating an object of DonkeyCart and calling its move method
dcObj = DonkeyCart("Donkey", "Brown")
# Creating an object of Boat and calling its move method
boatObj = Boat("Cruise", "2004")
# Creating an object of Plane and calling its move method
planeObj = Plane("Emirates", "Airbus")

# Looping over the objects and calling the move method, with error handling
for obj in (carObj, dcObj, boatObj, planeObj):
    try:
        obj.move()  # Attempt to call the 'move' method
    except AttributeError:  # Handle the case where 'move' method doesn't exist
        print(f"{obj.__class__.__name__} does not have a 'move' method.")
