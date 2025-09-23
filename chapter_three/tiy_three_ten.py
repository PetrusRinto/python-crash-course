# Patrick 22.09.2025
# A program that lists countries I want to visit and not

# A regular list of three countries (it will increase).
countries = ['thailand', 'zanzibar', 'france']

# a message that prints the list:
print('This is the original list.')
print(f'Original: {countries}')

# Alphabetical order, but not permanent
print(f'\nSorted in alphabetical order, but not permanent.')
print(f'Sorted: {sorted(countries)}')

# Proving the change was temporary
print(f'\nThe original again to prove the temporary change.')
print(f'Original: {countries}')

# Sorting in alphabetical, but reversed
print(f'\nSorted in reverse-alphabetical order.')
print(f'Reversed alphabetically:{sorted(countries, reverse=True)}')

# Proving the temporary change by outputting the original
print(f'\nProving the temporary change.')
print(f'Original: {countries}')

# Using variables to sort diferentally and permanentally
print(f'\nCreating a variable to permanentally reverse the order.')
countries.reverse()
print(f'Reversed original: {countries}')

# Reverse again outputs the original format
print(f'\nTo revert back to the original we have to revere it again.')
countries.reverse()
print(f'Original: {countries}')

# Patrick 23.09.2025