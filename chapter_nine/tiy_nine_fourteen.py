# Patrick 19.11.2025.
# 9-14 Lottery.

from random import choice

tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd']

print("Any ticket matching these 4 numbers or letters wins a prize!")

for element in range(1, 5):
    lottery_ticket = choice(tickets)
    print(lottery_ticket)