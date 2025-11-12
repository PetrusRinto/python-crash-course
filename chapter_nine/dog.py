# Patrick 12.11.2025.
# Get familiar with classes.
# Dogs.

class Dog:
    """A simple attemt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
