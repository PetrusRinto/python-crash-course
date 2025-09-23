# Patrick 22.09.2025
# A program that lists countries I want to visit and not

# A regular list of three countries (it will increase).
countries = ['thailand', 'zanzibar', 'france']

# a message that prints the list:
print('This is the original list.') # Patrick 23.09.2025
print(f'Original: {countries}')

# Alphabetical order, but not permanent
print(f'\nSorted in alphabetical order, but not permanent.') # Patrick 23.09.2025
print(f'Sorted: {sorted(countries)}')

# Proving the change was temporary
print(f'\nThe original again to prove the temporary change.') # Patrick 23.09.2025
print(f'Original: {countries}')

# Sorting in alphabetical, but reversed
print(f'\nSorted in reverse-alphabetical order.') # Patrick 23.09.2025
print(f'Reversed alphabetically:{sorted(countries, reverse=True)}')

# Proving the temporary change by outputting the original
print(f'\nProving the temporary change.') # Patrick 23.09.2025
print(f'Original: {countries}')

# Using variables to sort diferentally and permanentally
print(f'\nCreating a variable to permanentally reverse the order.') # Patrick 23.09.2025
countries.reverse()
print(f'Reversed original: {countries}')

# Reverse again outputs the original format
print(f'\nTo revert back to the original we have to revere it again.') # Patrick 23.09.2025
countries.reverse()
print(f'Original: {countries}')

# Patrick 23.09.2025
# Permanently sorting in reversed-alphabetical order
print(f'\nPermanently changed the order in reversed-alphabetical order with a variable.')
countries.sort(reverse = True)
print(f'Reversed alphabetically: {countries}')

# Let us test adding a new country to the list and see how the code reacts
countries.append('japan')
print(f'\nAdded Japan to the list to check if the order changed.')
print(f'New list: {countries}') # Proved the sorting is not dynamic.

# Let's sort it in alphabetical order.
print(f'\nSorting the new list alphabetically.')
countries.sort()
print(f'Alphabetical order: {countries}')

# Using integer to identify my favorite country out of the current list. Using 'title' to capitalize.
print(f'\nCreating a variable to output my favorite country based on the current list using index.')
most_fav_int = countries[1]
print(f'Index 1 should be Japan, my favorite is: {most_fav_int.title()}!')

# Popping out and displaying my least favourite based on the current list.
least_fav_int = countries.pop(0)
print(f'\n{least_fav_int}')
