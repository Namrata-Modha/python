"""
Purpose: Demonstrate the use of encapsulation in python
Date: 07-11-2024
"""
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute (encapsulated)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited.")
        else:
            print("Invalid amount.")

    def __calculate_interest(self):
        # Private method to calculate interest
        return self.__balance * 0.05

    def get_balance(self):
        # Public method to access private balance
        return self.__balance
# Usage example
account = BankAccount("Namrata", 1000)
print(account.get_balance())    # Output: 1000
account.deposit(500)            # Output: $500 deposited.
print(account.get_balance())    # Output: 1500

# Trying to access private attributes directly
#print(account.__balance)        # AttributeError: 'BankAccount' object has no attribute '__balance'

print(account.__calculate_interest()) #AttributeError: 'BankAccount' object has no attribute '__calculate_interest'
