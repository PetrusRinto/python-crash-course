# Patrick 19.11.2025. / 20.11.2025.
# 9-15 Lottery Analysis.

from random import choice

class Lottery:
    """A class representing a lottery simulator.."""

    def __init__(self, pool=None):
        """Initializing attributes."""
        if pool is None:
            pool = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
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


class Player:
    """A class representing the player."""

    def __init__(self, player_ticket):
        """Initializing attributes for the player's ticket."""
        self.player_ticket = player_ticket


class Judge:
    """A class deciding the winner or loser."""

    def __init__(self, lottery, player):
        """Initializing attributes for the judge."""
        self.lottery = lottery
        self.player = player
    
    def judge(self):
        """Method to decide the winner."""
        winning_ticket = self.lottery.pull_items()

        print(f"Winning ticket: {winning_ticket}")
        print(f"Your ticket: {self.player.player_ticket}")

        if winning_ticket == self.player.player_ticket:
            print("You won!")
        else:
            print("You lost!")


class Probability:
    """Class that represents the probability of winning."""

    def __init__(self, lottery, player):
        """Initializing probability attributes."""
        self.lottery = lottery
        self.player = player
        self.attempts = 0
    
    def tries(self):
        """Method representing tries."""
        while True:
            self.attempts += 1
            pull = self.lottery.pull_items()

            if pull == self.player.player_ticket:
                return self.attempts

    
# lottery = Lottery()
# lottery.pull_items()

# my_ticket = (2, 'e', 'c', 6)

# attempts = 0
# won = False

# while not won:
#     attempts += 1
#     pull = lottery.pull_items()

#     if pull == my_ticket:
#         print(f"It took {attempts} attempts for you to win!")
#         won = True

lottery = Lottery()
player = Player([2, 'e', 'c', 6])

print("\n- Did you win? -")
judge = Judge(lottery, player)
judge.judge()

print("\n- Trying until you win -")
probability = Probability(lottery, player)
attempts = probability.tries()
print(f"It took {attempts} attempts to win!")