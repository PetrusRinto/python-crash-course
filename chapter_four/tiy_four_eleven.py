# Patrick 30.09.2025
# 4-11 My Pizzas, Your Pizzas.
# Copy pizzas from 4-1 and call it 'friend_pizzas'

# Program from 4-1
my_pizzas = ['campino', 'napolitan', 'homemade'] # renamed it 'my pizzas' for relevance

# 4-11 Assignment:
# Copy the list and name it 'friend_pizzas'
friend_pizzas = my_pizzas[:]

# Adding a new pizza to 'my_pizzas'
my_pizzas.append('pepperoni')
# Adding a different pizza to 'friend_pizzas'
friend_pizzas.append('margarita')

# Proving a successful seperation
print(f'My favorite pizzas are:')
for my_pizza in my_pizzas:
    print(my_pizza.title())

print(f"\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())
