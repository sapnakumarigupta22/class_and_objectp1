"""
Project 2
Employee Management System

Concepts Covered
----------------
1. Single Inheritance
2. Multilevel Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance
5. Encapsulation
6. Static Method
7. Magic Methods
"""


# -------------------------------------------------
# Parent Class
# -------------------------------------------------

class Employee:

    company = "TechNova"

    def __init__(self, emp_id, name, salary):

        self.emp_id = emp_id
        self.name = name

        # Private Attribute
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def work(self):
        print(f"{self.name} is working.")

    @staticmethod
    def company_policy():
        """
        Static methods are shared
        across all employees.
        """

        print("Office timing: 9 AM - 6 PM")

    def __str__(self):
        return f"{self.name} ({self.emp_id})"


# -------------------------------------------------
# Single Inheritance
# -------------------------------------------------

class Developer(Employee):

    def code(self):
        print(f"{self.name} is writing Python code.")


# -------------------------------------------------
# Multilevel Inheritance
# Employee
#      ↓
# Developer
#      ↓
# SeniorDeveloper
# -------------------------------------------------

class SeniorDeveloper(Developer):

    def review_code(self):
        print(f"{self.name} is reviewing pull requests.")


# -------------------------------------------------
# Hierarchical Inheritance
# Employee
#    ↓        ↓
# Developer   Manager
# -------------------------------------------------

class Manager(Employee):

    def manage_team(self):
        print(f"{self.name} is managing the team.")


# -------------------------------------------------
# Another Parent
# -------------------------------------------------

class Trainer:

    def train(self):
        print("Conducting employee training.")


# -------------------------------------------------
# Multiple Inheritance
#
# Employee
#      ↓
# Developer
#
# Trainer
#      ↓
#
# TechLead
# -------------------------------------------------

class TechLead(Developer, Trainer):

    def lead_project(self):
        print(f"{self.name} is leading the project.")


# -------------------------------------------------
# Objects
# -------------------------------------------------

dev = Developer(101, "Rahul", 70000)

senior = SeniorDeveloper(102, "Amit", 120000)

manager = Manager(103, "Priya", 100000)

lead = TechLead(104, "Sneha", 150000)

print(dev)
print(senior)
print(manager)
print(lead)

print()

dev.work()
dev.code()

print()

senior.work()
senior.code()
senior.review_code()

print()

manager.work()
manager.manage_team()

print()

lead.work()
lead.code()
lead.train()
lead.lead_project()

print()

print("Salary:", lead.get_salary())

print()

Employee.company_policy()