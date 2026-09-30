"""
Project 1
Smart Bank Account Management System

Concepts Covered
----------------
1. Class & Object
2. Attributes
3. Methods
4. Encapsulation
5. Static Method
6. Magic Methods
"""

class BankAccount:

    # Class Attribute
    bank_name = "OpenAI Bank"

    def __init__(self, account_number, holder_name, balance):
        """
        Constructor
        Automatically runs whenever an object is created.
        """

        self.account_number = account_number
        self.holder_name = holder_name

        # Encapsulation
        # Private attribute
        self.__balance = balance

    def deposit(self, amount):
        """Add money into account"""

        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        """Withdraw money"""

        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient Balance.")

    def get_balance(self):
        """
        Getter Method

        Since __balance is private,
        users cannot access it directly.
        """

        return self.__balance

    # Static Method
    @staticmethod
    def calculate_interest(balance):
        """
        Static methods belong to the class.

        They don't need object data.
        """

        return balance * 0.05

    # Magic Method
    def __str__(self):
        return f"{self.holder_name} ({self.account_number})"

    # Magic Method
    def __len__(self):
        """
        Returns the number of digits
        in account number.
        """

        return len(str(self.account_number))


# ---------------------------------------
# Creating Objects
# ---------------------------------------

acc1 = BankAccount(1001, "Rahul", 5000)
acc2 = BankAccount(1002, "Priya", 12000)

print(acc1)
print(acc2)

print()

acc1.deposit(2000)
acc1.withdraw(1000)

print()

print("Current Balance:", acc1.get_balance())

interest = BankAccount.calculate_interest(acc1.get_balance())
print("Estimated Interest:", interest)

print()

print("Length of Account Number:", len(acc1))

# This will fail because balance is private
# print(acc1.__balance)