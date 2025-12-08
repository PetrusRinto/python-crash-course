# Patrick 08.12.2025.
# 11-3 Employee.

class Employee:
    """A class that represents an employee."""

    def __init__(self, first, last, salary=''):
        """Initializing employee's attributes."""
        self.first = first.title()
        self.last = last.title()
        self.salary = salary
    
    def give_raise(self, amount=''):
        """A method that adds a raise to the employee's salary."""
        if amount:
            amount = amount
        else:
            amount = 5000
        new_salary = amount + self.salary
        return new_salary