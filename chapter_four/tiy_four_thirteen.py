# Patrick 30.09.2025
# 4-13 Buffet.
# Storing menu in a tuple with five basic foods

# Storing the menu as a tuple
menu = ('soup', 'meatballs', 'spaghetti', 'beef', 'salad')
# For loop to print each food.
for food in menu:
    print(food.title())

# Modification attempt to force an error
del(menu[-2])
print(f'\nNew menu:')
print(f'{menu}') # Successful error