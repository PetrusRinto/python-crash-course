# Patrick 19.11.2025. / 20.11.2025.
# 9-15 Lottery Analysis.

from random import choice

class Lottery:
    """A class representing a lottery simulator.."""

    def __init__(self, pool=[1,2,3,4,5,6,7,8,9,10,
                             'a','b','c','d','e']):
        """Initializing attributes."""
        self.pool = pool
    
    def pull_items(self, count=4):
        """A method that represents "pulling" the winner."""
        available = self.pool[:]
        ticket = []

        # While loop to avoid duplicates.
        while len(ticket) < count:
            pick = choice(available)
            ticket.append(pick)
            available.remove(pick)
        return ticket

lottery = Lottery()
lottery.pull_items()

my_ticket = [2, 'e', 'c', 6]

attempts = 0
won = False

while not won:
    attempts += 1
    pull = lottery.pull_items()

    if pull == my_ticket:
        print(f"It took {attempts} attempts for you to win!")
        won = True