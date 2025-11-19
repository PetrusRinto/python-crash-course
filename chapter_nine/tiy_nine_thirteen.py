# Patrick 18.11.2025.
# 9-13 Dice.

from random import randint

class Die:
    """Simple attempt to recreate a dice."""

    def __init__(self, sides=6):
        """Initiates dice attributes."""
        self.sides = sides
    
    def roll_dice(self):
        """Simple method to print a random number."""
        print(f"{randint(1, self.sides)}")
    
    def update_dice(self, side):
        """Simple method to change the amount of sides."""
        self.sides = side

roll = Die()

print("6 sided die:")
for num in range(1, 11):
    roll.roll_dice()
print("\n")

print("10 sided die:")
roll.update_dice(10)
for num in range(1, 11):
    roll.roll_dice()
print("\n")

print("20 sided die:")
roll.update_dice(20)
for num in range(1, 11):
    roll.roll_dice()