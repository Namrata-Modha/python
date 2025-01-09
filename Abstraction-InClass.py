"""
Purpose: Demonstrate the use of Abstraction in python
Date: 07-11-2024
"""

from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        # This is an abstract method
        pass

# Concrete class for Dog
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

# Concrete class for Cat
class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"
    #
 Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling make_sound method
print(dog.make_sound())  # Output: Woof! Woof!
print(cat.make_sound())  # Output: Meow! Meow!

