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