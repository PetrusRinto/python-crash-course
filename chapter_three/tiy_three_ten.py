# Patrick 22.09.2025
# A program that lists countries I want to visit and not

# A regular list of three countries (it will increase).
countries = ['thailand', 'zanzibar', 'france']

# a message that prints the list:
print(f'Original: {countries}')

print(f'\nSorted: {sorted(countries)}') # Alphabetical order, but not permanent

print(f'\nOriginal: {countries}')

print(f'\nReverse alphabetically:{sorted(countries, reverse=True)}')

print(f'\nOriginal: {countries}')

# Using variables to sort diferentally and permanentally.
countries.reverse()
print(f'\nReverse originally: {countries}')

# Reverse again outputs the original format
countries.reverse()
print(f'\nOriginal: {countries}')