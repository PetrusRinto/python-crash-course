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
        win_ticket = []

        # While loop to avoid duplicates.
        while len(win_ticket) < count:
            pick = choice(available)
            win_ticket.append(pick)
            available.remove(pick)
        return win_ticket
    

class Ticket(Lottery):
    """A class representing a player's ticket."""

    def __init__(self, ticket):
        """Initializing attributes for the ticket."""
        self.ticket = ticket

class Judge:
    """A class deciding the winner or loser."""

    def __init__(self, judge):
        """Initializing attributes for the judge."""
        self.judge = judge
    
lottery = Lottery()
ticket = Ticket()
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