# Patrick 17.09.2025
# Creating a list of places I want to visit and sorting them differently

# Storing the places I want to visit in a variable
places = ['hokkaido', 'zanzibar', 'beijing', 'hong kong', 'nordkapp']

# printing in original order
print(f'The list displayed in original order:')
print(places)

# temporarily sorting the list in alphabetical order
print(f'\nThe list displayed in alphabetical order:')
print(f'{sorted(places)}')

# verifying that the change was temporary
print(f'\nThe list displayed in original order again:')
print(places)

# temporarily sorting in reverse order
reverse_sorted = sorted(places, reverse=True) # 18.09.2025
print(f'\nThe list displayed in reverse-alphabetical order:') # 19.09.2025
print(reverse_sorted)

# verifying the list change
print(f'\nThe list displayed in original order again:')
print(places)

# reversing the orginal order
places.reverse()
print(f'\nThe original list displayed in reverse:')
print(f'{places}')

# reverse again to revert to the original list
places.reverse()
print(f'\nThe reversed list displayed in reverse:')
print(f'{places}')

# using sort() to store the list in alphabetical order
places.sort()
print(f'\nThe "original" list displayed in alphabetical order:')
print(f'{places}')

# storing places in reverse-alphabetical order
places.sort(reverse=True)
print(f'\nThe list displayed in reverse-alphabetical order:')
print(f'{places}')
