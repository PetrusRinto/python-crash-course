# Patrick 30.09.2025.
# 4-12 More loops.
# Writing two for loops to print any foods.py program.

# First chosen version of foods.py.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
# Assignment 4-12.
for my_food in my_foods:
    print(my_food.title())

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food.title())